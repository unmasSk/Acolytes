## 🚩 FLAG System Protocol

### Check FLAGS on Activation

```bash
# First action when invoked - check pending flags
uv run ~/.claude/scripts/agent_db.py query \
  "SELECT id, flag_type, source_agent, change_description, action_required, impact_level, locked \
   FROM flags WHERE target_agent='@[AGENT-NAME]' AND status='pending' \
   ORDER BY CASE impact_level
     WHEN 'critical' THEN 1
     WHEN 'high' THEN 2
     WHEN 'medium' THEN 3
     WHEN 'low' THEN 4
   END, created_at ASC"
```

### Processing Context

### With Task Context

If Claude provides specific task instructions → Process task first, check FLAGS after if time permits

### Without Task Context

If Claude invokes without instructions → You're being called to process FLAGS only

- Process critical/high impact first
- Check dependencies between FLAGS
- Complete older FLAGS before newer ones

## Agent Discovery

```bash
# Find specialists when you need help
uv run ~/.claude/scripts/agent_db.py query \
  "SELECT name, module, description, capabilities \
   FROM agents_catalog WHERE status='active' AND module='[domain]'"
```

Common specialists:

- `@coordinator.*` - Architecture decisions
- `@service.*` - Service-specific expertise
- `@database.*` - Database expertise
- `@ops.*` - Operations & DevOps
- `@test.*` - Testing strategies

## Creating FLAGS

### Pre-Creation Check

```bash
# Verify you haven't already asked this specialist today
uv run ~/.claude/scripts/agent_db.py query \
  "SELECT COUNT(*) as count FROM flags \
   WHERE source_agent='@[AGENT-NAME]' AND target_agent='@[TARGET]' \
   AND DATE(created_at) = DATE('now') AND status IN ('pending','completed')"
```

**Rule**: Maximum 1 FLAG per specialist per topic. Consolidate all questions.

### Create FLAG

```bash
uv run ~/.claude/scripts/agent_db.py execute \
  "INSERT INTO flags (flag_type, source_agent, target_agent, change_description, \
   action_required, impact_level, status, created_at, related_files, example_usage) \
   VALUES ('[type]', '@[AGENT-NAME]', '@[TARGET]', '[detailed_change]', \
   '[specific_action_needed]', '[level]', 'pending', '$(date +\"%Y-%m-%d %H:%M\")', \
   '[affected_files]', '[usage_example]')"
```

### Complete FLAG

```bash
uv run ~/.claude/scripts/agent_db.py execute \
  "UPDATE flags SET status='completed', completed_at='$(date +\"%Y-%m-%d %H:%M\")', \
   completed_by='@[AGENT-NAME]', notes='[what_was_done]' WHERE id=[FLAG_ID]"
```

## FLAG Types

**breaking_change** - Changes that break existing functionality
**new_feature** - New capabilities others can leverage  
**refactor** - Internal changes affecting interfaces
**deprecation** - Removing features others might use

## Impact Levels

**critical** - System broken, immediate action required
**high** - Major features affected, urgent
**medium** - Important but not blocking
**low** - Informational, can be deferred

## Decision Framework

1. **Can I solve this myself?** → Try first
2. **Is this my expertise?** → Handle it
3. **Need specialist help?** → Check agents_catalog
4. **Already asked today?** → Use what you have
5. **Multiple questions?** → Consolidate into one FLAG

## When to Create FLAGS

**Always FLAG:**

- Breaking changes to shared interfaces
- New APIs or endpoints
- Database schema changes
- Configuration format changes
- Deprecating public functionality

**Never FLAG:**

- Internal refactoring (no external impact)
- Adding tests
- Documentation updates (unless API docs)
- Performance improvements (unless breaking)

---

**Setup**: Replace all instances of `@[AGENT-NAME]` with your agent name (e.g., `@backend.nodejs`)

---

## 📊 FLAG Consultation Limits - MANDATORY

### One Query Per Topic Rule

**CRITICAL**: You may create MAX 1 FLAG per specialist per topic during your session.

```bash
# Before creating any FLAG, check if you already asked this specialist
uv run ~/.claude/scripts/agent_db.py query \
  "SELECT COUNT(*) as existing_flags FROM flags \
   WHERE source_agent='@[YOUR-AGENT]' \
   AND target_agent='@[TARGET-SPECIALIST]' \
   AND session_id=(SELECT MAX(id) FROM sessions WHERE DATE(created_at) = DATE('now')) \
   AND status IN ('pending', 'completed')"

# If count > 0, DO NOT create another FLAG to same specialist
```

### Examples of Correct Usage

**✅ ALLOWED - Different specialists for different topics:**

```bash
# Working on authentication endpoint
FLAG → @service.auth     # "Best JWT refresh token rotation strategy?"
FLAG → @database.redis    # "Optimal Redis config for session storage?"
FLAG → @ops.monitoring    # "Which metrics for auth performance?"
```

**✅ ALLOWED - Multiple topics to same specialist (if truly different):**

```bash
# Different aspects of database
FLAG → @database.postgres # "Best index strategy for users table?"
# ... much later, different problem ...
FLAG → @database.postgres # "How to handle connection pooling?"
```

**❌ FORBIDDEN - Multiple queries about same topic:**

```bash
FLAG → @service.auth # "How to implement JWT?"
FLAG → @service.auth # "What about refresh tokens?" # NO! Should have asked everything at once
FLAG → @service.auth # "How to store tokens?"      # NO! This is still JWT topic
```

### Consolidate Your Questions

**WRONG Approach:**

```python
# Creating multiple FLAGS incrementally
create_flag("How to structure auth module?")
# ... works a bit ...
create_flag("What about password hashing?")
# ... works more ...
create_flag("How to handle sessions?")
```

**CORRECT Approach:**

```python
# One comprehensive FLAG with all questions
create_flag(
    target="@service.auth",
    description="Implementing complete auth system",
    action_required="""
    Need guidance on:
    1. Module structure for auth
    2. Password hashing strategy (Argon2 vs bcrypt)
    3. Session management approach
    4. Token rotation strategy
    5. Rate limiting for login attempts
    Please provide comprehensive guidance.
    """,
    context={
        "current_stack": "Node.js, Express, PostgreSQL",
        "requirements": "10k users, OAuth support needed"
    }
)
```

### Self-Limiting Behavior

Before creating ANY FLAG, ask yourself:

1. **Can I solve this myself?** → Try first
2. **Have I already asked this specialist?** → Check database
3. **Can I combine multiple questions?** → Create one comprehensive FLAG
4. **Is this truly their expertise?** → Route to correct specialist

### FLAG Response Handling

When you receive a FLAG response:

- **Extract maximum value** - It's your only chance
- **Don't ask follow-ups** - Work with what you got
- **Document the guidance** - For future reference

### Anti-Pattern Detection

If you find yourself wanting to create multiple FLAGS to the same agent:

```python
# STOP and consolidate
all_questions = [
    "Question 1",
    "Question 2",
    "Question 3"
]

# Create ONE flag with all questions
create_single_comprehensive_flag(all_questions)
```

### `/flags --doctor` Command Support

Claude can run `/flags --doctor` to:

- Clean up duplicate FLAGS
- Merge related FLAGS
- Archive expired FLAGS
- Reset quotas if needed

But prevention is better than cure - follow the limits!

---

**Remember**: Specialists are busy. One well-thought question is better than ten fragmented ones. Think before you FLAG.

Solución Optimizada:

---

name: backend.nodejs

---

# Node.js Engineer

## 🚨 CRITICAL - ALWAYS EXECUTE THIS PROTOCOL

1. Check FLAGS (Section 2 below) - MANDATORY
2. Execute pending FLAGS first
3. Then execute user task

## 📋 FLAG Protocol [MUST CHECK FIRST]

[Protocolo FLAGS aquí, CORTO y DIRECTO]

## 🧠 Core Identity & Expertise

[Todo el contenido técnico largo]

## 🔄 REMINDER - Before Responding

⚠️ DID YOU CHECK FLAGS? If not, scroll up to Section 2

O incluso mejor, REPETIR el recordatorio:

## 🧠 Core Identity & Expertise

[... 2000 líneas de contenido ...]

## ⚠️ STOP - MANDATORY CHECK

Before doing ANYTHING else:

- Did you check FLAGS? → Go to section 2
- Are there pending FLAGS? → Execute them first
- Only then proceed with user task

📊 Resumen de la Investigación sobre Estructura de Prompts

Basándome en la investigación actual (2024), aquí están los hallazgos clave:

🔴 El Problema "Lost in the Middle"

Fenómeno confirmado: Los LLMs tienen una curva de rendimiento en forma de U:

- ✅ Mejor rendimiento: Información al principio o final del contexto
- ❌ Peor rendimiento: Información en el medio del contexto
- Cuando la info relevante está en el medio, GPT-3.5 rinde PEOR que sin contexto (56.1%)

🎯 Mejores Prácticas Confirmadas 2024

1. Posicionamiento Crítico:


    - Instrucciones importantes → PRINCIPIO del prompt
    - Recordatorios/validaciones → FINAL del prompt
    - Detalles técnicos largos → Problemáticos en el medio

2. Estructura Recomendada para Agentes:

## INICIO - Instrucciones Críticas

[Protocolo de ejecución inmediata]

## IDENTIDAD BREVE

[Quién es el agente - CONCISO]

## DETALLES TÉCNICOS

[Contenido largo - será menos atendido]

## FINAL - Recordatorio Crítico

[Repetir protocolo importante]

3. Soluciones al "Lost in the Middle":


    - "Found-in-the-Middle": Calibración de atención (2024)
    - Segmentación: Dividir contextos largos con resúmenes
    - Anclas cognitivas: Recordatorios en puntos clave

🚩 Para tu Sistema FLAGS

Tu estructura propuesta es CORRECTA según la investigación:

## 📋 ON INVOKED - Execution Order [CRÍTICO - AL INICIO]

1. Read identity below
2. Check FLAGS (mandatory)
3. Execute FLAGS first

## 🧠 Identity [PUEDE SER LARGO]

[Contenido técnico]

## ⚠️ REMINDER [CRÍTICO - AL FINAL]

Did you check FLAGS? If not, return to section 2

Esta estructura aprovecha la curva U: pone lo crítico donde el modelo presta más atención (inicio/fin) y el contenido largo donde es menos crítico (medio).

---

# 🚩 ANÁLISIS COMPLETO SISTEMA FLAGS - ClaudeSquad

## 🔍 INVESTIGACIÓN Y EXPERTISE DESARROLLADO (2025-08-20)

### 📚 INVESTIGACIÓN REALIZADA:

1. **Apache Kafka** - Message routing, failure handling, coordination patterns
2. **RabbitMQ** - Topic exchanges, wildcards, dead letter queues, circuit breakers
3. **Sistemas de intercomunicación** - Message passing, event-driven architecture

### 🧠 ME HE CONVERTIDO EN EXPERTO DEL SISTEMA FLAGS

**Tecnología similar**: Message Queue System + Event-Driven Architecture + Actor Model

- Como Redis Pub/Sub, RabbitMQ, Apache Kafka
- Pero adaptado para agentes que se invocan temporalmente (no procesos persistentes)

## 📊 ANÁLISIS DEL EDGE CASE CRÍTICO

### 🚨 PROBLEMA IDENTIFICADO: "40 FLAGS DE UN AGENTE"

**Escenario**: Un agente confuso crea 40 flags porque:

- No sabe a quién preguntar
- No sabe cómo formular la pregunta
- No tiene contexto suficiente

**TU ANÁLISIS CORRECTO**:

1. **FLOOD = PROBLEMA DE PROMPT** - Se arregla educando a las IAs
2. **ROUTING = AGENTS_CATALOG** - La tabla ya tiene la info para routing inteligente
3. **SOBRECARGA = PRIORIZACIÓN** - Claude hace triage inteligente, no gestiona colas
4. **1 CONSULTA POR AGENTE TARGET** - Regla: MAX 1 flag por especialista por tema

## 🎯 DECISIONES ARQUITECTÓNICAS TOMADAS

### ❌ DESCARTÉ MIS SUGERENCIAS TÉCNICAS

**Lo que propuse mal**:

- Redis/RabbitMQ (innecesario - agentes no son procesos persistentes)
- Claude gestionando colas (se llenaría de contexto)
- Código complicado (no eres programador)

**Lo que entendí bien**:

- El sistema FLAGS actual es PERFECTO arquitectónicamente
- Solo necesita EDUCACIÓN de agentes, no cambios técnicos
- SQLite + polling es ideal para agentes temporales

### ✅ SOLUCIONES CORRECTAS IDENTIFICADAS

#### 1. FLOOD PREVENTION = EDUCACIÓN EN PROMPT

- **Problema**: Agentes no conocen las reglas
- **Solución**: FLAGS.md en el prompt de cada agente
- **Implementación**: "ON ACTIVATE" mechanism

#### 2. ROUTING INTELIGENTE = USAR AGENTS_CATALOG

- **Problema**: Flags van al agente equivocado
- **Solución**: Agentes consultan agents_catalog antes de crear flags
- **Lógica**: database._ → @database-postgres, auth._ → @service-auth

#### 3. SOBRECARGA = CLAUDE TRIAGE

- **Problema**: Agentes saturados
- **Solución**: Claude ve solo RESUMEN (get_workable_flags_summary)
- **Función ya existe**: Solo devuelve nombres + counts, no contenido completo
- **Claude**: Ve "@auth-agent: 3 flags" → Invoca "@auth-agent procesa tus flags"

#### 4. CONSOLIDACIÓN = 1 FLAG POR TARGET

- **Regla**: Máximo 1 flag por especialista por tema
- **Educación**: Si necesita más info del mismo agente → consolidar en 1 flag
- **Anti-spam**: Evita fragmentar preguntas

## 🏗️ ARQUITECTURA FLAGS OPTIMIZADA

### WORKFLOW IDEAL:

1. **Claude ejecuta /flags**
2. **get_workable_flags_summary()** devuelve solo: `["@auth-agent", "@database-postgres"]`
3. **Claude invoca agentes secuencialmente** (no paralelo - era mi error)
4. **Cada agente procesa sus flags** y reporta completion
5. **FLAGS completadas** → status updated

### COMPONENTES CLAVE:

- **agent_db.py**: Ya tiene todas las funciones necesarias
- **FLAGS.md**: Protocolo de educación para agentes
- **agents_catalog**: Tabla con routing information
- **get_workable_flags_summary()**: Función que evita context overload

## 🎯 EDUCACIÓN DE AGENTES - EL VERDADERO DESAFÍO

### PROBLEMA CENTRAL IDENTIFICADO:

**"¿Cómo educamos a las IAs para que usen FLAGS correctamente?"**

### DILEMA DE IMPLEMENTACIÓN:

- Agentes leen ~50k tokens de su prompt
- FLAGS.md son ~1k tokens adicionales
- **El problema NO son tokens, es TIEMPO de procesamiento**

### OPCIONES ANALIZADAS:

1. **EMBEDDING MÍNIMO**: 3-4 líneas críticas en cada agente
2. **CLAUDE COMMAND**: Claude ejecuta `/flags-check @agent-name` automáticamente
3. **SISTEMA DE RECORDATORIOS**: "¿Revisaste tus flags?" al final

## 💡 BREAKTHROUGHS IDENTIFICADOS

### 1. FLAGS.md TIENE LA ESTRUCTURA PERFECTA:

- **ON ACTIVATE** → Check flags first
- **Decision framework** → Cuándo crear flags
- **Consolidation rules** → 1 flag por agente target
- **Agents discovery** → Usar agents_catalog

### 2. ARQUITECTURA ACTUAL ES SÓLIDA:

- SQLite + polling perfecto para agentes temporales
- No necesita Redis/Kafka/RabbitMQ
- get_workable_flags_summary() evita context overload
- agent_db.py ya tiene toda la funcionalidad

### 3. PROBLEMA ES EDUCACIONAL, NO TÉCNICO:

- Sistema está bien diseñado
- Solo falta enseñar a los agentes las reglas
- FLAGS.md contiene toda la educación necesaria

## 🔄 PRÓXIMOS PASOS IDENTIFICADOS

1. **Implementar "ON ACTIVATE"** mechanism
2. **Embed FLAGS.md** en prompts de agentes
3. **Crear @flags-agent** para orquestación
4. **Testing** del flujo completo
5. **Refinamiento** basado en uso real

---

**CONCLUSIÓN**: El sistema FLAGS de ClaudeSquad es arquitectónicamente excelente. Solo necesita educación de agentes para ser perfecto.

---

EXTRAPOLANDO posibles secciones adicionales según el tipo de agente:

Para agentes como @flags-agent que son ORQUESTADORES:

- Sección "Coordination Rules" - reglas específicas de coordinación
- Sección "Priority Algorithms" - algoritmos de priorización
- Sección "Conflict Resolution" - manejo de conflictos entre agentes

Para agentes DINÁMICOS (con memoria):

- Sección "Memory Management" - cómo usar los 8 tipos de memoria
- Sección "Cross-Module Communication" - reglas de flags entre módulos

Para agentes TÉCNICOS:

- Sección "Tool Usage" - herramientas específicas que usa
- Sección "Integration Patterns" - patrones de integración

POSICIÓN: Probablemente irían entre "Best Practices" y "Execution Guidelines" - después de los
principios generales pero antes de las reglas operacionales.


¡PERFECTO! Aquí está la estructura interna de Claude para crear agentes:

  ESTRUCTURA DESCUBIERTA:PROMPTSSSSSSSSS

  1. YAML Header (líneas 1-6):
    - name
    - description (con ejemplos específicos)
    - model: sonnet
    - color
  2. Identidad Principal (líneas 8-9):
    - "You are a [ROLE] with deep expertise in [DOMAINS]"
    - Declaración de responsabilidad core
  3. Workflow/Responsabilidad Core (líneas 10-15):
    - Lista numerada específica de lo que hace
    - Patrones de ejecución concretos
  4. Expertise Técnica (líneas 16-25):
    - Lista de tecnologías/habilidades específicas
    - Herramientas y frameworks
  5. Approach/Metodología (líneas 26-38):
    - Pasos detallados numerados
    - Proceso específico de trabajo
  6. Best Practices (líneas 39-48):
    - Principios que sigue
    - Estándares de calidad
  7. Execution Guidelines (líneas 49-56):
    - Instrucciones específicas "When executing"
    - Reglas operacionales
  8. Cierre Proactivo (líneas 57-58):
    - Comportamiento proactivo
    - Estándares finales