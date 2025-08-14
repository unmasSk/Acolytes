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
[Task 1] {{agent_1}} → {{task_1}}
[Task 2] {{agent_2}} → {{task_2}}  
[Task 3] {{agent_3}} → {{task_3}}"
```

## 📋 Dynamic Agent Invocation Protocol

### 🚨 CRITICAL: ALWAYS PROVIDE COMPLETE CONTEXT

**Agents have integrated knowledge but need specific context for the current task.**

### ✅ CORRECT Flow:

```
1. DIRECT QUERY to specialized agent:
   
   "@{{module_agent}}, I need to implement [function X]. 
   
   CONTEXT:
   - Location: {{module_path}}
   - Files: {{key_files}}
   - Patterns: {{patterns}}
   - Constraints: {{constraints}}
   
   How should I proceed?"
   
2. IMPLEMENTATION with engineer:
   
   "@engineer-{{framework}}, implement according to {{module_agent}} specifications:
   [INCLUDE complete response from specialized agent]"
   
3. FINAL REVIEW:
   
   "@{{module_agent}}, review this implementation: [details]"
```

## 🔄 Multi-Agent Orchestration

### **REAL PARALLEL - Multiple queries:**
```bash
"Query these agents IN PARALLEL:
[Task 1] {{agent_1}} → {{module_1}} module analysis
[Task 2] {{agent_2}} → {{domain_2}} patterns  
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

## 🛠️ Useful Commands

```bash
# View available agents
ls .claude/agents/

# View agent memory
cat .claude/memory/agents/{{agent_example}}/knowledge.json

# View pending flags
cat .claude/memory/flags/pending.json

# View processed flags
cat .claude/memory/flags/processed.json

# View project structure
tree .claude/

# View activity logs
tail -20 .claude/memory/context/activity.log
```

## 🚨 Troubleshooting

If an agent doesn't respond correctly:
1. Verify it exists in `.claude/agents/[agent-name].md`
2. Confirm it has memory in `.claude/memory/agents/[agent_name]/`
3. Use direct invocation: `@agent-name, [your query]`
4. For parallelism: multiple Task calls in one message

## 🏗️ PROJECT: {{project_name}}

### 📊 PROJECT IDENTITY

- **Name**: {{project_name}}
- **Type**: {{project_type}}
- **Phase**: {{project_phase}}
- **Stack**: {{tech_stack}}

### 🎯 SPECIFIC CONTEXT

{{project_description}}

### 📁 ARCHITECTURAL STRUCTURE

{{architecture_description}}

### 🛠️ TECHNOLOGY STACK

```yaml
stack:
  {{#each tech_stack_details}}
  {{category}}: "{{technology}}"
  {{/each}}
```

### 🏆 UNIQUE FEATURES

{{#each unique_features}}
- **{{name}}**: {{description}}
{{/each}}

### 🚨 CRITICAL ISSUES IDENTIFIED

{{#each critical_issues}}
- **{{category}}**: {{description}}
  - **Impact**: {{impact}}
  - **Solution**: {{solution}}
{{/each}}

### 🔧 NEXT PRIORITIES

{{#each priorities}}
{{id}}. {{description}}
{{/each}}

---

**For parallelism**: Use multiple Task calls in a single message - Claude Code supports up to 10 simultaneous subagents.