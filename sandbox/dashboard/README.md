# Acolytes Dashboard MVP

## Overview
Multi-agent coordination dashboard with real-time monitoring and chat system.

## Features
- **5 Tabs Navigation**: Vista General, Agentes, Quests, FLAGS, Agent Chat
- **Real-time Updates**: Auto-refresh every 5 seconds
- **Broadcast Chat**: Multi-agent communication system
- **REST API**: Full API for programmatic access

## Running the Dashboard

### Start the server
```bash
cd sandbox/dashboard
python server.py
```

Access at: http://localhost:5000

## API Endpoints

### System Statistics
```bash
curl http://localhost:5000/api/stats
```

### Agent Information
```bash
curl http://localhost:5000/api/agents
```

### Quest Status
```bash
curl http://localhost:5000/api/quests
```

### FLAGS System
```bash
curl http://localhost:5000/api/flags
```

## Chat System Commands

### Send a Message via API
```bash
# Basic message
curl -X POST http://localhost:5000/api/chat/broadcast \
  -H "Content-Type: application/json" \
  -d "{\"agent_name\": \"YourAgent\", \"message\": \"Your message here\"}"

# Message with quest context
curl -X POST http://localhost:5000/api/chat/broadcast \
  -H "Content-Type: application/json" \
  -d "{\"agent_name\": \"YourAgent\", \"message\": \"Message text\", \"quest_id\": \"quest-123\"}"
```

### Get Chat Messages
```bash
# Get all messages
curl http://localhost:5000/api/chat/messages

# Get messages with pagination
curl "http://localhost:5000/api/chat/messages?limit=10&offset=0"

# Format JSON output
curl http://localhost:5000/api/chat/messages | python -m json.tool
```

### Get Quest Context for Chat
```bash
curl http://localhost:5000/api/chat/quests
```

## Database

The dashboard uses SQLite database at `sandbox/dashboard/project.db`

### Chat Messages Table
```sql
-- View chat messages directly
sqlite3 sandbox/dashboard/project.db "SELECT * FROM agent_chat_messages ORDER BY timestamp DESC LIMIT 10;"

-- Insert message directly (for testing)
sqlite3 sandbox/dashboard/project.db "INSERT INTO agent_chat_messages (agent_name, message) VALUES ('TestAgent', 'Test message');"
```

## Testing Examples

### Complete Chat Test
```bash
# 1. Send message from command line
curl -X POST http://localhost:5000/api/chat/broadcast \
  -H "Content-Type: application/json" \
  -d "{\"agent_name\": \"CLI-Test\", \"message\": \"Testing from command line\"}"

# 2. Check it was saved
curl http://localhost:5000/api/chat/messages | grep "CLI-Test"

# 3. View in dashboard
# Open http://localhost:5000 and click "Agent Chat" tab
```

### Monitor Server Logs
```bash
# Run server in foreground to see logs
python server.py

# Or check background process
ps aux | grep server.py
```

## Architecture

```
Dashboard (HTML/JS)
    ↓
Flask API (server.py)
    ↓
SQLite Database (project.db)
```

## Files

- `index.html` - Frontend with 5-tab interface
- `server.py` - Flask backend with 7 API endpoints
- `project.db` - SQLite database with agent_chat_messages table
- `ROADMAP_MVP.md` - Original implementation plan

## Quest Integration

The chat system was implemented by 4 agents working autonomously:
1. **@acolyte.sandbox** - Leader/Coordinator
2. **@database.sqlite** - Created database schema
3. **@backend.python** - Implemented API endpoints
4. **@frontend.vue** - Built UI interface

Quest ID: 44 (quest-20250901-214302)

## Notes

- **No authentication** required (MVP)
- **Broadcast only** - All messages visible to all
- **Auto-refresh** - Updates every 5 seconds
- **Mobile responsive** - Works on all devices
- **Windows compatible** - Tested on Git Bash

## Troubleshooting

### Port already in use
```bash
# Find process using port 5000
netstat -ano | grep :5000

# Kill the process (Windows)
taskkill //F //PID [PID_NUMBER]
```

### Special characters in curl
Avoid special characters or use ASCII only:
```bash
# Bad (might fail)
curl -d "{\"message\": \"¡Hola!\"}"

# Good (will work)
curl -d "{\"message\": \"Hola!\"}"
```

### Database locked
```bash
# Check if another process is using the database
lsof | grep project.db

# Or simply restart the server
```

---

**Created by**: Acolytes QUEST System v2.0
**Date**: 2025-09-01
**Status**: Fully operational