# Agent Tools Optimization - Specialized Tool Profiles

## Overview

Analysis of 4 repositories in MEJORAS-INVESTIGACION reveals clear patterns in tool usage across agent specializations. Instead of giving all agents access to all tools, we can optimize token usage by creating specialized tool profiles.

## Current Problem

- **All 57 agents** currently have access to **all Claude tools** + **all MCP tools**
- **Token waste**: Auditors don't need Write/Edit, analysts don't need Bash
- **Security risk**: Agents with unnecessary write permissions
- **Performance**: Unnecessary tool loading and context

## Research Sources

1. **awesome-claude-code-subagents**: 100+ agents with detailed tool specifications
2. **wshobson-agents**: 61+ agents with minimal tool specs
3. **awesome-claude-code**: Claude workflows and commands
4. **claude_code_sub_agents**: Legal analysis examples

## Tool Profiles by Agent Type

### 🔧 Core Universal Tools

**ALL agents need these:**

- `Read` - File reading capability
- `Grep` - Search functionality
- `Glob` - File pattern matching

## MCPs Found in Research Repos (TO INSTALL)

**Infrastructure/DevOps MCPs:**

- `docker` - Container operations
- `kubernetes` - K8s cluster management
- `terraform` - Infrastructure as Code
- `ansible` - Configuration management
- `prometheus` - Monitoring and alerting
- `jenkins` - CI/CD pipelines
- `aws-cli` - AWS services
- `azure-cli` - Azure services
- `gcloud` - Google Cloud services

**Database MCPs:**

- `psql` - PostgreSQL operations
- `mysql` - MySQL operations
- `mongosh` - MongoDB operations
- `redis-cli` - Redis operations
- `pg_dump` - PostgreSQL backup
- `elasticsearch` - Search operations

**Development MCPs:**

- `python` - Python environment
- `jupyter` - Jupyter notebooks
- `pandas` - Data manipulation
- `sklearn` - Machine learning
- `matplotlib` - Data visualization
- `adb` - Android development
- `xcode` - iOS development
- `gradle` - Android builds
- `cocoapods` - iOS dependencies
- `fastlane` - Mobile CI/CD

**Security MCPs:**

- `nessus` - Vulnerability scanning
- `qualys` - Security assessment
- `openvas` - Vulnerability testing
- `prowler` - AWS security
- `scout-suite` - Multi-cloud security
- `compliance-checker` - Compliance validation

**Business/Productivity MCPs:**

- `jira` - Project management
- `salesforce` - CRM operations
- `tableau` - Business intelligence
- `powerbi` - Analytics
- `slack` - Team communication
- `zoom` - Video conferencing

**Documentation MCPs:**

- `markdown` - Markdown processing
- `asciidoc` - AsciiDoc processing
- `sphinx` - Documentation generation
- `mkdocs` - Documentation sites
- `docusaurus` - Documentation platform
- `swagger` - API documentation

**Testing/Quality MCPs:**

- `axe` - Accessibility testing
- `wave` - Web accessibility
- `lighthouse` - Performance auditing
- `pa11y` - Accessibility testing

**Research MCPs:**

- `google-scholar` - Academic research
- `draw.io` - Diagram creation

### 📝 Development Profile (Backend/Full-Stack)

**Usage:** backend.python, backend.nodejs, backend.laravel, backend.go, backend.java, backend.rust, backend.api, backend.serverless

**Claude Tools:**

- `Read`, `Write`, `Edit`, `MultiEdit`, `Bash`, `Grep`, `Glob`
- `NotebookEdit` (for Python agents)

**MCP Tools:**

- `mcp__server-git__*` (Git operations)
- `mcp__MCP_SQLite_Server__*` (Database access)
- `mcp__context7__*` (Documentation lookup)
- `docker` (Container operations) - TO INSTALL
- `psql` (PostgreSQL operations) - TO INSTALL
- `mysql` (MySQL operations) - TO INSTALL
- `redis-cli` (Redis operations) - TO INSTALL

**Reasoning:** Need full file manipulation + database access + git operations

### 🎨 Frontend Profile

**Usage:** frontend.react, frontend.vue, frontend.angular, frontend.mobile

**Claude Tools:**

- `Read`, `Write`, `Edit`, `MultiEdit`, `Bash`, `Grep`, `Glob`

**MCP Tools:**

- `mcp__server-git__*` (Git operations)
- `mcp___21st-dev_magic__*` (UI component generation)
- `mcp__context7__*` (Documentation lookup)
- `mcp__playwright__*` (Browser testing)
- `axe` (Accessibility testing) - TO INSTALL
- `wave` (Web accessibility) - TO INSTALL
- `lighthouse` (Performance auditing) - TO INSTALL
- `adb` (Android development - mobile only) - TO INSTALL
- `xcode` (iOS development - mobile only) - TO INSTALL
- `fastlane` (Mobile CI/CD - mobile only) - TO INSTALL

**Reasoning:** Need UI generation + browser testing + component creation + accessibility

### 🛡️ Security/Audit Profile

**Usage:** audit.security, audit.compliance, coordinator.security

**Claude Tools:**

- `Read`, `Grep`, `Glob` (READ ONLY - no Write/Edit)

**MCP Tools:**

- `mcp__MCP_SQLite_Server__query` (Read-only database access)
- `nessus` (Vulnerability scanning) - TO INSTALL
- `qualys` (Security assessment) - TO INSTALL
- `openvas` (Vulnerability testing) - TO INSTALL
- `prowler` (AWS security) - TO INSTALL
- `scout-suite` (Multi-cloud security) - TO INSTALL
- `compliance-checker` (Compliance validation) - TO INSTALL

**Reasoning:** Analysis and reading only, no code modification rights, specialized security tools

### 📊 Data Analysis Profile

**Usage:** analyst.data, analyst.strategic, service.data

**Claude Tools:**

- `Read`, `Write`, `Grep`, `Glob`, `WebSearch`, `WebFetch`
- `NotebookEdit` (Jupyter notebooks)

**MCP Tools:**

- `mcp__MCP_SQLite_Server__*` (Database analytics)
- `mcp__context7__*` (Research documentation)
- `python` (Python environment) - TO INSTALL
- `jupyter` (Jupyter notebooks) - TO INSTALL
- `pandas` (Data manipulation) - TO INSTALL
- `sklearn` (Machine learning) - TO INSTALL
- `matplotlib` (Data visualization) - TO INSTALL
- `elasticsearch` (Search operations) - TO INSTALL
- `google-scholar` (Academic research) - TO INSTALL
- `tableau` (Business intelligence) - TO INSTALL
- `powerbi` (Analytics) - TO INSTALL

**Reasoning:** Research + analysis + notebook manipulation + data science tools

### 📝 Documentation Profile

**Usage:** docs.specialist

**Claude Tools:**

- `Read`, `Write`, `Edit`, `MultiEdit`, `Grep`, `Glob`, `WebFetch`

**MCP Tools:**

- `mcp__server-git__*` (Git operations for docs)
- `mcp__context7__*` (Documentation research)
- `mcp___21st-dev_magic__*` (UI examples in docs)
- `markdown` (Markdown processing) - TO INSTALL
- `asciidoc` (AsciiDoc processing) - TO INSTALL
- `sphinx` (Documentation generation) - TO INSTALL
- `mkdocs` (Documentation sites) - TO INSTALL
- `docusaurus` (Documentation platform) - TO INSTALL
- `swagger` (API documentation) - TO INSTALL
- `draw.io` (Diagram creation) - TO INSTALL

**Reasoning:** Document creation + research + specialized documentation tools

### 💾 Database Profile

**Usage:** database.postgres, database.mongodb, database.redis, database.sqlite, database.vectorial, database.pgvector, database.postgis, database.mariadb

**Claude Tools:**

- `Read`, `Write`, `Edit`, `MultiEdit`, `Bash`, `Grep`, `Glob`

**MCP Tools:**

- `mcp__server-git__*` (Version control)
- `mcp__MCP_SQLite_Server__*` (Meta-database access)
- Database-specific MCP tools (when available)

**Reasoning:** Database configuration + scripting + performance tuning

### 🧩 Service Profile

**Usage:** service.auth, service.ai, service.communication, service.data, service.integrations, service.mapbox

**Claude Tools:**

- `Read`, `Write`, `Edit`, `MultiEdit`, `Bash`, `Grep`, `Glob`

**MCP Tools:**

- `mcp__server-git__*` (Git operations)
- `mcp__MCP_SQLite_Server__*` (Database access)
- `mcp__context7__*` (Documentation lookup)
- Service-specific MCP tools (Trello, Voice Mode, etc.)

**Reasoning:** Integration + configuration + external service management

### ⚙️ Operations Profile

**Usage:** ops.git, ops.monitoring, ops.containers, ops.webserver, ops.cicd, ops.iac, ops.troubleshooting, ops.performance

**Claude Tools:**

- `Read`, `Write`, `Edit`, `MultiEdit`, `Bash`, `Grep`, `Glob`

**MCP Tools:**

- `mcp__server-git__*` (Git operations)
- `mcp__MCP_SQLite_Server__*` (Database access)
- `docker` (Container operations) - TO INSTALL
- `kubernetes` (K8s cluster management) - TO INSTALL
- `terraform` (Infrastructure as Code) - TO INSTALL
- `ansible` (Configuration management) - TO INSTALL
- `prometheus` (Monitoring and alerting) - TO INSTALL
- `jenkins` (CI/CD pipelines) - TO INSTALL
- `aws-cli` (AWS services) - TO INSTALL
- `azure-cli` (Azure services) - TO INSTALL
- `gcloud` (Google Cloud services) - TO INSTALL

**Reasoning:** Full system access + comprehensive infrastructure management tools

### 🏢 Business Profile

**Usage:** business.payment, business.billing, business.subscription

**Claude Tools:**

- `Read`, `Write`, `Edit`, `Grep`, `Glob`
- Limited `Bash` (configuration only)

**MCP Tools:**

- `mcp__MCP_SQLite_Server__*` (Database access)
- `mcp__trello__*` (Business workflow)
- `jira` (Project management) - TO INSTALL
- `salesforce` (CRM operations) - TO INSTALL
- `tableau` (Business intelligence) - TO INSTALL
- `powerbi` (Analytics) - TO INSTALL
- `slack` (Team communication) - TO INSTALL
- `zoom` (Video conferencing) - TO INSTALL

**Reasoning:** Business logic + workflow management + business intelligence tools

### 🎯 Coordinator Profile

**Usage:** coordinator.backend, coordinator.database, coordinator.devops, coordinator.frontend, coordinator.infrastructure, coordinator.migration, coordinator.security, coordinator.testing

**Claude Tools:**

- `Read`, `Write`, `Edit`, `Grep`, `Glob`, `WebSearch`, `WebFetch`
- Limited `MultiEdit` and `Bash`

**MCP Tools:**

- `mcp__MCP_SQLite_Server__*` (Database access)
- `mcp__context7__*` (Research and documentation)

**Reasoning:** Strategic analysis + limited implementation capabilities

## Implementation Strategy

### Phase 1: Add Tool Profiles to Agent Frontmatter

```yaml
---
name: backend.python
description: ...
model: sonnet
color: blue
tool_profile: development
mcp_profile: development
---
```

### Phase 2: Create Profile Definitions

```yaml
# .claude/config/tool-profiles.yml
development:
  claude_tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, NotebookEdit]
  mcp_tools: [mcp__server-git__*, mcp__MCP_SQLite_Server__*, mcp__context7__*]

security:
  claude_tools: [Read, Grep, Glob]
  mcp_tools: [mcp__MCP_SQLite_Server__query]

documentation:
  claude_tools: [Read, Write, Edit, MultiEdit, Grep, Glob, WebFetch]
  mcp_tools: [mcp__server-git__*, mcp__context7__*, mcp___21st-dev_magic__*]
```

### Phase 3: Update Agent System

- Modify agent loading to respect tool profiles
- Update Task tool to filter available tools per agent
- Add validation to prevent unauthorized tool usage

## Benefits

### Token Optimization

- **Estimated 40-60% reduction** in tool-related tokens per agent invocation
- **Faster agent loading** with fewer tools to initialize
- **Cleaner context** without irrelevant tools

### Security Improvement

- **Principle of least privilege**: Agents only get tools they need
- **Reduced attack surface**: Limited write access for audit agents
- **Better isolation**: Specialized tools for specialized functions

### Performance Enhancement

- **Faster tool resolution** with smaller tool sets
- **Reduced memory usage** per agent invocation
- **Cleaner error messages** without irrelevant tools

### Maintenance Benefits

- **Clear tool dependencies** documented per agent type
- **Easier debugging** with focused tool sets
- **Better testing** with predictable tool usage

## Tool Profile Summary Table

| Profile       | Agents               | Core Tools       | Write Access    | MCP Tools            | Use Case            |
| ------------- | -------------------- | ---------------- | --------------- | -------------------- | ------------------- |
| Development   | 8 backend agents     | Full toolkit     | ✅ Yes          | Git + DB + Docs      | Code implementation |
| Frontend      | 4 frontend agents    | Full toolkit     | ✅ Yes          | UI + Browser + Git   | UI development      |
| Security      | 2 audit agents       | Read-only        | ❌ No           | Query-only DB        | Security analysis   |
| Documentation | 1 docs agent         | Write toolkit    | ✅ Limited      | Git + Research + UI  | Documentation       |
| Database      | 8 database agents    | Full toolkit     | ✅ Yes          | DB + Git             | Database management |
| Service       | 6 service agents     | Full toolkit     | ✅ Yes          | External services    | Integration work    |
| Operations    | 8 ops agents         | Full toolkit     | ✅ Yes          | Infrastructure       | System management   |
| Business      | 3 business agents    | Limited toolkit  | ✅ Limited      | Business tools       | Business logic      |
| Data Analysis | 2 analyst agents     | Research toolkit | ✅ Limited      | Analytics + Research | Data analysis       |
| Coordination  | 8 coordinator agents | Strategy toolkit | ✅ Very Limited | Research + DB        | Strategic planning  |

## Next Steps

1. **Define tool profiles configuration** in `.claude/config/tool-profiles.yml`
2. **Update all agent frontmatter** with appropriate profile assignments
3. **Modify agent loading system** to respect tool profiles
4. **Test with sample agents** to verify token reduction
5. **Monitor for missing tools** and adjust profiles as needed
6. **Document profile usage** for future agent creation

This optimization maintains full functionality while significantly reducing token usage and improving security through specialized tool access patterns.
