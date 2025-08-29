# Diseño Conceptual: Sistema de Chat Inter-Agente

## Arquitectura Conceptual

### 1. Modelo de Datos SQLite

```sql
-- Tabla de mensajes de chat entre agentes
CREATE TABLE agent_chat_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id TEXT NOT NULL,
    from_agent TEXT NOT NULL,
    to_agent TEXT NOT NULL,
    message_type TEXT DEFAULT 'text', -- text, request, response, system
    content TEXT NOT NULL,
    metadata TEXT, -- JSON con datos adicionales
    status TEXT DEFAULT 'pending', -- pending, read, acknowledged
    timestamp INTEGER DEFAULT (strftime('%s', 'now')),
    expires_at INTEGER, -- TTL para mensajes temporales
    priority INTEGER DEFAULT 3, -- 1=alta, 2=media, 3=baja
    thread_id TEXT, -- Para hilos de conversación
    reply_to_id INTEGER, -- Referencia a mensaje padre
    FOREIGN KEY (reply_to_id) REFERENCES agent_chat_messages(id)
);

-- Tabla de conversaciones activas
CREATE TABLE agent_conversations (
    id TEXT PRIMARY KEY, -- UUID de la conversación
    participants TEXT NOT NULL, -- JSON array de agentes
    topic TEXT, -- Tema de la conversación
    status TEXT DEFAULT 'active', -- active, archived, closed
    created_at INTEGER DEFAULT (strftime('%s', 'now')),
    last_activity INTEGER DEFAULT (strftime('%s', 'now')),
    metadata TEXT -- JSON con configuración
);

-- Tabla de presencia de agentes
CREATE TABLE agent_presence (
    agent_name TEXT PRIMARY KEY,
    status TEXT DEFAULT 'offline', -- online, busy, offline
    last_seen INTEGER DEFAULT (strftime('%s', 'now')),
    current_task TEXT, -- Descripción de tarea actual
    listening_for TEXT -- JSON array de tipos de mensajes que espera
);
```

### 2. Flujo de Trabajo del Chat

```
┌─────────────────┐    Polling    ┌─────────────────┐
│  @acolyte.api   │◄──────────────┤   SQLite DB     │
│                 │    cada 30s   │                 │
│ 1. Check msgs   │               │ agent_chat_     │
│ 2. Send reply   │──────────────►│ messages        │
│ 3. Update       │               │                 │
│    presence     │               │                 │
└─────────────────┘               └─────────────────┘
        ▲                                   ▲
        │                                   │
        │ Conversación                      │
        │ Paralela                          │
        ▼                                   ▼
┌─────────────────┐               ┌─────────────────┐
│ @backend.nodejs │◄──────────────┤  Otros Agentes  │
│                 │    Polling    │                 │
│ 1. Check msgs   │    cada 30s   │  @frontend.react│
│ 2. Process req  │               │  @database.pg   │
│ 3. Send response│──────────────►│  @security.audit│
│ 4. Update task  │               │                 │
└─────────────────┘               └─────────────────┘
```

### 3. Tipos de Mensajes

#### 3.1 Mensaje de Texto Simple
```json
{
    "conversation_id": "conv_api_nodejs_20250829_001",
    "from_agent": "@acolyte.api",
    "to_agent": "@backend.nodejs",
    "message_type": "text",
    "content": "¿Puedes revisar el endpoint /users/{id} para validación de permisos?",
    "priority": 2,
    "thread_id": "permissions_review"
}
```

#### 3.2 Mensaje de Solicitud
```json
{
    "conversation_id": "conv_api_nodejs_20250829_001",
    "from_agent": "@acolyte.api",
    "to_agent": "@backend.nodejs",
    "message_type": "request",
    "content": "Need code review for authentication middleware",
    "metadata": {
        "files": ["middleware/auth.js", "routes/protected.js"],
        "deadline": "2025-08-29T18:00:00Z",
        "requirements": ["security_audit", "performance_check"]
    },
    "priority": 1
}
```

#### 3.3 Mensaje de Respuesta
```json
{
    "conversation_id": "conv_api_nodejs_20250829_001",
    "from_agent": "@backend.nodejs",
    "to_agent": "@acolyte.api",
    "message_type": "response",
    "content": "Code review completed. Found 2 security improvements needed.",
    "reply_to_id": 123,
    "metadata": {
        "status": "completed",
        "findings": [
            "JWT validation needs rate limiting",
            "Add CORS headers validation"
        ],
        "estimated_fix_time": "30min"
    }
}
```

### 4. Sistema de Polling Inteligente

#### 4.1 Estrategia de Polling por Prioridad
```
Prioridad 1 (Alta):     Polling cada 10s
Prioridad 2 (Media):    Polling cada 30s (estándar)
Prioridad 3 (Baja):     Polling cada 60s

Escalación automática:
- Si mensaje no leído > 5min → Prioridad +1
- Si agente objetivo offline > 10min → Notificar a @ops.monitor
```

#### 4.2 Filtros de Polling Eficientes
```sql
-- Query optimizada para cada agente
SELECT * FROM agent_chat_messages 
WHERE to_agent = ? 
  AND status = 'pending' 
  AND (expires_at IS NULL OR expires_at > ?)
ORDER BY priority ASC, timestamp ASC 
LIMIT 50;
```

### 5. Gestión de Conversaciones

#### 5.1 Creación Automática de Conversaciones
```
Reglas de agrupación:
- Mismo topic + participantes = misma conversación
- Timeout sin actividad (2h) = nueva conversación
- Máximo 100 mensajes por conversación → Auto-archivo
```

#### 5.2 Hilos de Conversación
```
Thread Hierarchy:
├── Main conversation: "API Optimization Project"
│   ├── Thread: "Authentication Review"
│   │   ├── @acolyte.api: "Need JWT validation review"
│   │   └── @backend.nodejs: "Will check middleware"
│   └── Thread: "Performance Testing"
│       ├── @acolyte.api: "Load tests failing"
│       └── @ops.monitor: "Checking server metrics"
```

### 6. Sistema de Presencia

#### 6.1 Estados de Agente
```
online:  Agente ejecutándose activamente
busy:    Procesando tarea compleja (no interrumpir)
offline: No visto en >2min, mensajes quedan pendientes
```

#### 6.2 Indicadores de Actividad
```json
{
    "agent_name": "@backend.nodejs",
    "status": "busy",
    "current_task": "Refactoring user authentication system",
    "listening_for": ["security_questions", "urgent_requests"],
    "estimated_completion": "2025-08-29T17:30:00Z"
}
```

### 7. Gestión de TTL y Limpieza

#### 7.1 Políticas de Retención
```
Mensajes de chat:           30 días
Conversaciones archivadas:  90 días
Presencia offline:          7 días
Mensajes no leídos:         14 días
```

#### 7.2 Cleanup Automático
```sql
-- Query de limpieza (ejecutar cada 24h)
DELETE FROM agent_chat_messages 
WHERE timestamp < (strftime('%s', 'now') - 2592000); -- 30 días

DELETE FROM agent_presence 
WHERE status = 'offline' 
  AND last_seen < (strftime('%s', 'now') - 604800); -- 7 días
```

### 8. Casos de Uso Prácticos

#### 8.1 Solicitud de Code Review
```
@acolyte.api → @backend.nodejs:
"Hey, can you review the new validation logic in user.controller.js?"

@backend.nodejs → @acolyte.api:
"Sure, checking now... Found issue with email validation regex."

@backend.nodejs → @acolyte.api:
"Fixed the regex pattern. Also added unit tests. Ready for merge."
```

#### 8.2 Coordinación Multi-Agente
```
@frontend.react → [multiple agents]:
"New user registration flow is ready. Need integration updates."

@backend.nodejs: "API endpoints updated, new fields added"
@database.postgres: "Schema migration completed"
@service.auth: "JWT payload updated with new user fields"
```

#### 8.3 Escalación de Problemas
```
@acolyte.api → @backend.nodejs:
[Priority: HIGH] "Critical: Authentication failing for all users"

@backend.nodejs → @ops.monitor:
"Investigating auth failure. May need to rollback recent deployment."

@ops.monitor → @service.communication:
"Sending alert to dev team. Preparing rollback procedure."
```

### 9. Ventajas del Diseño

1. **Asíncrono**: Compatible con el modelo de muerte/resurrección de agentes
2. **Persistente**: Mensajes sobreviven a reinicios de agentes
3. **Escalable**: Polling distribuido sin conflictos
4. **Contextual**: Conversaciones agrupadas por tema
5. **Prioritizado**: Mensajes urgentes procesados primero
6. **Trazable**: Historial completo de comunicaciones
7. **Eficiente**: Queries optimizados para SQLite

### 10. Integración con Sistema Existente

El chat complementaría el sistema de FLAGS existente:
- **FLAGS**: Notificaciones formales de cambios técnicos
- **Chat**: Comunicación informal y colaboración en tiempo real
- **Ambos**: Misma base SQLite, compatible con polling actual