---
command: todo
description: TODO management with SQLite
---

When this command is invoked:

For `/todo` (no arguments):
- Read ALL TODOs from SQLite using MCP
- Display as PLAIN TEXT table with simple borders:
  ┌────┬───┬────────────────────────────────────────────┬──────┬───────────┐
  │ ID │ ✓ │ Tarea                                      │ Prio │ Tipo      │
  ├────┼───┼────────────────────────────────────────────┼──────┼───────────┤
  │  4 │ ☐ │ [FLAG #2] Update OAuth endpoints           │  🔴  │ maint     │
  └────┴───┴────────────────────────────────────────────┴──────┴───────────┘

Column formatting:
- ID: Right-align, 3 chars max (e.g., "  4", " 25", "123")
- ✓: Center checkbox - ☐ (pending), ☑ (completed), ☒ (blocked)
- Tarea: 62 chars total width, truncate at 60 chars with "..."
  - IMPORTANT: Add space AFTER text to pad to full width
  - Example: "│ Fix authentication bug in login module                       │"
  - The text + spaces must always equal 62 chars before the │
- Prio: Center emoji - 🔴 (critical), 🟠 (high), 🟡 (medium), 🟢 (low)
- Tipo: Left-align categories - feature, bug, test, docs, maint, refactor
- Separator line ONLY between pending and completed sections
- Show summary at bottom: Total: X pendientes

For `/todo add "task"`:
- Use TodoWrite to add the task
- Show: "✅ Added: [task]"

For `/todo sync`:
- Sync TodoWrite with SQLite
- Reorganize by categories
- Show sync summary

For `/todo smart`:
- Analyze pending TODOs
- Generate AI report with insights