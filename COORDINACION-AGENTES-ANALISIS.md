# ANÁLISIS COMPLETO: COORDINACIÓN DE AGENTES SIN MEMORIA

## 🚨 PROBLEMA IDENTIFICADO

### Situación Anoche
- **Dashboard task**: Múltiples agentes trabajaron simultáneamente
- **Resultado**: Trabajo duplicado, incompatible, 30 minutos perdidos
- **Causa raíz**: Agentes trabajaban independientemente sin coordinación

### Diagnóstico Real
**NO es problema técnico del sistema FLAGS**. Es problema de **CLARIDAD Y ESPECIFICIDAD** en templates:
- Claude: Demasiado vago en delegación
- Acolytes: No crean roadmaps suficientemente detallados
- FLAGS.agent: Solo analiza flags pendientes, no previene conflictos

## ⚡ ARQUITECTURA REAL DEL SISTEMA (CRÍTICO)

### Flujo de Agentes SIN MEMORIA
```
1. Agente NACE → memoria = 0
2. Lee sus memorias SQLite (si existen)
3. Procesa FLAGS pendientes  
4. Ejecuta request de Claude
5. Guarda interacción en BD
6. MUERE → memoria = 0 otra vez
```

**IMPLICACIÓN CRÍTICA**: Cada invocación el agente empieza desde cero. No recuerda conversación anterior.

### Roles Definidos
- **Claude**: Orquestador, NO escribe código, solo coordina y recibe resúmenes
- **Acolytes**: Especialistas de módulo, NO escriben código, crean ROADMAPS detallados
- **Implementadores**: (@backend.nodejs, @frontend.react, etc.) SÍ escriben código

## 📋 SOLUCIÓN: ROADMAPS MICRO-DETALLADOS

### Problema Central
Acolytes deben crear roadmaps PERFECTOS porque:
- Pierden memoria al apagarse
- Implementadores necesitan instrucciones EXACTAS
- No hay iteración, debe funcionar primera vez

### Formato Timeline Matemático
```markdown
# Dashboard Module Roadmap

## CONTEXT & NOTES
**Module Purpose**: Métricas de usuario en tiempo real
**Dependencies**: API users, Database metrics_table, Auth JWT

## PHASE 1: Base Structure (Paralelo seguro)
### 1.1 Database → @database.postgres
- [ ] 1.1.1 Create metrics_table (id, user_id, value, timestamp)
- [ ] 1.1.2 Add indexes (user_id, timestamp)

### 1.2 Types → @backend.typescript  
- [ ] 1.2.1 Create /dashboard/types/MetricsTypes.ts
  - Interface: MetricsData, DashboardConfig, UserMetrics
  - Export all interfaces

## PHASE 2: Services (Depende Phase 1 completo)
### 2.1 API Service → @backend.nodejs
- [ ] 2.1.1 Create /dashboard/services/MetricsService.js
  - Method: async getMetrics(userId): Promise<MetricsData[]>
  - Method: async updateMetric(id, value): Promise<void>
  - Dependencies: axios, ./types/MetricsTypes
  - Error handling: MetricsError class

## PHASE 3: Frontend (Depende Phase 2 completo)  
### 3.1 Components → @frontend.react
- [ ] 3.1.1 Create /dashboard/components/MetricsCard.tsx
  - Props: MetricsData, onUpdate callback
  - Styling: Tailwind only, no CSS modules
  - Max 150 lines, split if larger
```

## 🔧 MODIFICACIONES EN TEMPLATES

### Template Claude (Orquestador)
```markdown
**FUNDAMENTAL TRUTH**: You coordinate agents. You SHOULD NOT write code directly. You create DETAILED ROADMAPS and delegate SPECIFIC TASKS.

### Golden Rule: "ASK SPECIALISTS → GET ROADMAP → DELEGATE WITH SPECIFICS"

**DELEGATION TEMPLATE:**
"@{implementer}, create {exact_file_path} with:
- Interface: {specific_interface}
- Functionality: {bullet_points}  
- Dependencies: {exact_imports}
- Constraints: {what_NOT_to_include}
- Tests: {test_file_location}"
```

### Template Acolytes (Especialistas)
```markdown
**YOUR PRIMARY ROLE: CREATE IMPLEMENTATION ROADMAPS**

When asked "How to implement X?", you MUST respond with:
- FILES TO CREATE (exact paths)
- DETAILED SPECIFICATIONS (interfaces, dependencies, constraints)  
- IMPLEMENTATION ORDER (sequence by dependencies)
- DELEGATION COMMANDS (ready-to-use instructions)

**CRITICAL**: Timeline debe ser MATEMÁTICAMENTE CORRECTO:
- A antes que B si B depende de A
- Paralelo = mismo nivel (1.1, 1.2)
- Secuencial = números consecutivos (1.1 → 1.2)
```

### Template FLAGS.agent (Coordinador)
```markdown
**ENHANCED ROLE**: ROADMAP VALIDATOR + Conflict Prevention

**NEW WORKFLOW**:
1. Read pending flags
2. VALIDATE ROADMAPS - Check file conflicts, dependency violations
3. CREATE EXECUTION PLAN with phases
4. Direct Claude with conflict resolutions

**OUTPUT FORMAT**:
```
ROADMAP VALIDATION: OK/CONFLICTS
EXECUTION PLAN:
Phase 1: @acolyte.auth (create roadmap)
Phase 2: @backend.nodejs, @database.postgres (parallel - different domains)  
Phase 3: @frontend.react (depends on Phase 2 APIs)

Claude, execute Phase 1, then Phase 2 parallel, then Phase 3
```

## 💾 SISTEMA DE PERSISTENCIA: ROADMAPS

### Problema de Memoria Cero
Acolytes pierden memoria → necesitan roadmaps persistentes como "TodoWrite"

### Solución: Archivos module_roadmap.md
```
/módulo/
  module_roadmap.md  ← UN archivo por módulo
  src/
  tests/
```

### Ventajas vs Base de Datos
- ✅ Visible para humanos en IDE
- ✅ Versionado con git automático  
- ✅ Fácil para implementadores (solo Read tool)
- ✅ No añade complejidad a BD

## 🔄 FLUJO EVOLUTIVO DE CONOCIMIENTO

### Primera Invocación (Memoria = 0)
```
Acolyte nace → lee /project docs (básico/vacío)
→ <95% seguro → pregunta Claude
→ Claude actualiza /project/vision.md con respuesta
→ Acolyte muere
```

### Segunda Invocación (Memoria = 0, pero docs mejorados)
```  
Nuevo Acolyte nace → lee /project docs (más info)
→ ≥95% seguro → crea roadmap completo
→ No pregunta nada → roadmap perfecto
```

### Regla de Oro
- **≥95% seguro** → crea roadmap
- **<95% seguro** → pregunta a Claude → Claude actualiza /project
- **Claude no sabe** → pregunta al usuario → Claude actualiza /project

## 🧩 DEPENDENCIAS ENTRE MÓDULOS

### Autodiscovery de Dependencias
Acolyte debe saber qué módulos necesita para crear timeline correcto.

### Fuente de Dependencias
**Memorias SQLite existentes**:
- `dependencies` - qué módulos necesito
- `interfaces` - qué expongo a otros

### Flujo Dependency Discovery
```bash
# 1. Leo MIS dependencias  
uv run python ~/.claude/scripts/agent_db.py get-memory "@acolyte.orders" "dependencies"

# 2. Leo dependencias de mis dependencias
uv run python ~/.claude/scripts/agent_db.py get-memory "@acolyte.users" "dependencies" 

# 3. Construyo cadena: orders → users → database
# Timeline: 1.1 database, 2.1 users, 3.1 orders
```

### Problema Primera Vez
¿Cómo sabe acolyte sus dependencias si acaba de nacer?

**Solución**: Lee /project docs + template + prompt Claude = suficiente contexto

## 🚫 EDGE CASES IDENTIFICADOS

### 1. Múltiples Acolytes por Módulo
- acolyte.api, acolyte.api-auth, acolyte.api-payments
- **Solución**: Un roadmap por acolyte con naming específico

### 2. Conflictos de Escritura
- Dos agentes modificando mismo archivo
- **Solución**: Timeline matemático previene esto

### 3. Roadmap Obsoleto vs Código Real  
- Código evoluciona, roadmap queda desactualizado
- **Solución**: Acolyte lee código existente + roadmap actual

### 4. Dependencias Circulares
- Módulo A necesita B, B necesita A
- **Solución**: FLAGS.agent detecta ciclos, sugiere refactoring

### 5. Implementador No Encuentra Roadmap
- Archivo corrupto/no existe
- **Solución**: Fallback a consulta directa al acolyte

### 6. Roadmap Parcial
- Acolyte se apaga antes de completar roadmap
- **Solución**: Roadmap incremental, cada fase independiente

## ✅ VALIDACIONES CRÍTICAS

### TodoWrite Limitation
**DESCUBRIMIENTO**: Solo Claude puede usar TodoWrite, agentes NO.
- Agentes usan scripts externos
- Coordinación debe centralizarse en Claude

### Granularidad
**Pregunta resuelta**: ¿Hasta qué nivel detallar?
- **Archivo completo**: "Crear AuthService.js" 
- **Función por función**: "Crear AuthService.login(), luego logout()"
- **Decisión**: Nivel archivo con especificaciones de funciones clave

## 🎯 PRÓXIMOS PASOS

### Implementación Inmediata
1. **Actualizar templates** con roadmap protocols
2. **Crear estructura /project** para evolución de docs
3. **Definir formato estándar** module_roadmap.md
4. **Probar flujo completo** con caso dashboard

### Validación  
1. Probar caso multi-módulo (orders → users → database)
2. Verificar que timeline matemático funciona
3. Confirmar que acolytes pueden autodescubrir dependencias
4. Validar que coordinación previene conflictos

---

## 🔄 PROPUESTA MEJORA: PROTOCOLO TIPO TCP/IP PARA FLAGS

### Analogía TCP/IP vs Sistema FLAGS Actual

**TCP/IP Ejemplo**: Enviar archivo login.js de A → B
```
1. SYN        - A: "¿Puedes recibir archivo?"
2. SYN-ACK    - B: "Sí, puerto 8080 listo"  
3. ACK        - A: "OK, empezando envío"
4. DATA[1]    - A: "Paquete 1/10: function login..."
5. ACK[1]     - B: "Paquete 1 recibido OK"
6. DATA[2]    - A: "Paquete 2/10: const user = await..."
7. ACK[2]     - B: "Paquete 2 recibido OK"
8. DATA[3] se pierde → TIMEOUT → A reenvía automáticamente
9. FIN        - A: "Archivo completo"
10. ACK       - B: "Todo recibido, cerrando"
```

**Sistema FLAGS Actual**: Acolyte → Backend implementar login()
```
1. CREATE-FLAG    - Acolyte: "Implementa login() en AuthService.js"
2. [AGENTE MUERTO - no confirma recepción]
3. [Claude invoca backend]
4. WORK           - Backend: *hace el código*
5. COMPLETE-FLAG  - Backend: "Login() implementado" 
6. NEW-FLAG       - Backend: "Trabajo terminado"
7. COMPLETE-FLAG  - Acolyte: "OK recibido"
```

### Gaps Identificados vs TCP/IP

❌ **CONFIRMACIÓN RECEPCIÓN**: TCP tiene SYN-ACK, FLAGS no confirma recepción
❌ **ACKNOWLEDGMENT INMEDIATO**: TCP confirma cada paquete, FLAGS solo al final  
❌ **TIMEOUT & RETRY**: TCP reenvía automáticamente, FLAGS se quedan colgadas
❌ **PROGRESO**: TCP dice "paquete 3/10", FLAGS no reportan avance

### Mejoras Propuestas (Limitadas por Arquitectura)

**IMPORTANTE**: Los agentes NO están siempre vivos, solo cuando Claude los invoca.

#### 1. FLAG Acknowledgment Inmediato
```bash
# Agente confirma recepción al nacer
uv run python ~/.claude/scripts/agent_db.py ack-flag [FLAG_ID] "@backend.nodejs" --status "received"
```

#### 2. Progress Tracking Básico  
```bash
# Agente reporta progreso antes de empezar trabajo principal
uv run python/.claude/scripts/agent_db.py update-flag [FLAG_ID] --progress "starting_implementation"
# Durante trabajo (si es largo)
uv run python/.claude/scripts/agent_db.py update-flag [FLAG_ID] --progress "50_percent_complete"  
```

#### 3. Timeout Detection (por @flags.agent)
```bash
# @flags.agent detecta FLAGS abandonadas > 10 min
uv run python/.claude/scripts/agent_db.py query "SELECT * FROM flags WHERE status='pending' AND created_at < datetime('now', '-10 minutes')"
```

#### 4. Retry Mechanism
```bash
# @flags.agent reenvía FLAGS no respondidas  
uv run python/.claude/scripts/agent_db.py retry-flag [FLAG_ID] --attempt 2 --reason "timeout_detected"
```

### Limitaciones Arquitecturales

**NO ES POSIBLE**:
- Stream continuo (agentes muertos la mayoría del tiempo)
- Notificaciones push (no hay agentes escuchando)  
- Comunicación directa agent-to-agent (pasan por Claude)
- Updates tiempo real automáticos

**SÍ ES POSIBLE**:
- Confirmaciones inmediatas al nacer
- Progress updates puntuales durante trabajo
- Timeout detection por coordinador (@flags.agent)
- Retry logic coordinado por Claude

### Implementación Dashboard

Con estas mejoras, el dashboard podría mostrar:
- 🟢 FLAGS confirmadas vs 🔴 FLAGS sin confirmar
- 📊 Progreso trabajo en tiempo real  
- ⏰ FLAGS con timeout detectado
- 🔄 FLAGS reenviadas automáticamente

---

**NOTA PARA FUTURO CLAUDE**: Este documento contiene análisis completo del sistema de coordinación de agentes. Los agentes NO TIENEN MEMORIA entre invocaciones - cada vez empiezan desde cero y deben ser completamente autónomos basándose en documentación y memorias SQLite.