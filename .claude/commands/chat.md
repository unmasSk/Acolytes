---
command: chat
description: 💬 Review past conversation summaries. Usage: /chat or /chat [number]
---

# Chat Command

Review detailed conversation summaries from past sessions using MCP SQLite.

## Usage

```bash
/chat          # List last 5 sessions with numbers
/chat 3        # Show detailed conversation flow from session #3
```

## EXECUTION RULES

**CRITICAL**: When this command is invoked:

1. DO NOT explain what you're doing
2. Execute MCP operations SILENTLY
3. Return ONLY the formatted output
4. Use clean formatting with emojis

## Implementation Instructions

### /chat (no parameters)

When user types `/chat`, execute via MCP:

1. Query via `mcp__MCP_SQLite_Server__query`:

```sql
SELECT
    ROW_NUMBER() OVER (ORDER BY s.created_at DESC) as num,
    s.id,
    s.job_id,
    s.title,
    s.created_at,
    m.total_exchanges,
    m.duration_minutes
FROM sessions s
LEFT JOIN messages m ON s.id = m.session_id
ORDER BY s.created_at DESC
LIMIT 5
```

2. Format output as:

```
💬 RECENT SESSIONS
==================

1. SQLite migration and hook cleanup
   Job: migration-sqlite
   Date: 2025-08-17 14:30
   Exchanges: 45
   Duration: 80 min

2. Command implementation review
   Job: work-20250817
   Date: 2025-08-17 10:15
   Exchanges: 23
   Duration: 35 min

Use /chat [number] to view full conversation
```

### /chat [number]

When user types `/chat 3`, execute:

1. Get the session by position:

```sql
WITH numbered_sessions AS (
    SELECT s.*, ROW_NUMBER() OVER (ORDER BY s.created_at DESC) as num
    FROM sessions s
)
SELECT * FROM numbered_sessions WHERE num = 3
```

2. Get conversation flow:

```sql
SELECT conversation_flow, total_exchanges, duration_minutes
FROM messages WHERE session_id = [session_id from step 1]
```

3. Format output as:

```
💬 SESSION #3: [Title]
=====================
Job: [job_id]
Date: [created_at]
Duration: [duration] minutes
Exchanges: [total]

📝 CONVERSATION FLOW:
--------------------
[conversation_flow text]

📊 SESSION METRICS:
- Quality Score: [score]/10
- Bugs Fixed: [count]
- Tasks Completed: [count from accomplishments]
```

## Python Fallback (only if MCP unavailable)

```python
import sqlite3
import json
from pathlib import Path

DB_PATH = Path(".claude/memory/project.db")

if not DB_PATH.exists():
    print("❌ Database not found")
    exit(1)

conn = sqlite3.connect(str(DB_PATH))
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Get last 5 sessions that have saved messages
cursor.execute("""
    SELECT
        ROW_NUMBER() OVER (ORDER BY s.created_at DESC) as num,
        s.id,
        s.job_id,
        s.title,
        s.created_at,
        s.ended_at,
        m.total_exchanges,
        m.duration_minutes
    FROM sessions s
    LEFT JOIN messages m ON s.id = m.session_id
    ORDER BY s.created_at DESC
    LIMIT 5
""")

sessions = cursor.fetchall()

if not sessions:
    print("No sessions found in database")
    conn.close()
    exit(0)

print("=" * 60)
print("💬 RECENT SESSIONS")
print("=" * 60)

for session in sessions:
    # Format display
    num = session['num']
    title = session['title'] or "Untitled Session"
    job = session['job_id']
    date = session['created_at']

    print(f"\n{num}. {title}")
    print(f"   Job: {job}")
    print(f"   Date: {date}")

    if session['total_exchanges']:
        print(f"   Exchanges: {session['total_exchanges']}")
    if session['duration_minutes']:
        print(f"   Duration: {session['duration_minutes']} min")

    # Check if messages exist
    if not session['total_exchanges']:
        print("   ⚠️ No conversation summary saved")

print("\n" + "=" * 60)
print("Use /chat [number] to view full conversation flow")

conn.close()
```

### Step 2: Show Specific Session

When user types `/chat 3`:

```python
import sys

# Parse the number from command
if len(sys.argv) < 2:
    print("Usage: /chat [number]")
    exit(1)

try:
    selection = int(sys.argv[1])
except ValueError:
    print("❌ Please provide a valid number")
    exit(1)

conn = sqlite3.connect(str(DB_PATH))
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Get the Nth most recent session
cursor.execute("""
    WITH numbered_sessions AS (
        SELECT
            ROW_NUMBER() OVER (ORDER BY created_at DESC) as num,
            id
        FROM sessions
        ORDER BY created_at DESC
        LIMIT 5
    )
    SELECT
        s.*,
        m.conversation_flow,
        m.total_exchanges,
        m.duration_minutes
    FROM numbered_sessions ns
    JOIN sessions s ON ns.id = s.id
    LEFT JOIN messages m ON s.id = m.session_id
    WHERE ns.num = ?
""", (selection,))

result = cursor.fetchone()

if not result:
    print(f"❌ Session #{selection} not found")
    conn.close()
    exit(1)

# Display session header
print("=" * 70)
print(f"📝 SESSION: {result['title'] or 'Untitled'}")
print("=" * 70)
print(f"Session ID: {result['id']}")
print(f"Job: {result['job_id']}")
print(f"Date: {result['created_at']} to {result['ended_at'] or 'ongoing'}")

if result['quality_score']:
    print(f"Quality Score: {result['quality_score']}/10")

# Display accomplishments
if result['accomplishments']:
    accomplishments = json.loads(result['accomplishments'])
    if accomplishments:
        print(f"\n✅ ACCOMPLISHMENTS ({len(accomplishments)}):")
        for acc in accomplishments:
            print(f"   • {acc}")

# Display decisions
if result['decisions']:
    decisions = json.loads(result['decisions'])
    if decisions:
        print(f"\n📋 DECISIONS ({len(decisions)}):")
        for dec in decisions:
            print(f"   • {dec}")

# Display bugs fixed
if result['bugs_fixed']:
    bugs = json.loads(result['bugs_fixed'])
    if bugs:
        print(f"\n🐛 BUGS FIXED ({len(bugs)}):")
        for bug in bugs:
            print(f"   • {bug}")

# Display errors
if result['errors_encountered']:
    errors = json.loads(result['errors_encountered'])
    if errors:
        print(f"\n❌ ERRORS ENCOUNTERED ({len(errors)}):")
        for err in errors:
            print(f"   • {err}")

# Display breakthrough
if result['breakthrough_moment']:
    print(f"\n💡 BREAKTHROUGH:")
    print(f"   {result['breakthrough_moment']}")

# Display next priority
if result['next_session_priority']:
    print(f"\n🎯 NEXT PRIORITY:")
    print(f"   {result['next_session_priority']}")

# Display conversation flow if available
if result['conversation_flow']:
    print("\n" + "=" * 70)
    print("💬 CONVERSATION FLOW")
    print("=" * 70)
    print(result['conversation_flow'])
else:
    print("\n⚠️ No detailed conversation summary available for this session")
    print("Conversation summaries are saved when using /save command")

# Display pending tasks
if result['pending']:
    pending = json.loads(result['pending'])
    if pending:
        print("\n" + "=" * 70)
        print(f"⏳ PENDING TASKS ({len(pending)}):")
        for task in pending:
            print(f"   • {task}")

conn.close()
```

## Features

### What This Command Shows

1. **Session List** (`/chat`):

   - Last 5 sessions numbered for easy selection
   - Basic info: title, job, date
   - Indicates if conversation summary exists

2. **Session Details** (`/chat [num]`):
   - Full session information from SESSIONS table
   - Conversation flow from MESSAGES table (if saved)
   - All accomplishments, decisions, bugs, errors
   - Breakthrough moments and next priorities

### Important Notes

- **MESSAGES is optional**: Not all sessions will have conversation_flow saved
- **Numbering is dynamic**: Session #1 is always the most recent
- **Read-only operation**: This command only reads, never modifies data
- **Context preservation**: Helps recover lost context or review past work

## Error Handling

- Database not found → Clear error message
- Invalid number → Usage instructions
- Session not found → Helpful error
- No messages saved → Indicates data not available

## Future Enhancements

- Search by job: `/chat --job migration-sqlite`
- Search by date: `/chat --date 2025-08-16`
- Export to markdown: `/chat 3 --export`
- Full text search: `/chat --search "breakthrough"`

---

_Command created for ClaudeSquad conversation review system_
_Version: 1.0_
