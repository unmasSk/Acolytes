# PRE-QUEST Agent Chat System Implementation
Generated: 2025-09-01 23:59:00
Module: /sandbox
Request: Create a simple chat system in a new tab of the dashboard

## MINI-ROADMAP FOR AGENT CHAT IMPLEMENTATION

### Phase 1 - Database Schema (SANDBOX Database)
**Target**: sandbox/dashboard/project.db (Use sandbox database for chat!)
- Create new table `agent_chat_messages` for broadcast chat
- Add indexes for performance on timestamp and agent lookup
- Test connection from server.py to sandbox database

### Phase 2 - Backend API Extensions 
**Target**: /sandbox/dashboard/server.py
- Keep DB_PATH pointing to sandbox database (sandbox/dashboard/project.db)
- Add POST /api/chat/broadcast - send message endpoint
- Add GET /api/chat/messages - get all messages endpoint  
- Add GET /api/chat/quests - enhanced quest info for chat context
- Add proper error handling and JSON validation

### Phase 3 - Frontend Chat Tab
**Target**: /sandbox/dashboard/index.html
- Add 5th tab "Agent Chat" to existing 4-tab structure
- Create chat interface with:
  - Message list (scrollable, auto-scroll to bottom)
  - Input field + Send button
  - Agent selector/identification
  - Real-time message polling (integrate with existing 5s refresh)

### Phase 4 - Integration & Testing
- Integrate chat polling with existing dashboard refresh cycle
- Test broadcast functionality (all agents see messages)
- Test quest context integration
- Ensure mobile responsiveness with existing Tailwind CSS

## FILES TO CREATE/MODIFY

### Database Schema (New)
- **Table**: `agent_chat_messages` in SANDBOX database
  ```sql
  CREATE TABLE agent_chat_messages (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      agent_name TEXT NOT NULL,
      message TEXT NOT NULL,
      timestamp INTEGER DEFAULT (strftime('%s', 'now')),
      quest_id TEXT,
      message_type TEXT DEFAULT 'broadcast',
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
  ```

### Backend Files (Modified)
- **/sandbox/dashboard/server.py** (13.4KB → ~16KB estimated)
  - Keep DB_PATH as sandbox database
  - Add chat endpoints (3 new routes)
  - Add message validation and sanitization

### Frontend Files (Modified)
- **/sandbox/dashboard/index.html** (24KB → ~28KB estimated)
  - Add 5th tab structure
  - Add chat JavaScript class
  - Integrate with existing AcolytesDashboard class

### No New Files Created
- Using existing Flask server architecture
- Using existing HTML/CSS/JS structure
- Using existing database connection patterns

## AGENTS NEEDED FOR QUEST EXECUTION

### Primary Agents (Sequential Execution)
1. **@database.sqlite** - Database specialist
   - Create agent_chat_messages table in SANDBOX database
   - Add proper indexes and constraints
   - Test connection from sandbox server

2. **@backend.python** - Flask server specialist  
   - Keep server.py with SANDBOX database path
   - Implement 3 new chat API endpoints
   - Add JSON validation and error handling

3. **@frontend.vue** - Frontend specialist (can adapt to HTML/JS)
   - Add 5th chat tab to existing dashboard
   - Implement chat interface with real-time updates
   - Integrate with existing dashboard refresh system

### Support Agent (If Needed)
- **@test.quality** - Testing specialist
  - Create simple test plan for chat functionality
  - Verify broadcast works across multiple browser tabs

## DEPENDENCIES & EXECUTION ORDER

### Critical Dependencies
1. **Database MUST be created first** - Backend needs table to exist
2. **Backend endpoints MUST work** - Frontend needs API to function
3. **Frontend integrates last** - Depends on working backend

### Execution Sequence
```
Sequential: @database.sqlite → @backend.python → @frontend.vue
No parallel execution needed - simple linear dependency chain
```

### Technical Constraints
- **SANDBOX database access**: Server.py keeps connection to sandbox/dashboard/project.db
- **Existing dashboard**: Must not break current 4-tab functionality
- **Real-time updates**: Use existing 5-second polling (no WebSockets needed for MVP)
- **Mobile responsive**: Must work with existing Tailwind CSS framework

## ESTIMATED IMPLEMENTATION TIME
- **Database**: 15 minutes (simple table creation)
- **Backend**: 45 minutes (3 endpoints + database connection change)
- **Frontend**: 60 minutes (new tab + chat interface + integration)
- **Testing**: 15 minutes (basic functionality verification)

**Total**: ~2 hours with 3 workers in sequence

## SUCCESS CRITERIA
1. New "Agent Chat" tab appears in dashboard
2. Messages can be sent and appear for all viewers (broadcast)
3. Chat integrates with existing 5-second refresh cycle
4. Messages are stored in SANDBOX database
5. Quest context is available in chat interface
6. Existing dashboard functionality remains intact

## TECHNICAL NOTES
- **No authentication needed**: MVP uses agent names directly
- **No message history limit**: Keep all messages (can optimize later)
- **Simple broadcast only**: No private messages or channels for MVP
- **Quest integration**: Show active quests in chat context for reference

---

**NEXT STEP**: Create QUEST with workers @database.sqlite, @backend.python, @frontend.vue