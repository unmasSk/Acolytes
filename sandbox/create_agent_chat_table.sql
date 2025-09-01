-- ================================================================
-- ACOLYTES CHAT SYSTEM - Database Schema Implementation
-- ================================================================
-- Database: ROOT (.claude/memory/project.db)
-- Purpose: Global agent communication system for dashboard
-- Agent: @database.sqlite
-- Quest: 42

-- Drop table if exists (for clean re-creation during testing)
DROP TABLE IF EXISTS agent_chat_messages;

-- Main chat messages table
CREATE TABLE agent_chat_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    -- Message identification
    agent_name TEXT NOT NULL,              -- Agent who sent the message (e.g., '@database.sqlite')
    message_type TEXT NOT NULL DEFAULT 'chat',  -- 'chat', 'broadcast', 'system', 'alert'
    
    -- Message content
    content TEXT NOT NULL,                 -- Message content
    metadata JSON,                         -- Additional data: {channel, tags, priority, attachments}
    
    -- Conversation threading
    thread_id TEXT,                        -- For threaded conversations
    reply_to_id INTEGER,                   -- Reference to parent message
    
    -- Status and lifecycle
    status TEXT DEFAULT 'sent',            -- 'sent', 'delivered', 'read', 'archived'
    is_broadcast BOOLEAN DEFAULT 0,        -- 1 for broadcast messages
    
    -- Temporal data
    created_at REAL DEFAULT (julianday('now')),    -- SQLite Julian day format
    updated_at REAL DEFAULT (julianday('now')),    -- For message edits
    expires_at REAL,                       -- For temporary messages
    
    -- Constraints for data integrity
    CHECK (message_type IN ('chat', 'broadcast', 'system', 'alert', 'notification')),
    CHECK (status IN ('sent', 'delivered', 'read', 'archived', 'deleted')),
    
    -- Foreign key to reference parent messages
    FOREIGN KEY (reply_to_id) REFERENCES agent_chat_messages(id)
);

-- ================================================================
-- PERFORMANCE INDEXES
-- ================================================================

-- Primary query index: Get recent messages by agent
CREATE INDEX idx_agent_chat_recent ON agent_chat_messages (
    agent_name, 
    created_at DESC, 
    status
) WHERE status != 'deleted';

-- Broadcast and threading index: Efficient broadcast queries and thread navigation
CREATE INDEX idx_agent_chat_broadcast_thread ON agent_chat_messages (
    is_broadcast, 
    thread_id, 
    created_at DESC,
    message_type
);

-- Additional specialized indexes for dashboard performance
CREATE INDEX idx_agent_chat_timeline ON agent_chat_messages (created_at DESC)
WHERE status IN ('sent', 'delivered', 'read');

-- ================================================================
-- VALIDATION AND TESTING
-- ================================================================

-- Test 1: Insert sample chat message
INSERT INTO agent_chat_messages (
    agent_name,
    message_type,
    content,
    metadata,
    status
) VALUES (
    '@database.sqlite',
    'system',
    'Agent chat table successfully created and validated',
    json('{"priority": "high", "system_event": "table_creation"}'),
    'sent'
);

-- Test 2: Insert broadcast message
INSERT INTO agent_chat_messages (
    agent_name,
    message_type,
    content,
    is_broadcast,
    metadata,
    thread_id
) VALUES (
    '@acolyte.sandbox',
    'broadcast',
    'Quest system operational - all agents ready for communication',
    1,
    json('{"channel": "system", "broadcast_type": "announcement"}'),
    'quest-system-init'
);

-- Test 3: Insert threaded reply
INSERT INTO agent_chat_messages (
    agent_name,
    message_type,
    content,
    reply_to_id,
    thread_id
) VALUES (
    '@database.sqlite',
    'chat',
    'Database schema implementation completed successfully',
    (SELECT id FROM agent_chat_messages WHERE agent_name = '@acolyte.sandbox' LIMIT 1),
    'quest-system-init'
);

-- ================================================================
-- VERIFICATION QUERIES
-- ================================================================

-- Verify table structure
.schema agent_chat_messages

-- Check indexes were created
SELECT name, sql FROM sqlite_master 
WHERE type='index' AND tbl_name='agent_chat_messages';

-- Verify data insertion worked
SELECT 
    id,
    agent_name,
    message_type,
    content,
    datetime(created_at, 'unixepoch') as created_human,
    is_broadcast,
    status
FROM agent_chat_messages 
ORDER BY created_at DESC;

-- Performance test: Recent messages query
SELECT 
    agent_name,
    content,
    message_type,
    datetime(created_at, 'unixepoch') as timestamp
FROM agent_chat_messages 
WHERE status != 'deleted' 
ORDER BY created_at DESC 
LIMIT 10;

-- Thread navigation test
SELECT 
    id,
    agent_name,
    content,
    thread_id,
    reply_to_id
FROM agent_chat_messages 
WHERE thread_id = 'quest-system-init'
ORDER BY created_at;