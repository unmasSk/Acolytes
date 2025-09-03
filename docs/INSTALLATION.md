# 🚀 Acolytes Installation Guide
## **Complete Setup for the World's First Multi-Agent Coordination System**

> **One-time setup** to unlock the power of 55 specialized agents + 5 setup agents

---

## 📋 **INSTALLATION OVERVIEW**

The Acolytes system has **TWO installation levels**:
- **🌐 Global Installation**: Install the system once on your machine
- **🏗️ Project Setup**: Configure each project individually

---

## 🌐 **GLOBAL INSTALLATION**

### **Step 1: Install Acolytes Package**
```bash
pip install acolytes
```

**What gets installed globally in `~/.claude/`:**
- ✅ **53 Specialized Agents** (backend.nodejs, frontend.vue, database.postgres, etc.) + **5 Setup Agents**
- ✅ **Quest Coordination Scripts** (quest_create.py, quest_monitor.py, quest_respond.py)
- ✅ **Professional Templates** (carefully crafted agent templates)
- ✅ **CLI Commands** (acolytes --init, --doctor, --repair, etc.)
- ✅ **MCP Integration** (code indexing, SQLite connections)

### **Step 2: Initialize System**
```bash
acolytes --init
```

**What this initialization does:**
- 🔧 **Installs uv** (Python package manager) if needed
- ⚙️ **Generates settings.json** for Claude Code integration  
- 📁 **Creates base structure** in ~/.claude/
- 🔗 **Configures MCP connections** for advanced features
- 🛡️ **Sets up safety hooks** to prevent system disasters

### **Step 3: Verify Installation**
```bash
acolytes --doctor
```

**Expected healthy output:**
```
✅ Python 3.8+ installed
✅ uv package manager available  
✅ Claude Code configuration valid
✅ SQLite database accessible
✅ MCP connections active
✅ All 55 specialized + 5 setup agents available
✅ Quest system operational
```

---

## 🏗️ **PROJECT SETUP**

### **🚨 CRITICAL: Always Start Claude in Dangerous Mode**

**Every time you work with Acolytes, you MUST start Claude Code with special permissions:**

```bash
# Start Claude Code with unrestricted permissions
claude --dangerously-skip-permissions
```

**⚠️ Why "dangerous" mode is required:**
- Claude won't ask permission before executing commands
- Required for automated system setup and file creation  
- Enables MCP connections and database operations
- **Essential for agent coordination and Quest system**
- **Use this EVERY TIME you start Claude for Acolytes work**

**🛡️ Safety Guarantees:**
- ✅ **Safety hooks are active** - prevent destructive commands (`rm -rf`, etc.)
- ✅ **Malicious intent protection** - blocks dangerous operations
- ✅ **Project scope limitation** - operations restricted to your project
- ✅ **Automatic validation** - all commands pre-validated before execution

### **⚡ Two Command Setup**
```bash
# 1. Navigate to your project directory
cd /path/to/your/project

# 2. Start Claude with required permissions
claude --dangerously-skip-permissions

# 3. Run setup (works for both new and existing projects)
/setup
```

---

## 🔀 **TWO DIFFERENT PROJECT FLOWS**

### **📂 EXISTING PROJECT SETUP**

**What happens automatically:**

#### **Phase 1: Deep Code Analysis**

1. **🔍 MCP Code-Index Integration**
   - Indexes your entire codebase instantly
   - Creates searchable database of functions, classes, files
   - Enables lightning-fast code navigation for agents

2. **👥 4 Setup Agents Deployed in Parallel**
   ```
   @setup.codebase       → Architecture, patterns, tech stack analysis
   @setup.context        → Project purpose, domain, business logic  
   @setup.environment    → Dependencies, tools, configuration
   @setup.infrastructure → Deployment, CI/CD, hosting analysis
   ```

3. **📚 Perfect Documentation Generated**
   
   **Location: `.claude/project/`**
   ```
   vision.md              → Project purpose and business context
   architecture.md        → Technical decisions and system design
   technical-decisions.md → Rationale for technology choices
   team-preferences.md    → Coding standards and practices
   project-context.md     → Specific project details and constraints
   roadmap.md             → Development roadmap (if user chooses to create one)
   ```

4. **🎯 Strategic Roadmap Generation** *(Optional but Recommended)*
   - **@plan.strategy** analyzes your existing project
   - Creates **dopamine-driven development roadmap** 
   - Identifies improvement opportunities and next phases
   - **User choice**: Create structured roadmap OR work organically
   - Roadmap becomes organized "jobs" for systematic development

#### **Phase 2: Intelligent Agent Creation**

5. **🤖 Module-Specific Acolytes Created**
   - `@setup.acolytes-creator` analyzes your modules
   - Creates specialized agents: `acolyte.auth.md`, `acolyte.api.md`, `acolyte.frontend.md`
   - **Each agent gets 14 types of persistent memory**
   - **They never forget anything they've learned about your project**

6. **📋 CLAUDE.md Profile Generated**
   - Custom instructions based on your project
   - Filled from professionally crafted templates
   - Contains project context, preferences, and agent assignments

#### **Phase 3: Memory Initialization**

7. **🧠 Agent Memory Population**
   - Each acolyte performs deep analysis of their assigned module
   - Populates 14 memory types with discovered information
   - Creates comprehensive knowledge base
   - **Born with full project context - no learning curve**

---

### **🆕 NEW PROJECT SETUP**

**What happens:**

#### **Phase 1: Intelligent Requirements Interview**

1. **🎯 Project Classification**
   ```
   Claude: "What type of project is this?"
   Options: MVP, Startup, Enterprise, Proof of Concept, Production Ready
   
   Claude: "What's your development approach?"  
   Options: Vibe Coder (you focus on vision) vs Programmer (you code)
   ```

2. **🧠 Smart Question Flow**
   - **Conditional areas**: Questions adapt based on your project type
   - **Domain detection**: Automatically detects fintech, healthcare, e-commerce
   - **Skip rules**: MVPs skip performance questions, POCs skip compliance
   - **Cross-validation**: Catches inconsistencies early

3. **📝 Progressive Documentation**
   - Interview answers saved every 4-5 questions (no context loss)
   - Specialist consultations based on your tech choices
   - Same `.claude/project/` documentation structure created

#### **Phase 2: Strategic Roadmap Planning**

4. **🎯 @plan.strategy Agent Consultation**
   - **@plan.strategy** analyzes all your interview requirements
   - Creates **dopamine-driven development roadmap** 
   - Phases designed to keep you motivated and engaged
   - Milestones that provide satisfaction and momentum
   - **Strategic planning** optimized for success and completion

5. **📋 Job System Setup**
   - Roadmap phases become organized "jobs"
   - Each job groups related work sessions
   - **System requires active job at all times**
   - Jobs prevent context overflow (max 4-5 sessions per job)

#### **Phase 3: Architecture-Based Agent Creation**

6. **🏗️ Planned Module Agents**
   - Acolytes created based on planned architecture
   - They read the documentation and prepare for implementation
   - Memory initialized with planned structure and expectations

---

## 🔄 **MANDATORY RESTART PROCESS**

### **⚠️ Critical Step After Setup**

**Claude will automatically request this restart:**

```bash
# Exit current session
exit  # or Ctrl+C twice

# Restart with continuation flag (-c = continue same conversation)
claude --dangerously-skip-permissions -c
```

**Why this restart is essential:**
- ✅ **Integrates new acolytes** into Claude's system
- ✅ **Activates MCP connections** for SQLite and code indexing  
- ✅ **Applies configuration changes** from setup
- ✅ **Enables quest coordination** between agents
- ✅ **Safety hooks remain active** - protection continues

**🚨 Command Explanation:**
- **`--dangerously-skip-permissions`**: Enables unrestricted operations (required for agent coordination)
- **`-c` flag**: Continues the exact same conversation (preserves all context and progress)
- **NOT a new session** - picks up exactly where you left off
- **Safety hooks remain active** - malicious commands still blocked

---

## 📁 **PROJECT STRUCTURE CREATED**

**After successful setup, your project will have:**

```
[PROJECT_ROOT]/
├── CLAUDE.md                       # PROJECT INSTRUCTIONS
├── .claude/
│   ├── project/                    # PROJECT DOCUMENTATION
│   │   ├── vision.md               # Project vision and business context
│   │   ├── architecture.md         # Technical decisions
│   │   ├── roadmap.md              # Development phases
│   │   ├── technical-decisions.md  # Rationale for choices
│   │   ├── team-preferences.md     # Standards and practices
│   │   └── project-context.md      # Specific project details
│   ├── agents/                     # PROJECT-SPECIFIC ACOLYTES
│   │   ├── acolyte.auth.md         # Authentication module specialist
│   │   ├── acolyte.api.md          # API module specialist
│   │   ├── acolyte.frontend.md     # Frontend module specialist
│   │   └── ...                     # One per detected/planned module
│   └── memory/                     # PERSISTENT MEMORY
│       ├── chat/                   # Chat conversations  
│       └── project.db              # SQLite with agents, jobs, sessions, and ALL agent memories (14 types per agent)
```

---

## 🔧 **TROUBLESHOOTING INSTALLATION**

### **Common Installation Issues**

#### **❌ pip install fails**
```bash
# Solution 1: Update pip
python -m pip install --upgrade pip

# Solution 2: Use specific Python version
python3.11 -m pip install acolytes

# Solution 3: Install in virtual environment
python -m venv acolytes-env
source acolytes-env/bin/activate  # Linux/Mac
acolytes-env\Scripts\activate     # Windows
pip install acolytes
```

#### **❌ acolytes --init fails**
```bash
# Solution: Check permissions and retry
sudo acolytes --init  # Linux/Mac
# Or run as administrator on Windows

# Alternative: Manual initialization
acolytes --repair
```

#### **❌ MCP connection issues**
```bash
# Solution: Re-run initialization
acolytes --repair

# Then restart Claude
claude --dangerously-skip-permissions
```

#### **❌ "/setup command not recognized"**
```bash
# Solution: Ensure you're in Claude Code CLI with proper permissions
claude --dangerously-skip-permissions

# Check if acolytes is installed
acolytes --list

# If still not working, verify installation
acolytes --doctor
```

#### **❌ "Permission denied" during setup**
```bash
# Solution: You MUST use dangerous mode for setup
# Exit current session and restart with:
claude --dangerously-skip-permissions

# Then run setup again
/setup
```

### **System Health Verification**

```bash
# Run comprehensive diagnosis
acolytes --doctor

# List all available agents
acolytes --list

# Check installation integrity
acolytes --clean  # Removes orphaned files
```

---

## 💾 **GLOBAL COMMANDS REFERENCE**

### **Installation Commands**
```bash
acolytes --init      # Initialize system (first time)
acolytes --update    # Update to latest version
acolytes --doctor    # Diagnose system health
acolytes --repair    # Fix configuration issues  
acolytes --list      # Show available agents
acolytes --backup    # Backup current installation
acolytes --clean     # Clean orphaned files
acolytes --version   # Show current version
```

### **Maintenance Commands**
```bash
# Update global agents and templates
acolytes --update

# Backup before major changes
acolytes --backup

# Restore from backup if needed
acolytes --repair --restore-backup

# Clean up orphaned files
acolytes --clean
```

---

## 🎯 **INSTALLATION VERIFICATION**

### **✅ Successful Installation Checklist**

After installation, you should have:

1. **Global system installed:**
   ```bash
   acolytes --doctor  # All green checkmarks
   ```

2. **Claude Code integration:**
   ```bash
   claude --dangerously-skip-permissions
   # Should start without errors and show safety hooks active
   ```

3. **Project setup capability:**
   ```bash
   cd your-project
   /setup
   # Should begin setup process
   ```

4. **All 55 specialized + 5 setup agents available:**
   ```bash
   acolytes --list
   # Should show full agent catalog
   ```

---

## 🚀 **NEXT STEPS**

**Installation complete!** 

Now you can:

1. **📖 Read the [HOW-TO Guide](HOW-TO.md)** - Learn how to use the Quest system
2. **🎯 Read the [Quest System Overview](QUEST.md)** - Understand the magic behind coordination
3. **⚡ Try your first setup:**
   ```bash
   cd your-project
   /setup
   ```

---

## 🆘 **GETTING HELP**

### **If something goes wrong:**

1. **Run diagnostics:**
   ```bash
   acolytes --doctor
   ```

2. **Try repair:**
   ```bash
   acolytes --repair
   ```

3. **Clean installation:**
   ```bash
   pip uninstall acolytes
   # Remove ~/.claude directory
   pip install acolytes
   acolytes --init
   ```

4. **Check system requirements:**
   - Python 3.8+
   - Git 2.0+  
   - Node.js 18+ (for some features)
   - Claude Code CLI installed

---

**🎉 Welcome to the Multi-Agent Revolution!**

*Installation complete. The future of AI development starts now.*

---

## 🆘 **FOUND A BUG OR ISSUE?**

**If you encounter any problems, errors, or have suggestions:**

📋 **Report issues**: https://github.com/unmasSk/acolytes/issues  
📧 **Contact**: Create a detailed issue with:
- Your operating system and Python version
- Complete error messages and logs  
- Steps to reproduce the problem
- Expected vs actual behavior

**Help us improve the system for everyone!** 🚀

---

*🚀 Acolytes for Claude Code - Installation Guide*  
*⚡ From zero to coordinated AI team in minutes*