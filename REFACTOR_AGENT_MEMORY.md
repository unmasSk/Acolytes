# Refactor Agent Memory System - Implementation Guide

## Overview
Refactor the agent memory system to eliminate redundancy and use agent names directly instead of numeric IDs.

## Current Problems
1. **Redundant tables**: `acolytes` and `agents_catalog` store duplicate information
2. **Numeric agent_id**: Agents don't know their numeric ID, making memory updates difficult
3. **Complex lookups**: Need to query ID first, then use it for memory operations
4. **Phantom table**: Scripts reference table `agents` that doesn't exist (should be `agents_catalog`)
5. **Deprecated scripts**: `todo_command.py` and `compact_memory.py` were created early and never used

## Proposed Solution
- **Remove** `acolytes` table (redundant)
- **Keep** `agents_catalog` as single source of truth
- **Modify** `agents_memory` to use `agent_name` instead of `agent_id`
- **Fix** phantom references to non-existent `agents` table
- **Update** deprecated scripts to work with new schema

---

## FILES TO MODIFY

### 1. Database Schema: `acolytes/data/scripts/init_db.sql`

**REMOVE** the entire `acolytes` table creation (lines 17-24):
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

**MODIFY** `agents_memory` table (lines 60-68) - NOTE: already renamed with 's':
```sql
-- OLD VERSION (CURRENT)
CREATE TABLE IF NOT EXISTS agents_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id INTEGER NOT NULL,
    memory_type TEXT CHECK(memory_type IN ('knowledge', 'structure', 'patterns', 'interfaces', 'dependencies', 'schemas', 'quality', 'operations', 'context', 'domain', 'security', 'errors', 'performance', 'history')) NOT NULL,
    content JSON NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (agent_id) REFERENCES acolytes(id) ON DELETE CASCADE
);

-- NEW VERSION (REPLACE WITH)
CREATE TABLE IF NOT EXISTS agents_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_name TEXT NOT NULL,  -- Changed from agent_id INTEGER
    memory_type TEXT CHECK(memory_type IN ('knowledge', 'structure', 'patterns', 'interfaces', 'dependencies', 'schemas', 'quality', 'operations', 'context', 'domain', 'security', 'errors', 'performance', 'history')) NOT NULL,
    content JSON NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (agent_name) REFERENCES agents_catalog(name) ON DELETE CASCADE,
    UNIQUE(agent_name, memory_type)  -- Added unique constraint
);
```

**MODIFY** `todos` table to remove agent_id column (optional - can keep assigned_to):
```sql
-- Remove agent_id column, just use assigned_to TEXT field
-- Line ~211: Remove "agent_id INTEGER," from table definition
-- The assigned_to field already stores the agent name
```

---

### 2. Agent Database Script: `acolytes/data/scripts/agent_db.py`

**Modify `create_agent` function** (currently at lines ~139-178):
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
        # Check if agent already exists in agents_catalog (NOT acolytes table)
        cursor = conn.execute("SELECT 1 FROM agents_catalog WHERE name = ?", (name,))
        if cursor.fetchone():
            conn.close()
            return json.dumps({"error": f"Agent '{name}' already exists in agents_catalog"})
        
        # Start explicit transaction
        conn.execute("BEGIN TRANSACTION")
        
        # Insert ONLY into agents_catalog (no more acolytes table)
        conn.execute(
            "INSERT INTO agents_catalog (name, type, module, sub_module) VALUES (?, 'acolyte', ?, ?)",
            (name, module, sub_module)
        )
        
        # Insert 14 empty memory records using agent_name directly
        for memory_type in MEMORY_TYPES:
            conn.execute(
                "INSERT INTO agents_memory (agent_name, memory_type, content, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                (name, memory_type, '{}', timestamp, timestamp)  # Using name instead of agent_id
            )
        
        # Commit the transaction
        conn.commit()
        conn.close()
        
        return json.dumps({
            "success": True,
            "agent_name": name,
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

**Modify `update_memory` function** (currently at lines ~85-107):
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
    
    # Update memory directly using agent_name (no ID lookup needed)
    cursor = conn.execute(
        "UPDATE agents_memory SET content = ?, updated_at = ? WHERE agent_name = ? AND memory_type = ?",
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

**Modify `get_memory` function** (currently at lines ~108-136):
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
            "SELECT * FROM agents_memory WHERE agent_name = ? AND memory_type = ?",
            (agent_name, memory_type)
        )
    else:
        # Get all memories for agent
        cursor = conn.execute(
            "SELECT * FROM agents_memory WHERE agent_name = ? ORDER BY memory_type",
            (agent_name,)
        )
    
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    if not results:
        return json.dumps({"error": f"No memories found for agent '{agent_name}'"})
    
    return json.dumps(results, indent=2)
```

---

### 3. Todo Command Script: `acolytes/data/scripts/todo_command.py` (DEPRECATED - UPDATE)

**Fix phantom table references** - Change all references from `agents` to `agents_catalog`:
```python
# Line 53 - OLD:
cursor.execute("SELECT id FROM agents WHERE name = ?", (assigned_to,))
# NEW:
cursor.execute("SELECT name FROM agents_catalog WHERE name = ?", (assigned_to,))

# Lines 248, 306, 324 - Same change
# Line 439 - OLD:
LEFT JOIN agents a ON t.agent_id = a.id
# NEW:
LEFT JOIN agents_catalog ac ON t.assigned_to = ac.name
```

**Remove agent_id usage** - Use assigned_to field directly for agent names

---

### 4. Compact Memory Script: `acolytes/data/scripts/compact_memory.py` (DEPRECATED - UPDATE)

**Fix phantom table references**:
```python
# Line 186 - OLD:
cursor = conn.execute("SELECT id FROM agents WHERE name = ?", (agent_name,))
# NEW:
cursor = conn.execute("SELECT name FROM agents_catalog WHERE name = ?", (agent_name,))

# Line 196 - Change to agents_memory with agent_name:
cursor = conn.execute("""
    SELECT memory_type, content 
    FROM agents_memory 
    WHERE agent_name = ?
""", (agent_name,))

# Line 283 - OLD:
JOIN agents a ON h.agent_id = a.id
# NEW:
JOIN agents_catalog ac ON h.agent_name = ac.name
```

---

### 5. Acolyte Template: `acolytes/data/resources/templates/acolytes-template.md`

**Update query at line 618**:
```sql
-- OLD:
uv run python ~/.claude/scripts/agent_db.py query "SELECT name FROM acolytes WHERE module = '{{module_name}}' AND name != '{{agent-name}}'"

-- NEW:
uv run python ~/.claude/scripts/agent_db.py query "SELECT name FROM agents_catalog WHERE type = 'acolyte' AND module = '{{module_name}}' AND name != '{{agent-name}}'"
```

**Memory access examples already use agent names, so no changes needed there**

---

### 6. Claude Template: `acolytes/data/resources/templates/claude-template.md`

**Update database structure documentation**:
- Remove references to `acolytes` table
- Update to show `agents_memory` uses `agent_name` instead of `agent_id`

---

### 7. Setup Acolytes Creator: `acolytes/data/agents/setup.acolytes-creator.md`

**Update to work with new schema**:
- Agent creation should only insert into `agents_catalog`
- Memory initialization uses `agent_name` directly
- No references to `acolytes` table



---

## IMPORTANT NOTES

1. **NO EXISTING DATABASE** - This is a fresh installation, no migration needed
2. **Table name already changed** - `agent_memory` → `agents_memory` (with 's') already done
3. **Deprecated scripts** - `todo_command.py` and `compact_memory.py` were created early but never used, need updates
4. **Phantom table** - Scripts reference table `agents` that doesn't exist in schema (should be `agents_catalog`)

---

## TESTING CHECKLIST

After implementing changes:

1. [ ] Test `create-agent` command creates agent in `agents_catalog` only
2. [ ] Test `update-memory` works with agent name
3. [ ] Test `get-memory` retrieves memories by name
4. [ ] Verify no references to `acolytes` table remain
5. [ ] Verify no references to numeric `agent_id` remain in agents_memory
6. [ ] Test setup.acolytes-creator creates agents correctly
7. [ ] Update todo_command.py if planning to use it
8. [ ] Update compact_memory.py if planning to use it

---

## SUMMARY OF CHANGES

### Database Schema Changes:
1. **Remove** `acolytes` table entirely
2. **Modify** `agents_memory` to use `agent_name` instead of `agent_id`
3. **Optional** - Remove `agent_id` from `todos` table (already has `assigned_to`)

### Code Changes Required:
1. **agent_db.py** - Create agents only in `agents_catalog`, use `agent_name` for memories
2. **todo_command.py** - Fix phantom `agents` table references → `agents_catalog`
3. **compact_memory.py** - Fix phantom `agents` table references → `agents_catalog`
4. **acolytes-template.md** - Update SQL query to use `agents_catalog`
5. **claude-template.md** - Update documentation
6. **setup.acolytes-creator.md** - Ensure it uses new schema
7. **setup.md** - NO CHANGES NEEDED (delegates to setup.acolytes-creator)

---

## Expected Benefits

1. **Simpler**: One table for all agents, one table for memories
2. **Clearer**: Agents use their name directly, no ID lookups
3. **Maintainable**: Less code, fewer joins, easier to understand
4. **Future-proof**: Agents can easily access their own memories