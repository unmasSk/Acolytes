---
command: setup
description: 🚀 Setup project with ClaudeSquad agents. Params: --update
---

## ⚡ MANDATORY COMMAND FLOW

This system provides intelligent project setup with ClaudeSquad's 57 specialized agents, supporting both existing projects and new project creation from expert consultation.

## Usage

```
/setup          # Initial complete setup for new projects OR existing projects
/setup --update # Update existing setup (new modules, refresh agents)
```

---

### ⚠️ **IMMUTABLE RULES – NO EXCEPTIONS**

1. **NEVER** analyze without creating documentation
2. **ALWAYS** create Database & MCP first (Phase 1)
3. **ALWAYS** create ALL required files and documentation
4. **NEVER** ask whether to create — just create
5. **ALL** documentation, code, comments, SQLite in English
6. **ALWAYS** use multiple Task calls for parallel execution

---

## 🎯 UNIFIED FLOW FOR BOTH PROJECT TYPES

### 1️⃣ **PHASE 1: ENVIRONMENT & DATABASE SETUP**

**Universal setup regardless of project type:**

```yaml
ENVIRONMENT_CHECK:
  - Execute: uv run python ~/.claude/scripts/environment_check.py
  - Validates: Python 3.8+, Git 2.0+, Node 18+, uv package manager
  - Creates environment report in .claude/project/environment-status.md
  - Auto-fixes common issues where possible

DATABASE_AND_MCP:
  1. Configure MCP SQLite:
    - Run: python ~/.claude/scripts/setup_mcp.py
    - Create project.db if not exists
    - Configure MCP to point to project.db
    - User may need to restart Claude Code

  2. Initialize database schema:
    - Execute: python ~/.claude/scripts/init_db.py (if exists) OR directly create DB with schema
    - Database will auto-create: agents_catalog (51 agents), jobs table with initial job, sessions, messages, etc.
    - Initial job 'Project Setup' automatically created with high priority
    - All tables, indexes, triggers, and constraints ready

  3. Install missing MCP servers as needed
```

---

### 2️⃣ **PHASE 2: ANALYSIS & DOCUMENTATION**

**Different approaches based on project type:**

#### **FOR EXISTING PROJECTS**

```yaml
PARALLEL_ANALYSIS:
  mode: REAL PARALLEL
  agents:
    - setup.codebase
    - setup.context
    - setup.infrastructure
    - setup.environment
  execution: MULTIPLE TASK CALLS IN ONE MESSAGE

DOCUMENTATION_CREATION:
  location: .claude/project/
  files:
    - vision.md (project purpose and goals)
    - architecture.md (technical decisions and structure)
    - roadmap.md (development phases - initially empty template)
    - technical-decisions.md (rationale for tech choices)
    - team-preferences.md (coding standards and practices)
    - project-context.md (specific project details)
  format: English markdown with consistent structure
```

#### **FOR NEW PROJECTS**

```yaml
REQUIREMENTS_INTERVIEW:
  rounds: 14 areas of questions
  persistence: .claude/project/requirements-interview.md
  areas:
    1. Business & Domain (4 questions)
    2. Technical Architecture (4 questions)
    3. Database & Data (4 questions)
    4. Security & Compliance (4 questions)
    5. Infrastructure & Deployment (4 questions)
    6. CI/CD & DevOps (4 questions)
    7. Monitoring & Observability (4 questions)
    8. Testing Strategy (4 questions)
    9. Documentation & Knowledge (4 questions)
    10. Accessibility & I18N (4 questions)
    11. Team & Collaboration (4 questions)
    12. Development Environment (4 questions)
    13. Language & Communication (4 questions)
    14. User Experience Level (4 questions)

SPECIALIST_CONSULTATION:
  process: Claude analyzes all answers from requirements-interview.md
  action: Consult relevant specialists based on responses
  execution: 
    - Use Task tool for PARALLEL consultation when specialists are independent
    - Use sequential if one specialist's response is needed for another's question
    - Apply logic to determine dependencies between consultations
  examples:
    - "React + PostgreSQL + Auth0" → @frontend.react, @database.postgres, @service.auth (parallel)
    - "Vue + MongoDB + Stripe" → @frontend.vue, @database.mongodb, @business.payment (parallel)
  storage: Append specialist recommendations to requirements-interview.md

PLAN_STRATEGY_ORGANIZATION:
  agent: @plan.strategy
  input: All interview answers + specialist recommendations
  output:
    - Complete project plan with phases and timeline
    - Same 6 documentation files in .claude/project/
    - Jobs created in SQLite database
    - Roadmap.md fully populated with executable phases
```

---

### 3️⃣ **PHASE 3: CLAUDE.MD CREATION**

```yaml
CLAUDE_MD_GENERATION:
  source: Aggregated information from Phase 2
  template: .claude/resources/templates/claude-md-template.md
  placeholders:
    - {{project_name}} → from analysis/interview
    - {{project_description}} → from vision.md
    - {{tech_stack}} → from architecture.md
    - {{agents}} → planned dynamic agents
  dynamic_sections:
    - Project-specific architecture
    - Detected/planned critical issues
    - Technology stack with rationale
    - Reference to .claude/project/ documentation
```

---

### 4️⃣ **PHASE 4: JOBS & AGENT CREATION**

#### **FOR EXISTING PROJECTS**

```yaml
DYNAMIC_AGENT_CREATION:
  - Create project-specific agents based on detected modules
  - Multiple Task calls in parallel
  - Example: api-agent, auth-agent, frontend-agent
  - NO job creation (jobs created when agents start working)

AGENT_STRUCTURE:
  location: .claude/agents/[module]-agent.md
  database: Pre-create agent entries and 8 memory records per agent
```

#### **FOR NEW PROJECTS**

```yaml
PLAN_EXECUTION:
  - @plan.strategy already created jobs in SQLite
  - Create dynamic agents based on planned architecture
  - Agent creation guided by plan.strategy recommendations

INITIAL_SCAFFOLDING:
  - Generate project folder structure
  - Create initial configuration files
  - Set up development environment templates
```

---

### 5️⃣ **PHASE 5: DEEP ANALYSIS & INITIALIZATION**

```yaml
DYNAMIC_AGENT_ACTIVATION:
  existing_projects:
    - All dynamic agents perform deep module analysis
    - Fill their 8 memory records with comprehensive knowledge
    - Update agent_memory table in SQLite

  new_projects:
    - Dynamic agents create their initial memory structures
    - Set up monitoring for their planned modules
    - Prepare for development phase execution
```

---

### 6️⃣ **PHASE 6: FINALIZATION**

```yaml
COMPLETION_SUMMARY:
  - Confirm all documentation created in .claude/project/
  - Verify SQLite database populated with agents and memories
  - Present system summary to user
  - List available agents with their expertise areas
  - Show next steps for development

NEXT_STEPS:
  existing_projects: "Ready for development with full ClaudeSquad support"
  new_projects: "Ready to begin development following the generated roadmap"
```

---

## 📁 **STRUCTURE CREATED BY /setup**

```
[PROJECT_ROOT]/
├── .claude/
│   ├── project/                    # PROJECT DOCUMENTATION (NEW!)
│   │   ├── vision.md               # Project purpose and goals
│   │   ├── architecture.md         # Technical decisions
│   │   ├── roadmap.md              # Development phases
│   │   ├── technical-decisions.md  # Rationale for choices
│   │   ├── team-preferences.md     # Standards and practices
│   │   └── project-context.md      # Specific project details
│   ├── agents/                     # DYNAMIC AGENTS
│   │   ├── [module]-agent.md       # One per detected/planned module
│   │   └── ...
│   ├── memory/                     # PERSISTENT MEMORY
│   │   └── project.db              # SQLite with agent memories, jobs, setup data
│   ├── commands/                   # CUSTOM COMMANDS
│   └── CLAUDE.md                   # PROJECT INSTRUCTIONS
```

---

## 🚩 **FLAGS Protocol**

**Claude's Role**: Check workable flags and invoke agents, NOT read flag content

```bash
# Claude checks summary ONLY (no context overload)
python .claude/scripts/agent_db.py get-workable-flags
# Result: @auth-agent: 3 flags, @api-agent: 1 flag
# Claude invokes: "@auth-agent review your pending flags"
```

**Agent Workflow**:

1. **Check**: `python .claude/scripts/agent_db.py get-agent-flags "@agent-name"`
2. **Work**: Process flags with full context
3. **Create**: `python .claude/scripts/agent_db.py create-flag-for-agent --target_agent "@other-agent" ...`
4. **Complete**: `python .claude/scripts/agent_db.py complete-flag [id] "@agent-name"`

---

## 📊 **NEW VS EXISTING PROJECT COMPARISON**

| Phase | Existing Project             | New Project                             |
| ----- | ---------------------------- | --------------------------------------- |
| 1     | Environment + Database setup | Environment + Database setup            |
| 2     | 4 setup agents analyze code  | 14 interview rounds + specialists       |
| 3     | CLAUDE.md creation           | CLAUDE.md creation                      |
| 4     | Dynamic agent creation       | Jobs + agent creation via plan.strategy |
| 5     | Deep module analysis         | Agent initialization                    |
| 6     | Finalization summary         | Finalization summary                    |

**Key Difference**: Existing projects analyze what exists; new projects plan what will be built.

---

## ❌ **COMMON ERRORS**

- ❌ Running setup agents sequentially instead of parallel
- ❌ Not creating .claude/project/ documentation
- ❌ Asking user about language preferences (always English)
- ❌ Not creating SQLite database first
- ❌ Creating documentation in wrong location

---

## 🎯 **EXAMPLE EXECUTION**

```bash
User: /setup

Claude:
1. [Phase 1] Environment + Database setup ✅
2. [Phase 2]
   - IF existing project: "Analyze this project using 4 setup agents IN PARALLEL"
   - IF new project: "Starting requirements interview - Business & Domain questions"
3. [Phase 3] Generate CLAUDE.md with project context ✅
4. [Phase 4] Create dynamic agents + jobs (if new project) ✅
5. [Phase 5] Initialize agent memories ✅
6. [Phase 6] "✅ Setup complete: ClaudeSquad ready with full documentation"
```

---

**THIS IS THE OFFICIAL FLOW. NO INTERPRETATIONS.**
