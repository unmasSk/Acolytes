# 🗺️ ROADMAP COMPLETO - ClaudeSquad 2.0

**Última actualización**: 2024-12-08
**Versión**: 2.0 - Con todas las decisiones arquitectónicas

## 🎯 VISIÓN ÚNICA DE CLAUDESQUAD

**Lo que NADIE más hace:**
- **Agentes Dinámicos**: Genera agentes especializados basados en TUS módulos
- **Setup Inteligente**: Analiza tu proyecto y crea agentes específicos
- **Memoria POR PROYECTO**: Sistema de conocimiento persistente local
- **Orquestación por Claude**: Claude ES el orquestador principal, no un agente

### Ejemplo de la Magia:
```
Tu proyecto tiene:
backend/
├── api/
├── db/
├── core/
├── embeddings/
└── semantic/

ClaudeSquad genera automáticamente:
- api-agent.md (NO specialist, los agents son dinámicos)
- db-agent.md  
- core-agent.md
- embeddings-agent.md
- semantic-agent.md
```

## 📌 DECISIONES ARQUITECTÓNICAS CLAVE

### Ubicación de Componentes:
- **Agentes Globales**: `~/.claude/agents/` (71 agentes reutilizables)
- **Agentes Dinámicos**: `/proyecto/.claude/agents/` (generados por /setup)
- **Memoria**: `/proyecto/.claude/memory/` (POR PROYECTO, no global)
- **CLAUDE.md**: `/proyecto/CLAUDE.md` (mapeo de agentes del proyecto)

### Nomenclatura:
- **Globales**: `engineer-laravel`, `coordinator-backend` (specialist/engineer/coordinator)
- **Dinámicos**: `api-agent`, `payments-agent` (module-agent, NO specialist)

### Orquestación:
- **Claude ES el orquestador principal** cuando se invoca desde terminal
- **Context-manager es un agente más**, no el orquestador
- Los agentes NO se comunican directamente, lo hacen a través de Claude + memoria

---

## 📋 ROADMAP SIN TIEMPOS - ORDEN LÓGICO DE IMPLEMENTACIÓN

### FASE 1: FUNDACIÓN - Estructura Base
#### 1.1 Reorganizar Estructura de Carpetas ✅ COMPLETADO

⚠️ **CORRECCIÓN IMPORTANTE (2024-12-08):**
La documentación oficial de Claude Code NO confirma si se permiten subdirectorios en `.claude/agents/`.
Los ejemplos muestran estructura PLANA. Por seguridad, usar estructura plana con prefijos.

```
ACTUAL:                          NUEVO (ESTRUCTURA PLANA CONFIRMADA):
.claude/agents/                  .claude/agents/
├── [71 archivos planos]         ├── context-manager.md
                                 ├── coord-backend.md
                                 ├── coord-frontend.md
                                 ├── coord-database.md
                                 ├── eng-laravel.md
                                 ├── eng-react.md
                                 ├── eng-postgres.md
                                 ├── spec-security.md
                                 ├── spec-testing.md
                                 └── [... todos planos con prefijos ...]

# Usar prefijos para organización:
# coord- = Coordinadores
# eng-   = Engineers
# spec-  = Specialists
# util-  = Utilities
# dyn-   = Dinámicos (generados)
```

#### 1.2 Migrar a YAML Frontmatter Estándar ⚠️ EN PROGRESO
**Estado actual (2024-12-09):**
- [x] engineer-laravel.md ✅ COMPLETADO - 1400 líneas
- [x] context-manager.md ✅ COMPLETADO - 466 líneas
- [x] agent-creator.md ✅ COMPLETADO - 240 líneas
- [x] coordinator-backend.md ✅ COMPLETADO - 688 líneas
- [x] coordinator-frontend.md ✅ COMPLETADO - 676 líneas
- [x] coordinator-database.md ✅ COMPLETADO - 719 líneas
- [x] Corregido model: sonnet-3.5 → sonnet en todos los agentes
- [x] Documentado en DOCS/AGENT-YAML-FINDINGS.md que campos extra no causan errores
- [ ] Otros 67 agentes tienen YAML básico pero contenido en [TODO]
- [ ] Decisión: Completar SOLO los agentes críticos ahora, resto al final

**Formato target (como engineer-laravel):**
```yaml
---
name: engineer-[specialty]
description: [Detailed description]
model: haiku|sonnet|opus  # Basado en complejidad
version: 2.0.0
category: engineer|coordinator|specialist
priority: high|medium|low
tools: [List of tools including MCP]
activation: auto|manual
expertise_level: junior|senior|expert
quality_level: mvp|production|enterprise|hyperscale
---
```

#### 1.3 Crear Context Manager Central ✅ COMPLETADO
- [x] Crear `context-manager.md` (adaptado de wshobson)
- [x] Definir protocolo de consulta inicial
- [x] Integrar con todos los agentes

---

### FASE 2: ADOPCIÓN - Mejores Prácticas

#### 2.1 Adaptar Contenido de VoltAgent (120+ agentes)
- [ ] Analizar sus mejores agentes
- [ ] Adaptar contenido a nuestros 71 agentes
- [ ] Mantener nuestra estructura de coordinadores
- [ ] Añadir secciones que ellos tienen y nosotros no

#### 2.2 Integrar Comandos de Orquestación (yzyydev)
- [ ] Adaptar `/start` - Loop infinito
- [ ] Adaptar `/solve` - Resolución paralela
- [ ] Adaptar `/prime` - Context optimization
- [ ] Mantener nuestro `/setup` (único)
- [ ] Completar `/analyze`, `/coordinate`, `/delegate`, `/escalate`

#### 2.3 Añadir Model Specification (wshobson)
- [ ] Añadir campo `model: haiku/sonnet/opus` a YAML
- [ ] Definir criterios de asignación
- [ ] Optimizar por costo/performance

#### 2.4 Implementar Protocolo JSON de Comunicación
- [ ] Crear estándar de mensajes inter-agente
- [ ] Definir tipos de request/response
- [ ] Implementar en agents-registry.json

---

### FASE 3: DIFERENCIACIÓN - Lo Único de ClaudeSquad

#### 3.1 Sistema de Generación Dinámica de Agentes (/setup) ✅ COMPLETADO

##### 3.1.1 Análisis Inteligente del Proyecto con Agent Creator
**El comando `/setup` funciona con proyectos VACÍOS o EXISTENTES:**

```markdown
/setup detecta módulos
    ↓
Claude invoca: "@agent-creator analiza estos módulos y crea sus agentes"
    ↓
agent-creator (ESPECIALISTA IA):
    - Analiza CADA módulo completamente
    - Lee TODOS los archivos
    - Entiende el propósito y patrones
    - Crea agentes con conocimiento COMPLETO embebido
    ↓
Agentes dinámicos creados con 10,000+ líneas si hace falta
```

**DECISIÓN CLAVE (2024-12-09)**: 
- NO usamos scripts Python para analizar
- Usamos un AGENTE ESPECIALISTA (agent-creator) que entiende contexto
- Los agentes dinámicos nacen con TODO el conocimiento, no aprenden después

##### 3.1.2 Template Inteligente para Agentes Dinámicos
**Cada agente dinámico captura TODO sobre su módulo:**

```markdown
---
name: {module}-agent
description: Expert agent for {module_path} module with deep knowledge
module_path: {module_path}
tools: Read, Write, Edit, MultiEdit, Bash, Grep, Glob
---

# {Module} Agent - Module Expert

## Module Intelligence
- **Purpose**: {detected_purpose}
- **Framework**: {framework}
- **Patterns**: {patterns}
- **Database Tables**: {tables}
- **Complexity**: {complexity}/10

## My Deep Knowledge
### Structure
{complete_tree_structure}

### Key Files
{important_files_with_descriptions}

### Dependencies
- Depends on: {modules_i_need}
- Used by: {modules_that_need_me}

### API Contracts
- Input: {what_i_receive}
- Output: {what_i_provide}
- Events: {events_i_emit}

### Testing
- Test location: {test_path}
- Coverage: {coverage}%
- Run: {test_command}

### Common Operations
1. {operation_1_with_steps}
2. {operation_2_with_steps}

### Performance Profile
- Response time: {avg_response}
- Bottlenecks: {known_bottlenecks}
- Optimization opportunities: {suggestions}
```

##### 3.1.3 Generación del CLAUDE.md del Proyecto
**CLAUDE.md mapea TODO para que Claude orqueste correctamente:**

```markdown
# Project: {project_name}

## Architecture
{architecture_summary}

## Dynamic Agents Available
- api-agent: Expert on /backend/api [45k LOC, 89% coverage]
- payments-agent: Expert on /modules/payments [12k LOC, 92% coverage]
- semantic-agent: Expert on /ai/semantic [8k LOC, 76% coverage]

## Global Agents Recommended
Based on your stack, these global agents are relevant:
- engineer-laravel (PHP/Laravel expertise)
- coordinator-database (PostgreSQL management)
- testing-automation (PHPUnit/Pest)

## Orchestration Map
When working on:
- API endpoints → api-agent + engineer-laravel
- Database changes → coordinator-database + affected module agents
- Testing → testing-automation + all module agents
- Security → auditor-security + api-agent

## Project Patterns
- Repository Pattern in use
- Service Layer for business logic
- API Resources for transformations
- Queue jobs for heavy operations

## Critical Paths
- Never modify {protected_files}
- Always run {required_checks}
- Follow {project_conventions}
```

##### 3.1.4 Gestión de Contexto y Tokens
**Cada agente tiene ventana de 200k+ tokens, podemos usar 2000-3000 sin problema:**

```yaml
# Context-manager puede proveer contexto amplio
context_summary:
  current_task: "Add OAuth to API"
  full_architecture: # 500-1000 tokens
    - "Monolith Laravel with 5 modules"
    - "Repository pattern everywhere"
    - "Service layer for business logic"
  module_details: # 1000-1500 tokens
    api_module:
      - "Controllers structure"
      - "Current auth implementation"
      - "Middleware stack"
      - "Rate limiting setup"
  recent_work: # 500 tokens
    - "Last 10 changes to API"
    - "Current sprint goals"
  conventions: # 500 tokens
    - "Always use Resources"
    - "Tests required 90%+"
  total: 2500-3500 tokens  # TOTALMENTE ACEPTABLE
```

##### 3.1.5 Roles Específicos de Agentes

**Agentes Dinámicos (api-agent, payment-agent)**:
- CONOCEN su módulo profundamente
- PROVEEN contexto específico cuando se les pregunta
- REVISAN que las implementaciones sigan SUS convenciones
- DETECTAN duplicaciones y antipatrones en SU dominio
- NO implementan, solo guían y revisan

**Agentes Globales (engineer-laravel, engineer-react)**:
- IMPLEMENTAN el código real
- RECIBEN contexto de los agentes dinámicos
- SIGUEN las convenciones que les indican
- EJECUTAN con su expertise técnico

**Flujo correcto**:
1. Claude pregunta al agente del módulo: "¿Qué necesito saber?"
2. Agente del módulo da contexto completo (2000-3000 tokens)
3. Claude arma prompt para el engineer especialista
4. Engineer implementa
5. Agente del módulo REVISA y valida
6. Si hay issues, se corrigen
7. Se guarda en memoria

#### 3.2 CLAUDE.md Dinámico para el Proyecto
- [ ] Generar CLAUDE.md con mapeo completo
- [ ] Incluir métricas de cada módulo
- [ ] Definir rutas de orquestación
- [ ] Actualizar automáticamente con cambios

---

### FASE 4: MEMORIA - Sistema POR PROYECTO

#### 4.1 Estructura de Memoria Local (Por Proyecto) ✅ COMPLETADO
**DECISIÓN CLAVE: La memoria es POR PROYECTO, no global**
**IMPLEMENTADO 2024-12-09**: Sistema completo con hooks y Python

```
/mi-proyecto/.claude/memory/     # Memoria SOLO de este proyecto
├── context/
│   ├── architecture.md         # Arquitectura de ESTE proyecto
│   ├── decisions.md           # Decisiones de ESTE proyecto
│   ├── conventions.md          # Convenciones de ESTE proyecto
│   └── stack.md               # Stack tecnológico usado
├── modules/
│   ├── api/                   # Conocimiento del módulo API
│   │   ├── patterns.json      # Patrones detectados
│   │   ├── issues.md          # Problemas conocidos
│   │   └── optimizations.md   # Optimizaciones aplicadas
│   └── [cada módulo]/
├── sessions/
│   ├── current.json           # Sesión actual de trabajo
│   └── history/               # Sesiones anteriores
└── consolidated/
    ├── patterns.json          # Patrones consolidados
    ├── antipatterns.json      # Qué evitar
    └── knowledge_graph.json   # Grafo de conocimiento
```

#### 4.2 Scripts de Captura y Carga ✅ COMPLETADO
```python
Scripts implementados:
- memory_manager.py      # Script unificado que maneja todo:
  - save_from_stdin     # Al terminar subagente (SubagentStop)
  - load [agent]        # Carga manual de memoria
  - consolidate [agent] # Consolidación de memoria
  - track_file_change   # Tracking de cambios (PostToolUse)
```

#### 4.3 Sistema de Flags Cross-Domain
- [ ] Implementar detección de impacts
- [ ] Sistema de routing de flags
- [ ] Priority queue para delegaciones
- [ ] Trazabilidad completa

#### 4.4 Hooks para Automatización ✅ COMPLETADO
```json
{
  "SubagentStop": [
    {"matcher": ".*-agent$", "command": "python .claude/scripts/memory_manager.py save_from_stdin"},
    {"matcher": "engineer-.*", "command": "python .claude/scripts/memory_manager.py save_from_stdin"},
    {"matcher": "coordinator-.*", "command": "python .claude/scripts/memory_manager.py save_from_stdin"}
  ],
  "PostToolUse": [
    {"tool": "Edit|Write|MultiEdit", "command": "python .claude/scripts/memory_manager.py track_file_change"}
  ]
}
```
**Nota**: SubagentStart no es necesario porque los agentes siempre inician fresh

---

### FASE 5: INTEGRACIÓN - MCP y Herramientas

#### 5.1 MCP Servers Esenciales
- [ ] Memory Server (knowledge graph)
- [ ] GitHub Server (con auto-PR)
- [ ] PostgreSQL Server
- [ ] Docker Server
- [ ] Filesystem (mejorado)

#### 5.2 Herramientas Especializadas
- [ ] magic (de VoltAgent)
- [ ] context7 (de VoltAgent)
- [ ] playwright (para testing)
- [ ] Herramientas custom por módulo

---

### FASE 6: INTELIGENCIA - Optimización y Learning

#### 6.1 Métricas y Analytics
- [ ] Track de performance por agente
- [ ] Métricas de delegación
- [ ] Success rate tracking
- [ ] Context usage optimization

#### 6.2 Auto-Optimización
- [ ] Routing inteligente basado en métricas
- [ ] Ajuste de modelos por tarea
- [ ] Consolidación inteligente de memoria
- [ ] Pattern recognition automático

#### 6.3 Dashboard de Monitoreo
- [ ] Estado de agentes
- [ ] Memoria usage
- [ ] Performance metrics
- [ ] Cross-domain communications

---

### FASE 7: TESTING - Validación Completa

#### 7.1 Test del Sistema Base
- [ ] Test de cada coordinador
- [ ] Test de delegación
- [ ] Test de comunicación JSON
- [ ] Test de context manager

#### 7.2 Test de Generación Dinámica
- [ ] Proyectos Laravel
- [ ] Proyectos React
- [ ] Proyectos Python
- [ ] Proyectos mixtos

#### 7.3 Test de Memoria
- [ ] Captura correcta
- [ ] Carga efectiva
- [ ] Consolidación sin pérdida
- [ ] Cross-domain flags

#### 7.4 Test de Orquestación
- [ ] Comandos /start, /solve, /prime
- [ ] Procesamiento paralelo
- [ ] Infinite loops
- [ ] Error handling

---

## 🔄 FLUJO COMPLETO DE TRABAJO

### Flujo 1: Setup Inicial
```mermaid
Usuario ejecuta: claude /setup
         ↓
Analiza estructura del proyecto
         ↓
Detecta módulos (api/, payments/, etc)
         ↓
Genera agentes dinámicos (api-agent.md)
         ↓
Crea estructura de memoria local
         ↓
Genera CLAUDE.md con mapeo
         ↓
Proyecto listo para ClaudeSquad
```

### Flujo 2: Trabajo Normal (CORREGIDO)
```mermaid
Usuario: claude "implementa OAuth en API"
         ↓
Claude lee memoria proyecto (2000-3000 tokens está bien)
         ↓
Claude pregunta a api-agent: "¿Cómo implementar OAuth aquí?"
         ↓
api-agent responde con contexto del módulo:
  - Estructura actual de auth
  - Archivos relevantes
  - Patrones usados
  - Qué NO hacer (duplicaciones)
         ↓
Claude genera prompt completo para engineer-laravel
         ↓
engineer-laravel implementa con toda la info
         ↓
api-agent REVISA la implementación:
  - ¿Sigue convenciones del módulo?
  - ¿No duplicó código?
  - ¿Está en los archivos correctos?
  - ¿Tests incluidos?
         ↓
Si hay problemas → api-agent pide correcciones
         ↓
Guardar en memoria del proyecto
```

### Flujo 3: Comunicación Inter-Agente
```
NO directa: Agent A → Memoria → Claude → Agent B
SÍ a través de Claude y memoria del proyecto
```

---

### FASE 8: DOCUMENTACIÓN - Professional Grade

#### Documentos Creados
- ✅ `DOCS/AGENT-YAML-FINDINGS.md` (2024-12-09)
  - Investigación completa sobre campos YAML válidos
  - Campos confirmados vs campos custom
  - Evidencia de que campos extra no causan errores
  - Correcciones aplicadas (model: sonnet-3.5 → sonnet)

#### 8.1 Documentación de Usuario
- [ ] README principal actualizado
- [ ] Guía de instalación
- [ ] Guía de uso
- [ ] Ejemplos prácticos

#### 8.2 Documentación Técnica
- [ ] Arquitectura del sistema
- [ ] Protocolo de comunicación
- [ ] Sistema de memoria
- [ ] API de generación dinámica

#### 8.3 Documentación por Agente
- [ ] Cada agente con docs completa
- [ ] Ejemplos de uso
- [ ] Patterns y best practices
- [ ] Troubleshooting

---

### FASE 9: AUTOMATIZACIÓN - Deployment

#### 9.1 Instalador Automático
- [ ] Script de instalación one-click
- [ ] Detección de OS
- [ ] Verificación de prerequisites
- [ ] Setup wizard interactivo

#### 9.2 Herramientas de Gestión
- [ ] CLI para gestión de agentes
- [ ] Backup/restore de memoria
- [ ] Import/export de configuración
- [ ] Update mechanism

---

### FASE 10: PUBLICACIÓN - Release

#### 10.1 Preparación
- [ ] Version tagging
- [ ] CHANGELOG completo
- [ ] Migration guide desde otros sistemas
- [ ] Compatibility matrix

#### 10.2 Lanzamiento
- [ ] GitHub release
- [ ] Announcement post
- [ ] Demo videos
- [ ] Comparison table con otros sistemas

---

## 🎯 ORDEN DE PRIORIDAD SUGERIDO

### CRÍTICO - Sin esto no funciona
1. Estructura de carpetas + YAML
2. Context manager
3. Adaptar contenido base de agentes
4. Comando /setup mejorado

### IMPORTANTE - Diferenciadores clave
5. Generación dinámica de agentes
6. Sistema de memoria
7. Comandos de orquestación
8. Protocolo JSON

### VALIOSO - Mejoras significativas
9. MCP servers
10. Hooks automation
11. Model specification
12. Cross-domain flags

### NICE-TO-HAVE - Polish
13. Métricas
14. Dashboard
15. Auto-optimización
16. Instalador automático

---

## 📊 CHECKPOINTS DE VALIDACIÓN

### Checkpoint 1: "Base Funcional"
- [ ] 10 agentes core funcionando
- [ ] Context manager operativo
- [ ] YAML frontmatter en todos
- [ ] Estructura de carpetas nueva

### Checkpoint 2: "Diferenciación"
- [ ] Generación dinámica funcionando
- [ ] Memoria básica capturando
- [ ] Comandos de orquestación
- [ ] 30 agentes completos

### Checkpoint 3: "Sistema Completo"
- [ ] 71 agentes funcionando
- [ ] Memoria cross-domain
- [ ] Hooks automáticos
- [ ] MCP servers integrados

### Checkpoint 4: "Production Ready"
- [ ] Testing completo
- [ ] Documentación lista
- [ ] Instalador automático
- [ ] Métricas funcionando

---

## ❓ PREGUNTAS FRECUENTES (FAQ)

### ¿Dónde van los agentes?
- **Globales (71)**: `~/.claude/agents/` - Reutilizables en todos los proyectos
- **Dinámicos**: `/proyecto/.claude/agents/` - Específicos del proyecto

### ¿Quién es el orquestador?
- **Claude ES el orquestador principal** cuando ejecutas desde terminal
- Context-manager es solo un agente que gestiona memoria

### ¿La memoria es global o local?
- **LOCAL por proyecto** en `/proyecto/.claude/memory/`
- Cada proyecto tiene su propia memoria aislada

### ¿Cómo se comunican los agentes?
- **NO directamente** entre ellos
- Siempre a través de Claude + memoria del proyecto

### ¿Qué hace /setup exactamente?
1. Analiza tu proyecto (vacío o existente)
2. Detecta módulos y tecnologías
3. Genera agentes dinámicos inteligentes (api-agent, etc)
4. Crea estructura de memoria
5. Genera CLAUDE.md con mapeo completo

### ¿Los agentes dinámicos son inteligentes?
**SÍ**, capturan:
- Estructura completa del módulo
- Patrones y convenciones
- Dependencies y relaciones
- Tests y cobertura
- Performance metrics
- Common operations

### ¿Cuántos tokens puede usar el context-manager?
- Cada agente tiene ventana de 200k+ tokens
- Puede proveer contexto de 2000-3000 tokens sin problema
- Solo información relevante para la tarea actual
- No hay que ser tacaño con el contexto

### ¿Qué son los Cross-Domain Flags?
- Notificaciones cuando un cambio afecta otros módulos
- Ejemplo: cambio en DB → flag para actualizar models
- Claude los lee y activa agentes necesarios

### ¿Necesito instalar MCP servers?
- **NO para empezar** - funcionan las herramientas nativas
- **Opcional**: magic-mcp, context7 para features avanzadas
- Los agentes usan Bash para ejecutar comandos

### ¿Quién hace qué en el sistema?

**Agentes Dinámicos (api-agent, payment-agent)**:
- ✅ Conocen su módulo profundamente
- ✅ Proveen contexto cuando se les pregunta
- ✅ Revisan implementaciones
- ✅ Detectan duplicaciones
- ❌ NO implementan código

**Agentes Globales (engineer-laravel, engineer-react)**:
- ✅ Implementan código real
- ✅ Tienen expertise técnico
- ✅ Siguen convenciones indicadas
- ❌ NO conocen el proyecto específico

**Claude (Orquestador)**:
- ✅ Coordina todo
- ✅ Pregunta a agentes dinámicos
- ✅ Instruye a agentes globales
- ✅ Gestiona memoria

### ¿Cuál es la diferencia con otros sistemas?
- **VoltAgent**: No tiene memoria ni agentes dinámicos
- **wshobson**: Sin generación dinámica
- **yzyydev**: Sin memoria persistente
- **ClaudeSquad**: TODO lo anterior + flujo inteligente de revisión

## 🚀 RESULTADO FINAL ESPERADO

**ClaudeSquad 2.0:**
- ✅ Único sistema con generación dinámica de agentes
- ✅ Memoria persistente POR PROYECTO
- ✅ Orquestación inteligente por Claude
- ✅ Se adapta a CUALQUIER proyecto
- ✅ Aprende y mejora con el uso
- ✅ Agentes que conocen PROFUNDAMENTE cada módulo

**Ventaja Competitiva:**
Mientras otros dan agentes genéricos, ClaudeSquad crea agentes ESPECÍFICOS para TU proyecto, con memoria persistente y aprendizaje continuo.

---

*Roadmap creado: 2024-12-08*
*Actualizado con todas las decisiones arquitectónicas*
*Sin restricciones de tiempo - Implementar en orden lógico*
*Cada fase se valida antes de continuar*