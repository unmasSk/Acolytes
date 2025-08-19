---
command: db
description: 🗄️ Database operations via MCP. Params: tables, stats, doctor, query ["SQL"]
---

# Database Command

Direct database operations using MCP SQLite Server. Returns formatted output without explanations.

## Usage

```bash
/db             # Database overview (default)
/db tables      # List all tables
/db doctor      # Run diagnostics and repairs
/db stats       # Database statistics
/db query SQL   # Execute raw SQL
```

## EXECUTION RULES

**CRITICAL**: When this command is invoked:

1. DO NOT explain what you're doing
2. DO NOT use phrases like "Let me..." or "I'll check..."
3. Execute MCP operations SILENTLY
4. Return ONLY the formatted output
5. Use tables, boxes, and emojis for visual clarity

## Implementation Instructions

### /db (no arguments)

When user runs `/db` with no arguments, show database overview:

1. `mcp__MCP_SQLite_Server__db_info()` for database metadata
2. `mcp__MCP_SQLite_Server__query` to count records in each table
3. Query for active items (jobs, todos, flags)

Expected output format:

```
📊 DATABASE OVERVIEW
====================
📁 Path: project.db
💾 Size: 272.0 KB
📅 Modified: Sun Aug 17 2025 15:33:05
📋 Tables: 9

📈 RECORD COUNTS
================
agents          2 records
agent_memory    16 records
jobs            1 record
sessions        2 records
tool_logs       350 records ⚠️
messages        3 records
flags           2 records
agent_health    3 records
todos           12 records

🔥 ACTIVE ITEMS
===============
✓ Active Jobs: 1
✓ Pending TODOs: 11
✓ Pending Flags: 1
```

### /db tables

When user runs `/db tables`, execute:

1. `mcp__MCP_SQLite_Server__list_tables()` to get all tables
2. For each table, run `mcp__MCP_SQLite_Server__query` with `SELECT COUNT(*) FROM [table]`
3. Format output as clean ASCII table

Expected output format:

```
📊 DATABASE TABLES
==================
agents          (77 records)
sessions        (45 records)
todos           (23 records)
messages        (12 records)
flags           (8 records)
```

### /db stats

When user runs `/db stats`, execute multiple MCP queries to gather:

- Database info via `mcp__MCP_SQLite_Server__db_info()`
- Record counts for each table
- Active items (pending todos, active jobs, etc.)

Expected output format:

```
📊 DATABASE STATISTICS
======================
Database: project.db
Size: 145 KB
Tables: 13

RECORD COUNTS:
  agents: 77
  sessions: 45
  todos: 23

ACTIVE ITEMS:
  Active Jobs: 2
  Pending TODOs: 8
  Pending Flags: 3
```

### /db doctor

When user runs `/db doctor`, execute these checks:

1. `mcp__MCP_SQLite_Server__query` with `PRAGMA integrity_check`
2. Check all required tables exist
3. Look for orphaned records
4. If issues found, fix them and report

Expected output format:

```
🏥 DATABASE DOCTOR
==================
✅ Integrity check: OK
✅ Required tables: 13/13 present
⚠️  Orphaned records: 3 found and fixed
✅ Database optimized

Diagnosis complete!
```

### /db query "SQL"

When user runs `/db query "SQL"`, execute:

1. `mcp__MCP_SQLite_Server__query` with the provided SQL
2. Format results as table
3. Limit display to 20 rows if more

## Python Fallback (if MCP fails)

Only use this if MCP is not available:

```python
import sqlite3
from pathlib import Path

DB_PATH = Path(".claude/memory/project.db")

if not DB_PATH.exists():
    print("❌ Database not found")
    exit(1)

conn = sqlite3.connect(str(DB_PATH))
cursor = conn.cursor()

cursor.execute("""
    SELECT name, type
    FROM sqlite_master
    WHERE type IN ('table', 'view')
    AND name NOT LIKE 'sqlite_%'
    ORDER BY type, name
""")

results = cursor.fetchall()

print("=" * 50)
print("📊 DATABASE TABLES & VIEWS")
print("=" * 50)

for name, obj_type in results:
    icon = "📋" if obj_type == "table" else "👁️"
    print(f"{icon} {name}")

conn.close()
```

### /db stats

Show database statistics:

```python
import sqlite3
from pathlib import Path
import os

DB_PATH = Path(".claude/memory/project.db")

if not DB_PATH.exists():
    print("❌ Database not found")
    exit(1)

conn = sqlite3.connect(str(DB_PATH))
cursor = conn.cursor()

# Gather statistics
stats = {}

# Count records in each table
tables = ['agents', 'agent_memory', 'jobs', 'sessions', 'messages', 'flags', 'todos']
for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    stats[table] = cursor.fetchone()[0]

# Special queries
cursor.execute("SELECT COUNT(*) FROM jobs WHERE status = 'active'")
stats['active_jobs'] = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM flags WHERE status = 'pending'")
stats['pending_flags'] = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM todos WHERE status = 'pending'")
stats['pending_todos'] = cursor.fetchone()[0]

# Database size
db_size = os.path.getsize(DB_PATH) / 1024  # KB

print("=" * 50)
print("📊 DATABASE STATISTICS")
print("=" * 50)
print(f"Database: project.db")
print(f"Size: {db_size:.1f} KB")
print()
print("RECORD COUNTS:")
for table in tables:
    print(f"  {table}: {stats[table]}")
print()
print("ACTIVE ITEMS:")
print(f"  Active Jobs: {stats['active_jobs']}")
print(f"  Pending Flags: {stats['pending_flags']}")
print(f"  Pending TODOs: {stats['pending_todos']}")

# Recent activity
cursor.execute("""
    SELECT COUNT(*) as sessions_today
    FROM sessions
    WHERE date(created_at) = date('now', 'localtime')
""")
today_sessions = cursor.fetchone()[0]
print(f"  Sessions Today: {today_sessions}")

conn.close()
```

### /db doctor

Diagnose and repair database issues:

```python
import sqlite3
from pathlib import Path
import sys

DB_PATH = Path(".claude/memory/project.db")

print("=" * 60)
print("🏥 DATABASE DOCTOR")
print("=" * 60)

# Check if database exists
if not DB_PATH.exists():
    print("❌ Database not found at .claude/memory/project.db")
    print("   Creating new database...")

    # Run init_db.sql to create database
    init_sql = Path(".claude/scripts/init_db.sql")
    if init_sql.exists():
        conn = sqlite3.connect(str(DB_PATH))
        with open(init_sql, 'r') as f:
            conn.executescript(f.read())
        conn.close()
        print("✅ Database created successfully")
    else:
        print("❌ init_db.sql not found")
        exit(1)
else:
    print("✅ Database file exists")

# Connect and run diagnostics
conn = sqlite3.connect(str(DB_PATH))
cursor = conn.cursor()
issues = []
fixed = []

try:
    # 1. Check integrity
    cursor.execute("PRAGMA integrity_check")
    result = cursor.fetchone()[0]
    if result != "ok":
        issues.append(f"Integrity check failed: {result}")
        cursor.execute("VACUUM")
        fixed.append("Ran VACUUM to fix integrity")
    else:
        print("✅ Database integrity OK")

    # 2. Check required tables
    required_tables = [
        'agents', 'agent_memory', 'jobs', 'sessions',
        'messages', 'flags', 'agent_health', 'tool_logs', 'todos'
    ]

    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
    """)
    existing_tables = [row[0] for row in cursor.fetchall()]

    missing_tables = set(required_tables) - set(existing_tables)
    if missing_tables:
        issues.append(f"Missing tables: {', '.join(missing_tables)}")

        # Try to create missing tables from init_db.sql
        init_sql = Path(".claude/scripts/init_db.sql")
        if init_sql.exists():
            with open(init_sql, 'r') as f:
                sql_content = f.read()
                for table in missing_tables:
                    # Extract CREATE TABLE statement for this table
                    import re
                    pattern = f"CREATE TABLE IF NOT EXISTS {table}.*?;\\s*(?=CREATE|--|$)"
                    match = re.search(pattern, sql_content, re.DOTALL | re.IGNORECASE)
                    if match:
                        try:
                            conn.executescript(match.group(0))
                            fixed.append(f"Created missing table: {table}")
                        except:
                            pass
    else:
        print(f"✅ All {len(required_tables)} required tables present")

    # 3. Check for orphaned records
    # Sessions without jobs
    cursor.execute("""
        SELECT COUNT(*) FROM sessions
        WHERE job_id NOT IN (SELECT id FROM jobs)
        AND job_id IS NOT NULL
    """)
    orphaned_sessions = cursor.fetchone()[0]
    if orphaned_sessions > 0:
        issues.append(f"Found {orphaned_sessions} orphaned sessions")
        cursor.execute("""
            UPDATE sessions SET job_id = NULL
            WHERE job_id NOT IN (SELECT id FROM jobs)
        """)
        fixed.append(f"Fixed {orphaned_sessions} orphaned sessions")

    # Messages without sessions
    cursor.execute("""
        SELECT COUNT(*) FROM messages
        WHERE session_id NOT IN (SELECT id FROM sessions)
    """)
    orphaned_messages = cursor.fetchone()[0]
    if orphaned_messages > 0:
        issues.append(f"Found {orphaned_messages} orphaned messages")
        cursor.execute("""
            DELETE FROM messages
            WHERE session_id NOT IN (SELECT id FROM sessions)
        """)
        fixed.append(f"Removed {orphaned_messages} orphaned messages")

    # 4. Check indexes
    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='index' AND name NOT LIKE 'sqlite_%'
    """)
    indexes = [row[0] for row in cursor.fetchall()]

            'idx_agent_memory': 'CREATE INDEX idx_agent_memory ON agent_memory(agent_id, memory_type)',
            'idx_sessions_time': 'CREATE INDEX idx_sessions_time ON sessions(datetime(created_at) DESC)',
            'idx_flags_pending': "CREATE INDEX idx_flags_pending ON flags(status) WHERE status = 'pending'",
            'idx_tool_logs_session': 'CREATE INDEX idx_tool_logs_session ON tool_logs(session_id, timestamp)'
        }
    missing_indexes = set(required_indexes) - set(indexes)
    if missing_indexes:
        issues.append(f"Missing indexes: {', '.join(missing_indexes)}")
        # Recreate missing indexes
        index_sql = {
            'idx_agent_memory': 'CREATE INDEX idx_agent_memory ON agent_memory(agent_id, memory_type)',
            'idx_sessions_time': 'CREATE INDEX idx_sessions_time ON sessions(datetime(created_at) DESC)',
            'idx_flags_pending': 'CREATE INDEX idx_flags_pending ON flags(status) WHERE status = "pending"',
            'idx_tool_logs_session': 'CREATE INDEX idx_tool_logs_session ON tool_logs(session_id, timestamp)'
        }
        for idx in missing_indexes:
            if idx in index_sql:
                try:
                    cursor.execute(index_sql[idx])
                    fixed.append(f"Created index: {idx}")
                except:
                    pass
    else:
        print(f"✅ All required indexes present")

    # 5. Database size and optimization
    cursor.execute("PRAGMA page_count")
    page_count = cursor.fetchone()[0]
    cursor.execute("PRAGMA page_size")
    page_size = cursor.fetchone()[0]
    db_size = (page_count * page_size) / 1024  # KB

    cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
    table_count = cursor.fetchone()[0]

    print(f"📊 Database size: {db_size:.1f} KB")
    print(f"📊 Total tables: {table_count}")

    # Run optimization if database is fragmented
    cursor.execute("PRAGMA freelist_count")
    freelist = cursor.fetchone()[0]
    if freelist > 100:
        cursor.execute("VACUUM")
        fixed.append(f"Optimized database (freed {freelist} pages)")

    # Commit all fixes
    conn.commit()

    # Report results
    print()
    if issues:
        print(f"🔍 Found {len(issues)} issues:")
        for issue in issues:
            print(f"   ⚠️ {issue}")
    else:
        print("✅ No issues found")

    if fixed:
        print(f"\n🔧 Fixed {len(fixed)} issues:")
        for fix in fixed:
            print(f"   ✅ {fix}")

    print("\n🏥 Diagnosis complete!")

except Exception as e:
    print(f"❌ Error during diagnosis: {e}")
    issues.append(str(e))
finally:
    conn.close()

# Exit with error code if issues remain unfixed
if len(issues) > len(fixed):
    exit(1)
```

### /db query "SQL"

Execute a read-only SQL query:

```python
import sqlite3
from pathlib import Path
import json
import sys

if len(sys.argv) < 2:
    print("Usage: /db query \"SELECT * FROM table\"")
    exit(1)

sql_query = sys.argv[1]

# Safety check - only allow SELECT queries
if not sql_query.strip().upper().startswith('SELECT'):
    print("❌ Only SELECT queries are allowed")
    exit(1)

DB_PATH = Path(".claude/memory/project.db")

if not DB_PATH.exists():
    print("❌ Database not found")
    exit(1)

try:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(sql_query)
    results = cursor.fetchall()

    if not results:
        print("No results found")
    else:
        # Convert to list of dicts for display
        data = []
        for row in results[:20]:  # Limit to 20 rows for display
            data.append(dict(row))

        # Display results
        if data:
            # Get column names
            columns = list(data[0].keys())

            # Print header
            print("=" * 70)
            print(" | ".join(columns[:5]))  # Show first 5 columns
            print("=" * 70)

            # Print rows
            for row in data:
                values = []
                for col in columns[:5]:
                    val = str(row[col])[:15]  # Truncate long values
                    values.append(val)
                print(" | ".join(values))

        if len(results) > 20:
            print(f"... and {len(results) - 20} more rows")

    conn.close()

except sqlite3.Error as e:
    print(f"❌ Query error: {e}")
    exit(1)
```

## Examples

```bash
# View all tables
/db tables

# Get statistics
/db stats

# Custom queries
/db query "SELECT * FROM jobs WHERE status = 'active'"
/db query "SELECT id, title FROM sessions ORDER BY created_at DESC LIMIT 5"
/db query "SELECT COUNT(*) as total FROM agents"
```

## Safety Notes

- Only SELECT queries are allowed (read-only)
- Use agent_db.py for write operations
- Database path: `.claude/memory/project.db`

---

_Command created for ClaudeSquad SQLite database management_
