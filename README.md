# 🚀 ClaudeSquad

> Complete multi-agent orchestration system for Claude Code with 71 specialized engineers, dynamic agent generation, and **persistent memory system**. Transform Claude into an intelligent project orchestrator that delegates complex tasks to domain experts with cumulative learning capabilities.

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-blue)](https://www.anthropic.com/claude)
[![Agents](https://img.shields.io/badge/Engineers-71-green)](./.claude/agents)
[![Memory](https://img.shields.io/badge/Memory-Persistent-red)](./.claude/memory)
[![Setup](https://img.shields.io/badge/Setup-Automated-orange)](./.claude/commands/setup.md)
[![Version](https://img.shields.io/badge/Version-2.0.0-purple)](./MEJORAS-INVESTIGACION/ROADMAP-COMPLETO.md)

## 🎯 What is ClaudeSquad?

ClaudeSquad transforms Claude Code from a single AI assistant into a complete development team. Claude becomes the orchestrator, intelligently delegating to 71 specialized engineers, each an expert in their domain.

### 🏗️ System Architecture

```
Claude Principal (Main Conversation) = ORCHESTRATOR
    │
    ├── LEVEL 1: 9 Domain Coordinators
    │   ├── backend-coordinator
    │   ├── frontend-coordinator
    │   ├── database-coordinator
    │   └── [6 more coordinators...]
    │
    ├── LEVEL 2: 62 Specialized Engineers
    │   ├── laravel-engineer, react-engineer, postgres-engineer
    │   ├── docker-engineer, security-auditor, test-automation-engineer
    │   └── [56 more engineers...]
    │
    └── LEVEL 3: Project-Specific Modules (auto-generated)
        └── Created based on your project needs
```

**Key Innovation:** No separate orchestrator agent - Claude itself becomes the orchestrator through CLAUDE.md configuration.

## ✨ Core Features

### 🎯 Intelligent `/setup` Command

One command configures everything:

```bash
claude /setup
```

**For NEW projects:** Interactive conversation gathering 14 areas of requirements
**For EXISTING projects:** Automatic detection and configuration

### 📊 Comprehensive Project Analysis

Three specialized engineers analyze your project:
- `discovery-engineer` - Structure, stack, dependencies
- `quality-engineer` - Tests, security, performance
- `architecture-engineer` - Patterns, tech debt, improvements

### 🧠 Persistent Memory System v2.0

**NEW**: Agents now maintain memory between invocations! Each agent starts fresh but automatically loads their previous knowledge.

```
.claude/memory/
├── agents/           # Per-agent persistent knowledge
│   ├── dream-agent/
│   │   ├── knowledge.json    # Module understanding
│   │   ├── history.json      # Previous interactions
│   │   └── patterns.json     # Detected patterns
│   └── [agent-name]/
├── context/          # Project-wide context
├── flags/            # Cross-domain communications
└── sessions/         # Session tracking
```

**How it works:**
1. **SubagentStop hook** automatically saves agent knowledge
2. Next invocation loads previous memory
3. Agents build cumulative expertise over time
4. Cross-domain flags enable agent collaboration

### 🔄 Cross-Domain Communication

Automatic coordination through flags:
- Engineer discovers issue → Sets flag → Orchestrator routes to specialist
- No context pollution between agents
- Systematic problem resolution

## 🚀 Quick Start

### Prerequisites

- Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- Git configured
- Your preferred IDE

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ClaudeSquad.git
cd ClaudeSquad

# 2. Copy to global Claude directory (Windows)
Copy-Item ".\.claude\*" "$env:USERPROFILE\.claude\" -Recurse -Force

# 2. Copy to global Claude directory (Mac/Linux)
cp -r .claude/* ~/.claude/

# 3. Navigate to your project
cd /path/to/your/project

# 4. Run setup
claude /setup
```

## 🎮 Usage Examples

### Automatic Orchestration

```bash
"Build a user authentication system with 2FA"
# Claude automatically:
# → Delegates to backend-coordinator
# → Laravel-engineer implements auth
# → Database-coordinator designs schema
# → Security-auditor reviews implementation
```

### Direct Engineer Invocation

```bash
"Have the react-engineer optimize component performance"
```

### Complex Problem Solving

```bash
"The checkout process is slow"
# Orchestrated investigation:
# → Backend-coordinator checks API
# → Database-coordinator analyzes queries
# → Frontend-coordinator reviews rendering
# → Solution: 500ms → 15ms (33x improvement)
```

## 📦 Available Engineers (71 Total)

### 🎯 Domain Coordinators (9)
- `backend-coordinator` - Orchestrates server-side development
- `frontend-coordinator` - Manages UI/UX implementation
- `database-coordinator` - Oversees data architecture
- `infrastructure-coordinator` - Handles deployment and scaling
- `security-coordinator` - Ensures security compliance
- `testing-coordinator` - Manages quality assurance
- `devops-coordinator` - CI/CD and automation
- `data-coordinator` - Analytics and ML workflows
- `migration-coordinator` - System transitions

### 🔧 Specialized Engineers (62)

**Backend (7):** laravel, fastapi, nodejs, graphql engineers
**Frontend (6):** react, vue, angular, nextjs, ui-ux engineers
**Database (8):** postgres, mysql, redis, sqlite, postgis engineers
**DevOps (9):** docker, git, logging, observability engineers
**Security (8):** security-auditor, compliance, gdpr engineers
**Testing (3):** test-automation, e2e, performance engineers
**Analysis (3):** discovery, quality, architecture engineers
**And 21 more specialists...**

[Full list in .claude/agents/README.md](./.claude/agents/README.md)

## 🛠️ Setup Process

### Phase 0: Environment Verification
- Checks Git, Node, Docker, permissions
- Identifies missing tools
- Provides installation commands

### Phase 1-3: Project Analysis
- Deep analysis by 3 specialized engineers
- Ambiguity clarification if needed
- User confirmation of detected stack

### Phase 4-5: Configuration Generation
- Custom CLAUDE.md for your project
- 30+ configuration templates
- Language and experience preferences

### Phase 6-7: Installation & Verification
- Interactive agent installation
- Complete verification checklist
- Ready-to-use commands

## 📋 What Gets Configured

### For New Projects
- 14 comprehensive requirement areas
- Business domain to deployment strategy
- Security, compliance, monitoring
- Team structure and workflows

### For Existing Projects
- Complete stack detection
- Dependency audit
- Security vulnerability scan
- Performance baseline
- Technical debt assessment

### Generated Files (30+)
- `.env.example`
- `docker-compose.yml`
- `.github/workflows/ci.yml`
- `CONTRIBUTING.md`
- `SECURITY.md`
- And 25+ more...

## 🌍 Language Configuration

Claude adapts to your preferences:
- User communication language
- Documentation language
- Code comments language
- Variable naming conventions
- Commit message language
- Error message languages

## 📈 System Benefits

- **Context Efficiency:** Each engineer uses only needed context
- **Parallel Processing:** Multiple engineers work simultaneously
- **Knowledge Accumulation:** Memory system improves over time
- **Systematic Execution:** Task-based approach prevents oversight
- **Enterprise Ready:** Security, compliance, monitoring built-in

## 📚 Documentation

- [Project Status](./ESTADO-ACTUAL-PROYECTO.md) - Current implementation status
- [System Documentation](./SISTEMA-COMPLETO.md) - Technical architecture
- [Agent Catalog](./.claude/agents/README.md) - All 71 engineers detailed
- [Setup Command](./.claude/commands/setup.md) - Complete setup documentation

## 🚧 Current Status

```
[████████████████████░░░░░░░░] 70% Complete

✅ Architecture Design: 100%
✅ File Structure: 100%
✅ Setup Command: 100%
✅ Documentation: 80%
⏳ Agent Content: 0% (structure ready, content pending)
⏳ Testing: 0%
⏳ Automation: 20%
```

## 🎯 Roadmap

- [ ] Complete agent content (71 engineers)
- [ ] Automated installer script
- [ ] Web-based configuration generator
- [ ] VS Code extension
- [ ] Agent marketplace
- [ ] Performance metrics dashboard

## 🤝 Contributing

This project is in active development. Key areas for contribution:
- Agent content development
- Testing and validation
- Documentation improvements
- Language-specific templates

## 📜 License

MIT License - Free for commercial and personal use

## 🙏 Acknowledgments

- Anthropic team for Claude Code
- Community feedback and contributions
- Inspired by microservices architecture

## 💬 Support & Contact

- GitHub Issues for bugs and features
- Discussions for questions and ideas
- Star ⭐ if you find this useful!

---

**Transform your Claude Code into a complete development team today!** 🚀

*Note: Agents are currently template structures. Content development in progress.*