# 🔄 Cross-Domain Communication - Visual Example

## Real Scenario: Auth Module Performance Issue

### Timeline of Events

```
TIME: 10:00 AM - User reports: "Login is slow"
```

### Step 1: Orchestrator Delegates

```yaml
orchestrator → backend-coordinator: "Investigate slow login"

backend-coordinator → laravel-specialist: "READ:
  - .claude/memory/backend/laravel.md
  - .claude/memory/modules/auth.md
  INVESTIGATE: Login performance"
```

### Step 2: Laravel Specialist Investigates

```php
// Laravel finds in LoginController.php:
$user = User::find($id);
$permissions = [];
foreach ($user->roles as $role) {
    foreach ($role->permissions as $permission) {
        $permissions[] = $permission->name; // N+1 QUERY!
    }
}
// This runs 50+ queries!
```

### Step 3: Laravel Documents Discovery

```markdown
# In .claude/memory/backend/laravel.md:

## Cross-Domain Discovery

- Found: N+1 query in LoginController
- Impact: 50+ queries per login
- Time: 500ms+ delay
- Flag: DATABASE_INVESTIGATION

# In .claude/memory/modules/auth.md:

## Performance Issue (from Laravel)

- Date: 2024-01-15 10:15 AM
- Problem: N+1 in permission loading
- Location: LoginController::authenticate()
- Needs: Database optimization
```

### Step 4: Laravel Returns with Flag

```yaml
laravel_specialist → orchestrator:
  summary: "Found N+1 query causing 500ms delay"
  cross_domain_flag:
    type: DATABASE_INVESTIGATION
    severity: HIGH
    module: auth
    details: "Permission loading runs 50+ queries"
```

### Step 5: Orchestrator Processes Flag

```yaml
orchestrator:
  receives: DATABASE_INVESTIGATION flag
  updates: Task queue

orchestrator → database-coordinator: "CROSS-DOMAIN ISSUE from Laravel
  Investigate auth module performance"

database-coordinator → postgres-expert: "READ:
  - .claude/memory/modules/auth.md (see Laravel's note)
  - .claude/memory/database/postgres.md
  FOCUS: Permission query optimization"
```

### Step 6: PostgreSQL Expert Investigates

```sql
-- PostgreSQL analyzes and finds:
-- No index on role_permissions.role_id
-- No index on user_roles.user_id
-- Creates compound index:
CREATE INDEX idx_user_role_permissions
ON user_roles(user_id, role_id);

CREATE INDEX idx_role_permissions
ON role_permissions(role_id, permission_id);
```

### Step 7: PostgreSQL Documents Solution

```markdown
# In .claude/memory/database/postgres.md:

## Optimization Applied

- Module: auth
- Problem: N+1 from Laravel
- Solution: Added compound indexes
- Result: 50 queries → 3 queries
- Time: 500ms → 45ms

# In .claude/memory/modules/auth.md:

## Solution (from PostgreSQL)

- Date: 2024-01-15 10:30 AM
- Fix: Added indexes on permission tables
- Performance: 500ms → 45ms
- Laravel can now use eager loading efficiently
```

### Step 8: PostgreSQL Returns Success

```yaml
postgres_expert → orchestrator:
  summary: "Fixed with indexes, 10x improvement"
  recommendation: "Laravel should implement eager loading"
  flag: OPTIMIZATION_AVAILABLE
```

### Step 9: Orchestrator Queues Follow-up

```yaml
orchestrator:
  notes: "PostgreSQL fixed DB side"
  queues: "Next Laravel session: implement eager loading"
  updates: CLAUDE.md with resolution
```

### Step 10: Next Laravel Session

```yaml
# Hours/days later when Laravel works on auth again:

orchestrator → laravel-specialist: "Optimize auth module
  NOTE: PostgreSQL added indexes yesterday
  READ: .claude/memory/modules/auth.md"

laravel_specialist:
  reads: auth.md
  sees: "PostgreSQL fixed indexes"
  implements:
```

```php
// Laravel now implements eager loading:
$user = User::with(['roles.permissions'])->find($id);
$permissions = $user->roles
    ->pluck('permissions')
    ->flatten()
    ->pluck('name')
    ->unique();
// Now only 3 queries total!
```

### Step 11: Final Documentation

```markdown
# In .claude/memory/modules/auth.md:

## Performance Resolution Complete

- Problem: N+1 query (Laravel found)
- DB Fix: Indexes added (PostgreSQL)
- Code Fix: Eager loading (Laravel)
- Final Performance: 500ms → 15ms (33x improvement!)
- Status: RESOLVED
```

## Visual Flow Diagram

```
User: "Login slow"
    ↓
Orchestrator
    ↓
Laravel: "Found N+1" → 📄 auth.md ← PostgreSQL: "Fixed with index"
    ↓                                        ↑
    [FLAG: DB_INVESTIGATION] → Orchestrator delegates
    ↓
Laravel implements eager loading
    ↓
✅ 33x performance improvement
```

## Key Benefits of This System

1. **No Lost Memory**: Discovery documented immediately
2. **Clear Ownership**: Each specialist owns their domain
3. **Async Collaboration**: Specialists don't need to be active simultaneously
4. **Context Preservation**: Each uses their own 200K context
5. **Module History**: auth.md shows complete investigation trail

## Module File After Resolution

```markdown
# modules/auth.md

## Module: Authentication & Authorization

### Performance Investigation (Jan 15, 2024)

#### Discovery Phase

- **10:15 AM** - Laravel found N+1 query in LoginController
- **Impact**: 50+ queries per login, 500ms delay
- **Flag**: DATABASE_INVESTIGATION raised

#### Investigation Phase

- **10:30 AM** - PostgreSQL analyzed query patterns
- **Found**: Missing indexes on permission tables
- **Applied**: Compound indexes on join tables

#### Resolution Phase

- **2:00 PM** - Laravel implemented eager loading
- **Result**: 3 queries total, 15ms response time
- **Improvement**: 33x performance gain

#### Lessons Learned

- Always check for N+1 in permission systems
- Compound indexes crucial for many-to-many relations
- Eager loading requires proper indexes to be effective

### Module Architecture

[Updated with optimized query patterns]
```

This is how specialists collaborate without ever talking directly to each other!
