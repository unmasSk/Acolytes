---
command: jobs
description: 📊 View jobs status. Params: --list (show all history)
---

# Jobs Command

View current jobs and their status using MCP SQLite.

## Usage

```
/jobs         # Show active and paused jobs
/jobs --list  # Show ALL jobs (including completed)
```

## EXECUTION RULES

**CRITICAL**: When this command is invoked:

1. DO NOT explain what you're doing
2. Execute MCP operations SILENTLY
3. Return ONLY the formatted output
4. Use clean formatting with emojis

## Implementation Instructions

### /jobs (default)

When user types `/jobs`, execute via MCP:

1. Get active job:

```sql
SELECT j.*,
       COUNT(DISTINCT s.id) as session_count,
       MAX(s.created_at) as last_session
FROM jobs j
LEFT JOIN sessions s ON j.id = s.job_id
WHERE j.status = 'active'
GROUP BY j.id
```

2. Get last session priority:

```sql
SELECT next_session_priority, pending
FROM sessions
WHERE job_id = [active_job_id]
ORDER BY created_at DESC
LIMIT 1
```

3. Get paused jobs:

```sql
SELECT j.*, COUNT(DISTINCT s.id) as sessions
FROM jobs j
LEFT JOIN sessions s ON j.id = s.job_id
WHERE j.status = 'paused'
GROUP BY j.id
ORDER BY j.paused_at DESC
```

Expected output:

```
🚀 ACTIVE JOB: migration-sqlite
================================
Sessions: 5
Started: 2025-08-15 09:00
🎯 Priority: Test complete /setup flow
⏳ Pending: 3 tasks

⏸️ PAUSED JOBS:
• refactor-auth (2 sessions)
  Reason: Waiting for design approval
• api-v2 (8 sessions)
```

### /jobs --list

When user types `/jobs --list`, execute:

1. Get all jobs with stats:

```sql
SELECT
    j.*,
    COUNT(DISTINCT s.id) as session_count,
    COUNT(DISTINCT CASE WHEN s.bugs_fixed IS NOT NULL THEN s.id END) as bugs_fixed,
    MIN(s.created_at) as first_session,
    MAX(s.created_at) as last_session
FROM jobs j
LEFT JOIN sessions s ON j.id = s.job_id
GROUP BY j.id
ORDER BY
    CASE j.status
        WHEN 'active' THEN 1
        WHEN 'paused' THEN 2
        ELSE 3
    END,
    j.created_at DESC
```

Expected output:

```
📊 ALL JOBS HISTORY
===================

🟢 ACTIVE:
• migration-sqlite (5 sessions, 12 bugs fixed)
  Started: 2025-08-15 | Last: Today

🟡 PAUSED:
• refactor-auth (2 sessions, 3 bugs fixed)
  Started: 2025-08-10 | Last: 2025-08-14

✅ COMPLETED:
• setup-project (8 sessions, 23 bugs fixed)
  Started: 2025-08-01 | Completed: 2025-08-08
• fix-validation (3 sessions, 5 bugs fixed)
  Started: 2025-07-28 | Completed: 2025-07-30

Total: 4 jobs, 18 sessions, 43 bugs fixed
```

## Python Fallback (only if MCP unavailable)

```python
import sqlite3
from pathlib import Path

DB_PATH = Path(".claude/memory/project.db")

if not DB_PATH.exists():
    print("❌ Database not found")
    exit(1)

conn = sqlite3.connect(str(DB_PATH))
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Get active job
cursor.execute("""
    SELECT j.*,
           COUNT(DISTINCT s.id) as session_count,
           MAX(s.created_at) as last_session
    FROM jobs j
    LEFT JOIN sessions s ON j.id = s.job_id
    WHERE j.status = 'active'
    GROUP BY j.id
""")

active_job = cursor.fetchone()

if active_job:
    print("=" * 60)
    print(f"🚀 ACTIVE JOB: {active_job['id']}")
    print("=" * 60)
    print(f"   Sessions: {active_job['session_count']}")
    print(f"   Started: {active_job['created_at']}")

    # Get last session priority
    cursor.execute("""
        SELECT next_session_priority, pending
        FROM sessions
        WHERE job_id = ?
        ORDER BY created_at DESC
        LIMIT 1
    """, (active_job['id'],))

    last = cursor.fetchone()
    if last:
        if last['next_session_priority']:
            print(f"   🎯 Priority: {last['next_session_priority']}")
        if last['pending']:
import sqlite3
import json
from pathlib import Path
else:
    print("ℹ️ No active job")

# Get paused jobs
cursor.execute("""
    SELECT j.*, COUNT(DISTINCT s.id) as sessions
    FROM jobs j
    LEFT JOIN sessions s ON j.id = s.job_id
    WHERE j.status = 'paused'
    GROUP BY j.id
    ORDER BY j.paused_at DESC
""")

paused_jobs = cursor.fetchall()
if paused_jobs:
    print("\n⏸️  PAUSED JOBS:")
    for job in paused_jobs:
        print(f"   • {job['id']} ({job['sessions']} sessions)")
        if job['pause_reason']:
            print(f"     Reason: {job['pause_reason']}")

conn.close()
```

### --list: Show ALL Jobs History

```python
cursor.execute("""
    SELECT j.*,
           COUNT(DISTINCT s.id) as sessions,
           SUM(CASE WHEN s.accomplishments IS NOT NULL THEN 1 ELSE 0 END) as completed_sessions
    FROM jobs j
    LEFT JOIN sessions s ON j.id = s.job_id
    GROUP BY j.id
    ORDER BY
        CASE j.status
            WHEN 'active' THEN 1
            WHEN 'paused' THEN 2
            WHEN 'completed' THEN 3
        END,
        j.created_at DESC
""")

jobs = cursor.fetchall()

if jobs:
    print("=" * 60)
    print("📊 ALL JOBS HISTORY")
    print("=" * 60)

    for job in jobs:
        status_emoji = {
            'active': '🚀',
            'paused': '⏸️',
            'completed': '✅'
        }.get(job['status'], '❓')

        print(f"\n{status_emoji} {job['id']}")
        print(f"   Status: {job['status']}")
        print(f"   Sessions: {job['sessions']} (saved: {job['completed_sessions']})")
        print(f"   Created: {job['created_at']}")

        if job['status'] == 'paused' and job['pause_reason']:
            print(f"   Paused: {job['paused_at']} - {job['pause_reason']}")
        elif job['status'] == 'completed' and job['completed_at']:
            print(f"   Completed: {job['completed_at']}")
else:
    print("No jobs found")
```

## How It Works

Claude automatically manages jobs:

- Creates when detecting new work
- Pauses when context switches
- Completes when work finishes

The user just needs visibility with `/jobs` and `/jobs --list`

---

_Command created for ClaudeSquad job tracking system_
