---
command: todo
description: TODO management with SQLite
---

When this command is invoked:

For `/todo` (no arguments):
- Read ONLY active TODOs from SQLite using MCP (WHERE status IN ('pending', 'in_progress', 'blocked'))
- Display as PLAIN TEXT table with simple borders:
  ┌────┬───┬────────────────────────────────────────────────────────────────┐
  │ ID │ ✓ │ Task                                                           │
  ├────┼───┼────────────────────────────────────────────────────────────────┤
  │  4 │ ☐ │ Update OAuth endpoints                                         │
  └────┴───┴────────────────────────────────────────────────────────────────┘

Column formatting:
- ID: Right-align, 3 chars max (e.g., "  4", " 25", "123")
- ✓: Center checkbox - ☐ (pending), ⏸ (in_progress), ☒ (blocked)
- Task: 64 chars total width, truncate at 62 chars with "..."
  - IMPORTANT: Add space AFTER text to pad to full width
  - Example: "│ Fix authentication bug in login module                       │"
  - The text + spaces must always equal 64 chars before the │
- Show summary at bottom: Total: X pending

For `/todo add "task"`:
- Use TodoWrite to add the task
- Show: "✅ Added: [task]"

For `/todo sync`:
- Sync TodoWrite with SQLite
- Show sync summary

For `/todo smart`:
- Analyze pending TODOs
- Generate AI report with insights