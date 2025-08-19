---
allowed-tools:
  [
    no se que poner aqui,
    porque tiene que leer la conversacion y escribir en la db,
  ]
description: Save session and messages to SQLite with job tracking
---

# Save

Saves the current session and messages to SQLite database with comprehensive metrics and job tracking.

## Context

- Current active session was created by session_start.py hook and needs to be closed
- Session ID is available from database (sessions table where ended_at IS NULL)

## Instructions

**IMPORTANT: Analyze the current conversation to fill both sessions and messages tables**

## Analysis Approach

Extract data for SESSIONS table:

- **ID**: Generated session ID (session_a1b2c3d4e5f6)
- **Job ID**: Current or specified job identifier
- **Title**: Auto-generated session title from main accomplishment
- **Accomplishments**: Tasks completed, files created/modified, problems solved
- **Decisions**: Important choices made, architectural decisions, tool selections
- **Pending**: Tasks left incomplete, next steps identified
- **Bugs Fixed**: Specific bugs resolved during session
- **Errors Encountered**: Problems faced and how they were handled
- **Breakthrough Moment**: The key insight or solution that unlocked progress
- **Next Session Priority**: What should be done FIRST next time
- **Quality Score**: Dynamic score (1-10) based on session productivity and error count
- **Created At**: Timestamp when session was created by session_start.py hook
- **Ended At**: Timestamp when session was closed by this save command

Generate data for MESSAGES table:

- **Session ID**: Same as sessions.id
- **Conversation Flow**: Chronological narrative of what happened from start to finish
- **Total Exchanges**: Count of user-assistant message pairs in conversation
- **Duration Minutes**: Session length in minutes
- **Created At**: When summary was created

## Execute

- `uv run .claude/scripts/save_session.py` - Close current session and save analysis to database

## Response Format

```markdown
## 📊 Session Saved Successfully

**Session ID**: {session_id}
**Job**: {job_id}
**Quality Score**: {quality_score}/10

### 🎯 Accomplishments ({accomplishments_count})

{accomplishments_list}

### 🐛 Bugs Fixed ({bugs_count})

{bugs_list}

### ❌ Errors Encountered ({errors_count})

{errors_list}

### 💡 Breakthrough Moment

"{breakthrough_moment}"

### 🚀 Next Session Priority

"{next_priority}"

### ⏳ Pending Tasks ({pending_count})

{pending_list}

**Next Session**: When you return, say "Continue job **{job_id}**" to load all context

### 💬 Conversation Summary

## A detailed chronological narrative has been saved to MESSAGES table (ID: {message_id}).

## Session duration: {duration_minutes} minutes | Total exchanges: {total_exchanges}
```
