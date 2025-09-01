# Agent Chat System - Asynchronous Communication Architecture

## Overview

A database-driven asynchronous chat system that enables communication between the dashboard, users, and agents without requiring agents to be continuously running.

## Core Concept

Agents only exist when Claude invokes them via Task(). Therefore, all communication must be:
- **Asynchronous**: Messages wait in the database until processed
- **Persistent**: All conversations stored in SQLite
- **Queue-based**: Messages processed when Claude is active

## Database Schema

### New Table: `agent_chats`

```sql
CREATE TABLE agent_chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id TEXT NOT NULL DEFAULT (lower(hex(randomblob(8)))),
    sender_type TEXT CHECK(sender_type IN ('user', 'agent', 'system')) NOT NULL,
    sender_name TEXT NOT NULL, -- 'dashboard', '@service.auth', etc.
    recipient_type TEXT CHECK(recipient_type IN ('agent', 'broadcast', 'roundtable')),
    recipient_name TEXT, -- '@service.auth' or NULL for broadcast
    message TEXT NOT NULL,
    status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'processing', 'delivered', 'read')),
    priority INTEGER DEFAULT 5 CHECK(priority BETWEEN 1 AND 10),
    context JSON, -- Additional context, references, code snippets
    parent_message_id INTEGER REFERENCES agent_chats(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP,
    read_at TIMESTAMP,
    session_id TEXT REFERENCES sessions(id),
    quest_id TEXT REFERENCES acolyte_quests(id)
);

-- Indexes for performance
CREATE INDEX idx_chat_status ON agent_chats(status);
CREATE INDEX idx_chat_recipient ON agent_chats(recipient_name);
CREATE INDEX idx_chat_created ON agent_chats(created_at DESC);
CREATE INDEX idx_chat_chat_id ON agent_chats(chat_id);
```

### Integration with Existing Tables

```sql
-- Link chats to quests for automated processing
ALTER TABLE acolyte_quests ADD COLUMN chat_id TEXT;

-- Track agent responses in messages table
ALTER TABLE messages ADD COLUMN chat_reference TEXT;
```

## Communication Flow

### 1. User Sends Message from Dashboard

```python
# Dashboard API endpoint
@app.route('/api/chat/send', methods=['POST'])
def send_chat_message():
    data = request.json
    
    # Insert into agent_chats
    cursor.execute("""
        INSERT INTO agent_chats (
            sender_type, sender_name, 
            recipient_type, recipient_name,
            message, priority, context
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        'user', 'dashboard',
        'agent', data['agent'],
        data['message'],
        data.get('priority', 5),
        json.dumps(data.get('context', {}))
    ))
    
    # Create a quest for high-priority messages
    if data.get('priority', 5) >= 7:
        create_quest_for_chat(cursor.lastrowid)
    
    return {'status': 'queued', 'chat_id': chat_id}
```

### 2. Claude Processes Pending Messages

```python
# Hook: session_start.py checks for pending chats
def check_pending_chats():
    pending = cursor.execute("""
        SELECT COUNT(*) FROM agent_chats 
        WHERE status = 'pending' 
        AND recipient_type = 'agent'
    """).fetchone()[0]
    
    if pending > 0:
        print(f"📬 You have {pending} pending agent messages")
```

### 3. Claude Invokes Agents

```python
# Process chat messages during session
def process_agent_chats():
    # Get pending messages grouped by agent
    pending = cursor.execute("""
        SELECT recipient_name, COUNT(*) as count,
               GROUP_CONCAT(message, ' | ') as messages
        FROM agent_chats 
        WHERE status = 'pending'
        GROUP BY recipient_name
    """).fetchall()
    
    for agent, count, messages in pending:
        # Claude invokes agent with all pending messages
        prompt = f"You have {count} messages from the dashboard: {messages}"
        # Task(agent, prompt)
        
        # Mark as processing
        cursor.execute("""
            UPDATE agent_chats 
            SET status = 'processing' 
            WHERE recipient_name = ? AND status = 'pending'
        """, (agent,))
```

### 4. Agent Responses Stored

```python
# After agent responds, save to database
def save_agent_response(agent_name, response, chat_id):
    cursor.execute("""
        INSERT INTO agent_chats (
            sender_type, sender_name,
            recipient_type, recipient_name,
            message, status,
            parent_message_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        'agent', agent_name,
        'user', 'dashboard',
        response, 'delivered',
        chat_id
    ))
```

### 5. Dashboard Polls for Updates

```python
# Dashboard API endpoint for retrieving messages
@app.route('/api/chat/messages/<chat_id>')
def get_chat_messages(chat_id):
    messages = cursor.execute("""
        SELECT sender_type, sender_name, message, 
               created_at, status
        FROM agent_chats 
        WHERE chat_id = ? OR parent_message_id IN (
            SELECT id FROM agent_chats WHERE chat_id = ?
        )
        ORDER BY created_at ASC
    """, (chat_id, chat_id)).fetchall()
    
    return jsonify({'messages': messages})
```

## Special Features

### Round Table Discussions

Multiple agents can participate in a conversation:

```sql
-- Create a round table discussion
INSERT INTO agent_chats (
    sender_type, sender_name,
    recipient_type, recipient_name,
    message, context
) VALUES (
    'user', 'dashboard',
    'roundtable', NULL,
    'How should we architect the payment system?',
    '{"participants": ["@coordinator.backend", "@service.payment", "@database.postgres"]}'
);
```

### Message Threading

Support for conversation threads:

```sql
-- Get full conversation thread
WITH RECURSIVE thread AS (
    SELECT * FROM agent_chats WHERE id = ?
    UNION ALL
    SELECT ac.* FROM agent_chats ac
    JOIN thread t ON ac.parent_message_id = t.id
)
SELECT * FROM thread ORDER BY created_at;
```

### Priority Queue

High-priority messages get processed first:

```sql
-- Get next message to process
SELECT * FROM agent_chats 
WHERE status = 'pending'
ORDER BY priority DESC, created_at ASC
LIMIT 1;
```

## Dashboard UI Components

### Chat Interface

```javascript
// Vue component for chat
const AgentChat = {
    data() {
        return {
            messages: [],
            selectedAgent: null,
            newMessage: '',
            chatId: null
        }
    },
    methods: {
        async sendMessage() {
            const response = await fetch('/api/chat/send', {
                method: 'POST',
                body: JSON.stringify({
                    agent: this.selectedAgent,
                    message: this.newMessage,
                    priority: 5
                })
            });
            const data = await response.json();
            this.chatId = data.chat_id;
            this.pollForResponses();
        },
        
        async pollForResponses() {
            // Poll every 5 seconds for new messages
            setInterval(async () => {
                const response = await fetch(`/api/chat/messages/${this.chatId}`);
                const data = await response.json();
                this.messages = data.messages;
            }, 5000);
        }
    }
};
```

### Message Status Indicators

- 🔵 Pending: Message queued
- 🟡 Processing: Claude is handling
- 🟢 Delivered: Response ready
- ✓✓ Read: Message viewed

## Implementation Phases

### Phase 1: Basic Chat (MVP)
- Single agent messaging
- Text-only messages
- Manual processing via Claude

### Phase 2: Advanced Features
- Round table discussions
- Message threading
- Auto-quest creation for high priority

### Phase 3: Intelligence Layer
- Agent routing based on message content
- Context preservation across sessions
- Suggested responses

## Benefits

1. **No Agent Redesign**: Works with current Task() system
2. **Persistent History**: All chats saved in SQLite
3. **Asynchronous**: No need for agents to be "online"
4. **Dashboard Integration**: Real-time feel via polling
5. **Scalable**: Can handle multiple conversations

## Example Workflow

1. **User in Dashboard**: "Hey @service.auth, how to implement OAuth with Google?"
2. **System**: Creates database entry, status='pending'
3. **Dashboard**: Shows message as "Queued for processing"
4. **Claude (next session)**: Sees pending message
5. **Claude**: `Task("@service.auth", "User asks: how to implement OAuth with Google?")`
6. **Agent responds**: Detailed OAuth implementation guide
7. **System**: Saves response, status='delivered'
8. **Dashboard**: Shows agent's response in chat

## SQL Queries for Common Operations

```sql
-- Get all pending messages for an agent
SELECT * FROM agent_chats 
WHERE recipient_name = '@service.auth' 
AND status = 'pending'
ORDER BY priority DESC, created_at ASC;

-- Get conversation history
SELECT * FROM agent_chats 
WHERE chat_id = ? OR parent_message_id IN (
    SELECT id FROM agent_chats WHERE chat_id = ?
)
ORDER BY created_at ASC;

-- Mark messages as read
UPDATE agent_chats 
SET status = 'read', read_at = CURRENT_TIMESTAMP
WHERE chat_id = ? AND status = 'delivered';

-- Get unread message count
SELECT recipient_name, COUNT(*) as unread
FROM agent_chats 
WHERE status IN ('pending', 'delivered')
GROUP BY recipient_name;
```

## Future Enhancements

1. **WebSocket Notifications**: Real-time updates when responses arrive
2. **Rich Media**: Support for code snippets, images, files
3. **Agent Availability**: Show estimated response time
4. **Conversation Export**: Download chat history
5. **Smart Routing**: AI-powered agent selection based on query
6. **Batch Processing**: Group similar questions for efficiency

## Conclusion

This database-driven approach enables asynchronous agent communication without requiring architectural changes to the current system. It provides a chat-like experience while respecting the constraint that agents only exist when invoked by Claude.