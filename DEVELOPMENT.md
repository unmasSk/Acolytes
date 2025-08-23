# 🛠️ ClaudeSquad Development Environment

## 🚨 CRITICAL: Environment Isolation

**ClaudeSquad developers must use isolated environments to avoid conflicts between:**
- 🌐 **Global ClaudeSquad installation** (`~/.claude/`)
- 🔧 **Development workspace** (`~/.claude-dev/`)

## 🎯 Development Environment Setup

### 1. Set Development Environment

```bash
# Enable development mode
export CLAUDE_ENV=dev
echo 'export CLAUDE_ENV=dev' >> ~/.bashrc  # Linux/macOS
echo 'export CLAUDE_ENV=dev' >> ~/.zshrc   # macOS with Zsh
```

**Windows PowerShell:**
```powershell
$env:CLAUDE_ENV = "dev"
[System.Environment]::SetEnvironmentVariable("CLAUDE_ENV", "dev", "User")
```

### 2. Development Directory Structure

When `CLAUDE_ENV=dev`, all ClaudeSquad operations use:

```
~/.claude-dev/                    # Development isolation
├── agents/                       # Development agents (this project's agents)
├── memory/project.db             # Development database
├── hooks/                        # Development hooks
├── scripts/                      # Development scripts
└── resources/                    # Development resources
```

**vs Normal Mode:**
```
~/.claude/                        # Global installation
├── agents/                       # Production agents
├── memory/project.db             # Production database
└── ...
```

## 🔧 Development Workflow

### Daily Development

```bash
# 1. Ensure dev environment
export CLAUDE_ENV=dev

# 2. Verify isolation
echo "Using: $(if [[ "$CLAUDE_ENV" == "dev" ]]; then echo "~/.claude-dev/"; else echo "~/.claude/"; fi)"

# 3. Work on ClaudeSquad normally
claude /setup                     # Uses ~/.claude-dev/
uv run python .claude/scripts/agent_db.py list-agents  # Dev agents only
```

### Switch Between Modes

```bash
# Development mode (working ON ClaudeSquad)
export CLAUDE_ENV=dev
claude /setup  # → Uses ~/.claude-dev/

# Production mode (using ClaudeSquad globally)
unset CLAUDE_ENV
claude /setup  # → Uses ~/.claude/
```

## 📋 Environment Detection in Scripts

All ClaudeSquad Python scripts should detect environment:

```python
import os
from pathlib import Path

def get_claude_base_dir():
    """Get appropriate ClaudeSquad directory based on environment"""
    env_mode = os.getenv('CLAUDE_ENV', 'production')
    
    if env_mode == 'dev':
        base_dir = Path.home() / '.claude-dev'
        print("🔧 DEVELOPMENT MODE: Using ~/.claude-dev/")
    else:
        base_dir = Path.home() / '.claude'
        print("🌐 PRODUCTION MODE: Using ~/.claude/")
    
    return base_dir

# Usage in scripts
CLAUDE_BASE = get_claude_base_dir()
DATABASE_PATH = CLAUDE_BASE / 'memory' / 'project.db'
AGENTS_PATH = CLAUDE_BASE / 'agents'
```

## 🧪 Testing Environment Isolation

### Verify Isolation Works

```bash
# Test 1: Development mode
export CLAUDE_ENV=dev
python -c "from pathlib import Path; import os; print('Dev mode uses:', Path.home() / ('.claude-dev' if os.getenv('CLAUDE_ENV') == 'dev' else '.claude'))"

# Test 2: Production mode  
unset CLAUDE_ENV
python -c "from pathlib import Path; import os; print('Prod mode uses:', Path.home() / ('.claude-dev' if os.getenv('CLAUDE_ENV') == 'dev' else '.claude'))"
```

**Expected Output:**
```
Dev mode uses: /Users/you/.claude-dev
Prod mode uses: /Users/you/.claude
```

## 🚨 Critical Development Rules

### ✅ DO:
- **Always set `CLAUDE_ENV=dev`** when working on ClaudeSquad project
- **Test both environments** before commits
- **Document environment-specific behavior** in code
- **Use `get_claude_base_dir()`** function in all scripts

### ❌ DON'T:
- **Never hardcode** `~/.claude/` paths in development code
- **Never mix** development and production databases
- **Never commit** with production environment variables
- **Never assume** environment state in scripts

## 🔄 Environment Migration

### Moving from Development to Production

```bash
# 1. Export development agents (if ready for global use)
export CLAUDE_ENV=dev
uv run python .claude/scripts/export_agents.py --target=production

# 2. Test in production environment
unset CLAUDE_ENV
claude /setup --verify

# 3. Validate no conflicts
claude "Test global system functionality"
```

### Reset Development Environment

```bash
export CLAUDE_ENV=dev
rm -rf ~/.claude-dev/
# Re-initialize development environment
claude /setup
```

## 📊 Environment Status Check

```bash
#!/bin/bash
# check_environment.sh

echo "🔍 ClaudeSquad Environment Status"
echo "================================="

if [[ "$CLAUDE_ENV" == "dev" ]]; then
    echo "🔧 DEVELOPMENT MODE"
    echo "   Using: ~/.claude-dev/"
    echo "   Database: ~/.claude-dev/memory/project.db"
    echo "   Agents: ~/.claude-dev/agents/"
else
    echo "🌐 PRODUCTION MODE"
    echo "   Using: ~/.claude/"
    echo "   Database: ~/.claude/memory/project.db"  
    echo "   Agents: ~/.claude/agents/"
fi

echo ""
echo "Active Environment Variable: ${CLAUDE_ENV:-'(unset - production)'}"
echo "Database exists: $(if [[ -f "$(if [[ "$CLAUDE_ENV" == "dev" ]]; then echo "$HOME/.claude-dev/memory/project.db"; else echo "$HOME/.claude/memory/project.db"; fi)" ]]; then echo "✅"; else echo "❌"; fi)"
echo ""

# Show recent activity
if [[ "$CLAUDE_ENV" == "dev" ]]; then
    echo "🔧 Development database activity:"
    echo "   Last modified: $(stat -c %y ~/.claude-dev/memory/project.db 2>/dev/null || echo 'Not found')"
else
    echo "🌐 Production database activity:"
    echo "   Last modified: $(stat -c %y ~/.claude/memory/project.db 2>/dev/null || echo 'Not found')"
fi
```

## 🎯 Quick Reference

| Command | Development | Production |
|---------|-------------|------------|
| **Environment** | `export CLAUDE_ENV=dev` | `unset CLAUDE_ENV` |
| **Base Directory** | `~/.claude-dev/` | `~/.claude/` |
| **Database** | `~/.claude-dev/memory/project.db` | `~/.claude/memory/project.db` |
| **Agents** | `~/.claude-dev/agents/` | `~/.claude/agents/` |
| **Usage** | ClaudeSquad development | Global ClaudeSquad use |

---

**🚨 Remember**: Always check your environment before making changes to agents, database, or core ClaudeSquad functionality!

```bash
echo "Current mode: $(if [[ "$CLAUDE_ENV" == "dev" ]]; then echo "🔧 DEVELOPMENT"; else echo "🌐 PRODUCTION"; fi)"
```