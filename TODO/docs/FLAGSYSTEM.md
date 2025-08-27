# ClaudeSquad FLAG System - Complete Documentation

The FLAG system is the core inter-agent communication protocol that enables ClaudeSquad's 58+ agents to coordinate work without contaminating Claude's context window. It operates as an intelligent message queue with automatic prioritization, conflict detection, and chain tracking.

## System Architecture

### Core Principle

**Claude is NOT involved in day-to-day FLAG processing** - The system is designed to operate with minimal Claude intervention to preserve context efficiency. Claude only invokes the `@flags.agent` orchestrator, which manages the entire workflow autonomously.

### Agent Types

**Acolytes** (Project-specific):

- Created during `/setup` phase by analyzing project modules
- One agent per module (max 30 files per agent)
- Sub-module agents for large modules: `api-agent`, `api-auth-agent`
- Have 8 types of persistent memory in SQLite
- Expert guardians of their assigned modules

**Professional Agents** (58 global specialists):

- Backend, frontend, database, service specialists
- Invoked by Claude when @flags.agent determines work assignment
- Stateless - don't maintain project memory
- **Discoverable via semantic search** using keywords, capabilities, and descriptions

## Complete System Flow

### 1. User Request Processing

```
User → Claude → @api-agent (dynamic)
@api-agent reads complete memory → creates FLAG → closes
```

### 2. FLAG Processing Cycle

```
/flags command → @flags.agent → analyzes all pending FLAGs
@flags.agent → Claude: "invoke @backend.nodejs"
@backend.nodejs → completes work → creates response FLAG
```

### 3. Memory Updates

```
Dynamic agent reads response → updates memory → closes FLAG
If significant change → creates FLAG to @changelog-agent
```

## Semantic Agent Discovery

The FLAG system includes intelligent agent discovery to eliminate routing errors:

### How Semantic Search Works

```bash
# Command usage
uv run python .claude/scripts/agent_db.py search-agents "query" [limit]

# Example: Find authentication specialist
uv run python .claude/scripts/agent_db.py search-agents "JWT authentication implementation" 3
```

**Scoring Algorithm:**

- **Exact keyword match** (50 pts): Direct match in agent's routing_keywords
- **Keyword word match** (40 pts): Partial word matches in keywords
- **Capability match** (30 pts): Match in agent's technical capabilities
- **Description match** (20 pts): Match in agent's description text
- **Module match** (15 pts): Match in agent's primary/sub module
- **Multi-criteria bonus** (25 pts): When agent matches multiple categories

### Integration with FLAG Creation

**Before (Error-prone):**

```bash
# Agents had to guess the right target
create-flag --target_agent "@backend.nodejs" --action_required "..."
# Often wrong target → wasted cycles, delays
```

**After (Precision routing):**

```bash
# 1. Search for the right specialist
search-agents "JWT authentication Node.js implementation" 3
# Returns: @service.auth (score: 195), @backend.nodejs (score: 140)

# 2. Create FLAG to the TOP-RANKED specialist
create-flag --target_agent "@service.auth" --action_required "..."
# Always correct target → efficient workflow
```

### Benefits

- **Zero routing ambiguity**: Agents always find the RIGHT specialist
- **Expertise matching**: Tasks go to the most qualified agent
- **Reduced FLAG cycles**: No more "wrong agent" bouncing
- **Knowledge discovery**: Agents discover specialists they didn't know existed

## Complete Flow Examples

### Example 1: Simple Feature Addition

**User**: "Add JWT authentication to API"

1. **Claude** → `@api-agent` (acolyte for API module)
2. **@api-agent** reads all memory types, decides needs design consultation
3. **@api-agent** creates FLAG: `target: @service.auth, action: "Design JWT implementation for API module"`
4. **@api-agent** annotates consultation in memory, closes
5. **Next /flags cycle**: `@flags.agent` → **Claude**: "invoke @service.auth"
6. **@service.auth** reads FLAG, provides JWT design recommendations
7. **@service.auth** creates response FLAG: `target: @api-agent, action: "JWT design completed"`
8. **Next /flags cycle**: `@api-agent` reads design response
9. **@api-agent** creates NEW FLAG: `target: @backend.nodejs, action: "Implement JWT according to design"`
10. **Next /flags cycle**: `@flags.agent` → **Claude**: "invoke @backend.nodejs"
11. **@backend.nodejs** reads FLAG and design, writes actual JWT code
12. **@backend.nodejs** creates response FLAG: `target: @api-agent, action: "JWT implementation completed"`
13. **Next /flags cycle**: `@api-agent` reads completion, verifies implementation
14. **@api-agent** updates all memory types with new JWT implementation
15. **@api-agent** creates FLAG: `target: @changelog-agent, action: "Document JWT addition"`

**ChainFlag Tracking**: All flags have `chain_origin_id: 23` (original JWT request)

### Example 2: Cross-Module Impact

**User**: "Change database schema for users table"

1. **Claude** → `@database-agent`
2. **@database-agent** analyzes schema change impact
3. **@database-agent** creates multiple FLAGs:
   - `target: @database.postgres` - Execute schema migration
   - `target: @api-agent` - Update user endpoints
   - `target: @auth-agent` - Update authentication queries
4. **@flags.agent** processes in parallel (different modules, no conflicts)
5. Each target agent completes work, notifies originator
6. **@database-agent** verifies all changes, updates memory

### Example 3: Locked Flag Resolution

**User**: "Implement push notifications"

1. **@api-agent** creates FLAG to `@service.communication`
2. **@service.communication** doesn't know which push service to use
3. **@service.communication** **locks** original FLAG
4. **@service.communication** creates consultation FLAG: `target: @service.integrations, action: "Recommend push service"`
5. **Next /flags cycle**: `@flags.agent` prioritizes unlocking sequence:
   - **FIRST**: Execute `@service.integrations` (resolve consultation)
   - **SECOND**: Execute `@service.communication` (complete locked work)
6. **@service.integrations** responds with Firebase recommendation
7. **@service.communication** reads response, implements Firebase, unlocks original FLAG
8. **@api-agent** receives completion notification

### Example 4: File Conflict Prevention

**Parallel requests affecting same file**

1. Two FLAGs created targeting `src/api/auth.js`:
   - FLAG #45: `target: @backend.nodejs, action: "Add rate limiting to auth.js"`
   - FLAG #46: `target: @backend.nodejs, action: "Update error handling in auth.js"`
2. **@flags.agent** detects conflict via `related_files` field
3. **@flags.agent** → **Claude**: "invoke @backend.nodejs for FLAG #45 first"
4. **@backend.nodejs** completes FLAG #45, updates auth.js
5. **Next /flags cycle**: **@flags.agent** → **Claude**: "invoke @backend.nodejs for FLAG #46"
6. **@backend.nodejs** completes FLAG #46 on updated file
7. Prevents merge conflicts and duplicate work

### Example 5: Priority Degradation

**Multiple critical flags created**

1. 15 agents create FLAGs with `impact: critical`
2. **@flags.agent** analyzes: "Not all can be truly critical"
3. **@flags.agent** degrades priority based on:
   - Business impact analysis
   - Dependency chains
   - Resource availability
4. Rebalances to 3 critical, 7 high, 5 medium

### Example 6: Timeout Investigation

**Agent doesn't respond**

1. **@api-agent** creates FLAG to `@database.postgres`
2. **@database.postgres** never responds (broken prompt, etc.)
3. **@flags.agent** detects timeout after 3 cycles
4. **@flags.agent** → **Claude**: "Investigate @database.postgres - not responding to FLAGs"
5. **Claude** debugs agent, fixes issue

### Example 7: Audit Flag Creation

**Error detected in implementation**

1. **@api-agent** reviews recent changes, finds security vulnerability
2. **@api-agent** creates FLAG: `target: @audit.security, action: "Audit recent JWT implementation", impact: critical`
3. **@audit.security** performs security review
4. **@audit.security** creates corrective FLAGs if issues found

### Example 8: Submodule Coordination

**Large API module with submodules**

1. User requests OAuth integration
2. **@api-agent** determines this affects multiple submodules
3. **@api-agent** creates 3 separate FLAGs:
   - FLAG #67: `target: @api-auth-agent, action: "Implement OAuth authentication flow"`
   - FLAG #68: `target: @api-endpoints-agent, action: "Create OAuth endpoints"`
   - FLAG #69: `target: @api-middleware-agent, action: "Add OAuth middleware"`
4. **@flags.agent** processes the 3 flags (can run in parallel - different submodules)
5. **@flags.agent** → **Claude**: "invoke @api-auth-agent, @api-endpoints-agent, @api-middleware-agent"
6. Each submodule agent completes work, creates response FLAGs back to **@api-agent**
7. **@api-agent** receives 3 completions, verifies integration, updates memory

### Example 9: Documentation Chain

**Complete feature lifecycle**

1. Feature implemented by **@backend.nodejs**
2. **@backend.nodejs** creates documentation FLAGs:
   - FLAG #71: `target: @docs.technical, action: "Document new API endpoints"`
   - FLAG #72: `target: @changelog-agent, action: "Add feature to changelog"`
   - FLAG #73: `target: @docs.readme, action: "Update README with new feature"`
3. **@flags.agent** analyzes flags, determines can run in parallel (no conflicts - different files)
4. **@flags.agent** → **Claude**: "invoke in parallel: @docs.technical, @changelog-agent, @docs.readme"
5. All documentation agents work simultaneously
6. Complete feature delivery with full documentation

### Example 10: Emergency Rollback

**Critical issue detected in production**

1. **@ops.monitoring** detects system failure
2. **@ops.monitoring** creates critical FLAG: `target: @coordinator.backend, action: "Emergency rollback required"`
3. **@coordinator.backend** analyzes, creates multiple urgent FLAGs
4. **@flags.agent** prioritizes all rollback FLAGs as critical
5. Parallel execution of rollback procedures

## Algorithm & Prioritization

### [TO BE COMPLETED]

### Priority Levels

- `critical`: System broken, immediate action required
- `high`: Major features affected, urgent
- `medium`: Important but not blocking
- `low`: Informational, can be deferred

### Execution Order

1. **Unlock chains first**: Execute agents needed to resolve locked FLAGs
2. **Process locked FLAGs**: Execute agents with locked FLAGs (after unlock)
3. **New FLAGs by priority**: Process new work by impact level

### Parallelization Rules

- **Same agent**: NEVER in parallel (would duplicate work)
- **Same files**: Serialize via `related_files` detection
- **Different modules**: Can run in parallel
- **Max concurrent**: 10 agents maximum

### ChainFlag Sequencing

- **Phase 1**: Consultation/Request/Code modification
- **Phase 2**: Investigation/Execution
- **Phase 3**: Documentation/Changelog

## Agent Prompts & Templates

### Acolytes System Prompt

**[TO BE COMPLETED]**

Key requirements:

- Read all 8 memory types on invocation
- Update memory after any module changes
- Create FLAGs for cross-module impacts
- Never modify code directly - always delegate
- Annotate all decisions and changes

### Professional Agents System Prompt

**[TO BE COMPLETED]**

Key requirements:

- Check FLAGs first (mandatory)
- Complete pending FLAGs before user tasks
- Create response FLAGs when work completed
- No persistent memory - stateless operation

## Technical Information

### Database Schema

```sql
-- Core FLAGS table with ChainFlag support
CREATE TABLE flags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chain_origin_id INTEGER,  -- Links to original FLAG in chain
    flag_type TEXT NOT NULL,
    source_agent TEXT NOT NULL,
    target_agent TEXT NOT NULL,
    action_required TEXT NOT NULL,
    impact_level TEXT DEFAULT 'medium',
    status TEXT DEFAULT 'pending',
    locked BOOLEAN DEFAULT FALSE,
    related_files TEXT,
    created_at TEXT NOT NULL,
    -- ... additional fields
);
```

### Agent Memory Types

Every acolyte maintains 8 memory types:

- `knowledge`: Core understanding, purpose, features, architecture
- `structure`: Code organization, files, classes, functions, APIs
- `patterns`: Best practices, conventions, anti-patterns
- `dependencies`: Internal/external dependencies, services
- `quality`: Tests, coverage, performance, security analysis
- `operations`: Config, deployment, monitoring, CI/CD
- `context`: Business logic, decisions, roadmap
- `domain`: Specialized knowledge specific to the module

## System Benefits

### Context Efficiency

- **Claude context preserved**: No FLAG details in Claude's window
- **Autonomous operation**: System runs without constant supervision
- **Scalable**: Handles hundreds of concurrent FLAGs

### Quality Assurance

- **No code touched without agent approval**: Dynamic agents guard their modules
- **Complete audit trail**: Every change documented and reasoned
- **Cross-module coordination**: Automatic impact analysis

### Development Speed

- **Parallel processing**: Multiple non-conflicting tasks simultaneously
- **Intelligent prioritization**: Critical work always first
- **Automated documentation**: Changes auto-documented in chains

---

## Next Steps

1. Complete algorithm implementation in `@flags.agent`
2. Finalize acolyte prompt templates
3. Add ChainFlag tracking to database schema
4. Implement conflict detection algorithms
5. Create monitoring dashboard for FLAG system health

---

**The FLAG system transforms ClaudeSquad from a collection of agents into a coordinated, intelligent development team that operates with minimal human intervention while maintaining complete transparency and control.**
