# 🚀 {{project_name}} Project Configuration - ClaudeSquad Edition

## ⚠️ CRITICAL: ClaudeSquad System Active

**Specialized agents are configured with persistent knowledge and full tool access.**

## 🚩 FLAGS SYSTEM - Cross-Domain Communication

**CRITICAL**: When agents detect issues affecting OTHER modules, they create FLAGS for automatic coordination.

### Your Role in Flags Processing
1. **When agent says "🚩 FLAG CREATED: [type] for [module]"**:
   - Read `.claude/memory/flags/pending.json` for details
   - Identify target module from `flag.module_affected`
   - Delegate DIRECTLY to `[module]-agent` with complete flag context

2. **Flag Types & Direct Routing**:
   ```yaml
   DATABASE_INVESTIGATION → database-agent
   SECURITY_REVIEW → security-agent  
   API_CHANGE → api-agent
   PERFORMANCE_ISSUE → performance-agent
   ARCHITECTURE_CONFLICT → architecture-agent
   ```

3. **Multi-Module Flags**: If `affects_multiple`, delegate to ALL listed agents

### 🧠 SIMPLIFIED SYSTEM

**Dynamic agents ALREADY HAVE:**
- ✅ Complete knowledge of their modules
- ✅ Integrated persistent memory  
- ✅ Access to all tools
- ✅ Updated project context

### ✅ DIRECT INVOCATION:
```
@{{agent_example}}, I need help with...

@api-agent, review this implementation...

@frontend-agent, optimize this component...
```

### 🚀 REAL PARALLELISM:
```
# MULTIPLE AGENTS IN PARALLEL (limit: 10 simultaneous)
"Query these agents IN PARALLEL:
[Task 1] {{first_agent}} → analyze module structure
[Task 2] {{second_agent}} → review dependencies  
[Task 3] {{third_agent}} → validate patterns"
```

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

## 🚩 FLAGS System - Coordination

### What FLAGS are
Cross-agent coordination messages in SQLite database.

### FLAGS Workflow

When user requests `/flags`:
- Invoke @flags-agent 
- @flags-agent analyzes all pending FLAGS
- Follow its orchestration instructions

You DON'T check FLAGS - agents handle their own FLAGS when invoked.

Claude is router. Agents manage FLAGS. @flags-agent orchestrates when requested.

## 📋 Dynamic Agent Invocation Protocol

### 🚨 CRITICAL: ALWAYS PROVIDE COMPLETE CONTEXT

**Agents have integrated knowledge but need specific context for the current task.**

### ✅ CORRECT Flow:

```
1. DIRECT QUERY to specialized agent:
   
   "@{{agent_example}}, I need to implement [function X]. 
   
   CONTEXT:
   - Location: [specific module path]
   - Files: [relevant files]
   - Patterns: [detected patterns]
   - Constraints: [specific constraints]
   
   How should I proceed?"
   
2. IMPLEMENTATION with engineer:
   
   "@engineer-[framework], implement according to agent specifications:
   [INCLUDE complete response from specialized agent]"
   
3. FINAL REVIEW:
   
   "@{{agent_example}}, review this implementation: [details]"
```

## 🔄 Multi-Agent Orchestration

### **REAL PARALLEL - Multiple queries:**
```bash
"Query these agents IN PARALLEL:
[Task 1] {{first_agent}} → module analysis
[Task 2] {{second_agent}} → domain patterns  
[Task 3] security-coordinator → security requirements"
```

### **Coordinated implementation:**
1. Receive context from multiple agents simultaneously
2. Instruct engineers with complete context
3. Specialized agents review implementation
4. Iterative corrections if necessary
5. Knowledge updated automatically

### **ADVANTAGE of parallelism:**
- Richer context in less time
- Informed decisions by multiple specialists
- More robust implementation from the start

## 🎯 Available Agents for {{project_name}}

{{#each agents}}
### **{{name}}**
- **Module**: {{module}}
- **Specialty**: {{expertise}}
- **Files**: {{file_count}} files
- **Usage**: `@{{name}}, [your query about {{domain}}]`

{{/each}}

## 🛠️ System Access & Commands

### MCP Server Access
**You have DIRECT access to these MCP servers:**

#### SQLite Database MCP
- **Database**: `.claude/memory/project.db`
- **Direct SQL queries**: Use `mcp__MCP_SQLite_Server__query` tool
- **Tables**: sessions, jobs, agents_dynamic, agent_memory, flags, messages, tool_logs, todos, agent_health
- **Example**: `mcp__MCP_SQLite_Server__query("SELECT * FROM sessions WHERE job_id = 'job_123'")`

#### Context7 MCP  
- **Purpose**: Library documentation and version history
- **Access**: Use `mcp__context7__resolve-library-id` and `mcp__context7__get-library-docs`
- **Usage**: When you need up-to-date docs for frameworks/libraries

#### Other Available MCPs
- **Git MCP**: Git operations (use Bash tool instead for safety)
- **Fetch MCP**: Web content retrieval  
- **Trello MCP**: Project management integration
- **Voice Mode MCP**: Voice conversation capabilities
- **Playwright MCP**: Browser automation
- **IDE MCP**: Development environment integration

**Note**: Check available MCP tools with `/mcp` command

### Essential Commands

```bash
# List all available agents
uv run python .claude/scripts/agent_db.py list-agents

# Orchestrate FLAGS when user requests
/flags

# Monthly agent update
/setup --update
```

## 🚨 Troubleshooting

If an agent doesn't respond correctly:
1. Verify it exists in `.claude/agents/[agent-name].md`
2. Confirm it has memory in `.claude/memory/agents/[agent_name]/`
3. Use direct invocation: `@agent-name, [your query]`
4. For parallelism: multiple Task calls in one message

## 🏗️ PROJECT: {{project_name}}

<!-- INSERT: PROJECT_CONTEXT -->
<!-- Dynamic content from 4 setup agents will be inserted here:
     - Project Identity (setup-context)
     - Architecture Analysis (setup-infrastructure)
     - Technology Stack Details (setup-codebase)
     - Critical Issues (all agents)
     - Unique Features (setup-context)
     - Next Priorities (setup-infrastructure)
-->

## 🔄 Agent Memory Maintenance

### Monthly Update Schedule
Agents should be updated monthly to maintain accuracy:

```bash
/setup --update
```

- Re-analyzes all modules
- Updates agent memories with current code
- Maintains system accuracy

### Additional Resources
- **Context7 (MCP)**: Available for version history if needed
- **Agents**: Primary source of module expertise
- **FLAGS**: Automatic coordination between agents

---

**For parallelism**: Use multiple Task calls in a single message - Claude Code supports up to 10 simultaneous subagents.