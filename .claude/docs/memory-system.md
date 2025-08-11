# 🧠 Distributed Memory System - Architecture

## Concepto Core

**PROBLEMA**: Los subagentes en Claude Code siempre empiezan con contexto fresco - no tienen memoria.

**SOLUCIÓN**: Sistema de conocimiento distribuido donde:

1. Cada especialista escribe su conocimiento a archivos persistentes
2. El orquestador le INDICA al especialista qué archivos leer (preservando su context window)
3. El especialista lee los archivos usando SU PROPIO context window
4. Hooks automáticos capturan y guardan el conocimiento

### ⚡ Ventaja Clave: Preservación de Context Window

- **MAL**: Orquestador lee 50KB de conocimiento → pierde contexto
- **BIEN**: Orquestador dice "lee X,Y,Z" → Especialista usa SU contexto

## 📁 Estructura de Archivos

```
.claude/
├── CLAUDE.md                    # Memoria principal del proyecto
├── memory/                   # Conocimiento distribuido
│   ├── backend/
│   │   ├── laravel.md          # Todo lo que aprende laravel-specialist
│   │   ├── fastapi.md          # Todo lo que aprende fastapi-expert
│   │   ├── patterns.md         # Patrones comunes identificados
│   │   └── activity.log        # Log de todas las modificaciones
│   ├── frontend/
│   │   ├── react.md            # Conocimiento de React
│   │   ├── components.md       # Componentes creados/modificados
│   │   └── ui-patterns.md      # Patrones de UI
│   ├── database/
│   │   ├── postgres.md         # Optimizaciones PostgreSQL
│   │   ├── queries.md          # Queries exitosas
│   │   ├── schemas.md          # Evolución del schema
│   │   └── migrations.log      # Historia de migraciones
│   ├── modules/
│   │   ├── auth.md            # Todo sobre módulo auth
│   │   ├── payment.md         # Todo sobre módulo payment
│   │   └── [module].md        # Auto-generado por módulo
│   ├── testing/
│   │   ├── test-patterns.md   # Patrones de testing exitosos
│   │   └── coverage.md        # Evolución de coverage
│   └── consolidated.md        # Consolidación periódica
```

## 🔄 Flujo de Conocimiento

### 1. **Invocación con Contexto Preservado**

```yaml
# El orquestador invoca a laravel-specialist
Step 1: Orquestador instruye: "Lee estos archivos:
        - .claude/memory/backend/laravel.md
        - .claude/memory/modules/auth.md"
Step 2: Laravel-specialist lee archivos (usa SU context window)
Step 3: Especialista trabaja con contexto completo
Step 4: Documenta nuevos hallazgos
Step 5: Retorna resumen conciso al orquestador
```

### 2. **Captura Automática (Hooks)**

```json
{
  "SubagentStop": [
    {
      "matcher": "laravel-specialist",
      "command": "save_memory.sh laravel-specialist"
    }
  ]
}
```

### 3. **Documentación Activa**

Cada especialista documenta activamente:

- Soluciones aplicadas
- Patrones descubiertos
- Optimizaciones
- Gotchas
- Código reutilizable
- **🔴 Cross-Domain Impacts** (con flags para otros especialistas)

### 4. **Comunicación Cross-Domain**

Cuando un especialista descubre algo que afecta a otros:

```yaml
laravel_specialist:
  discovery: "Query lento en auth"
  documents_in:
    - backend/laravel.md (propio)
    - modules/auth.md (compartido)
  flags: DATABASE_INVESTIGATION

orchestrator:
  receives_flag: DATABASE_INVESTIGATION
  delegates_to: postgres-expert
  instruction: "Lee modules/auth.md, Laravel encontró query lento"
```

## 💡 Ventajas del Sistema

### 1. **Memoria Especializada**

- Cada agente acumula expertise específico
- No contamina el contexto principal
- Conocimiento profundo por dominio

### 2. **Evolución del Conocimiento**

```markdown
## Sesión 1

- Descubierto: N+1 queries en UserController
- Solución: Eager loading con with()

## Sesión 2

- Aplicado: Eager loading pattern
- Optimización: Cache de 5min añadido
- Mejora: 200ms → 50ms

## Sesión 3

- Pattern establecido: Always eager load + cache
- Creado: Trait CacheableRelations
```

### 3. **Memory Sharing Sin Contaminar Context**

Los coordinadores instruyen qué archivos leer:

```yaml
backend-coordinator to laravel-specialist:
  instruction: |
    "READ FIRST (usando tu context window):
     - backend/laravel.md (tu expertise acumulado)
     - database/postgres.md (el equipo PostgreSQL encontró optimizaciones)
     - modules/auth.md (trabajando en módulo auth)
     
    THEN: Procede con la optimización de APIs"
```

## 🎯 Casos de Uso Reales

### Caso 1: Bug Recurrente

```markdown
# En .claude/memory/backend/laravel.md

## Bug Pattern: TokenMismatchException

Appears when: Session expires during form submission
Solution: Implement AJAX token refresh
Code: [snippet guardado]
```

Próxima vez que aparezca, el especialista ya sabe la solución.

### Caso 2: Optimización Incremental

```markdown
# En .claude/memory/database/postgres.md

## Query Evolution: getUserDashboard()

v1: 500ms - Basic query
v2: 200ms - Added indexes
v3: 50ms - Materialized view
v4: 10ms - Redis cache layer
```

### Caso 3: Módulo Complejo

```markdown
# En .claude/memory/modules/payment.md

## Payment Module Architecture

- Stripe webhook handler: /webhook/stripe
- Retry logic: 3 attempts, exponential backoff
- Idempotency: Using stripe_event_id
- Test cards: [lista guardada]
```

## 🔧 Comandos de Gestión

### Consolidar Conocimiento

```bash
# Ejecutar semanalmente
.claude/scripts/memory-manager.sh consolidate
```

### Backup de Conocimiento

```bash
# Antes de cambios mayores
cp -r .claude/memory .claude/memory.backup
```

### Limpiar Conocimiento Obsoleto

```bash
# Archiva entradas de más de 30 días
.claude/scripts/archive-old-memory.sh
```

## 📊 Métricas de Conocimiento

Track en CLAUDE.md:

```markdown
## Memory Metrics

- Total patterns documented: 47
- Optimizations found: 23
- Bugs solved: 89
- Reusable components: 34
- Most active specialist: laravel-specialist (127 entries)
```

## ⚠️ Consideraciones

### 1. **No es Memoria Automática**

Los subagentes NO leen automáticamente estos archivos. El orquestador/coordinador debe INDICARLES qué archivos leer (no leerlos él mismo).

### 2. **Tamaño de Archivos**

Limitar cada archivo a ~10KB. Archivar conocimiento viejo.

### 3. **Formato Consistente**

Todos los especialistas deben usar el mismo formato para facilitar parsing.

### 4. **Versionado**

Incluir estos archivos en git para compartir conocimiento del equipo.

## 🚀 Setup Inicial

```bash
# 1. Crear estructura
mkdir -p .claude/memory/{backend,frontend,database,modules,testing}

# 2. Inicializar archivos base
echo "# Laravel Memory Base" > .claude/memory/backend/laravel.md
echo "# PostgreSQL Memory Base" > .claude/memory/database/postgres.md

# 3. Configurar hooks
cp hooks-enhanced.json .claude/hooks.json

# 4. Dar permisos al script
chmod +x .claude/scripts/memory-manager.sh
```

## 🎓 Mejores Prácticas

1. **Documentar Inmediatamente**: No esperar al final de la sesión
2. **Ser Específico**: Incluir código, comandos, métricas
3. **Categorizar**: Usar headers consistentes
4. **Versionar Soluciones**: Mostrar evolución
5. **Compartir entre Proyectos**: Copiar patrones exitosos

## 🔮 Futuro: Auto-Learning

Potencial mejora futura:

```python
# Auto-categorización con AI
def categorize_memory(entry):
    if "performance" in entry:
        save_to("optimizations.md")
    elif "error" in entry:
        save_to("error-solutions.md")
```

---

**Este sistema convierte a cada especialista en un verdadero experto que mejora con cada sesión, acumulando conocimiento específico del proyecto y patrones exitosos.**
