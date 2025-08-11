# 🎯 Agent Detection & Module Generation System

## Sistema de Detección y Generación de Agentes

Este archivo define cómo el comando `/setup` debe:
1. Detectar qué agentes globales necesita el proyecto
2. Crear agentes de módulo específicos
3. Generar CLAUDE.md con registro exacto de agentes disponibles

## 📊 Flujo Completo del Sistema

```mermaid
graph TD
    A[/setup command] --> B[Stack Detection]
    B --> C[Select Global Agents]
    C --> D[Detect Project Modules]
    D --> E[Create Module Agents]
    E --> F[Generate manifest.json]
    F --> G[Generate CLAUDE.md]
    G --> H[Setup Complete]
```

## 🔍 Phase 1: Stack Detection

### Archivos a revisar:
```yaml
Backend Detection:
  - composer.json → Laravel/PHP
  - requirements.txt → Python/FastAPI
  - package.json → Node.js
  - go.mod → Go
  - Gemfile → Ruby/Rails

Frontend Detection:
  - package.json dependencies:
    - react → React
    - vue → Vue
    - @angular → Angular
    - next → Next.js

Database Detection:
  - .env:
    - DB_CONNECTION=pgsql → PostgreSQL
    - DB_CONNECTION=mysql → MySQL
  - docker-compose.yml → Database services
  - database.yml → Rails databases

Infrastructure Detection:
  - Dockerfile → Docker
  - docker-compose.yml → Docker Compose
  - .github/workflows → GitHub Actions
  - terraform/ → Terraform/IaC
  - kubernetes/ → K8s
```

## 🤖 Phase 2: Global Agent Selection

Basándose en `agents-registry.json`:

```javascript
function selectGlobalAgents(detectedStack) {
  const requiredAgents = [];
  
  // Always include coordinators for detected domains
  if (detectedStack.backend) {
    requiredAgents.push('backend-coordinator');
    
    // Add specific backend engineers
    if (detectedStack.laravel) requiredAgents.push('laravel-engineer');
    if (detectedStack.fastapi) requiredAgents.push('fastapi-engineer');
    if (detectedStack.nodejs) requiredAgents.push('nodejs-engineer');
  }
  
  if (detectedStack.frontend) {
    requiredAgents.push('frontend-coordinator');
    
    // Add specific frontend engineers
    if (detectedStack.react) requiredAgents.push('react-engineer');
    if (detectedStack.vue) requiredAgents.push('vue-engineer');
    if (detectedStack.angular) requiredAgents.push('angular-engineer');
  }
  
  if (detectedStack.database) {
    requiredAgents.push('database-coordinator');
    
    // Add specific database engineers
    if (detectedStack.postgresql) requiredAgents.push('postgres-engineer');
    if (detectedStack.mysql) requiredAgents.push('mysql-engineer');
    if (detectedStack.redis) requiredAgents.push('redis-engineer');
  }
  
  // Always include essential utility engineers
  requiredAgents.push('debugging-engineer');
  requiredAgents.push('memory-engineer');
  
  return requiredAgents;
}
```

## 🏗️ Phase 3: Module Detection

### Patrones para detectar módulos:

```yaml
Laravel Modules:
  - app/Http/Controllers/AuthController.php → auth module
  - app/Http/Controllers/PaymentController.php → payment module
  - app/Models/User.php → user module
  - routes/api.php patterns → API modules

React Modules:
  - src/components/Auth/ → auth module
  - src/components/Checkout/ → checkout module
  - src/features/payment/ → payment module
  - src/pages/admin/ → admin module

Generic Patterns:
  - */auth/* → authentication module
  - */payment/* → payment processing module
  - */admin/* → administration module
  - */api/* → API module
  - */user/* → user management module
```

## 🛠️ Phase 4: Module Agent Creation

### Template para agentes de módulo:

```markdown
---
name: [module-name]-specialist
description: Expert in this project's [module-name] implementation
model: sonnet
tools: Read, Write, Edit, MultiEdit, Bash, Grep, Glob
---

# [Module Name] Module Specialist

## Role & Expertise
I am the dedicated specialist for the [module-name] module in this specific project. I have deep knowledge of:
- The exact implementation in this codebase
- All files, functions, and patterns used
- The business logic specific to this project
- Integration points with other modules

## Module Structure
[Auto-generated based on file discovery]

## Key Files
[List of files in this module]

## Core Functions
[Main functions/methods in this module]

## Dependencies
- Internal: [Other modules this depends on]
- External: [Libraries/packages used]

## Integration Points
[How this module connects with others]

## Known Issues & TODOs
[Extracted from comments/TODOs in code]

## Module-Specific Patterns
[Patterns unique to this implementation]

## Testing Coverage
[Test files related to this module]

## Recent Changes
[Git history for this module]
```

### Proceso de creación:

```javascript
function createModuleAgent(moduleName, moduleFiles, projectContext) {
  const agent = {
    name: `${moduleName}-module-specialist`,
    description: `Expert in this project's ${moduleName} implementation`,
    model: 'sonnet',
    tools: ['Read', 'Write', 'Edit', 'MultiEdit', 'Bash', 'Grep', 'Glob'],
    
    // Specific knowledge about THIS project's module
    module_structure: analyzeStructure(moduleFiles),
    key_files: moduleFiles,
    core_functions: extractFunctions(moduleFiles),
    dependencies: analyzeDependencies(moduleFiles),
    integration_points: findIntegrations(moduleFiles),
    known_issues: extractTODOs(moduleFiles),
    patterns: identifyPatterns(moduleFiles),
    test_coverage: findTests(moduleName),
    recent_changes: getGitHistory(moduleFiles)
  };
  
  // Save to project/.claude/agents/
  saveAgent(`${moduleName}-module-specialist.md`, agent);
  
  return agent;
}
```

## 📋 Phase 5: Manifest Generation

### Estructura del manifest.json:

```json
{
  "version": "1.0.0",
  "project": {
    "name": "detected-project-name",
    "type": "web-application",
    "stack": {
      "backend": "Laravel",
      "frontend": "React",
      "database": "PostgreSQL",
      "cache": "Redis"
    }
  },
  "agents": {
    "global": {
      "installed": [
        {
          "name": "backend-coordinator",
          "version": "1.0.0",
          "source": "~/.claude/agents/backend-coordinator.md",
          "installed_date": "2024-12-15",
          "reason": "Laravel backend detected"
        },
        {
          "name": "laravel-engineer",
          "version": "1.0.0",
          "source": "~/.claude/agents/laravel-engineer.md",
          "installed_date": "2024-12-15",
          "reason": "composer.json with Laravel framework"
        }
      ],
      "available_count": 15
    },
    "modules": {
      "created": [
        {
          "name": "auth-module-specialist",
          "created_date": "2024-12-15",
          "location": ".claude/agents/auth-module-specialist.md",
          "files_tracked": 23,
          "last_updated": "2024-12-15"
        },
        {
          "name": "payment-module-specialist",
          "created_date": "2024-12-15",
          "location": ".claude/agents/payment-module-specialist.md",
          "files_tracked": 18,
          "last_updated": "2024-12-15"
        }
      ],
      "total_created": 5
    }
  },
  "delegation_map": {
    "backend": ["backend-coordinator", "laravel-engineer"],
    "frontend": ["frontend-coordinator", "react-engineer"],
    "database": ["database-coordinator", "postgres-engineer"],
    "auth": ["auth-module-specialist"],
    "payment": ["payment-module-specialist"]
  },
  "last_updated": "2024-12-15T10:30:00Z",
  "setup_version": "1.0.0"
}
```

## 📝 Phase 6: CLAUDE.md Generation

### Template para CLAUDE.md:

```markdown
# Project Orchestrator Configuration

Generated: [timestamp]
Project: [project-name]
Stack: [detected-stack]

## Your Role as Orchestrator

You are the intelligent orchestrator for this [type] application. You have access to:
- **[X] Global specialist agents** from the ClaudeSquad system
- **[Y] Module-specific agents** created for this project

## 🌍 Available Global Agents

[Read from manifest.json - only installed ones]

### Coordinators (Level 1)
- **backend-coordinator**: Orchestrates backend tasks, delegates to Laravel specialists
- **database-coordinator**: Manages database operations, works with PostgreSQL

### Engineers (Level 2)
- **laravel-engineer**: Laravel expert, handles Eloquent, APIs, queues
- **postgres-engineer**: PostgreSQL optimization, indexing, performance

## 🏗️ Project-Specific Module Agents

[Generated for THIS project's modules]

### Module Specialists (Level 3)
- **auth-module-specialist**: Expert in THIS project's authentication system
  - Files: 23 files in app/Http/Controllers/Auth, app/Models/User
  - Knows: JWT implementation, 2FA system, role-based permissions
  
- **payment-module-specialist**: Expert in THIS project's payment processing
  - Files: 18 files in app/Services/Payment, app/Http/Controllers/Payment
  - Knows: Stripe integration, subscription logic, webhook handling

## 🔄 Delegation Patterns

When user says "fix login bug":
1. Check if it's a module-specific issue → auth-module-specialist
2. If it needs framework expertise → laravel-engineer
3. If it's database related → postgres-engineer

## 📊 Agent Registry Access

You have access to the complete agent registry at:
- Global registry: `~/.claude/agents-registry.json`
- Project manifest: `.claude/manifest.json`

Use these to understand each agent's capabilities and activation triggers.

## 🎯 Activation Examples

```yaml
User: "The login is slow"
→ auth-module-specialist (knows this project's auth)
→ postgres-engineer (if database issue)

User: "Add Redis caching"
→ backend-coordinator
→ redis-engineer

User: "Build new payment feature"
→ payment-module-specialist (knows existing payment code)
→ laravel-engineer (for new Laravel patterns)
```

## 📝 Memory Structure

```
.claude/memory/
├── backend/
│   └── laravel.md      # Laravel patterns in this project
├── modules/
│   ├── auth.md         # Auth module evolution
│   └── payment.md      # Payment module history
└── database/
    └── postgres.md     # Database optimizations
```

## ⚠️ Important Notes

1. **Module agents know THIS project** - They have specific knowledge of your codebase
2. **Global agents know the framework** - They have general expertise
3. **Use module agents first** - They know your specific implementation
4. **Delegate to global agents for new patterns** - They know best practices

---

*Configuration generated by ClaudeSquad setup v1.0.0*
```

## 🔧 Phase 7: Agent Access Verification

### Script para verificar acceso:

```javascript
function verifyAgentAccess() {
  const manifest = readFile('.claude/manifest.json');
  const errors = [];
  
  // Check global agents
  manifest.agents.global.installed.forEach(agent => {
    if (!fileExists(`~/.claude/agents/${agent.name}.md`)) {
      errors.push(`Global agent missing: ${agent.name}`);
    }
  });
  
  // Check module agents
  manifest.agents.modules.created.forEach(agent => {
    if (!fileExists(agent.location)) {
      errors.push(`Module agent missing: ${agent.name}`);
    }
  });
  
  // Verify CLAUDE.md references
  const claudeMd = readFile('.claude/CLAUDE.md');
  const referencedAgents = extractAgentReferences(claudeMd);
  
  referencedAgents.forEach(agentName => {
    if (!isAgentAvailable(agentName, manifest)) {
      errors.push(`CLAUDE.md references unavailable agent: ${agentName}`);
    }
  });
  
  return {
    valid: errors.length === 0,
    errors: errors
  };
}
```

## 🚀 Usage in Claude

Cuando Claude lee CLAUDE.md, ve:
1. **Exactamente qué agentes tiene disponibles**
2. **Para qué sirve cada uno** (del registry)
3. **Cuándo activarlos** (triggers)
4. **Cómo delegarles trabajo**

Ejemplo de uso:

```yaml
Claude's internal process:
1. User: "Fix the slow checkout"
2. Claude reads CLAUDE.md
3. Sees: checkout-module-specialist available
4. Delegates: "checkout-module-specialist, investigate performance"
5. Specialist has specific knowledge of THIS project's checkout
6. Returns findings
7. Claude coordinates solution
```

## 📊 Beneficios del Sistema

1. **Claude sabe exactamente qué agentes existen**
2. **No intenta usar agentes no instalados**
3. **Module agents tienen conocimiento específico del proyecto**
4. **Global agents proveen expertise general**
5. **Todo está trackeado y verificable**

---

*Este sistema asegura que CLAUDE.md siempre refleje la realidad de qué agentes están disponibles y qué pueden hacer.*