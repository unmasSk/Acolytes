# 🚀 Acolytes for Claude Code - Revolutionary Multi-Agent System

> Transform Claude Code into an **intelligent project orchestrator** with 57 specialized global agents + project-specific Acolytes. Features enterprise-grade **FLAGS coordination system** for seamless cross-agent communication and persistent SQLite memory for cumulative learning.

[![Agents](https://img.shields.io/badge/Global%20Agents-57-blue)](./.claude/resources/rules/agent-routing-catalog.md) [![FLAGS](https://img.shields.io/badge/FLAGS%20System-Coordination-red)](./.claude/memory)
[![Memory](https://img.shields.io/badge/SQLite%20Memory-10%20Tables-green)](./.claude/memory)
[![Hooks](https://img.shields.io/badge/Active%20Hooks-8-yellow)](./.claude/hooks)
[![Status](https://img.shields.io/badge/Status-Revolutionary-brightgreen)](https://github.com/unmasSk/Acolytes-for-Claude-Code)

## 🧠 What Makes Acolytes for Claude Code REVOLUTIONARY?

### 🚀 BREAKTHROUGH: Enterprise FLAGS Coordination System

**PRODUCTION-READY**: Acolytes for Claude Code features a sophisticated cross-agent communication protocol that enables seamless coordination between 57 specialists. The FLAGS system operates through SQLite database, ensuring no information loss and perfect task handoffs.

#### **FLAGS System Success Stories**

- ✅ **Zero Information Loss**: Perfect context preservation between agent handoffs
- ✅ **Automatic Coordination**: Agents create FLAGS when they detect cross-domain issues
- ✅ **Lock/Unlock Workflows**: Bidirectional communication for complex problem solving
- ✅ **Enterprise Reliability**: Production-tested coordination with audit trails

### 🏗️ Advanced Multi-Agent Architecture

#### **57 Global Specialists** (32 Audited Perfect ✅✅)

- **Engineers (20+)**: Laravel, Python, React, Vue, Node.js, Go, Rust, Java
- **Coordinators (9)**: Backend, Frontend, Database, DevOps, Security, Testing
- **Database Experts (8)**: PostgreSQL, MongoDB, Redis, Vector DBs, PostGIS
- **Operations (8)**: Git, CI/CD, Monitoring, Performance, Troubleshooting
- **Business Systems**: Payments, Billing, Subscriptions with Stripe/PayPal
- **AI/ML Integration**: LangGraph, CrewAI, AutoGen, RAG systems

#### **Acolytes** (Auto-Created per Project)

- One expert agent per detected module (auth-agent, api-agent, etc.)
- Deep module knowledge stored in 8-memory SQLite system
- Created during `/setup` Phase 6 via `agent-creator`

### 🎯 Intelligent Agent Routing System

**17-rule anti-ambiguity system** eliminates agent selection errors:

- **Strategy vs Implementation**: Coordinators for decisions, specialists for execution
- **RAG/Vector Search**: PostgreSQL+embeddings → `database.pgvector`, Any vector platform → `database.vectorial`
- **Auth vs Security**: OAuth/JWT → `service.auth`, Architecture/compliance → `coordinator.security`
- **Multi-Agent Workflows**: Sequential, parallel, and coordinated execution patterns

### 🗃️ Enterprise-Grade Memory System

**SQLite Database** (10 Tables) with MCP integration:

- `agents_catalog`: 57 global agents with routing rules
- `agent_memory`: 8 memory types per agent (knowledge, structure, patterns, etc.)
- `flags`: Cross-domain communication protocol
- `sessions`: Complete conversation history with accomplishments
- `jobs`: Project grouping and active work tracking

## ⚡ Quick Start

### Installation

````bash
# 1. Clone repository
git clone https://github.com/unmasSk/Acolytes-for-Claude-Code.git
cd Acolytes-for-Claude-Code

# 2. Copy agents to Claude Code (Windows)
xcopy /e /i .claude %USERPROFILE%\.claude

# 2. Copy agents to Claude Code (Mac/Linux)
cp -r .claude/* ~/.claude/

# 3. Navigate to YOUR project
cd /path/to/your/project

# 4. Initialize Acolytes for Claude Code (8-Phase Setup)
# 4. Initialize Acolytes for Claude Code (Unified 6-Phase Setup)
claude /setup

### What `/setup` Does (6 Phases):

1. Environment & Database Setup
2. Analysis & Documentation (parallel for existing; interview+specialists for new)
3. CLAUDE.md Creation
4. Jobs & Agent Creation
5. Deep Analysis & Initialization
6. Finalization
| Command       | Description                                           | Agent Integration                 |
| ------------- | ----------------------------------------------------- | --------------------------------- |
| `/setup`      | 6-phase project initialization with parallel analysis | 4 setup agents + dynamic creation |
| `/commit`     | Intelligent commits with 110+ emoji patterns          | `ops.git` specialist              |
| `/todo`       | TODO management with SQLite sync                      | Persistent task tracking          |
| `/flags`      | Process pending FLAGS from agents                     | Cross-agent coordination          |
| `/save`       | Save current session to SQLite database               | Session persistence               |
| `/mcp`        | Verify MCP connections and database status            | System health monitoring          |
| `@agent-name` | Direct agent invocation with specialized context      | Any of 57 global agents           |

### FLAGS System Examples

```bash
# Check and process pending FLAGS
claude "/flags"
# Output: Processing 3 FLAGS: @auth-agent (2), @database.postgres (1)

# Agent creates FLAG for cross-domain issue
# Example: auth-agent detects database schema needs update
FLAG created: "JWT tokens require new 'expires_at' column in users table"
Target: @database.postgres
Status: pending -> processed (automatic coordination)

# TODO management with SQLite persistence
claude "/todo add 'Implement OAuth2 refresh tokens'"
claude "/todo"  # Shows all TODOs with SQLite sync
````

### Agent Invocation & Command Examples

```bash
# Direct specialist access
claude "Use @backend.python to optimize the API endpoints"
claude "Use @database.postgres to fix the indexing issues"
claude "Use @service.auth to implement OAuth2 flow"

# System commands
claude "/save"    # Save session to SQLite
claude "/mcp"     # Check database connections
claude "/flags"   # Process agent coordination
claude "/todo smart"  # AI-powered TODO analysis

# Coordinator for strategic decisions
claude "Use @coordinator.backend to choose microservices architecture"
```

## 🏗️ Revolutionary Architecture

```
Main Claude Session (Orchestrator)
    │
    ├── 🌍 GLOBAL AGENTS (57) - ~/.claude/agents/
    │   ├── 💻 Engineers (20+): backend.laravel, backend.python, frontend.react, etc.
    │   ├── 🎛️ Coordinators (9): Strategic architects for complex decisions
    │   ├── 💾 Database (8): postgres, mongodb, redis, pgvector, vectorial
    │   ├── ⚙️ Operations (8): git, cicd, monitoring, performance
    │   ├── 💼 Business (3): payment, billing, subscription systems
    │   ├── 🔍 Audit (2): security, compliance specialists
    │   └── 📊 Analysis (2): data scientist, strategic analyst
    │
    ├── 🏠 PROJECT AGENTS - project/.claude/agents/
    │   ├── auth-agent (YOUR authentication logic)
    │   ├── api-agent (YOUR API endpoints)
    │   └── [Created per detected module in Phase 6]
    │
    ├── 🚩 FLAGS COORDINATION SYSTEM
    │   ├── Cross-agent communication via SQLite database
    │   ├── Lock/unlock workflows for complex problem solving
    │   ├── Automatic context preservation between specialists
    │   └── Zero information loss in agent handoffs
    │
    └── 🗄️ ENTERPRISE MEMORY (SQLite + MCP)
        ├── 10 Tables: agents_catalog, agent_memory, flags, sessions
        ├── 8 Memory Types: knowledge, structure, patterns, dependencies
        └── Cross-session persistence with MCP integration
```

## 🗄️ Enterprise Memory System

### SQLite Database (10 Tables)

- **`agents_catalog`**: 57 global agents with routing Keywords & Integrates
- **`agent_memory`**: 8 memory types per agent (knowledge, structure, patterns, dependencies, quality, operations, context, domain)
- **`flags`**: Cross-domain communication protocol with lock/unlock workflows
- **`sessions`**: Complete conversation history with accomplishments and breakthroughs
- **`jobs`**: Project grouping for active work coordination
- **`messages`**: Detailed conversation flow tracking
- **`tool_logs`**: Tool usage analysis and optimization
- **`agent_health`**: Performance metrics for Acolytes
- **`acolytes`**: Project-specific agent configurations
- **`todos`**: Persistent task management across sessions

### MCP Integration

- **Real-time access** to SQLite database during Claude sessions
- **Cross-session memory** persistence without data loss
- **Agent coordination** via FLAGS system in database
- **Automatic session loading** via `session_start.py` hook

## 🚀 Production Usage Examples

### FLAGS-Powered Multi-Agent Coordination

```bash
"Implement complete user authentication system"

# Acolytes for Claude Code automatically:
# 1. coordinator.security → Choose OAuth2 vs JWT strategy
# 2. service.auth → Implement authentication logic
# 3. backend.laravel → Create middleware and controllers
# 4. database.postgres → Design user/role tables
# 5. frontend.react → Build login/register components
# 6. All agents coordinate via FLAGS system in SQLite
```

### Advanced FLAGS Workflows

```bash
# Real-world FLAGS coordination example:
# 1. auth-agent detects JWT expiration issues
#    Creates FLAG: "JWT tokens expiring too quickly, affecting user experience"
#    Target: @database.postgres

# 2. database.postgres reviews FLAG, identifies session table issues
#    Creates FLAG: "Session cleanup job needed, Redis cache misconfigured"
#    Target: @database.redis

# 3. database.redis fixes caching, creates performance FLAG
#    Target: @ops.monitoring

# Result: Complete authentication system optimization with audit trail
```

### Cross-Domain Problem Solving with FLAGS

```bash
"The API is slow and users are complaining"

# Intelligent FLAGS workflow:
# 1. api-agent → Detects N+1 query patterns
# 2. Creates FLAG for @database.postgres: "N+1 queries in user endpoints"
# 3. database.postgres → Adds indexes and optimizes queries
# 4. Creates FLAG for @ops.monitoring: "Performance improved, need alerts"
# 5. ops.monitoring → Sets up monitoring and alerting
# 6. Result: 2.3s → 87ms response time (26x improvement)

# Every step is tracked in SQLite with full audit trail
```

### Production Commands Workflow

```bash
# Phase 1: Strategic Architecture
claude "Use @coordinator.backend to design microservices architecture"

# Phase 2: Session Management
claude "/save"     # Save architectural decisions to SQLite
claude "/flags"    # Process any cross-agent coordination needs

# Phase 3: Implementation with TODO tracking
claude "/todo add 'Implement user microservice with Node.js'"
claude "/todo add 'Set up PostgreSQL shared database'"
claude "Use @backend.nodejs and @database.postgres for implementation"

# Phase 4: Quality & Monitoring
claude "/todo smart"  # AI analysis of remaining tasks
claude "/mcp"        # Verify all systems healthy
claude "Use @audit.security to review the implementation"
```

## 📦 Agent Catalog (57 Global + Dynamic)

### ✅✅ Audited Perfect (32 agents - 56.1%)

**Complete with FLAGS, routing, and comprehensive expertise:**

#### **🏗️ Engineering Specialists**

- **`backend.laravel`** (1,634 lines) - Laravel 11+, Eloquent, Livewire, Horizon
- **`backend.nodejs`** (3,975 lines) - Node.js 20+, NestJS, TypeScript, microservices
- **`backend.python`** (3,274 lines) - Django, FastAPI, Celery, ML integration
- **`backend.go`** (1,967 lines) - Go 1.21+, gRPC, concurrency patterns
- **`backend.rust`** (1,754 lines) - Actix-web, Tokio, WebAssembly
- **`frontend.react`** (1,889 lines) - React 18+, Next.js, TypeScript
- **`frontend.vue`** (1,885 lines) - Vue 3+, Nuxt.js, Composition API
- **`frontend.angular`** (1,404 lines) - Angular 17+, RxJS, Signals API

#### **💾 Database Experts**

- **`database.postgres`** (1,974 lines) - PostgreSQL 15+, advanced indexing
- **`database.vectorial`** (6,498 lines) - Multi-platform vector databases
- **`database.pgvector`** (2,739 lines) - PostgreSQL + AI search
- **`database.mongodb`** (2,411 lines) - MongoDB 7+, aggregation pipelines
- **`database.redis`** (1,270 lines) - Redis 7+, caching strategies

#### **🤝 Business Systems**

- **`business.payment`** (2,762 lines) - Stripe, PayPal, PCI compliance
- **`business.billing`** (2,121 lines) - Invoice generation, tax calculation
- **`business.subscription`** (2,370 lines) - SaaS models, churn prevention

#### **🎛️ Strategic Coordinators**

- **`coordinator.backend`** (786 lines) - Microservices architecture
- **`coordinator.database`** (2,032 lines) - Data architecture decisions
- **`coordinator.frontend`** (299 lines) - UI framework selection
- All other coordinators (DevOps, Security, Testing, etc.)

### ✅ Created (11 agents - 19.3%)

Basic structure exists, being enhanced to audited perfect status.

### 🔳 In Development (14 agents - 24.6%)

Strategic placeholders for future expansion.

## 🎯 Acolytes for Claude Code vs Standard Claude Code

| Feature               | Standard Claude Code  | Acolytes for Claude Code                       |
| --------------------- | --------------------- | ----------------------------------------------- |
| **Agents**            | Single AI assistant   | **57 global specialists + Acolytes**      |
| **Memory**            | Session-only context  | **Persistent SQLite + MCP integration**         |
| **Coordination**      | Manual task switching | **Autonomous FLAGS system**                     |
| **Parallelism**       | Sequential processing | **FLAGS-based coordination and agent handoffs** |
| **Project Knowledge** | Generic responses     | **Deep module-specific expertise**              |
| **Agent Routing**     | Manual selection      | **17-rule anti-ambiguity system**               |
| **Setup**             | Manual configuration  | **6-phase automated initialization**            |

## 📈 Project Status & Recent Breakthroughs

### 🏆 Major Achievements (2025-08-23)

```
[██████████████████░░] 90% Production Features Complete

✅ PRODUCTION: Enterprise FLAGS Coordination System
✅ 57 Global Agents with intelligent routing
✅ SQLite database with 10 tables (4.2MB)
✅ 8 active hooks for session management
✅ Production command system (/todo, /flags, /save, /mcp)
✅ MCP integration for persistent memory
✅ 32 agents audited perfect (56.1% completion)
```

### Recent Production Updates

- **🚩 ENTERPRISE FLAGS**: Production-ready cross-agent coordination system
- **🎯 Agent Routing Evolution**: 17-rule system with Keywords & Integrates
- **💾 Enterprise Memory**: 10-table SQLite database with rich session history
- **🏗️ Advanced Architecture**: Coordinators + Specialists + Acolytes
- **⚙️ Production Hooks**: 8 verified hooks for automated workflows
- **🔧 Production Commands**: /todo, /flags, /save, /mcp for workflow optimization

### 🚧 Active Development Areas

- **Agent Completion**: 14 agents in development (24.6% remaining)
- **Testing Framework**: Comprehensive agent testing suite
- **Documentation**: API documentation generation
- **Performance**: Cross-agent coordination optimization

## 🌟 Why Acolytes for Claude Code is Revolutionary

### **Enterprise FLAGS Coordination System**

No other system provides seamless cross-agent coordination through a sophisticated FLAGS protocol stored in SQLite. This enables zero information loss during agent handoffs and perfect task continuity.

### **Enterprise-Grade Architecture**

Unlike simple prompt templates, Acolytes for Claude Code is a complete development ecosystem with persistent memory, intelligent routing, and cross-agent coordination that scales with your project complexity.

### **Production-Ready Command System**

With commands like /todo, /flags, /save, and /mcp, Acolytes for Claude Code provides a complete workflow management system that bridges sessions and maintains project continuity.

## 🤝 Contributing

### Priority Contribution Areas

1. **Agent Development**: Complete the 14 remaining agents (24.6%)
2. **Testing Framework**: Unit tests for agent functionality
3. **Documentation**: Enhanced agent and system documentation
4. **Optimization**: Performance improvements for FLAGS system

### Agent Development Template

Use **`backend.laravel`** (1,634 lines) as the gold standard template for new agents. It includes:

- Complete FLAGS system integration
- Comprehensive technical expertise
- Quality levels and best practices
- Execution guidelines

## 📚 Comprehensive Documentation

### **Core System Documentation**

- **[Agent Routing Rules](./.claude/resources/rules/agent-routing-catalog.md)** - Complete catalog with 17-rule system
- **[Setup Documentation](./.claude/commands/setup.md)** - 8-phase initialization process
- **[FLAGS Coordination System](./.claude/memory)** - Enterprise cross-agent communication
- **[CLAUDE.md Template](./.claude/resources/templates/claude-md-template.md)** - Project configuration

### **Research & Evolution Documentation**

- **[MEJORAS-INVESTIGACION/](./MEJORAS-INVESTIGACION/)** - Research collections and proposals
- **[awesome-claude-code](./MEJORAS-INVESTIGACION/awesome-claude-code/)** - Curated resources with automation
- **[Agent Routing Evolution](./AGENT-ROUTING-EVOLUTION.md)** - System evolution history
- **[FLAGS System Documentation](./.claude/memory)** - Cross-agent coordination protocol

## 🏆 Recognition & Impact

**Acolytes for Claude Code represents a breakthrough in AI agent orchestration:**

- ✅ First enterprise FLAGS coordination system for AI agents
- ✅ First implementation of persistent cross-session agent memory
- ✅ First intelligent agent routing system for Claude Code
- ✅ First production command system (/todo, /flags, /save, /mcp)

## 📜 License

MIT License - Free for commercial and personal use.

---

## ⭐ Transform Your Development Experience

Acolytes for Claude Code isn't just another tool—it's a **revolutionary development paradigm** that transforms Claude Code into an intelligent, coordinated team of specialists with persistent memory and autonomous coordination capabilities.

**Ready to experience the future of AI-assisted development?**

```bash
git clone https://github.com/unmasSk/Acolytes-for-Claude-Code.git
cd Acolytes-for-Claude-Code
xcopy /e /i .claude %USERPROFILE%\.claude
cd /your/project
claude /setup
```

**Welcome to the age of autonomous AI development teams.** 🚀✨
