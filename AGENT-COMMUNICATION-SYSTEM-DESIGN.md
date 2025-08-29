# Agent Communication System Design

## Overview

This document presents two complementary inter-agent communication systems designed for parallel agent execution using infinite bash loops. Each agent runs a continuous script that monitors for messages, processes them, and responds.

## Technical Model

**Agent Lifecycle Pattern:**
```bash
while true; do
  # Read messages directed to this agent
  # If message exists: process and respond
  # If no message: continue monitoring
  sleep 30  # Configurable polling interval
done
```

**Key Requirements:**
- Agents run in parallel (3-4 simultaneously)
- Each agent is "alive" while script executes
- Communication must be asynchronous
- Agent death = script termination
- Low latency preferred but not critical

## System 1: SQLite-Based Communication Hub

### Architecture

**Database Schema:**
```sql
-- Core message queue table
CREATE TABLE agent_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_agent VARCHAR(100) NOT NULL,
    to_agent VARCHAR(100) NOT NULL,
    message_type VARCHAR(50) NOT NULL,
    payload TEXT NOT NULL,  -- JSON data
    status VARCHAR(20) DEFAULT 'pending',
    priority INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    processed_at DATETIME NULL,
    response_id INTEGER NULL,
    timeout_seconds INTEGER DEFAULT 300,
    retry_count INTEGER DEFAULT 0,
    max_retries INTEGER DEFAULT 3,
    correlation_id VARCHAR(100) NULL
);

-- Agent registry and heartbeat
CREATE TABLE agent_registry (
    agent_id VARCHAR(100) PRIMARY KEY,
    status VARCHAR(20) DEFAULT 'active',
    last_heartbeat DATETIME DEFAULT CURRENT_TIMESTAMP,
    process_id INTEGER NULL,
    capabilities TEXT NULL,  -- JSON array of what agent can do
    current_load INTEGER DEFAULT 0,
    max_concurrent INTEGER DEFAULT 5
);

-- Response tracking
CREATE TABLE agent_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    from_agent VARCHAR(100) NOT NULL,
    to_agent VARCHAR(100) NOT NULL,
    response_payload TEXT NOT NULL,
    response_status VARCHAR(20) DEFAULT 'success',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES agent_messages(id)
);

-- Pub/Sub events
CREATE TABLE agent_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type VARCHAR(100) NOT NULL,
    publisher VARCHAR(100) NOT NULL,
    payload TEXT NOT NULL,
    published_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME NULL
);

-- Event subscriptions
CREATE TABLE agent_subscriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id VARCHAR(100) NOT NULL,
    event_type VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(agent_id, event_type)
);
```

### Communication Patterns

#### 1. Request-Response Pattern
```bash
# Agent A requests token validation
sqlite3 comm.db "
INSERT INTO agent_messages (from_agent, to_agent, message_type, payload, correlation_id)
VALUES ('@backend.nodejs', '@service.auth', 'validate_token', 
        '{\"token\": \"abc123\", \"user_id\": \"user456\"}', 'req_001');
"

# Agent B (service.auth) loop checks for messages
MESSAGES=$(sqlite3 comm.db "
SELECT id, from_agent, message_type, payload, correlation_id
FROM agent_messages 
WHERE to_agent = '@service.auth' AND status = 'pending'
ORDER BY priority DESC, created_at ASC
LIMIT 1;
")

if [ ! -z "$MESSAGES" ]; then
    # Process message and respond
    MESSAGE_ID=$(echo "$MESSAGES" | cut -d'|' -f1)
    PAYLOAD=$(echo "$MESSAGES" | cut -d'|' -f4)
    
    # Mark as processing
    sqlite3 comm.db "
    UPDATE agent_messages SET status = 'processing', processed_at = CURRENT_TIMESTAMP 
    WHERE id = $MESSAGE_ID;
    "
    
    # Process validation logic...
    VALIDATION_RESULT='{"valid": true, "user": "john_doe"}'
    
    # Send response
    sqlite3 comm.db "
    INSERT INTO agent_responses (request_id, from_agent, to_agent, response_payload)
    VALUES ($MESSAGE_ID, '@service.auth', '@backend.nodejs', '$VALIDATION_RESULT');
    
    UPDATE agent_messages SET status = 'completed' WHERE id = $MESSAGE_ID;
    "
fi

# Agent A checks for response
RESPONSE=$(sqlite3 comm.db "
SELECT ar.response_payload, ar.response_status
FROM agent_responses ar
JOIN agent_messages am ON ar.request_id = am.id
WHERE am.correlation_id = 'req_001' AND am.from_agent = '@backend.nodejs'
AND ar.created_at >= datetime('now', '-5 minutes');
")
```

#### 2. Pub/Sub Pattern
```bash
# Publisher (any agent)
sqlite3 comm.db "
INSERT INTO agent_events (event_type, publisher, payload)
VALUES ('user_login', '@service.auth', 
        '{\"user_id\": \"123\", \"timestamp\": \"2024-01-15T10:30:00Z\", \"ip\": \"192.168.1.1\"}');
"

# Subscribers check for events
EVENTS=$(sqlite3 comm.db "
SELECT ae.id, ae.event_type, ae.payload, ae.published_at
FROM agent_events ae
JOIN agent_subscriptions sub ON ae.event_type = sub.event_type
WHERE sub.agent_id = '@analytics.tracker' 
AND ae.published_at >= datetime('now', '-1 minute')
ORDER BY ae.published_at DESC;
")
```

#### 3. Task Distribution Pattern
```bash
# Task creator
sqlite3 comm.db "
INSERT INTO agent_messages (from_agent, to_agent, message_type, payload, priority)
VALUES ('@coordinator.backend', 'ANY_AVAILABLE', 'process_batch', 
        '{\"batch_id\": \"batch_001\", \"items\": 1000}', 5);
"

# Worker agents compete for tasks
TASK=$(sqlite3 comm.db "
SELECT id, from_agent, message_type, payload
FROM agent_messages 
WHERE to_agent = 'ANY_AVAILABLE' AND status = 'pending'
ORDER BY priority DESC, created_at ASC
LIMIT 1;
")

if [ ! -z "$TASK" ]; then
    TASK_ID=$(echo "$TASK" | cut -d'|' -f1)
    
    # Atomically claim the task
    CLAIMED=$(sqlite3 comm.db "
    UPDATE agent_messages 
    SET status = 'processing', to_agent = '@worker.batch.001', processed_at = CURRENT_TIMESTAMP
    WHERE id = $TASK_ID AND status = 'pending';
    SELECT changes();
    ")
    
    if [ "$CLAIMED" = "1" ]; then
        echo "Task claimed successfully!"
        # Process task...
    fi
fi
```

### Agent Loop Implementation

**Complete Agent Loop Script:**
```bash
#!/bin/bash
AGENT_ID="@backend.nodejs"
DB_PATH="./agent_comm.db"
POLL_INTERVAL=30

# Register agent
sqlite3 "$DB_PATH" "
INSERT OR REPLACE INTO agent_registry (agent_id, status, last_heartbeat, process_id)
VALUES ('$AGENT_ID', 'active', CURRENT_TIMESTAMP, $$);
"

# Cleanup on exit
cleanup() {
    sqlite3 "$DB_PATH" "
    UPDATE agent_registry SET status = 'inactive' WHERE agent_id = '$AGENT_ID';
    "
    exit 0
}
trap cleanup SIGINT SIGTERM

echo "Agent $AGENT_ID started (PID: $$)"

while true; do
    # Update heartbeat
    sqlite3 "$DB_PATH" "
    UPDATE agent_registry SET last_heartbeat = CURRENT_TIMESTAMP WHERE agent_id = '$AGENT_ID';
    "
    
    # Check for pending messages
    MESSAGES=$(sqlite3 "$DB_PATH" "
    SELECT id, from_agent, message_type, payload, correlation_id
    FROM agent_messages 
    WHERE to_agent = '$AGENT_ID' AND status = 'pending'
    ORDER BY priority DESC, created_at ASC
    LIMIT 5;
    ")
    
    # Process each message
    echo "$MESSAGES" | while IFS='|' read -r msg_id from_agent msg_type payload correlation_id; do
        if [ ! -z "$msg_id" ]; then
            echo "Processing message $msg_id from $from_agent: $msg_type"
            
            # Mark as processing
            sqlite3 "$DB_PATH" "
            UPDATE agent_messages SET status = 'processing' WHERE id = $msg_id;
            "
            
            # Process based on message type
            case "$msg_type" in
                "validate_token")
                    # Business logic here
                    response='{"valid": true, "user": "john_doe"}'
                    ;;
                "process_data")
                    # Another business logic
                    response='{"status": "processed", "records": 150}'
                    ;;
                *)
                    response='{"error": "unknown_message_type"}'
                    ;;
            esac
            
            # Send response
            sqlite3 "$DB_PATH" "
            INSERT INTO agent_responses (request_id, from_agent, to_agent, response_payload)
            VALUES ($msg_id, '$AGENT_ID', '$from_agent', '$response');
            
            UPDATE agent_messages SET status = 'completed' WHERE id = $msg_id;
            "
            
            echo "Response sent for message $msg_id"
        fi
    done
    
    # Check for subscribed events
    EVENTS=$(sqlite3 "$DB_PATH" "
    SELECT ae.id, ae.event_type, ae.payload
    FROM agent_events ae
    JOIN agent_subscriptions sub ON ae.event_type = sub.event_type
    WHERE sub.agent_id = '$AGENT_ID' 
    AND ae.published_at >= datetime('now', '-$POLL_INTERVAL seconds')
    ORDER BY ae.published_at DESC;
    ")
    
    echo "$EVENTS" | while IFS='|' read -r event_id event_type payload; do
        if [ ! -z "$event_id" ]; then
            echo "Processing event $event_id: $event_type"
            # Handle event based on type
            # Business logic here...
        fi
    done
    
    # Check for responses to our requests
    RESPONSES=$(sqlite3 "$DB_PATH" "
    SELECT ar.id, ar.request_id, ar.response_payload, ar.response_status
    FROM agent_responses ar
    JOIN agent_messages am ON ar.request_id = am.id
    WHERE am.from_agent = '$AGENT_ID' 
    AND ar.created_at >= datetime('now', '-$POLL_INTERVAL seconds');
    ")
    
    echo "$RESPONSES" | while IFS='|' read -r response_id request_id payload status; do
        if [ ! -z "$response_id" ]; then
            echo "Received response $response_id for request $request_id: $status"
            # Handle response...
        fi
    done
    
    sleep "$POLL_INTERVAL"
done
```

### SQLite Advantages
- **Persistence**: Messages survive agent restarts
- **ACID compliance**: Reliable message delivery
- **No external dependencies**: Single file database
- **SQL flexibility**: Complex queries for message filtering
- **Built-in locking**: Handles concurrent access

### SQLite Disadvantages
- **Performance limitations**: Not optimal for high-frequency messaging
- **Write serialization**: Only one write at a time
- **Polling overhead**: Requires periodic checks
- **File locking issues**: Potential deadlocks under heavy load

## System 2: Redis-Based High-Performance Hub

### Architecture

**Redis Data Structures:**
```redis
# Message queues per agent
LPUSH agent:@backend.nodejs:inbox '{"id":"msg001","from":"@service.auth","type":"validate_token","payload":"...","timestamp":1642234567}'

# Response channels
PUBLISH response:@backend.nodejs:msg001 '{"status":"success","data":"...","timestamp":1642234568}'

# Pub/Sub events
PUBLISH event:user_login '{"user_id":"123","ip":"192.168.1.1","timestamp":"2024-01-15T10:30:00Z"}'

# Agent registry with TTL
SETEX agent:@backend.nodejs:heartbeat 60 '{"status":"active","pid":1234,"capabilities":["api","auth"]}'

# Task distribution with atomic operations
LPUSH tasks:high_priority '{"id":"task001","type":"process_batch","data":"..."}'
BRPOP tasks:high_priority tasks:normal_priority tasks:low_priority 30
```

### Communication Patterns

#### 1. Request-Response with Redis
```bash
#!/bin/bash
AGENT_ID="@backend.nodejs"
REDIS_HOST="localhost"
REDIS_PORT="6379"

# Function to send message
send_message() {
    local to_agent="$1"
    local msg_type="$2"
    local payload="$3"
    local msg_id="msg_$(date +%s%N)"
    
    local message=$(jq -n \
        --arg id "$msg_id" \
        --arg from "$AGENT_ID" \
        --arg type "$msg_type" \
        --arg payload "$payload" \
        --arg timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        '{id: $id, from: $from, type: $type, payload: $payload, timestamp: $timestamp}')
    
    redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" LPUSH "agent:${to_agent}:inbox" "$message"
    
    # Subscribe to response channel
    timeout 30 redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" SUBSCRIBE "response:${AGENT_ID}:${msg_id}" | \
    while read -r type channel response; do
        if [ "$type" = "message" ]; then
            echo "Received response: $response"
            break
        fi
    done &
    
    echo "$msg_id"
}

# Main agent loop
while true; do
    # Update heartbeat
    redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" SETEX "agent:${AGENT_ID}:heartbeat" 60 \
        "{\"status\":\"active\",\"pid\":$$,\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"
    
    # Check inbox with blocking pop (30-second timeout)
    MESSAGE=$(redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" BRPOP "agent:${AGENT_ID}:inbox" 30)
    
    if [ ! -z "$MESSAGE" ]; then
        # Parse message (skip queue name from BRPOP result)
        MSG_DATA=$(echo "$MESSAGE" | tail -n1)
        
        MSG_ID=$(echo "$MSG_DATA" | jq -r '.id')
        FROM_AGENT=$(echo "$MSG_DATA" | jq -r '.from')
        MSG_TYPE=$(echo "$MSG_DATA" | jq -r '.type')
        PAYLOAD=$(echo "$MSG_DATA" | jq -r '.payload')
        
        echo "Processing message $MSG_ID from $FROM_AGENT: $MSG_TYPE"
        
        # Process based on message type
        case "$MSG_TYPE" in
            "validate_token")
                # Business logic here
                RESPONSE='{"valid": true, "user": "john_doe"}'
                ;;
            "process_data")
                RESPONSE='{"status": "processed", "records": 150}'
                ;;
            *)
                RESPONSE='{"error": "unknown_message_type"}'
                ;;
        esac
        
        # Send response
        RESPONSE_MSG=$(jq -n \
            --arg status "success" \
            --arg data "$RESPONSE" \
            --arg timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
            '{status: $status, data: $data, timestamp: $timestamp}')
        
        redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" PUBLISH "response:${FROM_AGENT}:${MSG_ID}" "$RESPONSE_MSG"
        
        echo "Response sent for message $MSG_ID"
    fi
done
```

#### 2. Pub/Sub Events with Redis
```bash
# Publisher
publish_event() {
    local event_type="$1"
    local payload="$2"
    
    local event_data=$(jq -n \
        --arg type "$event_type" \
        --arg publisher "$AGENT_ID" \
        --arg payload "$payload" \
        --arg timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        '{type: $type, publisher: $publisher, payload: $payload, timestamp: $timestamp}')
    
    redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" PUBLISH "event:${event_type}" "$event_data"
}

# Subscriber (run in background)
subscribe_to_events() {
    redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" PSUBSCRIBE "event:*" | \
    while read -r type pattern channel event_data; do
        if [ "$type" = "pmessage" ]; then
            EVENT_TYPE=$(echo "$channel" | cut -d':' -f2)
            echo "Received event $EVENT_TYPE: $event_data"
            # Handle event based on type...
        fi
    done &
}
```

#### 3. Task Distribution with Redis
```bash
# Task publisher
publish_task() {
    local priority="$1"
    local task_data="$2"
    
    redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" LPUSH "tasks:${priority}" "$task_data"
}

# Worker loop
while true; do
    # Block until task available (30-second timeout)
    TASK_RESULT=$(redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" BRPOP \
        "tasks:high_priority" \
        "tasks:normal_priority" \
        "tasks:low_priority" \
        30)
    
    if [ ! -z "$TASK_RESULT" ]; then
        QUEUE=$(echo "$TASK_RESULT" | head -n1)
        TASK_DATA=$(echo "$TASK_RESULT" | tail -n1)
        
        echo "Processing task from $QUEUE: $TASK_DATA"
        
        # Process task...
        # Mark as completed or publish result
        
        publish_event "task_completed" "{\"task\":\"$TASK_DATA\",\"worker\":\"$AGENT_ID\"}"
    fi
done
```

### Redis Advantages
- **High performance**: Sub-millisecond latency
- **Blocking operations**: BRPOP eliminates polling overhead
- **Built-in pub/sub**: Native event broadcasting
- **Atomic operations**: Race condition prevention
- **Rich data structures**: Lists, sets, hashes, streams

### Redis Disadvantages
- **External dependency**: Requires Redis server
- **Memory-based**: Data lost on Redis restart (unless persistence enabled)
- **Single point of failure**: Need Redis clustering for HA
- **Network overhead**: Additional network hops

## System Comparison

| Feature | SQLite | Redis |
|---------|--------|--------|
| **Latency** | 10-100ms | 1-10ms |
| **Throughput** | 100-1K msg/s | 10K-100K msg/s |
| **Persistence** | Always | Optional |
| **Dependencies** | None | Redis server |
| **Complexity** | Low | Medium |
| **Scalability** | Limited | High |
| **Memory Usage** | Low | Higher |
| **Query Flexibility** | High (SQL) | Medium |

## Hybrid Approach Recommendation

For optimal performance and reliability, use both systems:

1. **Redis for real-time communication** (request-response, events)
2. **SQLite for persistent tasks and audit trails**

### Hybrid Implementation
```bash
# Send urgent message via Redis
if [ "$MESSAGE_PRIORITY" = "urgent" ]; then
    send_redis_message "$TO_AGENT" "$MESSAGE_TYPE" "$PAYLOAD"
else
    # Send via SQLite for persistence
    send_sqlite_message "$TO_AGENT" "$MESSAGE_TYPE" "$PAYLOAD"
fi

# Log all communications to SQLite for audit
log_message_to_sqlite "$FROM_AGENT" "$TO_AGENT" "$MESSAGE_TYPE" "$PAYLOAD"
```

## Example Use Cases

### Use Case 1: Token Validation Flow
```bash
# @backend.nodejs needs token validation
MESSAGE_ID=$(send_message "@service.auth" "validate_token" '{"token":"jwt123","endpoint":"/api/users"}')

# @service.auth processes and responds
# @backend.nodejs receives response and continues API processing
```

### Use Case 2: Event Broadcasting
```bash
# @service.auth publishes login event
publish_event "user_login" '{"user_id":"123","session":"sess456","ip":"192.168.1.1"}'

# Multiple subscribers handle:
# - @analytics.tracker: Records user analytics
# - @audit.compliance: Logs security events
# - @service.communication: Sends welcome email
```

### Use Case 3: Batch Processing Distribution
```bash
# @coordinator.backend distributes work
for i in {1..100}; do
    publish_task "normal_priority" "{\"batch_id\":\"$i\",\"data\":\"dataset_$i\"}"
done

# Multiple @worker.batch.* agents compete for tasks
# Each processes their claimed batch independently
```

## Implementation Guidelines

### 1. Error Handling
```bash
# Implement timeouts for all operations
timeout 30 send_message "@service.auth" "validate_token" "$TOKEN_DATA" || {
    echo "Message timeout - using fallback validation"
    # Fallback logic here
}

# Retry mechanism for critical messages
retry_count=0
max_retries=3
while [ $retry_count -lt $max_retries ]; do
    if send_message "$TO_AGENT" "$MSG_TYPE" "$PAYLOAD"; then
        break
    fi
    retry_count=$((retry_count + 1))
    sleep $((retry_count * 2))  # Exponential backoff
done
```

### 2. Agent Health Monitoring
```bash
# Check agent health before sending messages
check_agent_health() {
    local agent="$1"
    
    # SQLite version
    LAST_HEARTBEAT=$(sqlite3 comm.db "
    SELECT last_heartbeat FROM agent_registry WHERE agent_id = '$agent';
    ")
    
    # Redis version
    HEARTBEAT=$(redis-cli GET "agent:${agent}:heartbeat")
    
    if [ -z "$HEARTBEAT" ]; then
        echo "Agent $agent appears to be down"
        return 1
    fi
    return 0
}
```

### 3. Message Prioritization
```bash
# High priority messages go to separate queues
if [ "$PRIORITY" = "urgent" ]; then
    redis-cli LPUSH "agent:${TO_AGENT}:urgent" "$MESSAGE"
else
    redis-cli LPUSH "agent:${TO_AGENT}:inbox" "$MESSAGE"
fi

# Consumer checks urgent queue first
MESSAGE=$(redis-cli BRPOP \
    "agent:${AGENT_ID}:urgent" \
    "agent:${AGENT_ID}:inbox" \
    30)
```

### 4. Dead Letter Handling
```bash
# Move failed messages to dead letter queue
handle_failed_message() {
    local message="$1"
    local failure_reason="$2"
    
    local dead_letter=$(jq -n \
        --arg original "$message" \
        --arg reason "$failure_reason" \
        --arg timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        '{original: $original, reason: $reason, failed_at: $timestamp}')
    
    redis-cli LPUSH "dead_letter_queue" "$dead_letter"
}
```

## Monitoring and Debugging

### Metrics Collection
```bash
# Track message throughput
redis-cli INCR "metrics:messages_sent:$(date +%Y%m%d%H)"
redis-cli INCR "metrics:messages_received:$(date +%Y%m%d%H)"

# Track response times
START_TIME=$(date +%s%N)
# ... send message and wait for response ...
END_TIME=$(date +%s%N)
RESPONSE_TIME=$(( (END_TIME - START_TIME) / 1000000 ))  # Convert to milliseconds
redis-cli LPUSH "metrics:response_times" "$RESPONSE_TIME"
```

### Debug Tools
```bash
# List all active agents
sqlite3 comm.db "
SELECT agent_id, status, last_heartbeat, 
       (julianday('now') - julianday(last_heartbeat)) * 86400 as seconds_since_heartbeat
FROM agent_registry 
WHERE status = 'active';
"

# Show message queue lengths
redis-cli LLEN "agent:@backend.nodejs:inbox"
redis-cli LLEN "agent:@service.auth:inbox"

# Monitor real-time events
redis-cli MONITOR
```

### Performance Tuning
```bash
# Adjust polling intervals based on load
if [ "$(redis-cli LLEN "agent:${AGENT_ID}:inbox")" -gt 10 ]; then
    POLL_INTERVAL=5  # Faster polling under load
else
    POLL_INTERVAL=30  # Slower polling when idle
fi

# Dynamic batch processing
BATCH_SIZE=$(redis-cli LLEN "agent:${AGENT_ID}:inbox")
if [ "$BATCH_SIZE" -gt 5 ]; then
    BATCH_SIZE=5  # Process up to 5 messages at once
fi

for i in $(seq 1 "$BATCH_SIZE"); do
    MESSAGE=$(redis-cli RPOP "agent:${AGENT_ID}:inbox")
    if [ ! -z "$MESSAGE" ]; then
        process_message_async "$MESSAGE" &
    fi
done
wait  # Wait for all background processes
```

## Conclusion

This dual-system approach provides both reliability (SQLite) and performance (Redis) for inter-agent communication. The choice between systems depends on specific use case requirements:

- **Use SQLite** for: Persistent tasks, audit trails, complex queries, simple deployments
- **Use Redis** for: Real-time messaging, event broadcasting, high-throughput scenarios
- **Use Hybrid** for: Production systems requiring both reliability and performance

Both systems support the infinite loop pattern while providing efficient, scalable communication between parallel agents.