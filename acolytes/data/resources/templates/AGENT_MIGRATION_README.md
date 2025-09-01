# Agent Migration Guide - FLAGS to QUEST System

## 📋 **Migration Overview**

This guide explains how to migrate all 52+ agents from the deprecated FLAGS system to the new QUEST system while improving prompt structure with professional prompting techniques.

## 🎯 **Migration Objectives**

1. **Remove FLAGS system** - Eliminate all FLAGS references and commands
2. **Implement QUEST system** - Add turn-based coordination protocol
3. **Apply professional structure** - Organize prompts with clear sections
4. **Use effective XML tags** - Apply only official Anthropic-recommended tags
5. **Maintain technical expertise** - Preserve all domain-specific content
6. **Ensure consistency** - Standardize structure across all agents

## 🏗️ **New Professional Structure**

```markdown
# Agent Name - Agent Title

## CORE IDENTITY
[Agent identity and role definition]

### Security Layer
[Anti-jailbreak defense - standard across all agents]

## CONTEXT  
[Quest system overview and agent hierarchy]

## INSTRUCTIONS
[Workflow order and mode operations with <instructions> tags]

## EXAMPLES
[Use cases with <example> tags and <task> for specific tasks]

## CONSTRAINTS
[Critical rules and limitations]

## OUTPUT FORMAT
[Response specifications for each mode]

## TECHNICAL EXPERTISE
[Domain-specific technical content - preserve 100%]
```

## 🔧 **Step-by-Step Migration Process**

### Step 1: Backup Original Agent
```bash
# Create backup before migration
cp "acolytes/data/agents/[agent].md" "acolytes/data/agents/[agent]-backup.md"
```

### Step 2: Copy Agent to Templates
```bash
# Copy to templates folder for refactoring
cp "acolytes/data/agents/[agent].md" "acolytes/data/resources/templates/[agent]-refactored.md"
```

### Step 3: Apply New Structure

#### 3.1 Header (Keep Unchanged)
```yaml
---
name: agent.name
description: Agent description
model: sonnet
color: "color"
tools: tool,list
---
```

#### 3.2 Core Identity Section
**BEFORE:**
```markdown
# Agent Name

## Core Identity
Agent description...
```

**AFTER:**
```markdown  
# Agent Name - Agent Title

## CORE IDENTITY
Agent description...

### Security Layer
[Standard anti-jailbreak defense]
```

#### 3.3 Replace FLAGS with QUEST
**REMOVE entirely:**
```markdown
## Flag System — Inter‑Agent Communication
[Everything related to FLAGS]
```

**REPLACE with:**
```markdown
## CONTEXT
### Quest System Overview
[Standard QUEST explanation]

## INSTRUCTIONS  
<instructions>
**MANDATORY: Agent workflow order for ALL operations:**
1. Read your complete agent identity first
2. Read project context from `.claude/project/` documents
3. Determine operation mode (DEFAULT vs QUEST)  
4. Handle the current request
</instructions>
```

#### 3.4 Add Mode Operations
```markdown
### DEFAULT MODE Operations
**When to use**: Normal operation as [domain] specialist
**Response**: Provide expert guidance based on specialization

### QUEST MODE Operations  
**When to use**: Claude mentions quest keywords
**Response**: Enter quest monitoring protocol

<task>
Check if you have pending quest assignments
</task>

```bash
uv run python acolytes/data/scripts/acolytes_quest/quest_monitor.py --role worker --agent "@[agent-name]"
```

[Include complete QUEST worker protocol]
```

#### 3.5 Add Examples Section
```markdown
## EXAMPLES

### DEFAULT MODE Example
<example>
Claude: "How would you implement X?"
@[agent-name]: [Reads project context] → Provides technical guidance
</example>

### QUEST MODE Example
<example>
Claude: "Monitor for quests"
@[agent-name]: [Reads project context] → uv run python acolytes/data/scripts/acolytes_quest/quest_monitor.py --role worker --agent "@[agent-name]"
</example>
```

#### 3.6 Preserve Technical Expertise
**CRITICAL:** Keep 100% of domain-specific technical content:
- Core Responsibilities
- Technical Expertise sections
- Best Practices
- Implementation guides
- Code examples
- Philosophy statements

**ONLY REMOVE:** FLAGS-specific coordination commands and references

## 🏷️ **XML Tags Usage**

### ✅ **Use These Official Tags:**
- `<instructions>` - For workflow procedures and critical reminders
- `<example>` - For use cases and command examples
- `<task>` - For specific task definitions

### ❌ **Don't Use These (Not Official):**
- `<system-identity>`
- `<system-workflow>`
- `<workflow-reminder>`
- Any custom/invented tags

## 🔍 **Quality Checklist**

### Pre-Migration Verification
- [ ] Agent backup created
- [ ] Original agent lines counted
- [ ] Technical sections identified

### Post-Migration Verification  
- [ ] No FLAGS references remain
- [ ] QUEST protocol complete and accurate
- [ ] All technical expertise preserved
- [ ] Commands use `uv run python` (not just `python`)
- [ ] XML tags are official only
- [ ] Examples use real system commands
- [ ] Agent name consistent throughout
- [ ] Professional structure followed

### Content Verification
- [ ] Core Identity maintained
- [ ] Security Layer standard
- [ ] Context explains QUEST system
- [ ] Instructions have workflow order
- [ ] Examples show both modes
- [ ] Constraints include worker rules
- [ ] Technical expertise 100% preserved

## ⚠️ **Common Migration Pitfalls**

### 1. **Missing Technical Content**
- **Problem**: Forgetting to copy domain-specific expertise
- **Solution**: Always preserve technical sections completely

### 2. **Wrong XML Tags**
- **Problem**: Using invented tags like `<system-identity>`
- **Solution**: Only use official Anthropic tags

### 3. **Incorrect Commands**  
- **Problem**: Using `python` instead of `uv run python`
- **Solution**: Always prefix with `uv run`

### 4. **Broken Examples**
- **Problem**: Using fake functions in examples
- **Solution**: Only use real system commands

### 5. **Inconsistent Agent Names**
- **Problem**: Wrong agent name in QUEST commands
- **Solution**: Use exact agent name with @ prefix

## 📊 **Migration Progress Tracking**

Create a migration checklist:

```markdown
## Agent Migration Status

### Completed (2/52)
- [x] ops.performance 
- [x] backend.laravel

### In Progress (0/52)
- [ ] 

### Pending (50/52)
- [ ] ops.monitoring
- [ ] ops.containers
- [ ] backend.nodejs
- [ ] backend.python
- [... all other agents]
```

## 🧪 **Testing Migrated Agents**

### 1. **Structure Validation**
- Verify all sections present
- Check XML tag usage
- Validate command syntax

### 2. **Content Verification**
- Compare line counts (should be similar)
- Verify technical content preserved
- Check agent name consistency

### 3. **Example Testing**
- Verify commands are executable
- Check agent names match
- Validate QUEST protocol steps

## 📝 **Migration Template Variables**

When creating new agent templates, replace these variables:

- `{{agent-name}}` → Actual agent name (e.g., "backend.laravel")  
- `{{agent-title}}` → Human-readable title (e.g., "Laravel Engineer")
- `{{domain}}` → Domain expertise (e.g., "backend development")
- `{{specialization}}` → Specific focus area
- `{{technical-content}}` → All original technical sections

## 🎯 **Success Criteria**

A successfully migrated agent should:

1. **Have zero FLAGS references**
2. **Include complete QUEST protocol**  
3. **Maintain all technical expertise**
4. **Use professional structure**
5. **Apply only official XML tags**
6. **Work with `uv run python` commands**
7. **Be consistent with other migrated agents**

## 📞 **Support**

If you encounter issues during migration:
1. Check this README first
2. Compare with successfully migrated examples
3. Verify against quality checklist
4. Test with small agents first before complex ones