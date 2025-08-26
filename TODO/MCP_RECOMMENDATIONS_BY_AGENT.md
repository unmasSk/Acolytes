# MCP and Tools Recommendations by Agent Type

## 🎯 Tool Assignment Strategy

### Core Principles:
1. **Coordinators** - No code editing tools (no Edit/MultiEdit/Write)
2. **Setup/Analysis Agents** - Read-only tools + code-index MCP
3. **Implementation Agents** - Full toolset including editing
4. **Audit/Security Agents** - Read-only + analysis tools
5. **Service Agents** - Specific MCPs for their domain

## 📊 Complete Tool & MCP Inventory

### Base Tools (17):
- Task, Bash, Glob, Grep, LS, ExitPlanMode
- Read, Edit, MultiEdit, Write, NotebookEdit
- WebFetch, TodoWrite, WebSearch
- BashOutput, KillBash
- ListMcpResourcesTool, ReadMcpResourceTool

### MCP Servers (15):
1. **server-git** - Git operations (13 tools)
2. **server-fetch** - URL fetching (1 tool)
3. **server-everything** - Testing/demo (10 tools)
4. **21st-dev_magic** - UI components (4 tools)
5. **MCP_SQLite_Server** - Project database (8 tools)
6. **voice-mode** - Voice interaction (26 tools)
7. **puppeteer** - Browser automation (6 tools)
8. **chrome-devtools** - Chrome DevTools (65 tools)
9. **sequential-thinking** - Sequential reasoning (1 tool)
10. **n8n-mcp** - Workflow automation (22 tools)
11. **code-index** - Fast code search (10 tools) ⚡
12. **context7** - Library documentation (2 tools)
13. **playwright** - Web automation (24 tools)
14. **ide** - VS Code integration (2 tools)
15. **server-everything** - Testing utilities (10 tools)

## 🏗️ Setup Agents (4)
**Tools:** Read, Bash, Glob, Grep, LS, Task, TodoWrite
**MCPs:** code-index (CRITICAL), MCP_SQLite_Server
**FORBIDDEN:** Edit, MultiEdit, Write, NotebookEdit

### setup.infrastructure
- Additional MCPs: server-git (for repo analysis)

### setup.environment  
- Additional MCPs: None

### setup.context
- Additional MCPs: None

### setup.codebase
- Additional MCPs: ide (for diagnostics if available)

## 🎯 Coordinators (9)
**Tools:** Read, Task, TodoWrite, Grep, Glob, LS, sequential-thinking
**MCPs:** MCP_SQLite_Server (for FLAGS)
**FORBIDDEN:** Edit, MultiEdit, Write, NotebookEdit

### coordinator.backend
### coordinator.frontend  
### coordinator.database
### coordinator.devops
### coordinator.testing
### coordinator.security
### coordinator.infrastructure
### coordinator.migration
### coordinator.data

## 💻 Backend Engineers (7)
**Tools:** ALL base tools
**Base MCPs:** code-index, MCP_SQLite_Server, server-git, context7

### backend.nodejs
- Additional: n8n-mcp, ide

### backend.python
- Additional: NotebookEdit, ide

### backend.go
- Additional: ide

### backend.rust
- Additional: ide

### backend.java
- Additional: ide

### backend.laravel
- Additional: ide

### backend.serverless
- Additional: n8n-mcp

### backend.api
- Additional: n8n-mcp, server-fetch

## 🎨 Frontend Engineers (4)
**Tools:** ALL base tools
**Base MCPs:** code-index, MCP_SQLite_Server, server-git, 21st-dev_magic

### frontend.react
- Additional: playwright, puppeteer, chrome-devtools

### frontend.vue
- Additional: playwright, puppeteer, chrome-devtools

### frontend.angular
- Additional: playwright, puppeteer, chrome-devtools

### frontend.mobile
- Additional: None (mobile-specific)

## 🗄️ Database Engineers (9)
**Tools:** ALL base tools
**Base MCPs:** code-index, MCP_SQLite_Server

### database.postgres
### database.mongodb  
### database.mysql/mariadb
### database.redis
### database.sqlite
- Additional: MCP_SQLite_Server (expert usage)

### database.pgvector
- Additional: context7 (for AI docs)

### database.postgis
- Additional: None

### database.vectorial
- Additional: context7 (for AI docs)

## 🔧 Service Engineers (6)
**Tools:** ALL base tools
**Base MCPs:** code-index, MCP_SQLite_Server, server-git

### service.auth
- Additional: None

### service.ai
- Additional: context7, voice-mode

### service.integrations
- Additional: n8n-mcp, server-fetch

### service.data
- Additional: n8n-mcp

### service.communication
- Additional: voice-mode

### service.mapbox
- Additional: None

## 💰 Business Engineers (3)
**Tools:** ALL base tools
**Base MCPs:** code-index, MCP_SQLite_Server

### business.payment
### business.billing
### business.subscription

## 🚀 Operations (13)
**Tools:** Read, Bash, Grep, Glob, LS, TodoWrite
**MCPs:** code-index, MCP_SQLite_Server, server-git
**FORBIDDEN:** Edit, MultiEdit, Write (except ops.bash, ops.iac)

### ops.bash
- ALLOWED: Edit, MultiEdit, Write (for scripts)

### ops.iac
- ALLOWED: Edit, MultiEdit, Write (for terraform/ansible)

### ops.cicd
- Additional: n8n-mcp

### ops.containers
### ops.git
### ops.monitoring
### ops.performance
### ops.troubleshooting
### ops.webserver

## 🔍 Audit Agents (3)
**Tools:** Read, Bash, Grep, Glob, LS, WebSearch
**MCPs:** code-index, MCP_SQLite_Server
**FORBIDDEN:** Edit, MultiEdit, Write, NotebookEdit

### audit.security
### audit.compliance

## 📊 Analyst Agents (2)
**Tools:** Read, Bash, Grep, Glob, LS, WebSearch, TodoWrite
**MCPs:** code-index, MCP_SQLite_Server
**FORBIDDEN:** Edit, MultiEdit, Write

### analyst.strategic
### analyst.data
- ALLOWED: NotebookEdit (for data analysis)

## 📝 Other Agents

### docs.specialist
**Tools:** ALL base tools
**MCPs:** code-index, MCP_SQLite_Server, context7

### plan.strategy
**Tools:** Read, Task, TodoWrite, sequential-thinking
**MCPs:** MCP_SQLite_Server
**FORBIDDEN:** Edit, MultiEdit, Write

### agent-creator
**Tools:** Read, Write, MultiEdit, Glob, Grep
**MCPs:** code-index, MCP_SQLite_Server
**Note:** Creates agents, needs Write

### flags.agent / flags-agent
**Tools:** Read, Task, TodoWrite
**MCPs:** MCP_SQLite_Server (primary tool)
**FORBIDDEN:** Edit, MultiEdit, Write

## 🎯 Testing Agents (3)
**Tools:** ALL base tools
**MCPs:** code-index, MCP_SQLite_Server, playwright, puppeteer

### coordinator.testing
### test.automation
### test.quality

## 📋 Summary Statistics

- **Total Agents:** 57
- **Agents with NO Edit/MultiEdit:** 23 (40%)
  - All Coordinators (9)
  - All Setup agents (4)
  - Most Ops agents (11, except bash/iac)
  - All Audit agents (3)
  - Most Analyst agents (1, except data)
  - Plan/Flags agents (2)
  
- **Most Used MCPs:**
  1. code-index - 57 agents (100%)
  2. MCP_SQLite_Server - 57 agents (100%)
  3. server-git - 30+ agents
  4. context7 - 10+ agents
  5. playwright/puppeteer - Frontend & Testing agents

## 🚀 Implementation Priority

1. **Phase 1:** Update all Setup agents (4) - Remove Edit/MultiEdit
2. **Phase 2:** Update all Coordinators (9) - Remove Edit/MultiEdit
3. **Phase 3:** Update Ops agents (13) - Remove Edit/MultiEdit except bash/iac
4. **Phase 4:** Update Audit/Analyst agents (5) - Remove Edit/MultiEdit
5. **Phase 5:** Add specialized MCPs to implementation agents
6. **Phase 6:** Verify consistency across all agents

## Notes

- **code-index** is MANDATORY for all agents for fast file operations
- **MCP_SQLite_Server** is MANDATORY for FLAGS system
- **sequential-thinking** recommended for complex reasoning agents
- **21st-dev_magic** for UI-generating agents only
- **voice-mode** for agents that interact with users
- **n8n-mcp** for workflow/automation agents