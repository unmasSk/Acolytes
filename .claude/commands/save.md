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

## CLAUDE'S ROLE

**YOU MUST ANALYZE THE REAL CONVERSATION MANUALLY**

The script CANNOT read our conversation content. YOU must:

1. **READ** our entire conversation from start to finish
2. **EXTRACT** real accomplishments, decisions, problems solved
3. **IDENTIFY** breakthrough moments and actual issues encountered  
4. **PROVIDE** this analyzed data to the script for saving

## What Claude Must Analyze

**ACCOMPLISHMENTS**: What we actually did
- Files created/modified with specific names
- Problems solved (be specific)
- Features implemented
- Scripts fixed/improved

**DECISIONS**: Important choices we made
- Technical approaches chosen
- Architecture decisions
- Tool selections and why

**BUGS FIXED**: Actual problems resolved
- Specific errors we encountered and fixed
- Scripts that were broken and are now working
- Issues with implementation that got resolved

**ERRORS ENCOUNTERED**: Problems we faced
- Things that didn't work as expected
- Mistakes that had to be corrected
- Technical barriers we hit

**BREAKTHROUGH MOMENT**: Key insight that unlocked progress
- The "aha!" moment that solved a big problem
- Critical realization that changed our approach

**NEXT PRIORITY**: What should be done first next time
- Based on what we learned and what's left incomplete
- Most important next step

## Script Execution

The script will:
- Get session duration from database timestamps  
- Count tool exchanges from tool_logs
- Accept the conversation analysis YOU provide
- Save everything to database

## Execute

1. **FIRST**: Analyze our conversation manually
2. **THEN**: `uv run .claude/scripts/save_session.py` with your analysis

## Response Format

After analyzing the conversation and executing the script, present results in this beautiful format:

```markdown
==============================================================================

# 📊 Session Saved Successfully

## Session Information
- **Session ID**: {session_id}  
- **Job**: {job_id}  
- **Quality Score**: {quality_score}/10 ⭐  
- **Duration**: {duration_minutes} minutes  
- **Total Exchanges**: {total_exchanges}  

## 🎯 Accomplishments ({accomplishments_count})

{accomplishments_list_with_bullets}

## 🐛 Bugs Fixed ({bugs_count})

{bugs_list_with_bullets}

## ⚠️ Errors Encountered ({errors_count})

{errors_list_with_bullets}

## 💡 Breakthrough Moment

> "{breakthrough_moment}"

## 🚀 Next Session Priority

**{next_priority}**

## ⏳ Pending Tasks ({pending_count})

{pending_list_with_bullets}

## 💬 Conversation Summary

A detailed chronological narrative has been saved to the **MESSAGES** table.

**Message ID**: {message_id}  
**Technical Metrics**: {tool_count} tools used ({successful_tools} successful, {failed_tools} failed)

### 🔄 Next Session

When you return, say **"Continue job {job_id}"** to load all context and continue where we left off.

*Session closed at {timestamp}* ✨

==============================================================================
```
