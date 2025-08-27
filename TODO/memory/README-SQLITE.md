# 📊 SQLite Memory System for Claude Code

## Overview

The SQLite memory system is a **persistent, universal memory architecture** designed to give Claude Code and its agents perfect recall across sessions. This system replaces the previous JSON-based memory with a robust, queryable database that scales from simple projects to complex enterprise systems.

## Why SQLite?

- **Performance**: 2-10x faster reads than JSON files
- **Atomicity**: ACID transactions prevent corruption
- **Concurrency**: Multiple agents can read simultaneously
- **Scalability**: Handles millions of records efficiently
- **Queryability**: SQL allows complex memory searches
- **Portability**: Single file database, works everywhere

## Database Schema

### Core Tables for Job Tracking

### Table: JOBS
Tracks high-level work initiatives that span multiple Claude sessions.

| Column | Type | Description |
|--------|------|-------------|
| id | TEXT PK | Job identifier (e.g., 'migration-sqlite') |
| status | TEXT | 'active', 'paused', or 'completed' |
| created_at | TEXT | When job started |
| paused_at | TEXT | When paused (if applicable) |
| resumed_at | TEXT | When resumed (if applicable) |
| completed_at | TEXT | When completed (if applicable) |
| pause_reason | TEXT | Why the job was paused |

### Table: SESSIONS
Individual Claude conversations tied to a job.

| Column | Type | Description |
|--------|------|-------------|
| id | TEXT PK | Claude's actual session_id |
| job_id | TEXT FK | References jobs(id) |
| title | TEXT | Session summary |
| accomplishments | JSON | List of completed tasks |
| decisions | JSON | Important choices made |
| pending | JSON | Tasks not completed |
| bugs_fixed | JSON | Bugs resolved |
| errors_encountered | JSON | Problems faced |
| breakthrough_moment | TEXT | Key insight/solution |
| next_session_priority | TEXT | What to do first next time |
| quality_score | INTEGER | Session effectiveness (0-10) |
| created_at | TEXT | Session start |
| ended_at | TEXT | Session end |

### Table: MESSAGES
Complete chronological conversation flow (backup, not auto-loaded).

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Message record ID |
| session_id | TEXT FK | References sessions(id) |
| conversation_flow | TEXT | Full narrative of what happened |
| total_exchanges | INTEGER | Number of user-assistant exchanges |
| duration_minutes | INTEGER | Session duration |
| created_at | TEXT | When saved |

### Table: FLAGS
Inter-module communication system for changes that affect other modules.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Flag identifier |
| session_id | TEXT FK | Session where flag was created |
| flag_type | TEXT | change/new_feature/refactor/deprecation/breaking_change |
| source_module | TEXT | Module that made the change |
| source_agent | TEXT | Agent that created the flag |
| affected_modules | TEXT | Comma-separated list of affected modules |
| change_description | TEXT | What changed (e.g., "Created global TIME utility") |
| action_required | TEXT | What other modules need to do |
| impact_level | TEXT | low/medium/high/critical (impact, not error severity) |
| status | TEXT | pending/acknowledged/in_progress/completed/skipped |
| related_files | TEXT | Files involved (comma-separated) |
| code_location | TEXT | file:line_number format if specific location |
| example_usage | TEXT | Example of how to use the new change |
| context | JSON | Additional structured data |
| created_at | TEXT | When flag was created |
| acknowledged_at | TEXT | When affected modules acknowledged |
| completed_at | TEXT | When all affected modules adapted |
| completed_by | TEXT | Agents that completed the adaptation |
| notes | TEXT | Resolution notes or comments |

### Table: AGENT_HEALTH
Monitors agent drift and memory size to maintain system health.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Health record identifier |
| agent_id | INTEGER FK | References agents(id) |
| session_id | TEXT FK | Session where check happened |
| drift_score | INTEGER | 0-100 drift from module reality |
| confidence_score | INTEGER | 0-100 confidence in agent knowledge |
| status | TEXT | healthy/degraded/critical/oversized |
| file_count_current | INTEGER | Current files in module |
| file_count_baseline | INTEGER | Files when agent was created/updated |
| memory_size_kb | INTEGER | Total size of all 8 memories in KB |
| memory_size_warning | TEXT | null/large/critical |
| largest_memory_type | TEXT | Which memory is largest |
| needs_compaction | BOOLEAN | If memories need cleaning |
| patterns_changed | TEXT | New patterns detected |
| dependencies_changed | TEXT | Changed dependencies |
| issues | JSON | Structured issues found |
| recommendations | TEXT | Clear action recommendation |
| auto_upgrade_eligible | BOOLEAN | Can be auto-upgraded |
| checked_at | TEXT | When health was checked |
| last_upgrade_at | TEXT | When agent was last upgraded |
| upgraded_by | TEXT | Who upgraded (auto/manual/agent) |

### Table: TOOL_LOGS
Comprehensive tracking of all tool usage for analytics and error detection.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Tool log identifier |
| session_id | TEXT FK | References sessions(id) |
| tool_name | TEXT | Name of tool used (Read/Write/Bash/etc) |
| tool_category | TEXT | file/search/execution/ai/mcp |
| parameters | JSON | Full parameters passed to tool |
| file_affected | TEXT | File path if applicable |
| lines_changed | INTEGER | Lines added/removed/modified |
| bytes_processed | INTEGER | Size of data processed |
| result_summary | TEXT | Brief result description |
| success | BOOLEAN | Whether tool succeeded |
| error_message | TEXT | Error if failed |
| blocked_by_hook | BOOLEAN | If pre_tool_use blocked it |
| hook_message | TEXT | Hook block reason |
| duration_ms | INTEGER | Execution time |
| timestamp | TEXT | When tool was called |

### Table: TODOS
Advanced task management with AI integration, agent delegation, and automatic synchronization.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | TODO identifier |
| task | TEXT | Task description |
| priority | TEXT | low/medium/high/critical |
| status | TEXT | pending/in_progress/completed/blocked/cancelled |
| due_date | TEXT | When task is due |
| created_at | TEXT | When created |
| completed_at | TEXT | When completed |
| agent_id | INTEGER FK | Agent assigned to task |
| session_id | TEXT FK | Session when created |
| assigned_to | TEXT | Agent or module assigned |
| estimated_hours | REAL | Estimated time to complete |
| actual_hours | REAL | Actual time spent |
| start_date | TEXT | When work started |
| reminder_at | TEXT | When to remind |
| category | TEXT | bug/feature/refactor/test/docs/maintenance |
| module | TEXT | Module affected |
| tags | JSON | Tags for search and filtering |
| dependencies | JSON | Array of TODO IDs that block this |
| created_by | TEXT | user/claude/system/agent |
| updated_at | TEXT | Last modification |
| updated_by | TEXT | Who modified it |
| completed_by | TEXT | Who completed it |
| related_files | JSON | Array of related file paths |
| subtasks_total | INTEGER | Total subtasks |
| subtasks_completed | INTEGER | Completed subtasks |
| blocked_reason | TEXT | Why it's blocked |
| auto_created | BOOLEAN | If created automatically |
| ai_suggested | BOOLEAN | If suggested by AI |
| context | JSON | Additional context (claude_id, parent_id, etc) |

### Agent Memory Tables

### Table 1: AGENTS

Stores all dynamic agents created for project modules.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Unique agent identifier |
| name | TEXT UNIQUE | Agent name (e.g., 'auth-agent') |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Last update timestamp |

### Table 2: AGENT_MEMORY

The heart of the system - stores 8 types of memory for each agent.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Unique memory record ID |
| agent_id | INTEGER FK | References agents(id) |
| memory_type | TEXT | One of 8 memory types (see below) |
| content | JSON | Memory content as JSON |
| created_at | TEXT | When memory was created |
| updated_at | TEXT | Last memory update |

## The 8 Memory Types

Every agent has up to 8 memory records, each serving a specific purpose:

### 1. **knowledge** - Core Understanding
```json
{
  "module_name": "authentication",
  "purpose": "Handles user authentication and authorization",
  "core_responsibility": "Secure user access management",
  "key_features": ["JWT tokens", "OAuth2", "2FA support"],
  "architecture": "Middleware-based with guards",
  "business_context": "Critical security module",
  "todos": ["Add biometric support", "Implement SSO"]
}
```

### 2. **structure** - Code Organization
```json
{
  "file_tree": {
    "controllers/AuthController.js": {
      "purpose": "Authentication endpoints",
      "functions": ["login", "logout", "refresh"],
      "lines": 245
    }
  },
  "api_endpoints": ["POST /auth/login", "POST /auth/logout"],
  "classes": ["AuthController", "AuthService", "TokenManager"],
  "total_files": 15
}
```

### 3. **patterns** - Best Practices
```json
{
  "design_patterns": ["Strategy", "Factory", "Middleware"],
  "conventions": {
    "naming": "camelCase for functions, PascalCase for classes",
    "file_size": "max 300 lines",
    "test_pattern": "*.test.js alongside source files"
  },
  "anti_patterns_found": ["God object in UserService"],
  "best_practices": ["Input validation", "Rate limiting"]
}
```

### 4. **dependencies** - Connections
```json
{
  "internal": ["UserModule", "DatabaseModule", "CacheModule"],
  "external": ["jsonwebtoken@9.0", "bcrypt@5.1", "passport@0.6"],
  "services": ["Redis", "PostgreSQL"],
  "integrations": ["Google OAuth", "Facebook Login"],
  "database_tables": ["users", "sessions", "refresh_tokens"]
}
```

### 5. **quality** - Code Health
```json
{
  "test_coverage": "87%",
  "test_suites": ["unit", "integration", "e2e"],
  "performance_metrics": {
    "avg_response_time": "45ms",
    "max_concurrent_users": 10000
  },
  "security_analysis": {
    "vulnerabilities": [],
    "last_audit": "2025-01-15"
  },
  "code_quality": {
    "complexity": "low",
    "duplication": "2%"
  }
}
```

### 6. **operations** - DevOps (Optional)
```json
{
  "environment_vars": ["JWT_SECRET", "OAUTH_CLIENT_ID"],
  "deployment": "Docker + Kubernetes",
  "monitoring": ["Datadog", "Sentry"],
  "ci_cd": "GitHub Actions",
  "migrations": ["001_create_users", "002_add_2fa"]
}
```

### 7. **context** - Business Logic
```json
{
  "business_importance": "Critical - all users must authenticate",
  "stakeholders": ["Security Team", "Product", "Compliance"],
  "decisions": [
    "Use JWT instead of sessions for scalability",
    "Implement 2FA for admin accounts only"
  ],
  "technical_debt": ["Refactor token refresh logic"],
  "roadmap": ["Q1: Biometric auth", "Q2: SSO integration"]
}
```

### 8. **domain** - Specialized Knowledge (Optional)
```json
{
  "security_protocols": ["OAuth2", "SAML", "OpenID Connect"],
  "compliance": ["GDPR", "SOC2", "HIPAA"],
  "domain_entities": ["User", "Session", "Permission", "Role"],
  "business_rules": [
    "Sessions expire after 24 hours",
    "Max 3 login attempts before lockout"
  ]
}
```

## How the FLAGS System Works

### Purpose

FLAGS are **NOT for reporting errors or problems**. They are a communication protocol for agents to notify other modules when they make changes that affect them. This enables coordinated evolution of the codebase without breaking dependencies.

### When to Create a FLAG

Agents create FLAGS when they:
- **Create a shared utility** that other modules should use
- **Change an API** that other modules consume
- **Refactor code** that others depend on
- **Add a feature** that others can leverage
- **Deprecate functionality** that others are using
- **Optimize an algorithm** allowing others to remove workarounds

### FLAG Lifecycle

1. **Creation**: Agent detects a change affecting other modules
   ```python
   python .claude/scripts/agent_db.py create-flag \
     --flag_type "new_feature" \
     --source_module "core" \
     --source_agent "core-agent" \
     --affected_modules "api,frontend,auth" \
     --change_description "Created centralized validation service" \
     --action_required "Replace local validation with ValidationService" \
     --impact_level "medium"
   ```

2. **Discovery**: Claude reads pending FLAGS and delegates to affected agents
   ```sql
   SELECT * FROM flags WHERE status = 'pending' 
   AND affected_modules LIKE '%my_module%'
   ```

3. **Acknowledgment**: Affected agents mark FLAG as acknowledged
   ```sql
   UPDATE flags SET status = 'acknowledged', 
   acknowledged_at = '2025-01-17 10:30' WHERE id = 42
   ```

4. **Resolution**: Agents adapt to the change and mark complete
   ```sql
   UPDATE flags SET status = 'completed',
   completed_at = '2025-01-17 11:00',
   completed_by = 'api-agent,frontend-agent'
   WHERE id = 42
   ```

### Real Example: TIME Utility

**Scenario**: CORE module creates a global TIME utility for consistent timestamp handling.

**FLAG Creation**:
```python
python .claude/scripts/agent_db.py create-flag \
  --flag_type "new_feature" \
  --source_module "core" \
  --source_agent "core-agent" \
  --affected_modules "semantic,embeddings,rag,api,frontend" \
  --change_description "Created global TIME utility for consistent timestamp handling" \
  --action_required "Replace local time functions with TIME.format() from @core/utils" \
  --impact_level "medium" \
  --related_files "src/core/utils/time.js" \
  --example_usage "import { TIME } from '@core/utils'; TIME.format(date, 'ISO');"
```

**Result**: All affected modules are notified to adopt the centralized TIME utility instead of maintaining their own implementations.

### FLAG Types

- **change**: Existing functionality modified
- **new_feature**: New capability added that others can use
- **refactor**: Code restructured (same functionality, different implementation)
- **deprecation**: Feature marked for future removal
- **breaking_change**: Change that requires immediate adaptation
- **enhancement**: Improvement that others can optionally adopt

### Impact Levels

- **low**: Optional improvement, no urgency
- **medium**: Should be adopted soon for consistency
- **high**: Important change, prioritize adaptation
- **critical**: Must be addressed immediately

## How Agents Use Memory

### 1. Memory Loading

When an agent is invoked, it loads its memories:

```python
# Agent loads all 8 memory types on activation
memories = {}
for memory_type in ['knowledge', 'structure', 'patterns', 'dependencies', 
                    'quality', 'operations', 'context', 'domain']:
    result = agent_db.get_memory(agent_name, memory_type)
    if result:
        memories[memory_type] = json.loads(result)
```

### 2. Memory Updates

Agents update their memories when changes occur:

```python
# After adding a new function
structure_memory = get_memory(agent_name, 'structure')
structure_memory['file_tree'][file_path]['functions'].append(new_function)
update_memory(agent_name, 'structure', structure_memory)

# After discovering a pattern
patterns_memory = get_memory(agent_name, 'patterns')
patterns_memory['design_patterns'].append('Observer')
update_memory(agent_name, 'patterns', patterns_memory)
```

### 3. Memory Queries

Agents can query specific memories:

```python
# Check test coverage
quality = get_memory(agent_name, 'quality')
coverage = quality['test_coverage']

# Find dependencies
deps = get_memory(agent_name, 'dependencies')
external_libs = deps['external']
```

## Agent Health System

### Purpose

The Agent Health system automatically monitors agent "drift" - when code changes but agents aren't updated, they lose sync with reality. It also monitors memory size to prevent context overflow.

### How It Works

#### 1. **Automatic Self-Check**

When any dynamic agent is invoked, it immediately:
- Counts files in its module
- Measures total memory size
- Calculates drift score
- Updates health record
- Creates FLAGS if issues detected

#### 2. **Drift Score Calculation**

```python
# File changes impact
file_drift = abs(current_files - baseline_files) * 10  # 10 points per file

# Time decay
days_old = (now - agent_created_date).days
time_drift = days_old * 2  # 2 points per day

drift_score = min(file_drift + time_drift, 100)  # Max 100
```

#### 3. **Health Status Levels**

- **healthy** (drift < 30, memory < 1MB): Operating normally
- **degraded** (drift 30-70, memory 1-2MB): Monitor closely
- **critical** (drift > 70): Needs immediate re-analysis
- **oversized** (memory > 2MB): Needs compaction

#### 4. **Automatic Actions**

When problems are detected:

```python
# Memory oversized
if memory_size_kb > 2000:
    create_flag(
        flag_type="maintenance",
        change_description="Agent memory oversized: 2456 KB",
        action_required="Run: python .claude/scripts/compact_memory.py api-agent"
    )

# Drift critical
if drift_score > 70:
    create_flag(
        flag_type="maintenance",
        change_description="Agent critically out of sync: drift 75",
        action_required="Agent needs re-analysis of module /src/api"
    )
```

### Memory Compaction

When agent memories grow too large, they're automatically compacted:

#### Compaction Strategies by Memory Type

| Memory Type | Strategy | Size Limit |
|-------------|----------|------------|
| **structure** | Keep only files > 100 lines | 200 KB |
| **context** | Keep last 10 changes + milestones | 100 KB |
| **dependencies** | Remove version numbers | 40 KB |
| **patterns** | Remove resolved anti-patterns | 30 KB |
| **quality** | Keep only latest metrics | 30 KB |
| **knowledge** | Remove completed TODOs | 50 KB |

#### Running Compaction

```bash
# Automatic - only if needed
python .claude/scripts/compact_memory.py --auto api-agent

# Force compaction
python .claude/scripts/compact_memory.py api-agent
```

#### Compaction Results

```json
{
  "agent": "api-agent",
  "total_before_kb": 2456.3,
  "total_after_kb": 487.2,
  "total_saved_kb": 1969.1,
  "reduction_percent": 80.2,
  "compacted_memories": [
    {"type": "structure", "before_kb": 1800, "after_kb": 200},
    {"type": "context", "before_kb": 400, "after_kb": 100}
  ]
}
```

### Health Monitoring Commands

```bash
# Check specific agent health
python .claude/scripts/agent_db.py get-health api-agent

# Check all agents
python .claude/scripts/agent_db.py get-health

# Manual health update (usually automatic)
python .claude/scripts/agent_db.py update-health \
  --agent_name api-agent \
  --drift_score 45 \
  --status degraded \
  --memory_size_kb 1500
```

### Best Practices

1. **Let agents self-monitor** - They check automatically when invoked
2. **Respond to FLAGS quickly** - Especially "critical" and "oversized"
3. **Regular compaction** - Run monthly or when FLAGS appear
4. **Re-analyze when drift > 70** - Agent knowledge is stale
5. **Split large agents** - If consistently > 2MB after compaction

### Health Metrics Dashboard

```sql
-- View health status of all agents
SELECT 
    a.name,
    h.status,
    h.drift_score,
    h.memory_size_kb,
    h.needs_compaction,
    h.checked_at
FROM agent_health h
JOIN agents a ON h.agent_id = a.id
ORDER BY h.drift_score DESC;
```

Example output:
```
api-agent     | critical  | 82  | 2456 | true  | 2025-01-17 10:30
auth-agent    | degraded  | 45  | 890  | false | 2025-01-17 10:25  
frontend-agent| healthy   | 12  | 456  | false | 2025-01-17 10:20
```

## Memory Creation Process

When `agent-creator` analyzes a module:

1. **Scans entire module** - Every file, function, pattern
2. **Categorizes information** - Sorts into 8 memory types
3. **Creates agent record** - Inserts into agents table
4. **Stores memories** - Creates 3-8 memory records (only what's needed)
5. **Generates agent file** - Creates .md file with agent definition

## Benefits of 8 Memory Types

### For Simple Projects
- Only create 3-4 memory types (knowledge, structure, patterns)
- Minimal overhead, fast queries
- Easy to understand and maintain

### For Complex Projects
- Use all 8 memory types for complete coverage
- Specialized memories for ML, GraphQL, etc.
- Detailed operational and compliance tracking

### Flexibility
- Each project uses only what it needs
- Memory types are well-defined and documented
- Agents know exactly what goes where

## Database Management

### Initialization
```bash
/db init  # Creates all tables and indexes
```

### Health Check
```bash
/db doctor  # Checks integrity, suggests optimizations
```

### Memory Statistics
```bash
/db stats  # Shows memory usage per agent
```

### Cleanup
```bash
/db cleanup  # Removes orphaned memories
```

## Best Practices

1. **Keep JSONs Focused** - Each memory type has a clear purpose
2. **Update Atomically** - Use transactions for multi-memory updates
3. **Version Control** - Database file can be committed to Git
4. **Regular Maintenance** - Run /db doctor weekly
5. **Document Changes** - Agents should log why memories changed

## Migration from JSON

For existing projects with JSON memories:

```bash
/db migrate  # Converts JSON files to SQLite
```

This will:
1. Read all .claude/memory/agents/*/\*.json files
2. Create agent records
3. Convert JSONs to 8 memory types
4. Preserve all data and timestamps

## Performance Characteristics

- **Memory Load Time**: <50ms for all 8 memories
- **Update Time**: <20ms per memory type
- **Query Time**: <10ms for specific memory
- **Database Size**: ~100KB per agent (average)
- **Concurrent Reads**: Unlimited
- **Concurrent Writes**: Serialized (SQLite limitation)

## Job Tracking System

### How It Works

1. **Session Start** (`session_start.py` hook):
   - Captures real session_id from Claude
   - Finds or creates active job
   - Inserts session record
   - Loads context from previous sessions

2. **During Work**:
   - Claude works on tasks
   - Agents update their memories
   - Progress is tracked mentally

3. **Session End** (`/save` command):
   - Updates session with accomplishments, decisions, etc.
   - Records bugs fixed and breakthroughs
   - Sets priority for next session
   - Optionally saves conversation to MESSAGES

### Job Management

Claude automatically:
- Creates jobs when detecting new work context
- Pauses jobs when switching to different work  
- Resumes most relevant job when returning
- Completes jobs when work is finished

Users can:
- View status with `/jobs`
- Save sessions with `/save`
- Review conversations with `/chat` (coming soon)

### Key Differences

- **SESSIONS**: What Claude reads on startup (summary, decisions, next steps)
- **MESSAGES**: Detailed conversation backup (only read when needed)
- **AGENTS**: Module-specific knowledge that persists forever

## Tool Usage Tracking System

### Purpose

The TOOL_LOGS table provides comprehensive analytics on tool usage patterns, error detection, and performance monitoring. Every tool call is logged with detailed metrics, enabling:

- **Error Pattern Detection**: Identify files causing repeated failures
- **Performance Analysis**: Track slow operations and optimize
- **Security Monitoring**: Detect and block dangerous operations
- **Usage Analytics**: Understand which tools are used most

### How It Works

#### 1. **Pre-Tool Hook** (`pre_tool_use.py`)

Before any tool executes:
- Logs tool name, parameters, target files
- Checks for dangerous operations (rm -rf, .env access)
- Can block execution with exit code 2
- Records in SQLite immediately

#### 2. **Post-Tool Hook** (`post_tool_use.py`)

After tool execution:
- Updates log with success/failure
- Records bytes processed, lines changed
- Captures error messages
- Calculates execution duration

### Tool Categories

| Category | Tools | Purpose |
|----------|-------|---------|
| **file** | Read, Write, Edit, MultiEdit | File operations |
| **search** | Grep, Glob, LS | Finding code/files |
| **execution** | Bash, BashOutput, KillBash | Running commands |
| **ai** | Task, WebSearch, WebFetch | AI operations |
| **mcp** | mcp__* tools | MCP server tools |

### Analytics Commands

```bash
# View recent tool usage
/tools                # Last 20 tool calls
/tools session        # Current session only
/tools blocked        # Blocked attempts
/tools stats          # Usage statistics

# Filter by tool
/tools Bash           # Only Bash commands
/tools Edit           # Only file edits
```

### Example Statistics Output

```
TOOL USAGE STATISTICS
================================================================================
Total tool calls: 1,247
Successful: 1,180 (94.6%)
Failed: 52 (4.2%)
Blocked: 15 (1.2%)

Most Used Tools:
  Read (file): 412 calls
  Bash (execution): 287 calls
  Edit (file): 198 calls
  Grep (search): 156 calls

Most Accessed Files:
  src/api/routes.js: 47 times
  package.json: 35 times
  .env.example: 28 times

Data Processed:
  Total: 156.3 MB
  Average per tool: 128.5 KB
```

### Security Features

#### Blocked Operations

The system automatically blocks:
- `rm -rf /` and dangerous deletions
- Access to `.env` files (not `.env.sample`)
- Commands matching custom patterns

#### Example Block

```python
# In pre_tool_use.py
if tool_name == 'Bash' and 'rm -rf' in command:
    log_to_sqlite(tool_data, blocked=True, 
                  block_reason="Dangerous rm command detected")
    print("BLOCKED: Dangerous rm command", file=sys.stderr)
    sys.exit(2)  # Blocks execution
```

### Performance Tracking

```sql
-- Find slow operations
SELECT tool_name, file_affected, duration_ms, timestamp
FROM tool_logs
WHERE duration_ms > 5000  -- Operations over 5 seconds
ORDER BY duration_ms DESC;

-- Files causing errors
SELECT file_affected, COUNT(*) as error_count
FROM tool_logs
WHERE success = 0 AND file_affected IS NOT NULL
GROUP BY file_affected
ORDER BY error_count DESC;
```

## TODO System - Intelligent Task Management

### Overview

The TODO system is a **fully automated, AI-integrated task management** system that:
- **Auto-syncs** with Claude's internal TodoWrite tool
- **Auto-categorizes** tasks using AI analysis
- **Auto-delegates** to appropriate agents
- **Auto-creates** from FLAGS, errors, and session analysis
- **Auto-tracks** subtasks and dependencies

### The Three Layers of Automation

#### Layer 1: TodoWrite Synchronization

When Claude uses TodoWrite internally:

```python
# todo_sync.py hook intercepts
TodoWrite({
  todos: [
    {id: "1", content: "Fix auth bug", status: "in_progress"},
    {id: "1.1", content: "Write test", status: "pending"},
    {id: "1.2", content: "Deploy fix", status: "pending"}
  ]
})

# Automatically:
# 1. Detects hierarchy (1 → 1.1, 1.2)
# 2. Categorizes as "bug"
# 3. Extracts module "auth"
# 4. Creates in SQLite with relationships
```

#### Layer 2: Task Tool Integration

When Claude delegates to subagents:

```python
# task_delegation.py hook captures
Task({
  description: "Analyze test coverage",
  subagent_type: "test-automation-specialist"
})

# Automatically:
# 1. Creates TODO assigned to specialist
# 2. Marks as in_progress
# 3. Updates when subagent completes
```

#### Layer 3: Session Intelligence

At session end:

```python
# session_end.py analyzes and creates TODOs for:
- Test failures: "Fix 3 failing tests in auth module"
- Linting errors: "Resolve 12 ESLint warnings"
- Pending FLAGS: "Address critical FLAG #42"
- Oversized agents: "Compact api-agent memory (2.5MB)"
- Incomplete work: "Continue: Implement OAuth flow"
```

### AI-Powered Features

#### Auto-Categorization

```python
def detect_category(task):
    # Analyzes keywords to categorize
    if 'bug' or 'fix' or 'error' in task:
        return 'bug'
    elif 'feature' or 'implement' in task:
        return 'feature'
    elif 'test' or 'spec' in task:
        return 'test'
    # ... etc
```

#### Smart Delegation

```python
# Module-based routing
if module == "auth":
    assign_to = "ClaudeSquad-auth"

# Category-based fallback
elif category == "bug":
    assign_to = "error-detective"
elif category == "test":
    assign_to = "test-automation-specialist"
```

#### Dependency Detection

```python
# Finds explicit dependencies
"Fix API after #23 is done" → dependencies: [23]
"Requires #15 to be completed" → dependencies: [15]

# Detects subtask hierarchies
"1. Main task"
"1.1 Subtask A" → parent: 1
"1.2 Subtask B" → parent: 1
```

### Command Usage

```bash
# Basic operations
/todo                           # List pending
/todo add "Fix bug" high        # Add with priority
/todo complete 42               # Mark done
/todo status 42 in_progress     # Update status

# Smart features
/todo sync                      # Sync with Claude's TodoWrite
/todo smart                     # AI analysis and categorization  
/todo delegate                  # Auto-assign to agents

# Automation
/todo from-flags                # Create from critical FLAGS
/todo session-end               # Analyze session for TODOs

# Filtering (15+ filters)
/todo list all                  # Everything
/todo list in_progress          # Active work
/todo list overdue              # Past due date
/todo list high                 # High/critical priority
/todo list assigned             # Has assignee
/todo list synced               # From Claude's TodoWrite
/todo list delegated            # From Task tool
```

### Advanced Filtering

The system supports 15+ filter types:

| Filter | Description | SQL Condition |
|--------|-------------|---------------|
| **pending** | Not started | `status = 'pending'` |
| **in_progress** | Being worked on | `status = 'in_progress'` |
| **completed** | Finished | `status = 'completed'` |
| **blocked** | Can't proceed | `status = 'blocked'` |
| **today** | Due today | `date(due_date) = date('now')` |
| **overdue** | Past due | `due_date < date('now')` |
| **week** | Next 7 days | `due_date <= date('now', '+7 days')` |
| **assigned** | Has owner | `assigned_to IS NOT NULL` |
| **unassigned** | Needs owner | `assigned_to IS NULL` |
| **high** | High/critical | `priority IN ('high','critical')` |
| **synced** | From Claude | `context->>'$.auto_synced' = 'true'` |
| **delegated** | From Task | `context->>'$.delegated_via' = 'Task tool'` |

### Hooks and Integration Points

#### Active Hooks

1. **todo_sync.py** - Captures TodoWrite calls
2. **task_delegation.py** - Captures Task tool usage
3. **session_end.py** - End-of-session analysis
4. **pre_tool_use.py** - Can create TODOs from errors
5. **post_tool_use.py** - Can create TODOs from failures

#### Database Integration

```sql
-- TODOs created from FLAGS
SELECT * FROM todos 
WHERE context->>'$.flag_id' IS NOT NULL;

-- TODOs from Claude's TodoWrite
SELECT * FROM todos 
WHERE context->>'$.claude_id' IS NOT NULL;

-- TODOs with subtasks
SELECT * FROM todos 
WHERE subtasks_total > 0
ORDER BY subtasks_completed / subtasks_total;
```

### Real-World Example Flow

1. **User**: "Implement user authentication with tests"

2. **Claude uses TodoWrite**:
   ```
   1. Implement auth module
   1.1 Create login endpoint
   1.2 Add JWT tokens
   1.3 Write unit tests
   ```

3. **todo_sync.py captures** → Creates 4 TODOs with hierarchy

4. **Claude delegates**: "Use @test-automation-specialist for tests"

5. **task_delegation.py** → Assigns TODO 1.3 to specialist

6. **Specialist works** → Updates TODO to in_progress

7. **Tests fail** → session_end.py creates "Fix 2 failing auth tests"

8. **Next session** → Claude sees pending TODOs and continues

### Benefits Over Standard TodoWrite

| Feature | TodoWrite | Our TODO System |
|---------|-----------|-----------------|
| **Persistence** | Session only | SQLite forever |
| **Auto-sync** | ❌ | ✅ Captures all |
| **Categorization** | ❌ | ✅ AI-powered |
| **Delegation** | ❌ | ✅ To agents |
| **Dependencies** | ❌ | ✅ Tracked |
| **Subtasks** | Basic | ✅ Full hierarchy |
| **FLAGS integration** | ❌ | ✅ Auto-creates |
| **Session analysis** | ❌ | ✅ Auto-TODOs |
| **Filtering** | Basic | ✅ 15+ filters |
| **Due dates** | ❌ | ✅ With urgency |

## Available Commands

- `/save` - Save current session to database
- `/save --job [name]` - Save to specific job
- `/jobs` - View active and paused jobs
- `/todo` - Manage tasks with AI integration
- `/tools` - View tool usage analytics

## Future Enhancements

- **Memory Compression** - For memories >1MB
- **Memory Versioning** - Track all changes over time
- **Memory Sharing** - Agents share common knowledge
- **Memory Analytics** - Visualize memory usage patterns
- **Memory Export** - Generate documentation from memories
- **Chat Command** - Review past conversations from MESSAGES

---

*The SQLite memory system ensures Claude Code never forgets, always learns, and constantly improves.*