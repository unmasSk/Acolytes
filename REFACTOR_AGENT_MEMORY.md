# Refactor Agent Memory System - Implementation Guide

## Overview
Refactor the agent memory system to eliminate redundancy and use agent names directly instead of numeric IDs.

## Current Problems
1. **Redundant tables**: `acolytes` and `agents_catalog` store duplicate information
2. **Numeric agent_id**: Agents don't know their numeric ID, making memory updates difficult
3. **Complex lookups**: Need to query ID first, then use it for memory operations

## Proposed Solution
- **Remove** `acolytes` table (redundant)
- **Keep** `agents_catalog` as single source of truth
- **Modify** `agent_memory` to use `agent_name` instead of `agent_id`

---

## FILES TO MODIFY

### 1. Database Schema: `acolytes/data/scripts/init_db.sql`

**REMOVE** the entire `acolytes` table creation (lines ~22-29):
```sql
-- DELETE THIS ENTIRE BLOCK
CREATE TABLE IF NOT EXISTS acolytes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    module TEXT NOT NULL,
    sub_module TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT
);
```

**MODIFY** `agent_memory` table (lines ~60-75):
```sql
-- OLD VERSION (REMOVE)
CREATE TABLE IF NOT EXISTS agent_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id INTEGER NOT NULL,
    memory_type TEXT CHECK(...) NOT NULL,
    content TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (agent_id) REFERENCES acolytes (id) ON DELETE CASCADE,
    UNIQUE(agent_id, memory_type)
);

-- NEW VERSION (REPLACE WITH)
CREATE TABLE IF NOT EXISTS agent_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_name TEXT NOT NULL,  -- Changed from agent_id INTEGER
    memory_type TEXT CHECK(memory_type IN ('knowledge', 'structure', 'patterns', 'interfaces', 'dependencies', 'schemas', 'quality', 'operations', 'context', 'domain', 'security', 'errors', 'performance', 'history')) NOT NULL,
    content TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (agent_name) REFERENCES agents_catalog(name) ON DELETE CASCADE,
    UNIQUE(agent_name, memory_type)  -- Changed from agent_id
);
```

**ADD** migration for existing databases (at end of file):
```sql
-- Migration: Convert existing agent_memory from agent_id to agent_name
-- This will be run manually when needed
/*
-- Step 1: Create new table with correct schema
CREATE TABLE agent_memory_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_name TEXT NOT NULL,
    memory_type TEXT CHECK(memory_type IN ('knowledge', 'structure', 'patterns', 'interfaces', 'dependencies', 'schemas', 'quality', 'operations', 'context', 'domain', 'security', 'errors', 'performance', 'history')) NOT NULL,
    content TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (agent_name) REFERENCES agents_catalog(name) ON DELETE CASCADE,
    UNIQUE(agent_name, memory_type)
);

-- Step 2: Copy data with name lookup
INSERT INTO agent_memory_new (agent_name, memory_type, content, created_at, updated_at)
SELECT ac.name, am.memory_type, am.content, am.created_at, am.updated_at
FROM agent_memory am
JOIN acolytes a ON am.agent_id = a.id
JOIN agents_catalog ac ON ac.name = a.name;

-- Step 3: Drop old table and rename new
DROP TABLE agent_memory;
ALTER TABLE agent_memory_new RENAME TO agent_memory;

-- Step 4: Drop redundant acolytes table
DROP TABLE acolytes;
*/
```

---

### 2. Agent Database Script: `acolytes/data/scripts/agent_db.py`

**Line 170-220** - Modify `create_agent` function:
```python
def create_agent(name, module=None, sub_module=None):
    """Create agent with 14 empty memory records and add to agents_catalog"""
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    # Ensure name starts with @
    if not name.startswith('@'):
        name = '@' + name
    
    # Module is required for acolytes
    if not module:
        conn.close()
        return json.dumps({"error": "Module parameter is required for acolytes"})
    
    try:
        # Check if agent already exists in agents_catalog
        cursor = conn.execute("SELECT 1 FROM agents_catalog WHERE name = ?", (name,))
        if cursor.fetchone():
            conn.close()
            return json.dumps({"error": f"Agent '{name}' already exists in agents_catalog"})
        
        # Start explicit transaction
        conn.execute("BEGIN TRANSACTION")
        
        # Insert into agents_catalog (single source of truth)
        conn.execute(
            "INSERT INTO agents_catalog (name, type, module, sub_module, created_at) VALUES (?, 'acolyte', ?, ?, ?)",
            (name, module, sub_module, timestamp)
        )
        
        # Insert 14 empty memory records using agent name directly
        for memory_type in MEMORY_TYPES:
            conn.execute(
                "INSERT INTO agent_memory (agent_name, memory_type, content, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                (name, memory_type, '{}', timestamp, timestamp)  # Using name instead of agent_id
            )
        
        # Commit the transaction
        conn.commit()
        conn.close()
        
        return json.dumps({
            "success": True,
            "agent_name": name,  # Changed from agent_id
            "module": module,
            "sub_module": sub_module,
            "memories_created": 14,
            "catalog_entry": "created"
        })
        
    except sqlite3.IntegrityError as e:
        conn.rollback()
        conn.close()
        return json.dumps({"error": f"Database integrity error: {str(e)}"})
    except Exception as e:
        conn.rollback()
        conn.close()
        return json.dumps({"error": f"Failed to create agent: {str(e)}"})
```

**Lines 80-120** - Modify `update_memory` function:
```python
def update_memory(agent_name, memory_type, content):
    """Update specific memory for an agent using agent name"""
    if memory_type not in MEMORY_TYPES:
        return json.dumps({"error": f"Invalid memory_type. Must be one of: {MEMORY_TYPES}"})
    
    # Ensure agent_name starts with @
    if not agent_name.startswith('@'):
        agent_name = '@' + agent_name
    
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    # Update memory directly using agent_name
    cursor = conn.execute(
        "UPDATE agent_memory SET content = ?, updated_at = ? WHERE agent_name = ? AND memory_type = ?",
        (content, timestamp, agent_name, memory_type)
    )
    
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    
    if affected == 0:
        return json.dumps({"error": f"No memory found for agent '{agent_name}' with type '{memory_type}'"})
    
    return json.dumps({
        "success": True,
        "agent": agent_name,
        "memory_type": memory_type,
        "updated_at": timestamp
    })
```

**Lines 120-140** - Modify `get_memory` function:
```python
def get_memory(agent_name, memory_type=None):
    """Get memory content for an agent using agent name"""
    # Ensure agent_name starts with @
    if not agent_name.startswith('@'):
        agent_name = '@' + agent_name
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    if memory_type:
        if memory_type not in MEMORY_TYPES:
            conn.close()
            return json.dumps({"error": f"Invalid memory_type. Must be one of: {MEMORY_TYPES}"})
        
        cursor = conn.execute(
            "SELECT * FROM agent_memory WHERE agent_name = ? AND memory_type = ?",
            (agent_name, memory_type)
        )
    else:
        # Get all memories for agent
        cursor = conn.execute(
            "SELECT * FROM agent_memory WHERE agent_name = ? ORDER BY memory_type",
            (agent_name,)
        )
    
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    if not results:
        return json.dumps({"error": f"No memories found for agent '{agent_name}'"})
    
    return json.dumps(results, indent=2)
```

---

### 3. Acolyte Template: `~/.claude/resources/templates/acolytes-template.md`

**Add section explaining how to access memories** (around line 900):
```markdown
## Accessing Your Memories

To read or update your memories, use your agent name directly:

```bash
# Read a specific memory
uv run python ~/.claude/scripts/agent_db.py get-memory "{{agent-name}}" "knowledge"

# Update a memory
uv run python ~/.claude/scripts/agent_db.py update-memory "{{agent-name}}" "knowledge" '{"learned": "something new"}'

# Read all your memories
uv run python ~/.claude/scripts/agent_db.py get-memory "{{agent-name}}"
```

You don't need to know your numeric ID - just use your name!
```

---

### 4. Setup Command: `acolytes/data/commands/setup.md`

**Phase 6** - Update references to remove acolytes table mentions:
```markdown
# OLD TEXT (around line 500)
"Creating agent in database (acolytes + agent_memory + agents_catalog)..."

# NEW TEXT
"Creating agent in database (agents_catalog + agent_memory)..."
```

---

### 5. Todo Command Script: `acolytes/data/scripts/todo_command.py`

**Lines 46-69** - Change agent_id assignment:
```python
# OLD
agent_id = None
if '@' in task:
    match = re.search(r'@(\S+)', task)
    if match:
        assigned_to = match.group(1)
        cursor.execute("SELECT id FROM agents WHERE name = ?", (f"@{assigned_to}",))
        agent = cursor.fetchone()
        if agent:
            agent_id = agent[0]

# NEW
# Just use agent_name directly, no ID needed
if '@' in task:
    match = re.search(r'@(\S+)', task)
    if match:
        assigned_to = f"@{match.group(1)}"  # Store full name with @
```

**Update INSERT statement** (remove agent_id column):
```python
# Remove agent_id from todos table and queries
```

---

### 6. Memory Compaction Script: `acolytes/data/scripts/compact_memory.py`

**Lines 184-198** - Use agent_name instead of ID lookup:
```python
# OLD
cursor = conn.execute("SELECT id FROM agents WHERE name = ?", (agent_name,))
agent = cursor.fetchone()
if not agent:
    return {"error": f"Agent '{agent_name}' not found"}
agent_id = agent['id']

cursor = conn.execute("""
    SELECT memory_type, content 
    FROM agent_memory 
    WHERE agent_id = ?
""", (agent_id,))

# NEW
cursor = conn.execute("""
    SELECT memory_type, content 
    FROM agent_memory 
    WHERE agent_name = ?
""", (agent_name,))
```

**All UPDATE statements** - Replace agent_id with agent_name:
```python
# OLD: WHERE agent_id = ?
# NEW: WHERE agent_name = ?
```

---

### 7. CLAUDE.md Files (both in huellaCarbono and main project)

**Update database structure section**:
```markdown
# OLD
| Table              | Purpose                | Key Fields                                            |
| ------------------ | ---------------------- | ----------------------------------------------------- |
| **acolytes**       | Dynamic project agents | name, module, sub_module                              |
| **agent_memory**   | 14 memories per agent  | agent_id, memory_type, content (JSON)                 |

# NEW
| Table              | Purpose                | Key Fields                                            |
| ------------------ | ---------------------- | ----------------------------------------------------- |
| **agent_memory**   | 14 memories per agent  | agent_name, memory_type, content (JSON)               |
| **agents_catalog** | All agents (includes acolytes) | name, type='acolyte', module, sub_module         |
```

---

## TESTING CHECKLIST

After implementing changes:

1. [ ] Backup existing databases
2. [ ] Run migration script on test database
3. [ ] Test `create-agent` command creates agent correctly
4. [ ] Test `update-memory` works with agent name
5. [ ] Test `get-memory` retrieves memories by name
6. [ ] Verify no references to `acolytes` table remain
7. [ ] Verify no references to numeric `agent_id` remain
8. [ ] Test setup.md Phase 6 creates agents correctly
9. [ ] Verify existing agents still work after migration

---

## MIGRATION SCRIPT

Save as `migrate_agent_memory.sql` and run on existing databases:

```sql
-- Backup first!
-- sqlite3 .claude/memory/project.db ".backup project_backup.db"

BEGIN TRANSACTION;

-- Create new agent_memory table
CREATE TABLE agent_memory_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_name TEXT NOT NULL,
    memory_type TEXT CHECK(memory_type IN ('knowledge', 'structure', 'patterns', 'interfaces', 'dependencies', 'schemas', 'quality', 'operations', 'context', 'domain', 'security', 'errors', 'performance', 'history')) NOT NULL,
    content TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (agent_name) REFERENCES agents_catalog(name) ON DELETE CASCADE,
    UNIQUE(agent_name, memory_type)
);

-- Migrate data
INSERT INTO agent_memory_new (agent_name, memory_type, content, created_at, updated_at)
SELECT a.name, am.memory_type, am.content, am.created_at, am.updated_at
FROM agent_memory am
JOIN acolytes a ON am.agent_id = a.id;

-- Replace old table
DROP TABLE agent_memory;
ALTER TABLE agent_memory_new RENAME TO agent_memory;

-- Remove redundant table
DROP TABLE acolytes;

COMMIT;
```

---

## ROLLBACK PLAN

If something goes wrong:

1. Restore from backup: `sqlite3 .claude/memory/project.db ".restore project_backup.db"`
2. Revert code changes in git
3. Document issues encountered

---

## Expected Benefits

1. **Simpler**: One table for all agents, one table for memories
2. **Clearer**: Agents use their name directly, no ID lookups
3. **Maintainable**: Less code, fewer joins, easier to understand
4. **Future-proof**: Agents can easily access their own memories