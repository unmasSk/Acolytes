# 📖 Acolytes How-To Guide
## **Master the World's First Multi-Agent Coordination System**

> **Step-by-step guide** to unleash the power of coordinated AI development

---

## 📋 **HOW-TO OVERVIEW**

This guide assumes you've completed the [Installation](INSTALL.md). Now learn how to:
- **🎮 Use the Quest System** for coordinated development
- **💾 Leverage persistent memory** across sessions
- **🎯 Optimize workflows** for maximum productivity
- **🔧 Handle advanced scenarios** and troubleshooting

---

## 🎮 **USING THE QUEST SYSTEM**

### **🎯 The Magic Two-Command Flow**

```bash
# Step 1: Create detailed implementation plan
/prequest implement user authentication system

# Step 2: Execute with coordinated agents
/quest
```

**This simple flow triggers the most sophisticated AI coordination ever built.**

**⚠️ IMPORTANT**: Always start Claude with `claude --dangerously-skip-permissions` for Acolytes to work properly.

---

## 🎯 **HOW TO COMMUNICATE WITH CLAUDE**

### **🤖 Agent Routing System**

Claude has access to **53 specialized agents + 5 setup agents** through an intelligent routing system. When you make requests, Claude automatically selects the right agents based on:

#### **🔍 Agent Discovery Commands**
```bash
# Find agents by domain/technology
"What agents handle authentication?"
"Show me database agents"
"Which agents work with React?"

# Get specific agent information
"Tell me about @backend.nodejs capabilities"
"What does @coordinator.database do?"
"Show @service.auth specialization"
```

#### **📋 Routing Rules (How Claude Decides)**

**Strategy vs Implementation:**
- 🧠 **"choose", "select", "compare", "decide", "architecture"** → **Coordinator first**
- ⚙️ **"implement", "configure", "optimize", "debug", "code"** → **Specialist directly**
- 🔄 **Both strategy + implementation** → **Coordinator → Specialist** (sequential)

**Example Routing:**
```bash
❌ "Build authentication" → Claude confused, multiple options
✅ "Implement JWT authentication with OAuth2" → @service.auth directly
✅ "Choose authentication strategy for enterprise" → @coordinator.security first
✅ "Design authentication then implement" → @coordinator.security → @service.auth
```

#### **🎭 Agent Categories**

**🎛️ Coordinators (Strategy/Architecture):**
- `@coordinator.backend` - Backend architecture decisions
- `@coordinator.database` - Data architecture strategy  
- `@coordinator.frontend` - UI architecture planning
- `@coordinator.security` - Security strategy & compliance
- `@coordinator.infrastructure` - Cloud & infrastructure design

**💻 Implementation Specialists:**
- `@backend.nodejs` `@backend.python` `@backend.java` etc.
- `@frontend.react` `@frontend.vue` `@frontend.angular`
- `@database.postgres` `@database.mongodb` `@database.redis`
- `@service.auth` `@service.payment` `@service.ai`

**⚙️ Operations Experts:**  
- `@ops.containers` `@ops.cicd` `@ops.monitoring`
- `@ops.performance` `@ops.troubleshooting`

#### **💡 Communication Best Practices**

**Be Specific About Technology:**
```bash
✅ "Create React components with TypeScript and hooks"
✅ "Optimize PostgreSQL queries with indexing" 
✅ "Setup Kubernetes deployment with Helm"

❌ "Build frontend" (which framework?)
❌ "Fix database" (which database?)
❌ "Deploy app" (which platform?)
```

**Use Clear Action Words:**
```bash
Strategy: "choose", "design", "plan", "architect", "evaluate"
Implementation: "implement", "create", "build", "configure", "deploy"
Optimization: "optimize", "improve", "enhance", "tune", "scale"  
Debugging: "debug", "fix", "troubleshoot", "diagnose", "resolve"
```

**Leverage Agent Expertise:**
```bash
# Instead of generic request
❌ "Help with my API"

# Be specific about what you need
✅ "Design RESTful API architecture with @backend.api"
✅ "Implement Node.js endpoints with @backend.nodejs"  
✅ "Setup API authentication with @service.auth"
✅ "Deploy API infrastructure with @coordinator.infrastructure"
```

### **🔄 Multi-Agent Coordination**

**Parallel Execution (Claude invokes simultaneously):**
```bash
"Build full-stack user management system"
→ @database.postgres + @backend.nodejs + @frontend.vue (parallel)
```

**Sequential Execution (Dependencies):**
```bash  
"Design then implement authentication system"
→ @coordinator.security → @service.auth → @backend.nodejs (sequential)
```

**Complex Workflows:**
```bash
"Create e-commerce platform with payments"
→ @coordinator.backend (architecture)
→ @database.postgres + @backend.nodejs + @frontend.vue (parallel)
→ @business.payment + @service.auth (integrations)
→ @ops.containers (deployment)
```

---

## 🔍 **PREQUEST: Strategic Planning**

### **What /prequest does:**

1. **🎯 Module Analysis**
   - Relevant acolyte examines their module + roadmap
   - Identifies the specific task from roadmap (or user request)
   - Analyzes current codebase state

2. **📋 Micro-Roadmap Creation**
   ```
   PREQUEST_20250902_143000.md created in module directory
   
   Contains:
   ├─ Specific files to create/modify
   ├─ Exact functions to implement  
   ├─ Required worker agents identified
   ├─ Dependencies and execution order
   ├─ Success criteria and testing approach
   └─ Estimated complexity and timeline
   ```

3. **👥 Worker Agent Identification**
   ```
   Workers needed:
   - @database.postgres: User tables and indexes
   - @backend.nodejs: Authentication endpoints
   - @frontend.vue: Login/register forms
   - @service.auth: JWT token management
   - @test.integration: Authentication flow tests
   ```

### **Advanced /prequest Usage**

#### **Be Specific for Better Results**
```bash
✅ /prequest implement JWT authentication with refresh tokens and rate limiting
✅ /prequest create REST API with CRUD operations for user management
✅ /prequest build responsive dashboard with real-time data updates

❌ /prequest add authentication
❌ /prequest make API
❌ /prequest create frontend
```

#### **Reference Roadmap Tasks**
```bash
# If you have a roadmap, reference specific points:
/prequest implement roadmap task 2.3: User Profile Management
/prequest execute phase 1: Database Setup and Initial Schema
```

#### **Custom Requirements**
```bash
# Add specific constraints or requirements:
/prequest implement payment processing with Stripe integration and webhook handling
/prequest create mobile-first responsive design with offline capabilities
```

---

## ⚡ **QUEST: Coordinated Execution**

### **What /quest does:**

1. **🚀 Parallel Agent Invocation**
   - **Claude automatically knows** which agents to invoke
   - **Exact prompts prepared** for each specialist  
   - **All agents launched simultaneously** in single message

2. **🎭 Role-Based Coordination**
   ```
   LEADER (@coordinator.backend):
   ├─ Creates quest in SQLite database
   ├─ Sends specific instructions to each worker
   ├─ Monitors progress and coordinates dependencies
   └─ Reviews work and completes quest

   WORKERS (@backend.*, @frontend.*, @database.*):
   ├─ Monitor for their assigned tasks
   ├─ Execute real work (create files, write code)
   ├─ Respond to leader with completion status
   └─ Continue monitoring until quest complete
   ```

3. **🔄 Turn-Based Communication**
   ```
   Quest Timeline Example:
   00:00 → Leader creates quest, assigns database work
   00:03 → @database.postgres creates schema
   00:05 → Leader assigns backend work  
   00:15 → @backend.nodejs creates API endpoints
   00:16 → Leader assigns frontend work in parallel
   00:25 → @frontend.vue creates login forms
   00:30 → @test.integration runs complete flow
   00:32 → All agents report completion
   00:35 → Leader marks quest complete
   ```

### **What You'll See During /quest**

#### **Real Agent Conversations**
```
🎭 @coordinator.backend: "Creating quest for user authentication system"
   ↓ Quest #1847 created

🗄️ @database.postgres: "Creating users table with email, password_hash, created_at..."
   ↓ Files: schema.sql, migrations/001_users.sql

⚙️ @backend.nodejs: "Building auth endpoints... need password requirements"
   ↓ ASKS: "Should passwords require special characters?"

🎭 @coordinator.backend: "Yes, minimum 8 chars, 1 special, 1 number"
   ↓ Updates requirements

⚙️ @backend.nodejs: "Auth API complete with validation"
   ↓ Files: auth.js, middleware/validate.js, routes/auth.js

🎨 @frontend.vue: "Login form created, need password strength indicator"
   ↓ ASKS: "Should I add real-time strength meter?"

🧪 @test.integration: "Testing auth flow... found SQL injection vulnerability"
   ↓ CRITICAL BUG DETECTED

⚙️ @backend.nodejs: "Fixed parameterized queries, added input sanitization"
   ↓ SECURITY PATCHED AUTOMATICALLY

✅ QUEST COMPLETE: Full auth system in 23 minutes
```

---

## 💾 **MEMORY & PERSISTENCE**

### **🔄 /save Command - The Memory Powerhouse**

```bash
/save
```

**What gets saved:**
- 💬 **Complete conversation history** with all agents
- 🧠 **Agent memory states** (all 14 memory types per agent)
- 🎯 **Quest states** and coordination history  
- 📋 **Job progress** and session organization
- 🔍 **Code analysis** and architectural decisions
- 📚 **Documentation updates** and knowledge base

**Result: TRUE PERSISTENT MEMORY**
- Claude remembers everything across sessions
- Acolytes never forget project details
- Context preserved indefinitely

### **🧠 Agent Memory System**

**Each acolyte maintains 14 memory types:**
```
1. identity       → Core role and specialization
2. history        → Actions taken and results
3. knowledge      → Technical facts and patterns
4. preferences    → Style and approach choices
5. context        → Current project understanding
6. objectives     → Goals and priorities
7. constraints    → Limitations and requirements  
8. relationships  → Dependencies on other agents
9. resources      → Tools and references used
10. experiences   → Lessons learned from past work
11. insights      → Discovered patterns and optimizations
12. assumptions   → Working hypotheses about the project
13. uncertainties → Known unknowns and risks
14. metadata      → Technical details and configurations
```

### **📚 Auto-Context Loading**

**Every time an agent is invoked:**
- ✅ Reads `.claude/project/` documentation
- ✅ Loads their 14 memory types from SQLite
- ✅ **Born with full project context**
- ✅ Never needs to "learn" the project again

---

## 🚀 **WORKFLOW EXAMPLES**

### **🏪 Example 1: E-commerce Platform**

```bash
# Setup (if not done already)
cd ~/my-ecommerce-project
/setup

# After restart: claude --dangerously-skip-permissions -c

# Create detailed plan
/prequest implement complete product catalog with search and filters

# Execute with coordinated agents
/quest
```

**What happens:**
- 8 agents coordinate automatically
- **@database.postgres**: Product tables with optimized indexes
- **@backend.nodejs**: REST API with search endpoints
- **@frontend.vue**: Catalog components with filtering UI
- **@service.search**: Elasticsearch integration
- **@test.integration**: Complete test suite
- **@docs.api**: OpenAPI documentation
- **Result**: Complete system in ~45 minutes

### **🏥 Example 2: Healthcare Dashboard**

```bash
cd ~/healthcare-app
/setup

# Requirements interview detects "healthcare" → triggers HIPAA compliance

/prequest build HIPAA-compliant patient monitoring dashboard
/quest
```

**What happens:**
- 12 agents coordinate with compliance focus
- **@audit.compliance**: HIPAA requirement analysis
- **@database.postgres**: Encrypted patient data schema
- **@backend.nodejs**: HIPAA-compliant API with audit logs
- **@frontend.vue**: Secure dashboard with role-based access
- **@service.communication**: Secure notification system
- **@docs.compliance**: Complete compliance documentation
- **Result**: Enterprise-grade system in ~1.8 hours

### **📱 Example 3: Mobile App Backend**

```bash
cd ~/mobile-backend
/setup

/prequest create mobile API with authentication and push notifications  
/quest
```

**What happens:**
- 6 agents coordinate for mobile optimization
- **@backend.nodejs**: JWT authentication system
- **@database.postgres**: Optimized mobile-friendly schema
- **@service.communication**: Push notification integration
- **@backend.api**: Mobile-optimized API responses
- **@test.integration**: Mobile-specific testing
- **@docs.api**: Mobile SDK documentation
- **Result**: Production-ready backend in ~25 minutes

### **🔄 Example 4: Legacy System Migration**

```bash
cd ~/legacy-php-app  
/setup

# Existing project analysis of PHP codebase

/prequest migrate user authentication from PHP sessions to JWT microservice
/quest
```

**What happens:**
- 9 agents coordinate complex migration
- **@backend.nodejs**: New JWT microservice
- **@database.postgres**: Migration scripts for user data
- **@backend.laravel**: PHP integration bridge
- **@ops.deployment**: Zero-downtime deployment strategy
- **@test.migration**: Migration validation tests
- **@docs.migration**: Complete migration guide
- **Result**: Seamless migration in ~2 hours

---

## 🎯 **ADVANCED USAGE PATTERNS**

### **🔗 Chaining Quests**

**Sequential Development:**
```bash
# Quest 1: Foundation
/prequest implement basic user authentication
/quest

# Quest 2: Build on foundation  
/prequest add OAuth2 social login to existing auth system
/quest

# Quest 3: Advanced features
/prequest implement two-factor authentication with TOTP
/quest
```

### **🎭 Custom Agent Combinations**

**For complex tasks, mention specific agents:**
```bash
/prequest implement real-time chat system requiring @backend.nodejs for WebSocket server, @database.redis for session management, @frontend.vue for real-time UI, and @service.communication for notifications
```

### **📊 Multi-Domain Projects**

**For projects spanning multiple domains:**
```bash
/prequest create fintech dashboard requiring @audit.compliance for financial regulations, @service.payment for transaction processing, @database.postgres for financial data, and @frontend.vue for trading interface
```

---

## 🔧 **TROUBLESHOOTING USAGE**

### **Quest Issues**

#### **❌ "No prequest found" during /quest**
```bash
# Solution: Always run /prequest first
/prequest [describe your task]
/quest
```

#### **❌ Agents not responding in quest**
```bash
# Solution 1: Check agent names are correct
# Use exact names: @backend.nodejs NOT @backend-nodejs

# Solution 2: Restart Claude
claude --dangerously-skip-permissions -c

# Solution 3: Save and restart
/save
exit
claude --dangerously-skip-permissions -c
```

#### **❌ Quest gets stuck or incomplete**
```bash
# Solution: Save current state and restart
/save

# Then check quest status (advanced users)
python ~/.claude/scripts/acolytes_quest/quest_status.py --list
```

### **Memory Issues**

#### **❌ "Agent doesn't remember previous work"**
```bash
# Solution: Use /save regularly
/save

# Agents auto-load memory, but manual saves help
```

#### **❌ "Context lost between sessions"**
```bash
# Solution 1: Always restart with -c flag
claude --dangerously-skip-permissions -c

# Solution 2: Check if /save was used
/save  # Save current session before exit
```

---

## 🎪 **BEST PRACTICES**

### **💡 Optimization Tips**

1. **Use /save regularly**
   ```bash
   /save  # After major milestones or before breaks
   ```

2. **Be specific in /prequest**
   ```bash
   ✅ /prequest implement JWT authentication with refresh tokens, rate limiting, and RBAC
   ❌ /prequest add authentication
   ```

3. **Let agents specialize**
   - Don't ask @frontend.vue to do database work
   - Use @coordinator.* for multi-domain coordination

4. **Follow the dopamine roadmap**
   - Use the roadmap system for motivation
   - Celebrate completed milestones
   - Break large features into satisfying chunks

5. **Leverage persistent memory**
   - Agents remember everything they've learned
   - Build incrementally on previous work
   - Reference past decisions and patterns

### **🚀 Power User Features**

#### **Custom Workflows**
```bash
# Create custom development flows
/prequest implement feature X following our established patterns from feature Y
/quest

# Reference previous implementations
/prequest create similar API endpoints to the user management system but for products
/quest
```

#### **Multi-Project Management**
```bash
# Each project has independent .claude/ directory
# Switch between projects seamlessly
cd ~/project-a && /prequest implement feature
cd ~/project-b && /prequest implement different feature

# Agents adapt automatically to each project's context
```

#### **Advanced Coordination**
```bash
# Complex multi-service coordination
/prequest integrate 5 different payment providers with failover logic, webhook handling, and comprehensive testing
/quest

# Results in sophisticated agent coordination with dependency management
```

---

## 📋 **COMMANDS CHEAT SHEET**

### **Essential Commands**
```bash
/setup               # Setup project (first time)
/prequest [task]     # Create implementation plan
/quest              # Execute coordinated development
/save               # Save all memory and progress
```

### **Job Management**
```bash
"Create a job for [task]"                    # Create new job
"Pause current job and switch to [task]"    # Switch jobs
"What jobs do I have?"                       # List jobs
"Complete current job"                       # Mark job done
```

### **Advanced Usage**
```bash
# Restart with continuation
claude --dangerously-skip-permissions -c

# System health check
acolytes --doctor

# Agent listing
acolytes --list
```

---

## 🎯 **MEASURING SUCCESS**

### **Signs of Perfect Coordination**

✅ **Agents communicate naturally** - You see real conversations  
✅ **Dependencies resolved automatically** - No blocking issues  
✅ **Code reviews happen between agents** - Quality is maintained  
✅ **Tests run automatically** - Bugs caught immediately  
✅ **Documentation generated** - No manual documentation needed  
✅ **Consistent patterns** - Agents follow established conventions  

### **Performance Metrics**

**Compare your results:**
- **Simple CRUD API**: Should complete in ~12 minutes
- **Full-stack MVP**: Should complete in ~45 minutes  
- **Enterprise system**: Should complete in ~2-4 hours
- **Complex integration**: Should complete in ~1 day

If times are longer, check:
- Specificity of /prequest instructions
- Network connection stability
- System resource availability

---

## 🎉 **MASTERY ACHIEVED**

**You now know how to:**
- ✨ Coordinate **57+ AI specialists** for any task
- 🧠 Leverage **persistent memory** across sessions
- ⚡ Deliver **enterprise systems** in hours
- 🤝 Enable **real AI peer review** and collaboration
- 🚀 Transform **impossible projects** into routine work

**The coordinated AI development revolution is in your hands.**

---

## 📞 **READY FOR MORE?**

**Explore advanced topics:**
- 📚 [Quest System Deep Dive](QUEST.md) - Understand the coordination magic
- 🎭 [Agent Catalog](../acolytes/data/resources/rules/agent-routing-catalog.md) - Complete list of all available agents
- 🧠 [Agent Routing Rules](../acolytes/data/resources/rules/agent-routing-rules.md) - How Claude selects agents automatically

**Need help?**
- Run `acolytes --doctor` for diagnostics
- Use `/save` before asking for support
- Reference specific quest IDs for troubleshooting

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

*📖 Acolytes for Claude Code - How-To Guide*  
*⚡ Master the impossible. Make it routine.*