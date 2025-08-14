# 🚩 FLAGS System - Cross-Domain Communication

## Core Concept

When a dynamic agent working on one module detects an issue that affects ANOTHER module, it creates a FLAG. This ensures cross-domain problems are automatically coordinated without losing information.

## How It Works

### **1. Flag Detection (By Dynamic Agents)**

```yaml
detection_triggers:
  DATABASE_INVESTIGATION:
    - N+1 queries found
    - Missing indexes detected
    - Slow query patterns
    - Schema inconsistencies
    
  SECURITY_REVIEW:
    - Hardcoded secrets found
    - Insecure API endpoints
    - Missing authentication
    - Vulnerability patterns
    
  API_CHANGE:
    - Breaking changes detected
    - New endpoints needed
    - Contract modifications
    - Version incompatibilities
    
  PERFORMANCE_ISSUE:
    - Memory leaks detected
    - CPU bottlenecks
    - Network latency
    - Bundle size problems
    
  ARCHITECTURE_CONFLICT:
    - Pattern violations
    - Dependency cycles
    - Design inconsistencies
    - Coupling issues
```

### **2. Flag Creation (JSON Structure)**

**Location**: `.claude/memory/flags/pending.json`

```json
{
  "flags": [
    {
      "id": "flag_001",
      "type": "DATABASE_INVESTIGATION",
      "module_affected": "database",
      "found_by": "api-agent",
      "description": "getUserPermissions() function runs 50+ queries causing 500ms delay",
      "severity": "high",
      "timestamp": "2024-01-15T10:30:00Z",
      "context": {
        "file_location": "src/api/controllers/UserController.php:145",
        "function_name": "getUserPermissions",
        "current_performance": "500ms average",
        "expected_performance": "<50ms",
        "impact": "All user authentication flows affected"
      },
      "suggested_action": "Create compound index on user_roles(user_id, role_id)",
      "status": "pending"
    }
  ],
  "last_updated": "2024-01-15T10:30:00Z",
  "processed_count": 0
}
```

### **3. Flag Processing (By Claude → Direct Delegation)**

#### **Claude Workflow**
```yaml
claude_process:
  1. Agent notifies: "🚩 FLAG CREATED: [type] for [module]"
  2. Claude reads pending.json to get flag details
  3. Claude directly delegates to target module agent
  4. No coordinators - direct delegation
```

#### **Flag Prioritization**
```yaml
severity_levels:
  critical: "Production down, security breach, data corruption"
  high: "Performance issues, API breaks, user impact"
  medium: "Code quality, technical debt, optimization"
  low: "Documentation, minor improvements, suggestions"

processing_order:
  1. Process all CRITICAL flags immediately
  2. Batch process HIGH flags
  3. Queue MEDIUM flags for next relevant session
  4. Archive LOW flags for periodic review
```

#### **Direct Delegation**
```yaml
claude_delegation:
  1. Read flag details from pending.json
  2. Identify target module from flag.module_affected
  3. Delegate directly to [module]-agent
  4. Provide complete flag context:
     - Original problem description
     - Finding agent's analysis
     - Suggested solutions
     - Impact assessment
     - Related files and code
```

### **4. Flag Resolution**

#### **Target Agent Processing**
```yaml
target_agent_workflow:
  1. Receive delegation with flag context from Claude
  2. Load own memory for similar past issues
  3. Read flag details from pending.json
  4. Analyze the specific problem
  5. Implement solution
  6. Document in own memory
  7. Move flag from pending.json to processed.json
  8. Report back to Claude
```

#### **Flag Completion**
```json
// Move from pending.json to processed.json
{
  "processed_flags": [
    {
      "original_flag": { /* original flag data */ },
      "resolution": {
        "resolved_by": "database-agent",
        "resolution_date": "2024-01-15T11:15:00Z",
        "solution_applied": "Created compound index idx_user_permissions(user_id, role_id)",
        "performance_improvement": "500ms → 45ms (11x improvement)",
        "files_modified": [
          "database/migrations/add_user_permissions_index.sql"
        ],
        "documentation_updated": [
          ".claude/memory/agents/database-agent/knowledge.json",
          ".claude/memory/agents/api-agent/knowledge.json"
        ]
      },
      "verification": {
        "tested": true,
        "performance_confirmed": true,
        "no_regressions": true
      }
    }
  ]
}
```

## Real-World Examples

### **Example 1: API Agent → Database Issue**

```yaml
scenario: "API agent optimizing user dashboard"

discovery:
  agent: api-agent
  finding: "Dashboard loads 15 user preferences individually"
  impact: "200ms delay per preference = 3s total load time"

flag_created:
  type: DATABASE_INVESTIGATION
  description: "getUserPreferences() has N+1 query pattern"
  context: "UserDashboardController::loadPreferences()"
  suggested_solution: "Eager loading with joins"

coordination:
  claude_delegates_to: database-agent
  solution: "CREATE INDEX idx_user_preferences(user_id, category)"
  
result:
  performance: "3s → 150ms (20x improvement)"
  api_agent_updated: "Implements eager loading pattern"
  knowledge_shared: "Both agents learn optimization pattern"
```

### **Example 2: Database Agent → Security Issue**

```yaml
scenario: "Database optimization discovers security flaw"

discovery:
  agent: database-agent
  finding: "User table has unencrypted PII in logs"
  impact: "GDPR violation, sensitive data exposure"

flag_created:
  type: SECURITY_REVIEW
  severity: critical
  description: "PII logging without encryption in user_audit table"
  context: "All user operations log plaintext emails and names"

coordination:
  claude_delegates_to: security-agent
  solution: "Implement field-level encryption + log scrubbing"

result:
  security: "PII encrypted, logs sanitized"
  compliance: "GDPR violation resolved"
  monitoring: "Automated PII detection added"
```

### **Example 3: Frontend Agent → API Change**

```yaml
scenario: "UI component needs new data structure"

discovery:
  agent: frontend-agent
  finding: "UserProfile component needs real-time status updates"
  impact: "Currently polls every 30s, needs WebSocket"

flag_created:
  type: API_CHANGE
  description: "Real-time user status endpoint needed"
  context: "UserProfile.tsx polling /api/user/status inefficiently"
  requirements: "WebSocket connection for instant updates"

coordination:
  claude_delegates_to: api-agent
  solution: "WebSocket endpoint /ws/user/status + Redis pub/sub"

result:
  api: "New WebSocket endpoint implemented"
  frontend: "Real-time updates without polling"
  infrastructure: "Redis pub/sub for scaling"
```

## Flag Types & Routing

### **Direct Agent Routing**
```yaml
flag_routing:
  DATABASE_INVESTIGATION: → database-agent
  SECURITY_REVIEW: → security-agent  
  API_CHANGE: → api-agent
  PERFORMANCE_ISSUE: → performance-agent
  ARCHITECTURE_CONFLICT: → architecture-agent
```

### **Multi-Module Flags**
Some flags affect multiple modules:

```json
{
  "type": "ARCHITECTURE_CONFLICT",
  "affects_multiple": ["backend", "frontend", "database"],
  "agents_to_notify": [
    "backend-agent",
    "frontend-agent", 
    "database-agent"
  ],
  "description": "Authentication flow redesign affects all layers"
}
```

## Benefits

### **1. Zero Information Loss**
- Every cross-domain discovery is captured
- Complete context preserved across handoffs
- Audit trail of all decisions

### **2. Direct Coordination**
- No manual intervention required
- Module agents get complete context
- Solutions flow back to original agents

### **3. Learning System**
- Patterns get documented
- Similar issues resolved faster
- Cross-domain knowledge builds over time

### **4. Performance Tracking**
- Flag resolution times measured
- Solution effectiveness tracked
- Continuous improvement of direct delegation

## Implementation Status

### **✅ Implemented**
- Flag creation in dynamic agent template ✅
- Flag storage structure (pending.json) ✅
- Agent-creator updated with flag protocol ✅
- Direct delegation pattern ✅
- setup.md updated with flags configuration ✅
- claude-md-template.md updated with flags instructions ✅

### **🔄 Ready for Use**
- Dynamic agents can create flags immediately ✅
- Claude instructed to read flags and delegate directly ✅
- Setup command configures flags directory structure ✅
- CLAUDE.md generated with flags protocol ✅
- Complete cross-domain workflow functional ✅

### **📋 Implementation Details**

#### **Files Updated**:
1. **setup.md**: Added Phase 5 for flags system configuration
2. **claude-md-template.md**: Added flags protocol instructions for Claude
3. **dynamic-agent-initial.md**: Already had flag creation protocol ✅
4. **agent-creator.md**: Already had flag creation protocol ✅

#### **What Setup Command Now Does**:
- Creates `.claude/memory/flags/` directory
- Initializes `pending.json` and `processed.json`
- Generates CLAUDE.md with flags instructions
- Configures complete cross-domain communication

#### **What Claude Now Knows** (from generated CLAUDE.md):
- How to read `pending.json` when agents create flags
- Flag types and routing rules
- Direct delegation pattern (no coordinators)
- Multi-module flag handling

### **📈 Future Enhancements**
- Flag analytics and metrics
- Automatic flag prioritization based on impact
- Machine learning for flag routing optimization
- Real-time flag processing notifications

---

**✅ SYSTEM STATUS: FULLY IMPLEMENTED AND READY FOR USE**

**The FLAGS system ensures that discoveries never fall through the cracks and cross-domain coordination happens automatically without human intervention.**