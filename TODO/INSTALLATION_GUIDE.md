# 🚀 Complete Installation Guide - Acolytes for Claude Code

## 📋 System Requirements

### Required Software
- **Claude Code CLI** (latest version)
- **Git** for version control
- **Python 3.10+** with pip/uv installed
- **Node.js 18+** and npm (for MCP servers)
- **SQLite3** (included with Python)
- **Windows/Mac/Linux** compatible

### Disk Space
- **Minimum**: 500 MB for base installation
- **Recommended**: 2 GB including MCP servers and dependencies

## 🎯 Quick Installation (3 minutes)

### Windows PowerShell
```powershell
# 1. Clone the repository
git clone https://github.com/unmasSk/Acolytes.git
cd Acolytes

# 2. Copy agent files to Claude Code
xcopy /e /i .claude %USERPROFILE%\.claude

# 3. Navigate to your project
cd C:\path\to\your\project

# 4. Initialize the system (8 automated phases)
claude /setup
```

### Mac/Linux Bash
```bash
# 1. Clone the repository
git clone https://github.com/unmasSk/Acolytes.git
cd Acolytes

# 2. Copy agent files to Claude Code
cp -r .claude/* ~/.claude/

# 3. Navigate to your project
cd /path/to/your/project

# 4. Initialize the system
claude /setup
```

## 📦 Detailed Step-by-Step Installation

### Step 1: Environment Preparation

#### 1.1 Verify Requirements
```bash
# Check Claude Code
claude --version

# Check Python
python --version  # Must be 3.10+

# Check Node.js
node --version   # Must be 18+

# Check Git
git --version
```

#### 1.2 Install Missing Dependencies

**Windows:**
```powershell
# Install Python from Microsoft Store or python.org
winget install Python.Python.3.11

# Install Node.js
winget install OpenJS.NodeJS.LTS

# Install Git
winget install Git.Git
```

**Mac:**
```bash
# With Homebrew
brew install python@3.11
brew install node@18
brew install git
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3-pip
sudo apt install nodejs npm
sudo apt install git
```

### Step 2: Clone and Install Acolytes for Claude Code

```bash
# 1. Clone repository
git clone https://github.com/unmasSk/Acolytes.git
cd Acolytes

# 2. Create directory structure (if not exists)
mkdir -p ~/.claude/agents
mkdir -p ~/.claude/commands
mkdir -p ~/.claude/hooks
mkdir -p ~/.claude/memory
mkdir -p ~/.claude/resources
```

### Step 3: Copy System Files

#### Windows (PowerShell as Administrator)
```powershell
# Copy entire .claude structure
xcopy /e /i /y .claude %USERPROFILE%\.claude

# Verify copy
dir %USERPROFILE%\.claude\agents
# You should see 59+ agent .md files
```

#### Mac/Linux
```bash
# Copy preserving structure
cp -r .claude/* ~/.claude/

# Verify
ls -la ~/.claude/agents/ | head -10
# You should see agent files
```

### Step 4: Configure MCP Servers

#### 4.1 Install SQLite MCP Server (CRITICAL)
```bash
# Install SQLite server for persistent memory
claude mcp add sqlite -s user -- npx -y @modelcontextprotocol/server-sqlite

# Verify installation
claude mcp list
# Should show: sqlite: npx -y @modelcontextprotocol/server-sqlite - ✓ Connected
```

#### 4.2 Install Git MCP Server
```bash
# For integrated version control
claude mcp add server-git -s user -- npx -y @modelcontextprotocol/server-git
```

#### 4.3 Install Fetch MCP Server
```bash
# To retrieve information from URLs
claude mcp add server-fetch -s user -- npx -y @modelcontextprotocol/server-fetch
```

#### 4.4 Install Puppeteer MCP (Optional - Web Automation)
```bash
# For visual browser automation
claude mcp add puppeteer -s user -- npx -y @modelcontextprotocol/server-puppeteer
```

#### 4.5 Install Magic UI MCP (Optional - UI Components)
```bash
# For instant React/Vue component generation
claude mcp add 21st-dev_magic -s user -- npx -y 21st.dev
```

### Step 5: Configure SQLite Database

```bash
# 1. Navigate to your project
cd /path/to/your/project

# 2. Create database structure
mkdir -p .claude/memory

# 3. The /setup command will automatically create:
# - project.db with 10 tables
# - Complete schema for agents, sessions, flags, etc.
```

### Step 6: Initialize in Your Project

```bash
# In your project root
cd /path/to/your/project

# Run 8-phase setup
claude /setup
```

#### What `/setup` does:

**Phase 1: Environment & Database Setup**
- Configures SQLite database
- Initializes 10 system tables
- Configures MCP connections

**Phase 2: Analysis & Documentation**
- For existing projects: Parallel analysis with 4 agents
- For new projects: Interactive interview + specialists

**Phase 3: CLAUDE.md Creation**
- Generates project-specific configuration
- Defines conventions and standards

**Phase 4: Jobs & Agent Creation**
- Creates active job in database
- Configures project-specific agents

**Phase 5: Deep Analysis & Initialization**
- Deep module analysis
- Creates Acolytes per module

**Phase 6: Acolyte Creation**
- Generates module-specific agents
- Configures agent memory

**Phase 7: Testing & Validation**
- System verification
- Component testing

**Phase 8: Finalization**
- System verification
- Configuration summary

## 🔧 Hook Installation (Automation)

### Available Hooks
```bash
# View available hooks
ls ~/.claude/hooks/

# Main hooks:
# - session_start.py: Loads previous context automatically
# - todo_sync.py: Syncs TODOs with SQLite
# - pre_tool_use.py: Git MCP protection
# - stop.py: Auto-save session
```

### Activate Hooks
Hooks activate automatically when copying `.claude/hooks/`.
No additional configuration required.

## 🚨 Common Troubleshooting

### Error: "MCP Server not connected"
```bash
# 1. Restart Claude Code
claude exit
claude

# 2. Verify MCP servers
claude mcp list

# 3. If any missing, reinstall
claude mcp remove [name] -s user
claude mcp add [name] -s user -- [command]
```

### Error: "Database not found"
```bash
# Create manually if /setup fails
mkdir -p .claude/memory
touch .claude/memory/project.db

# Retry setup
claude /setup
```

### Error: "Agents not found"
```bash
# Verify agent installation
ls ~/.claude/agents/ | wc -l
# Should show 59+ files

# If missing, recopy
cd /path/to/cloned/repo
cp -r .claude/agents/* ~/.claude/agents/
```

### Windows Error: "Access denied"
```powershell
# Run PowerShell as Administrator
# Then repeat xcopy commands
xcopy /e /i /y .claude %USERPROFILE%\.claude
```

## 📊 Installation Verification

### Complete System Test
```bash
# 1. Verify MCP servers
claude mcp list
# Should show at least: sqlite, server-git, server-fetch

# 2. Verify database
claude "Check SQLite database connection"
# Claude will execute: mcp__MCP_SQLite_Server__db_info

# 3. Verify agents
claude "List available agents"
# Should show 59 agents (52 user + 7 internal)

# 4. Test FLAGS command
claude /flags
# Should show FLAGS system working

# 5. Test TODO system
claude /todo add "Test task"
claude /todo
# Should show added task
```

## 🎯 Post-Installation Configuration

### 1. Customize CLAUDE.md
```bash
# Edit project configuration
claude "Edit CLAUDE.md to add project specific instructions"
```

### 2. Configure Preferred Language
```bash
# In CLAUDE.md add:
## Language Configuration
- **User interaction**: Spanish (or your language)
- **Documentation**: English
- **Code comments**: English
```

### 3. Create First Job
```bash
# Create active job
claude "/job create 'Initial Setup'"
```

### 4. Generate Specific Acolytes
```bash
# If you have specific modules
claude "Create acolyte for authentication module"
claude "Create acolyte for payment module"
```

## 🔐 Security and Best Practices

### Never Do
```bash
# ❌ NEVER use Git MCP to add files
mcp__server-git__git_add with ["."] or ["*"]

# ❌ NEVER commit .claude/memory/project.db
# Add to .gitignore:
echo ".claude/memory/*.db" >> .gitignore
```

### Always Do
```bash
# ✅ Use Bash for git operations
git add -A
git commit -m "message"

# ✅ Regular database backup
cp .claude/memory/project.db .claude/memory/backup_$(date +%Y%m%d).db
```

## 🚀 Essential Post-Installation Commands

```bash
# Agent system
claude "Use @backend.python to optimize the API"
claude "Use @coordinator.database for architecture decisions"

# Task management
claude /todo           # View all tasks
claude /todo smart     # AI analysis of pending tasks
claude /save          # Save current session

# FLAGS coordination
claude /flags         # Process pending FLAGS

# System verification
claude /mcp          # MCP servers status
```

## 📚 Additional Resources

### Documentation
- [GitHub Repository](https://github.com/unmasSk/Acolytes)
- [Agent Catalog](./.claude/resources/rules/agent-routing-catalog.md)
- [Setup Documentation](./.claude/commands/setup.md)
- [FLAGS System](./.claude/memory/README.md)

### Support
- Issues: https://github.com/unmasSk/Acolytes/issues
- Discord: [Community Discord]
- Email: support@acolytes.ai

## ✅ Complete Installation Checklist

- [ ] Claude Code CLI installed and working
- [ ] Python 3.10+ and Node.js 18+ installed
- [ ] Repository cloned successfully
- [ ] .claude files copied to home directory
- [ ] MCP servers installed (sqlite, git, fetch minimum)
- [ ] /setup command executed in project
- [ ] SQLite database created (10 tables)
- [ ] Hooks active and working
- [ ] Basic command tests successful
- [ ] CLAUDE.md customized for your project

## 🎉 Installation Complete!

If all checks are complete, your Acolytes for Claude Code system is ready.

**Recommended next steps:**
1. Run `claude /todo add "Explore available agents"`
2. Try an agent: `claude "Use @backend.python to analyze the codebase"`
3. Review FLAGS: `claude /flags`
4. Save your first session: `claude /save`

**Welcome to the era of autonomous AI development teams!** 🚀✨

---

*Last updated: August 2025*
*Version: 2.0.0 - Enterprise FLAGS System*