# Memory Server MCP - Guía de Uso para ClaudeSquad

## Overview

Memory Server es un servidor MCP que implementa un **grafo de conocimiento persistente** para Claude Code. Permite almacenar entidades, relaciones y observaciones que persisten entre todas las sesiones de Claude.

## Estado de Instalación

✅ **INSTALADO Y FUNCIONANDO** (14 de Agosto, 2025)

```bash
# Comando de instalación usado
claude mcp add-json server-memory --scope user '{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-memory"]
}'

# Verificación
claude mcp list
# Output: server-memory: npx -y @modelcontextprotocol/server-memory - ✓ Connected
```

## Arquitectura y Conceptos

### Grafo de Conocimiento
```
Entidad A ----[relación]----> Entidad B
    |                              |
[observaciones]              [observaciones]
```

### Componentes Clave

1. **Entidades**: Nodos del grafo con nombre y tipo
   - Ejemplo: "ClaudeSquad Project" (tipo: Project)
   - Ejemplo: "engineer-laravel" (tipo: Agent)

2. **Relaciones**: Conexiones dirigidas entre entidades
   - Ejemplo: ClaudeSquad Project --[has_gold_standard]--> engineer-laravel

3. **Observaciones**: Lista de hechos sobre una entidad
   - Ejemplo: ["77 agentes especializados", "Usa sistema FLAGS"]

### Almacenamiento

- **Ubicación**: `~/.cache/claude/mcp-servers/memory/memory.json`
- **Formato**: JSON plano
- **Persistencia**: Automática en cada operación
- **Compartido**: Entre todas las sesiones de Claude

## API Completa

### 1. create_entities
Crear nuevas entidades con observaciones iniciales.

```javascript
mcp__server-memory__create_entities({
  entities: [
    {
      name: "ClaudeSquad Project",
      entityType: "Project",
      observations: [
        "77 agentes especializados",
        "Sistema FLAGS para coordinación"
      ]
    }
  ]
})
```

### 2. create_relations
Crear relaciones entre entidades existentes.

```javascript
mcp__server-memory__create_relations({
  relations: [
    {
      from: "ClaudeSquad Project",
      to: "engineer-laravel",
      relationType: "has_gold_standard"
    }
  ]
})
```

### 3. add_observations
Añadir observaciones a entidades existentes.

```javascript
mcp__server-memory__add_observations({
  observations: [
    {
      entityName: "engineer-laravel",
      contents: [
        "Probado exitosamente con context7",
        "Tiempo promedio: 40 minutos"
      ]
    }
  ]
})
```

### 4. search_nodes
Buscar entidades por palabra clave.

```javascript
mcp__server-memory__search_nodes({
  query: "Laravel"
})
// Devuelve entidades y relaciones que contienen "Laravel"
```

### 5. open_nodes
Abrir nodos específicos por nombre.

```javascript
mcp__server-memory__open_nodes({
  names: ["engineer-laravel", "FLAGS System"]
})
// Devuelve solo estas entidades y sus relaciones
```

### 6. read_graph
Leer el grafo completo.

```javascript
mcp__server-memory__read_graph()
// Devuelve todas las entidades y relaciones
```

### 7. delete_entities
Eliminar entidades y sus relaciones.

```javascript
mcp__server-memory__delete_entities({
  entityNames: ["entidad_obsoleta"]
})
```

### 8. delete_observations
Eliminar observaciones específicas.

```javascript
mcp__server-memory__delete_observations({
  deletions: [
    {
      entityName: "engineer-laravel",
      observations: ["observación obsoleta"]
    }
  ]
})
```

### 9. delete_relations
Eliminar relaciones específicas.

```javascript
mcp__server-memory__delete_relations({
  relations: [
    {
      from: "Entidad A",
      to: "Entidad B",
      relationType: "relación_obsoleta"
    }
  ]
})
```

## Casos de Uso para ClaudeSquad

### 1. Gestión de Agentes
```javascript
// Registrar un nuevo agente
create_entities([{
  name: "engineer-react",
  entityType: "Agent",
  observations: [
    "Especialista en React 18+",
    "Integra con context7",
    "1200 líneas de documentación"
  ]
}])

// Relacionar con el proyecto
create_relations([{
  from: "ClaudeSquad Project",
  to: "engineer-react",
  relationType: "contains"
}])
```

### 2. Tracking de Decisiones Arquitectónicas
```javascript
// Crear decisión
create_entities([{
  name: "Decision: Usar MCP Memory",
  entityType: "ArchitecturalDecision",
  observations: [
    "Fecha: 14 Agosto 2025",
    "Razón: Persistencia entre sesiones",
    "Alternativa considerada: Solo JSON local"
  ]
}])

// Relacionar con proyecto
create_relations([{
  from: "ClaudeSquad Project",
  to: "Decision: Usar MCP Memory",
  relationType: "implements_decision"
}])
```

### 3. Sistema FLAGS Integration
```javascript
// Cuando se crea un FLAG
create_entities([{
  name: "FLAG-2025-08-14-001",
  entityType: "FLAG",
  observations: [
    "Tipo: Cross-domain",
    "Módulo afectado: Authentication",
    "Prioridad: Alta",
    "Estado: Pendiente"
  ]
}])

// Relacionar con agentes
create_relations([
  {
    from: "FLAG-2025-08-14-001",
    to: "engineer-laravel",
    relationType: "requires_action"
  }
])
```

### 4. Búsquedas Inteligentes
```javascript
// Buscar todo sobre Laravel
search_nodes("Laravel")

// Buscar decisiones
search_nodes("Decision")

// Buscar FLAGS pendientes
search_nodes("Pendiente")
```

## Mejores Prácticas

### Nomenclatura de Entidades
```
✅ BUENO:
- "engineer-laravel" (específico, único)
- "Decision: Usar TypeScript" (categorizado)
- "FLAG-2025-08-14-001" (identificable)

❌ EVITAR:
- "agente" (muy genérico)
- "decisión importante" (poco específico)
- "flag1" (sin contexto)
```

### Tipos de Entidad Recomendados
- **Project**: Proyectos principales
- **Agent**: Agentes de ClaudeSquad
- **System**: Sistemas como FLAGS
- **Configuration**: Configuraciones
- **Decision**: Decisiones arquitectónicas
- **FLAG**: FLAGS del sistema
- **Module**: Módulos del proyecto
- **Resource**: Recursos externos

### Relaciones Semánticas
```
✅ CLARAS:
- has_gold_standard
- implements
- uses
- requires_action
- depends_on

❌ AMBIGUAS:
- related_to
- connects
- links
```

## Comparación con Sistema JSON Actual

| Aspecto | Memory Server | JSON de Agentes |
|---------|--------------|-----------------|
| **Alcance** | Global, todas las sesiones | Por proyecto |
| **Persistencia** | Automática | Manual |
| **Búsqueda** | Integrada, semántica | Requiere código |
| **Relaciones** | Nativas, grafo | No soportadas |
| **Escalabilidad** | Miles de entidades | Cientos |
| **Control** | Mediante API | Total |

## Integración Recomendada

### Usar Memory Server para:
- Conocimiento permanente del proyecto
- Relaciones entre agentes
- Decisiones arquitectónicas
- FLAGS históricos
- Patrones aprendidos

### Mantener JSON para:
- Estado operacional inmediato
- FLAGS activos
- Configuraciones locales
- Cache temporal
- Datos sensibles

## Pruebas Realizadas

### Tests Exitosos (14/08/2025)
1. ✅ Crear entidades básicas
2. ✅ Crear relaciones complejas
3. ✅ Búsqueda por palabras clave
4. ✅ Añadir observaciones
5. ✅ Leer grafo completo
6. ✅ Abrir nodos específicos
7. ✅ Persistencia verificada

### Comportamientos Observados
- Las entidades persisten entre sesiones
- Las búsquedas son case-insensitive
- Las observaciones se acumulan
- Las relaciones son direccionales
- No hay límite práctico de almacenamiento

## Troubleshooting

### "Entity not found"
```javascript
// Verificar que existe
read_graph()
// Buscar el nombre exacto

// Crear si no existe
create_entities([{name: "entidad", ...}])
```

### Datos no persisten
```bash
# Verificar archivo de memoria
cat ~/.cache/claude/mcp-servers/memory/memory.json

# Verificar permisos
ls -la ~/.cache/claude/mcp-servers/memory/
```

### Búsquedas no devuelven resultados
```javascript
// Usar términos más generales
search_nodes("agent")  // en vez de "agente-específico"

// Verificar el grafo completo
read_graph()
```

## Comandos Útiles

### Inicialización para ClaudeSquad
```javascript
// Crear estructura base
create_entities([
  {name: "ClaudeSquad Project", entityType: "Project", observations: [...]},
  {name: "engineer-laravel", entityType: "Agent", observations: [...]},
  {name: "FLAGS System", entityType: "System", observations: [...]}
])

// Crear relaciones fundamentales
create_relations([
  {from: "ClaudeSquad Project", to: "engineer-laravel", relationType: "has_gold_standard"},
  {from: "ClaudeSquad Project", to: "FLAGS System", relationType: "implements"}
])
```

### Consultas Frecuentes
```javascript
// Ver todo el conocimiento
read_graph()

// Buscar agentes
search_nodes("Agent")

// Ver FLAGS
search_nodes("FLAG")

// Ver decisiones
search_nodes("Decision")
```

## Limitaciones Importantes Descubiertas

### No hay inicialización automática
- Claude NO busca automáticamente en Memory Server al inicio
- Requiere invocación manual o instrucciones explícitas
- SOLUCIÓN: Implementamos SESSION-INIT-CONTEXT pattern

### No puede acceder a archivos
- Memory Server NO puede leer /SESSIONS/ ni otros archivos
- Solo trabaja con su propio grafo de conocimiento
- SOLUCIÓN: Actualizar SESSION-INIT-CONTEXT al final de cada sesión

## Pattern SESSION-INIT-CONTEXT

### Implementación
1. **Entidad especial creada**: SESSION-INIT-CONTEXT con todo el contexto del proyecto
2. **CLAUDE.md actualizado**: Instrucciones para buscar esta entidad al inicio
3. **Actualización periódica**: Usar `/save-session` al final de cada sesión

### Uso
```javascript
// Al inicio de cada conversación (si Claude no lo hace automático)
mcp__server-memory__search_nodes("SESSION-INIT-CONTEXT")

// Para actualizar el contexto
mcp__server-memory__add_observations({
  observations: [{
    entityName: "SESSION-INIT-CONTEXT",
    contents: ["Nueva información de la sesión"]
  }]
})
```

## Comando /save-session

Comando personalizado que:
1. Resume la sesión actual
2. Actualiza SESSION-INIT-CONTEXT
3. Guarda logros, pendientes y aprendizajes
4. Incluye "sensación" de la conversación (calidad, inventos del agente, etc.)

## Ubicación Real del Archivo

**NO CONFIRMADA**: El archivo memory.json no está en las ubicaciones estándar documentadas.
**PERO FUNCIONA**: La persistencia está verificada y funcional.
**Probable ubicación**: Gestionada internamente por el servidor MCP.

## Próximos Pasos

1. ✅ SESSION-INIT-CONTEXT pattern implementado
2. ✅ CLAUDE.md actualizado con instrucciones
3. ⏳ Comando /save-session en desarrollo
4. Usar este pattern consistentemente
5. Actualizar contexto al final de cada sesión

---

*Última actualización: 14 de Agosto, 2025 - 23:00*
*Estado: ✅ FUNCIONANDO CON LIMITACIONES CONOCIDAS*
*Probado con: ClaudeSquad Project*
*Sesiones documentadas: Instalación y prueba de 6 MCP servers*