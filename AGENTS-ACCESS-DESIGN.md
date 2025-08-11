# 🔗 Sistema de Acceso a Agentes - Diseño Propuesto

## 🚨 PROBLEMA CRÍTICO IDENTIFICADO

El CLAUDE.md generado debe poder acceder a los agentes instalados, pero actualmente no hay un mecanismo claro de tracking y acceso.

## 📐 ARQUITECTURA PROPUESTA

### Opción A: Agentes Locales en el Proyecto
```
proyecto/
├── .claude/
│   ├── CLAUDE.md           # Generado por /setup
│   ├── agents/             # Agentes COPIADOS aquí
│   │   ├── backend-coordinator.md
│   │   ├── laravel-engineer.md
│   │   └── [solo los instalados]
│   └── manifest.json       # Registry de agentes instalados
```

**Ventajas:**
- Agentes versionados con el proyecto
- Sin dependencias externas
- Portabilidad completa

**Desventajas:**
- Duplicación de archivos
- Actualizaciones manuales

### Opción B: Agentes Globales con Registry
```
~/.claude/
├── agents/                 # Todos los 71 agentes
│   └── *.md
└── projects/
    └── [project-hash]/
        └── installed-agents.json

proyecto/
├── .claude/
│   ├── CLAUDE.md          # Referencias a agentes globales
│   └── .agents            # Lista de agentes habilitados
```

**Ventajas:**
- Sin duplicación
- Actualizaciones centralizadas
- Menor espacio en disco

**Desventajas:**
- Requiere sincronización
- Dependencia de carpeta global

## 📋 PROPUESTA DE IMPLEMENTACIÓN

### 1. Archivo manifest.json (o installed-agents.json)
```json
{
  "version": "1.0.0",
  "project": "my-laravel-app",
  "installed_agents": [
    {
      "name": "backend-coordinator",
      "version": "1.0.0",
      "location": "local|global",
      "path": ".claude/agents/backend-coordinator.md",
      "installed_date": "2024-12-15",
      "dependencies": ["laravel-engineer", "postgres-engineer"]
    },
    {
      "name": "laravel-engineer",
      "version": "1.0.0",
      "location": "local|global",
      "path": ".claude/agents/laravel-engineer.md",
      "installed_date": "2024-12-15"
    }
  ],
  "available_coordinators": [
    "backend-coordinator",
    "database-coordinator"
  ],
  "available_engineers": [
    "laravel-engineer",
    "postgres-engineer",
    "redis-engineer"
  ]
}
```

### 2. Actualización del CLAUDE.md

El CLAUDE.md generado debe incluir SOLO los agentes del manifest:

```markdown
# Project Orchestrator Configuration

## Available Engineers & Specialists

### Installed Coordinators:
- backend-coordinator: Backend orchestration
- database-coordinator: Database operations

### Installed Engineers:
- laravel-engineer: Laravel framework expert
- postgres-engineer: PostgreSQL optimization
- redis-engineer: Caching strategies

## Delegation Patterns

When you need backend work:
→ Delegate to backend-coordinator
  → It can use: laravel-engineer

When you need database work:
→ Delegate to database-coordinator
  → It can use: postgres-engineer, redis-engineer
```

### 3. Proceso de Instalación Mejorado

```yaml
Phase 6: Agent Installation (ENHANCED)

1. SELECTION:
   Based on detected stack, select agents:
   ☑ backend-coordinator (required)
   ☑ laravel-engineer (detected: composer.json)
   ☑ postgres-engineer (detected: .env DB_CONNECTION)
   ☐ mysql-engineer (not needed)
   ☑ redis-engineer (detected: CACHE_DRIVER)

2. INSTALLATION:
   Installing 4 agents to project...
   
   Option 1 - Local Installation:
   Copying agents to .claude/agents/
   [████████████████████] 4/4 Complete

   Option 2 - Global Reference:
   Linking to ~/.claude/agents/
   Creating manifest.json
   
3. REGISTRY UPDATE:
   Updating manifest.json with installed agents
   
4. CLAUDE.md GENERATION:
   Generating CLAUDE.md with 4 available agents
   
5. VALIDATION:
   ✓ All referenced agents exist
   ✓ Delegation paths valid
   ✓ Memory structure created
```

## 🔄 Flujo de Invocación

```mermaid
graph TD
    A[User Request] --> B[CLAUDE.md Orchestrator]
    B --> C{Check manifest.json}
    C -->|Agent exists| D[Load agent from path]
    C -->|Agent missing| E[Error: Agent not installed]
    D --> F[Execute agent]
    F --> G[Return