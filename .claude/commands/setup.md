---
command: setup
description: 🚀 Setup project with ClaudeSquad agents. Params: --update
---

## ⚡ MANDATORY COMMAND FLOW

This hybrid version merges the **technical depth and safeguards** of the original specification with the **clarity and structure** of the newer documentation, while retaining all _immutable rules_ and best practices from Claude Code.

## Usage

```
/setup         # Initial complete setup for new projects
/setup --update # Update existing setup (new modules, refresh agents)
```

---

### ⚠️ **IMMUTABLE RULES – NO EXCEPTIONS**

1. **NEVER** analyze without creating agents
2. **ALWAYS** invoke 4 setup agents in REAL PARALLEL (multiple Task calls)
3. **ALWAYS** create ALL required files and memory
4. **NEVER** ask whether to create — just create (exception: explicit language preference prompts in Phase 3)
5. **ALWAYS** use multiple Task calls for agent creation

---

## 📋 FOR EXISTING PROJECTS

The following 8 phases apply to existing projects with code already in place:

### 1️⃣ **PHASE 1: ENVIRONMENT VERIFICATION**

Before any project analysis begins, the system validates your development environment.

```yaml
Checking prerequisites:
  - Git version and configuration
  - Node.js/npm/yarn versions
  - PHP/Composer (if applicable)
  - Python/pip (if applicable)
  - Docker/Docker Compose
  - IDE/Editor configuration
  - Operating system details
  - File permissions
  - Network connectivity

If missing:
  - List missing tools
  - Provide installation commands
  - Suggest alternative solutions
```

---

### 2️⃣ **PHASE 2: PARALLEL ANALYSIS**

Execute **REAL PARALLEL** analysis using **4 specialized agents**:

```yaml
INVOCATION:
  mode: REAL PARALLEL
  agents:
    - setup-context
    - setup-codebase
    - setup-infrastructure
    - setup-environment
  execution: MULTIPLE TASK CALLS IN ONE MESSAGE
  instruction: "Analyze this project IN PARALLEL using 4 specialized agents"
```

**Agents and Purpose:**

| Agent                | Purpose                                         |
| -------------------- | ----------------------------------------------- |
| setup-context        | Project purpose, architecture, decisions        |
| setup-codebase       | Code structure, modules, patterns, quality      |
| setup-infrastructure | Deployment, databases, CI/CD, external services |
| setup-environment    | Tools, versions, system capabilities            |

✅ **Always** run these in parallel — never sequentially.  
⚠️ Limit: 10 simultaneous Task calls.

---

### 3️⃣ **PHASE 3: LANGUAGE CONFIGURATION**

**ALWAYS ASK USER BEFORE CREATING CLAUDE.MD:**

- User interaction language
- Private documentation language
- Public documentation language
- Comments and docstrings language

### 4️⃣ **PHASE 4: DATABASE & MCP SETUP**

```yaml
DATABASE_AND_MCP:
  executor: Claude (main)
  purpose: Configure MCP and create SQLite database

STEPS:
  1. Configure MCP SQLite FIRST:
    - Run: python .claude/scripts/setup_mcp.py
    - This will create project.db if not exists
    - Configure MCP to point to project.db
    - User may need to restart Claude Code

  2. Initialize database schema:
    - Run: sqlite3 .claude/memory/project.db < .claude/scripts/init_db.sql
    - Create initial job record with status='active'

  3. Pre-create agent entries and memories:
    For each module detected in Phase 2:
      - Insert agent record in 'agents' table
      - Insert 8 empty memory records (one per type)
      - Use python .claude/scripts/agent_db.py for insertions

  Example:
    Modules detected: auth, payments, notifications
    Actions:
      - Create project.db with all tables
      - Configure MCP to use project.db
      - Create 3 agents in DB
      - Create 24 memory records (3 agents × 8 memories)
```

**Why this phase:**

- Database AND MCP ready before agents need them
- No configuration issues later
- Everything prepared for parallel agent work

---

### 5️⃣ **PHASE 5: CLAUDE.MD CREATION**

```yaml
CLAUDE:
  - Receives information from the 4 agents
  - Creates CLAUDE.md with all intelligence and language preferences
  - Maps detected modules to specialized agents
  - Prepares agent list for agent-creator
  - INCLUDES Agent Selection Protocol instructions
```

`CLAUDE.md` includes:

- Complete tech stack mapping
- Module dependency structure
- Detected patterns and conventions
- Recommended agent creation plan
- **Agent Selection Protocol** (mandatory routing instructions)

#### Agent Selection Protocol Content for CLAUDE.md

When creating CLAUDE.md, include this exact section:

```markdown
## Agent Selection Protocol

**MANDATORY**: Before invoking any agent, follow this 3-step process:

### Step 1: Task Classification
Analyze the user prompt for these keywords:
- **STRATEGIC**: "choose", "select", "compare", "decide", "architecture", "strategy", "design"
  → Use Coordinator agents first (coordinator.*)
- **TACTICAL**: "implement", "configure", "optimize", "debug", "deploy", "code"  
  → Use Specialist agents directly (backend.*, database.*, etc.)
- **COMBINED**: Contains both strategic + tactical keywords
  → Use sequential: Coordinator → Specialist

### Step 2: Domain Identification
Identify the technical domain:
- Backend/API → coordinator.backend or backend.*
- Database/Data → coordinator.database or database.*
- Frontend/UI → coordinator.frontend or frontend.*
- DevOps/Ops → coordinator.devops or ops.*
- Services → service.*
- Business → business.*

### Step 3: Apply Routing Rules
Consult the global agent routing rules:
- Use the IF/THEN conditions to select exact agent
- For overlaps, apply Anti-Ambiguity Rules
- For multi-agent workflows, follow predefined sequences

### Examples:
- "Optimize PostgreSQL" → TACTICAL → database.postgres (direct)
- "Choose database for app" → STRATEGIC → coordinator.database → database.*
- "Implement RAG with Postgres" → database.pgvector (Anti-Ambiguity Rule)
- "Create user roles system" → coordinator.security → service.auth → database.* (sequential)

**Global Agent Catalog**: Refer to ~/.claude/resources/rules/agent-routing.md for complete routing rules.
```

---

### 6️⃣ **PHASE 6: AGENT CREATION**

```yaml
INVOCATION:
  agent: agent-creator
  mode: REAL PARALLEL – MULTIPLE TASK CALLS
  purpose: Create agent .md files ONLY (no data insertion)
  complexity_analysis: MANDATORY before creation
  tasks:
    - [Task 1] agent-creator → module-X-agent
    - [Task 2] agent-creator → module-Y-agent
    - [Task 3] agent-creator → module-Z-agent
```

#### Module Complexity Analysis
**MANDATORY**: Before creating agents, analyze module size and complexity:

- **Simple Module** (≤30 files): Create single agent
- **Complex Module** (>30 files): Create main agent + specialized sub-agents  
- **Multi-domain Module**: Create agent per clear sub-domain + main module agent

#### Complex Module Agent Structure
```bash
# Example: Large RAG module (>30 files)
[Task 1] agent-creator → rag-agent               # Main module agent (knows full context)
[Task 2] agent-creator → rag-embeddings-agent   # Vector processing specialist  
[Task 3] agent-creator → rag-retrieval-agent    # Search & ranking specialist
[Task 4] agent-creator → rag-generation-agent   # Response generation specialist
[Task 5] agent-creator → rag-evaluation-agent   # Quality metrics specialist
```

**Important Change:**

- agent-creator ONLY creates the .md file
- Does NOT insert data into database
- Database structure already exists from Phase 4

Example:

```bash
"Create these agents in parallel:
[Task 1] agent-creator → api-agent (create .claude/agents/api-agent.md)
[Task 2] agent-creator → database-agent (create .claude/agents/database-agent.md)
[Task 3] agent-creator → frontend-agent (create .claude/agents/frontend-agent.md)
[Task 4] agent-creator → auth-agent (create .claude/agents/auth-agent.md)"
```

---

### 7️⃣ **PHASE 7: DEEP MODULE ANALYSIS**

```yaml
DEEP_ANALYSIS:
  executor: All dynamic agents IN PARALLEL
  purpose: Each agent analyzes its module and fills its memories

INVOCATION:
  mode: REAL PARALLEL – MULTIPLE TASK CALLS
  instruction: "Analyze your module deeply and fill your 8 memories in the database"

  tasks:
    - [Task 1] api-agent → Deep analyze /src/api, fill 8 memories
    - [Task 2] database-agent → Deep analyze /src/database, fill 8 memories
    - [Task 3] frontend-agent → Deep analyze /src/frontend, fill 8 memories
    - [Task 4] auth-agent → Deep analyze /src/auth, fill 8 memories
    - [Task 5] payments-agent → Deep analyze /src/payments, fill 8 memories
    - [Task 6] notifications-agent → Deep analyze /src/notifications, fill 8 memories

What each agent does:
  1. Reads EVERY file in its module
  2. Detects all patterns, conventions, anti-patterns
  3. Maps all dependencies and connections
  4. Analyzes code quality, tests, performance
  5. Understands business context and decisions
  6. Updates its 8 memory records with findings:
     - UPDATE agent_memory SET content = {analysis} WHERE agent_id = X AND memory_type = 'knowledge'
     - UPDATE agent_memory SET content = {analysis} WHERE agent_id = X AND memory_type = 'structure'
     - ... (for all 8 types)

Benefits:
  - TRUE EXPERTS: Each agent becomes the real expert of its module
  - PARALLEL PROCESSING: All modules analyzed simultaneously
  - DEEP KNOWLEDGE: Agents do exhaustive analysis, not superficial
  - PERSISTENT MEMORY: All knowledge stored in SQLite for future use
```

---

### 8️⃣ **PHASE 8: FINALIZATION**

```yaml
CLAUDE:
  - Confirms all agents created and analyzed
  - Confirms database populated with deep knowledge
  - Presents system summary to user
  - Lists available agents with their expertise
  - Shows current system state
  - Reports total memories stored (agents × 8)
```

---

## 📁 **STRUCTURE CREATED BY /setup**

```
[PROJECT_ROOT]/
├── .claude/                      # IN THE ANALYZED PROJECT
│   ├── CLAUDE.md                 # Project instructions
│   ├── agents/                   # Dynamic agents
│   │   ├── calculator-agent.md
│   │   ├── emissions-agent.md
│   │   └── ...
│   ├── memory/                   # Persistent memory
│   │   └── project.db            # SQLite database with all agent memories
│   └── commands/                 # Custom project commands
```

---

## ❓ **ARCHITECTURE DECISIONS**

### **OPTION A: Single agent-creator invocation**

```bash
agent-creator → create all agents in one task
# ❌ Problem: Large context size in one window
```

### **OPTION B: Parallel agent creation** ✅ Recommended

```bash
# Multiple Task calls in one message
"Create these agents IN PARALLEL:
[Task 1] agent-creator → calculator-agent
[Task 2] agent-creator → emissions-agent
[Task 3] agent-creator → ui-agent"
```

---

## 🆕 FOR NEW/EMPTY PROJECTS

### 1️⃣ **PHASE 1: Requirements Interview**

Interactive Q&A covering **14 comprehensive areas**:

**1. Business & Domain**

- What problem does this solve?
- Who are the users/stakeholders?
- Business model and revenue streams
- Success metrics and KPIs

**2. Technical Architecture**

- Technology stack selection and rationale
- Monolith vs microservices vs serverless
- API design (REST/GraphQL/gRPC)
- Real-time requirements

**3. Database & Data**

- Database choice and rationale
- Data volume expectations
- ACID vs eventual consistency
- Data retention and privacy policies

**4. Security & Compliance**

- Authentication method (JWT/OAuth/SAML)
- Authorization model (RBAC/ABAC)
- Compliance requirements (GDPR/HIPAA/SOC2)
- Encryption and secrets management

**5. Infrastructure & Deployment**

- Cloud provider and services
- Container orchestration strategy
- Multi-region requirements
- Disaster recovery planning

**6. CI/CD & DevOps**

- Version control and branching strategy
- CI/CD platform and pipeline design
- Environment management
- Deployment strategies

**7. Monitoring & Observability**

- APM and error tracking tools
- Log aggregation strategy
- Alerting rules and SLA definitions
- Performance monitoring

**8. Testing Strategy**

- Coverage targets and test types
- Testing framework selection
- Performance and security testing
- Quality gates and automation

**9. Documentation & Knowledge**

- API and code documentation standards
- Architecture diagram requirements
- Knowledge sharing and onboarding
- Public vs internal documentation

**10. Accessibility & I18N**

- WCAG compliance requirements
- Supported languages and locales
- RTL language support
- Accessibility testing strategy

**11. Team & Collaboration**

- Team size, roles, and structure
- Communication and project management tools
- Code review and development processes
- Remote/hybrid work considerations

**12. Development Environment**

- Local development setup requirements
- Docker development environment
- Development tools and IDE configurations
- Onboarding time targets

**13. Language & Communication**

- Primary development languages
- Documentation languages
- Code comment standards
- International communication needs

**14. User Experience Level**

- Programming experience assessment
- Stack familiarity evaluation
- Learning preferences and mentorship needs
- Knowledge gaps identification

### 2️⃣ **PHASE 2: Architecture Generation**

```yaml
ARCHITECTURE:
  - Generate project scaffolding
  - Create templates (env, CI/CD, Docker)
  - Configure dev environment
  - Set up initial folder structure
```

### 3️⃣ **PHASE 3: Language Configuration**

```yaml
LANGUAGE_PREFERENCES:
  ALWAYS ASK USER:
    - User interaction language
    - Private documentation language
    - Public documentation language
    - Comments and docstrings language
```

### 4️⃣ **PHASE 4: Database & MCP Setup**

```yaml
DATABASE_AND_MCP:
  - Configure MCP SQLite
  - Create project.db
  - Initialize schema
  - Pre-create agent structures
```

### 5️⃣ **PHASE 5: CLAUDE.MD Creation**

```yaml
CLAUDE_MD:
  - Create with language preferences
  - Include architecture decisions
  - Document project structure
  - Set development guidelines
```

### 6️⃣ **PHASE 6: Dynamic Agent Creation**

```yaml
AGENT_CREATION:
  - Create project-specific agents
  - NOT base specialists (they exist in ~/.claude/agents)
  - Based on planned architecture
  - Multiple Task calls in parallel
```

### 7️⃣ **PHASE 7: Initial Code Generation**

```yaml
CODE_GENERATION:
  - Generate initial codebase
  - Create boilerplate files
  - Set up test structure
  - Configure development environment
```

### 8️⃣ **PHASE 8: Finalization**

```yaml
FINALIZATION:
  - Confirm all components created
  - Run initial tests
  - Present project summary
  - List next steps for development
```

---

## 📊 /init VS /setup COMPARISON

| Feature             | Claude Code /init      | ClaudeSquad /setup               |
| ------------------- | ---------------------- | -------------------------------- |
| Analysis            | Sequential single scan | 4 specialized agents in parallel |
| Agent Creation      | ❌ None                | ✅ Dynamic per module            |
| Memory System       | Static CLAUDE.md       | Persistent per agent             |
| Customization       | Limited                | Full specialist ecosystem        |
| Parallel Processing | No                     | Yes (10 concurrent)              |
| Error Prevention    | ❌ None                | ✅ Immutable rules               |

---

## 🚀 **REAL PARALLELISM IN CLAUDE CODE**

### **CONFIRMED TECHNICAL CAPABILITIES:**

```yaml
parallel_tasks:
  limit: "10 simultaneous subagents"
  batching: "Claude Code executes in batches"
  context: "Each Task has its own window"
  queue: "Automatic queue if > 10 tasks"
  syntax: "Multiple Task calls in ONE message"
```

### **CORRECT INVOCATION:**

```bash
# ✅ CORRECT - Real parallel:
"Execute these tasks IN PARALLEL:
[Task 1] agent-creator → docs-agent
[Task 2] agent-creator → api-agent
[Task 3] agent-creator → frontend-agent
[Task 4] agent-creator → database-agent"

# ❌ INCORRECT - Sequential:
Task → agent-creator → docs-agent
Task → agent-creator → api-agent
Task → agent-creator → frontend-agent
```

---

## 🔧 **HOOKS AND COMMANDS LOCATION**

### **DEFINITIVE ANSWER:**

```yaml
HOOKS:
  global: ~/.claude/settings.json
  project_shared: .claude/settings.json (committed to repo)
  project_local: .claude/settings.local.json (not committed, personal)
  reason: "Configured in settings files"

COMMANDS:
  location: .claude/commands/
  reason: "Customized per project"

MEMORY:
  created_by: "agent-creator automatically"
  location: ".claude/memory/agents/[agent-name]/"
 MEMORY:
   created_by: "agent-creator automatically"
   location: ".claude/memory/project.db"
   structure: "8 memory types stored in SQLite: knowledge, structure, patterns, dependencies, quality, operations, context, domain"
GLOBAL_VS_LOCAL:
  - .claude/: "In the analyzed project"
  - NOT in ClaudeSquad: "It's template, not destination"
```

---

## ❌ **COMMON ERRORS**

- ❌ Running setup agents sequentially
- ❌ Only analyzing without creating anything
- ❌ Asking user what to create
- ❌ Not creating agent memory
- ❌ Creating in ClaudeSquad instead of target project

---

## 🎯 **EXAMPLE EXECUTION**

```bash
User: /setup C:\project\example

Claude:
1. [Phase 1] Environment verification ✅

2. [Phase 2 - REAL PARALLEL] "Analyze this project IN PARALLEL using 4 specialized agents:
   [Task 1] setup-context
   [Task 2] setup-codebase
   [Task 3] setup-infrastructure
   [Task 4] setup-environment"

3. [Phase 3] Language Configuration:
   "What language preferences:
   - User interaction: English/Spanish?
   - Private documentation: English/Spanish?
   - Public documentation: English?
   - Comments/docstrings: English/Spanish?"

4. [Phase 4] Initialize database: Creates project.db with all tables and MCP configuration

5. [Phase 5] Creates complete CLAUDE.md with language preferences + aggregated analysis

6. [Phase 6 - REAL PARALLEL] "Create these agents IN PARALLEL:
   [Task 1] agent-creator → api-agent (creates .claude/agents/api-agent.md)
   [Task 2] agent-creator → database-agent (creates .claude/agents/database-agent.md)
   [Task 3] agent-creator → frontend-agent (creates .claude/agents/frontend-agent.md)"

7. [Phase 7 - REAL PARALLEL] Deep module analysis by all agents

8. [Phase 8] Confirms: "✅ Setup complete: 3 agents created with memories in SQLite database"
```

---

---

## 🚩 **FLAGS Protocol (NEW EXTENDED SYSTEM)**

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
5. **Lock/Unlock**: For conversation flows needing more info

**Key Features**: 
- Multiple targets via separate flag rows
- Lock/unlock for bidirectional conversations  
- Claude sees only counts, agents see full context

---

**THIS IS THE OFFICIAL FLOW. NO INTERPRETATIONS.**
