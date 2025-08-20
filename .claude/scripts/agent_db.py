#!/usr/bin/env python3
"""
SQLite helper for agents and Claude to manage the database
Usage: python agent_db.py [command] [args]

Commands:
  init                      - Initialize database with schema
  create-agent [name]       - Create agent with empty memories
  update-memory [agent] [type] [content] - Update specific memory
  get-memory [agent] [type] - Get specific memory content
  list-agents              - List all agents
  query [sql]              - Run read-only query
  execute [sql]            - Run write operation
  create-flag              - Create flag targeting specific agent (action_required >= 100 chars, change_description >= 50 chars)
  get_flags [target_agent] - Get pending flags for specific agent
"""
import sqlite3
import json
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Optional

def get_timestamp():
    """Get current timestamp in local time format"""
    return datetime.now().strftime('%Y-%m-%d %H:%M')

DB_PATH = Path(__file__).parent.parent / 'memory' / 'project.db'
MEMORY_TYPES = ['knowledge', 'structure', 'patterns', 'dependencies', 
                'quality', 'operations', 'context', 'domain']

def query(sql, params=None):
    """Read-only query"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.execute(sql, params or [])
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return json.dumps(results, indent=2)

def execute(sql, params=None):
    """Write operation with auto-timestamp"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute(sql, params or [])
    conn.commit()
    affected = cursor.rowcount
    last_id = cursor.lastrowid
    conn.close()
    return json.dumps({"affected": affected, "id": last_id})

def create_flag(flag_type, source_agent, target_agent, 
                change_description, action_required, impact_level='medium',
                related_files=None, code_location=None, example_usage=None,
                context=None, session_id=None):
    """Create a FLAG for inter-module communication about changes"""
    
    # QUALITY VALIDATION
    if len(action_required) < 100:
        return json.dumps({
            "error": "action_required must be at least 100 characters for quality control. Be specific: include file paths, line numbers, exact changes needed.",
            "current_length": len(action_required),
            "required_length": 100
        })
    
    if len(change_description) < 50:
        return json.dumps({
            "error": "change_description must be at least 50 characters. Describe what changed and why.",
            "current_length": len(change_description),
            "required_length": 50
        })
    
    if not target_agent and impact_level in ['high', 'critical']:
        return json.dumps({
            "error": "High/critical impact flags must have specific target_agent specified."
        })
    
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    # Get current session_id if not provided
    if not session_id:
        cursor = conn.execute("SELECT id FROM sessions WHERE ended_at IS NULL ORDER BY created_at DESC LIMIT 1")
        row = cursor.fetchone()
        session_id = row[0] if row else None
    
    # Validate target_agent format
    if target_agent and not target_agent.startswith('@'):
        target_agent = f"@{target_agent}"
    
    # Validate and sanitize related_files (keep as comma-separated TEXT)
    if related_files and isinstance(related_files, list):
        related_files = ', '.join(related_files)
    
    cursor = conn.execute("""
        INSERT INTO flags (
            chain_origin_id, session_id, flag_type, source_agent, target_agent,
            change_description, action_required, impact_level, related_files,
            code_location, example_usage, context, status, created_at, locked
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?, FALSE)
    """, (
        None, session_id, flag_type, source_agent, target_agent,
        change_description, action_required, impact_level, related_files,
        code_location, example_usage, json.dumps(context) if context else None, timestamp
    ))
    conn.commit()
    flag_id = cursor.lastrowid
    conn.close()
    return f"FLAG #{flag_id} created: {flag_type} from {source_agent} targeting {target_agent}"

def get_pending_flags(target_agent=None):
    """Get pending flags targeting a specific agent"""
    sql = "SELECT * FROM flags WHERE status='pending'"
    params = []
    if target_agent:
        # Validate agent name format
        if not target_agent.startswith('@'):
            target_agent = f"@{target_agent}"
        sql += " AND target_agent = ?"
        params.append(target_agent)
    sql += " ORDER BY CASE impact_level WHEN 'critical' THEN 1 WHEN 'high' THEN 2 WHEN 'medium' THEN 3 ELSE 4 END, created_at ASC"
    return query(sql, params)

def init_database():
    """Initialize database with schema from init_db.sql"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    sql_file = Path(__file__).parent / 'init_db.sql'
    
    if not sql_file.exists():
        return json.dumps({"error": "init_db.sql not found"})
    
    conn = sqlite3.connect(DB_PATH)
    with open(sql_file, 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    return json.dumps({"success": True, "message": f"Database initialized at {DB_PATH}"})

def create_agent(name):
    """Create agent with 8 empty memory records"""
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    try:
        # Insert agent
        cursor = conn.execute(
            "INSERT INTO agents_dynamic (name, module, created_at) VALUES (?, 'unknown', ?)",
            (name, timestamp)
        )
        agent_id = cursor.lastrowid
        
        # Insert 8 empty memory records
        for memory_type in MEMORY_TYPES:
            conn.execute(
                "INSERT INTO agent_memory (agent_id, memory_type, content, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                (agent_id, memory_type, '{}', timestamp, timestamp)
            )
        
        conn.commit()
        return json.dumps({
            "success": True, 
            "agent_id": agent_id, 
            "name": name,
            "memories_created": len(MEMORY_TYPES)
        })
    except Exception as e:
        conn.rollback()
        return json.dumps({"error": str(e)})
    finally:
        conn.close()

def update_memory(agent_name, memory_type, content):
    """Update specific memory for an agent"""
    if memory_type not in MEMORY_TYPES:
        return json.dumps({"error": f"Invalid memory_type. Must be one of: {MEMORY_TYPES}"})
    
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    try:
        # Get agent_id
        cursor = conn.execute("SELECT id FROM agents_dynamic WHERE name = ?", (agent_name,))
        row = cursor.fetchone()
        if not row:
            return json.dumps({"error": f"Agent '{agent_name}' not found"})
        
        agent_id = row[0]
        
        # Update memory
        cursor = conn.execute(
            "UPDATE agent_memory SET content = ?, updated_at = ? WHERE agent_id = ? AND memory_type = ?",
            (json.dumps(content) if isinstance(content, dict) else content, timestamp, agent_id, memory_type)
        )
        
        if cursor.rowcount == 0:
            return json.dumps({"error": f"Memory type '{memory_type}' not found for agent '{agent_name}'"})
        
        conn.commit()
        return json.dumps({"success": True, "agent": agent_name, "memory_type": memory_type, "updated": timestamp})
    except Exception as e:
        conn.rollback()
        return json.dumps({"error": str(e)})
    finally:
        conn.close()

def get_memory(agent_name, memory_type):
    """Get specific memory content for an agent"""
    if memory_type not in MEMORY_TYPES:
        return json.dumps({"error": f"Invalid memory_type. Must be one of: {MEMORY_TYPES}"})
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    cursor = conn.execute("""
        SELECT m.content, m.updated_at
        FROM agent_memory m
        JOIN agents_dynamic a ON m.agent_id = a.id
        WHERE a.name = ? AND m.memory_type = ?
    """, (agent_name, memory_type))
    
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return json.dumps({
            "agent": agent_name,
            "memory_type": memory_type,
            "content": json.loads(row['content']) if row['content'] else {},
            "updated_at": row['updated_at']
        })
    else:
        return json.dumps({"error": f"Memory not found for agent '{agent_name}' type '{memory_type}'"})

def update_health(agent_name, drift_score, status, memory_size_kb=None, 
                  file_count_current=None, needs_compaction=False,
                  largest_memory_type=None, recommendations=None):
    """Update agent health record"""
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    # Get agent_id
    cursor = conn.execute("SELECT id FROM agents_dynamic WHERE name = ?", (agent_name,))
    agent = cursor.fetchone()
    if not agent:
        conn.close()
        return json.dumps({"error": f"Agent '{agent_name}' not found"})
    
    agent_id = agent[0]
    
    # Get current session_id
    cursor = conn.execute("SELECT id FROM sessions WHERE ended_at IS NULL ORDER BY created_at DESC LIMIT 1")
    session = cursor.fetchone()
    session_id = session[0] if session else None
    
    # Determine memory warning level
    memory_warning = None
    if memory_size_kb:
        if memory_size_kb > 2000:
            memory_warning = "critical"
        elif memory_size_kb > 1000:
            memory_warning = "large"
    
    # Insert new health record (maintains history)
    conn.execute("""
        INSERT INTO agent_health (
            agent_id, session_id, drift_score, status, memory_size_kb,
            memory_size_warning, largest_memory_type, needs_compaction,
            file_count_current, recommendations, checked_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        agent_id, session_id, drift_score, status, memory_size_kb,
        memory_warning, largest_memory_type, needs_compaction,
        file_count_current, recommendations, timestamp
    ))
    
    conn.commit()
    health_id = cursor.lastrowid
    conn.close()
    
    return json.dumps({
        "success": True,
        "health_id": health_id,
        "agent": agent_name,
        "status": status,
        "drift_score": drift_score,
        "memory_warning": memory_warning
    })

def get_agent_health(agent_name=None):
    """Get health status for agent(s)"""
    sql = """
        SELECT 
            a.name, h.drift_score, h.status, h.memory_size_kb,
            h.memory_size_warning, h.needs_compaction, h.checked_at,
            h.recommendations
        FROM agent_health h
        JOIN agents_dynamic a ON h.agent_id = a.id
    """
    params = []
    
    if agent_name:
        sql += " WHERE a.name = ?"
        params.append(agent_name)
    
    sql += " ORDER BY h.checked_at DESC"
    
    return query(sql, params)

def create_todo(task, priority='medium', category=None, module=None, 
                assigned_to=None, due_date=None, estimated_hours=None,
                tags=None, related_files=None, auto_created=False,
                ai_suggested=False, session_id=None):
    """Create a new TODO task"""
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    # Get current session_id if not provided
    if not session_id:
        cursor = conn.execute("SELECT id FROM sessions WHERE ended_at IS NULL ORDER BY created_at DESC LIMIT 1")
        row = cursor.fetchone()
        session_id = row[0] if row else None
    
    # Get agent_id if assigned_to is an agent name
    agent_id = None
    if assigned_to:
        cursor = conn.execute("SELECT id FROM agents_dynamic WHERE name = ?", (assigned_to,))
        agent = cursor.fetchone()
        if agent:
            agent_id = agent[0]
    
    cursor = conn.execute("""
        INSERT INTO todos (
            task, priority, status, created_at, session_id,
            agent_id, assigned_to, category, module, due_date,
            estimated_hours, tags, related_files, auto_created,
            ai_suggested, created_by
        ) VALUES (?, ?, 'pending', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        task, priority, timestamp, session_id, agent_id,
        assigned_to, category, module, due_date, estimated_hours,
        json.dumps(tags) if tags else None,
        json.dumps(related_files) if related_files else None,
        auto_created, ai_suggested,
        'system' if auto_created else 'user'
    ))
    
    conn.commit()
    todo_id = cursor.lastrowid
    conn.close()
    
    return json.dumps({
        "success": True,
        "todo_id": todo_id,
        "task": task,
        "priority": priority,
        "created_at": timestamp
    })

def update_todo_status(todo_id, status, actual_hours=None, completed_by=None):
    """Update TODO status"""
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    # Use a dictionary for updates - safer and cleaner
    update_fields = {"status": status, "updated_at": timestamp}
    
    if status == 'in_progress' and actual_hours is None:
        update_fields["start_date"] = timestamp
    
    if status == 'completed':
        update_fields["completed_at"] = timestamp
        if completed_by:
            update_fields["completed_by"] = completed_by
    
    if actual_hours is not None:
        update_fields["actual_hours"] = actual_hours
    
    # Build SQL safely with parameterized placeholders
    set_clause = ", ".join(f"{k} = ?" for k in update_fields.keys())
    sql = f"UPDATE todos SET {set_clause} WHERE id = ?"
    params = list(update_fields.values()) + [todo_id]
    
    cursor = conn.execute(sql, params)
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    
    return json.dumps({"success": affected > 0, "todo_id": todo_id, "status": status})

def get_todos(status=None, assigned_to=None, module=None, limit=20):
    """Get TODO tasks with filters"""
    sql = """
        SELECT 
            t.*,
            a.name as agent_name,
            s.title as session_title
        FROM todos t
        LEFT JOIN agents_dynamic a ON t.agent_id = a.id
        LEFT JOIN sessions s ON t.session_id = s.id
        WHERE 1=1
    """
    params = []
    
    if status:
        sql += " AND t.status = ?"
        params.append(status)
    
    if assigned_to:
        sql += " AND (t.assigned_to = ? OR a.name = ?)"
        params.append(assigned_to)
        params.append(assigned_to)
    
    if module:
        sql += " AND t.module = ?"
        params.append(module)
    
    sql += " ORDER BY CASE t.priority WHEN 'critical' THEN 1 WHEN 'high' THEN 2 WHEN 'medium' THEN 3 ELSE 4 END, t.created_at DESC"
    
    if limit:
        sql += f" LIMIT {limit}"
    
    return query(sql, params)

def create_todo_from_flag(flag_id):
    """Auto-create TODO from a critical FLAG"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("""
        SELECT flag_type, source_module, affected_modules, 
               change_description, action_required, impact_level
        FROM flags WHERE id = ?
    """, (flag_id,))
    
    flag = cursor.fetchone()
    if not flag:
        conn.close()
        return json.dumps({"error": f"FLAG #{flag_id} not found"})
    
    # Parse affected_modules (comma-separated TEXT)
    affected_modules = [m.strip() for m in flag[2].split(',')] if flag[2] else []
    first_affected = affected_modules[0] if affected_modules else flag[1]  # fallback to source_module
    
    # Create TODO from FLAG
    task = f"[FLAG #{flag_id}] {flag[4]}"  # action_required
    priority = 'critical' if flag[5] == 'critical' else 'high' if flag[5] == 'high' else 'medium'
    
    result = create_todo(
        task=task,
        priority=priority,
        category='maintenance' if flag[0] == 'breaking_change' else 'refactor',
        module=flag[1],  # source_module
        assigned_to=first_affected,  # first affected module
        auto_created=True,
        related_files=[f"FLAG_{flag_id}"]
    )
    
    # Mark FLAG as having TODO created
    cursor = conn.execute(
        "UPDATE flags SET status = 'todo_created' WHERE id = ?",
        (flag_id,)
    )
    conn.commit()
    conn.close()
    
    return result

# NEW FLAGS SYSTEM FUNCTIONS

def get_workable_flags_summary():
    """Get summary of workable flags for Claude (locked=FALSE, status='pending')"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    cursor = conn.execute("""
        SELECT target_agent, COUNT(*) as workable_flags,
               MAX(impact_level) as highest_priority
        FROM flags 
        WHERE locked = FALSE AND status = 'pending' AND target_agent IS NOT NULL
        GROUP BY target_agent
        ORDER BY workable_flags DESC
    """)
    
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return json.dumps(results, indent=2)

def get_agent_flags(agent_name):
    """Get all pending flags for a specific agent"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    cursor = conn.execute("""
        SELECT * FROM flags 
        WHERE target_agent = ? AND status = 'pending'
        ORDER BY created_at ASC
    """, (agent_name,))
    
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return json.dumps(results, indent=2)

def complete_flag(flag_id, agent_name=None):
    """Mark a flag as completed"""
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    try:
        cursor = conn.execute("""
            UPDATE flags 
            SET status = 'completed', completed_at = ?, completed_by = ?
            WHERE id = ?
        """, (timestamp, agent_name, flag_id))
        
        if cursor.rowcount == 0:
            return json.dumps({"error": f"Flag {flag_id} not found"})
        
        conn.commit()
        return json.dumps({
            "success": True,
            "flag_id": flag_id,
            "completed_by": agent_name,
            "completed_at": timestamp
        })
        
    except Exception as e:
        conn.rollback()
        return json.dumps({"error": str(e)})
    finally:
        conn.close()

def lock_flag(flag_id):
    """Lock a flag (set locked=TRUE)"""
    conn = sqlite3.connect(DB_PATH)
    
    try:
        cursor = conn.execute("UPDATE flags SET locked = TRUE WHERE id = ?", (flag_id,))
        
        if cursor.rowcount == 0:
            return json.dumps({"error": f"Flag {flag_id} not found"})
        
        conn.commit()
        return json.dumps({"success": True, "flag_id": flag_id, "locked": True})
        
    except Exception as e:
        conn.rollback()
        return json.dumps({"error": str(e)})
    finally:
        conn.close()

def unlock_flag(flag_id):
    """Unlock a flag (set locked=FALSE)"""
    conn = sqlite3.connect(DB_PATH)
    
    try:
        cursor = conn.execute("UPDATE flags SET locked = FALSE WHERE id = ?", (flag_id,))
        
        if cursor.rowcount == 0:
            return json.dumps({"error": f"Flag {flag_id} not found"})
        
        conn.commit()
        return json.dumps({"success": True, "flag_id": flag_id, "locked": False})
        
    except Exception as e:
        conn.rollback()
        return json.dumps({"error": str(e)})
    finally:
        conn.close()

def cleanup_orphaned_jobs():
    """Clean up jobs that should be completed but are still marked as active"""
    conn = sqlite3.connect(DB_PATH)
    
    # Find jobs with no recent sessions (more than 24 hours old)
    cursor = conn.execute("""
        SELECT j.id FROM jobs j
        WHERE j.status = 'active' 
        AND NOT EXISTS (
            SELECT 1 FROM sessions s 
            WHERE s.job_id = j.id 
            AND datetime(s.created_at) > datetime('now', '-1 day')
        )
    """)
    
    orphaned_jobs = cursor.fetchall()
    
    if orphaned_jobs:
        # Mark them as paused with reason
        for job in orphaned_jobs:
            conn.execute("""
                UPDATE jobs SET 
                    status = 'paused',
                    paused_at = ?,
                    pause_reason = 'Auto-paused: No recent sessions detected'
                WHERE id = ?
            """, (get_timestamp(), job[0]))
        
        conn.commit()
        result = f"Cleaned up {len(orphaned_jobs)} orphaned jobs"
    else:
        result = "No orphaned jobs found"
    
    conn.close()
    return json.dumps({"message": result, "jobs_cleaned": len(orphaned_jobs)})

def list_available_agents():
    """List all available agents from catalog and dynamic agents"""
    conn = sqlite3.connect(DB_PATH)
    
    try:
        # Get global agents from catalog
        cursor = conn.execute("""
            SELECT name, type, module, description 
            FROM agents_catalog 
            WHERE status = 'active' 
            ORDER BY type, module, name
        """)
        global_agents = cursor.fetchall()
        
        # Get dynamic agents
        cursor = conn.execute("""
            SELECT name, module, created_at 
            FROM agents_dynamic 
            ORDER BY name
        """)
        dynamic_agents = cursor.fetchall()
        
        result = {
            "global_agents": [
                {
                    "name": agent[0],
                    "type": agent[1], 
                    "module": agent[2],
                    "description": agent[3]
                } for agent in global_agents
            ],
            "dynamic_agents": [
                {
                    "name": agent[0],
                    "module": agent[1],
                    "created_at": agent[2]
                } for agent in dynamic_agents
            ],
            "total_global": len(global_agents),
            "total_dynamic": len(dynamic_agents)
        }
        
        return json.dumps(result, indent=2)
        
    except Exception as e:
        return json.dumps({"error": str(e)})
    finally:
        conn.close()

def create_flag_for_agent(flag_type, source_agent, target_agent, change_description, 
                         action_required, impact_level='medium', related_files=None,
                         code_location=None, example_usage=None, context=None, chain_origin_id=None):
    """Create a FLAG targeting a specific agent (new system)"""
    
    # QUALITY VALIDATION
    if len(action_required) < 100:
        return json.dumps({
            "error": "action_required must be at least 100 characters for quality control. Be specific: include file paths, line numbers, exact changes needed.",
            "current_length": len(action_required),
            "required_length": 100
        })
    
    if len(change_description) < 50:
        return json.dumps({
            "error": "change_description must be at least 50 characters. Describe what changed and why.",
            "current_length": len(change_description),
            "required_length": 50
        })
    
    if not target_agent and impact_level in ['high', 'critical']:
        return json.dumps({
            "error": "High/critical impact flags must have specific target_agent specified."
        })
    
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    # Get current session_id 
    cursor = conn.execute("SELECT id FROM sessions WHERE ended_at IS NULL ORDER BY created_at DESC LIMIT 1")
    row = cursor.fetchone()
    session_id = row[0] if row else None
    
    # Validate related_files
    if related_files and isinstance(related_files, list):
        related_files = ', '.join(related_files)
    
    try:
        cursor = conn.execute("""
            INSERT INTO flags (
                chain_origin_id, session_id, flag_type, source_agent, target_agent,
                change_description, action_required, impact_level, related_files,
                code_location, example_usage, context, status, created_at, locked
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?, FALSE)
        """, (
            chain_origin_id, session_id, flag_type, source_agent, target_agent,
            change_description, action_required, impact_level, related_files,
            code_location, example_usage, json.dumps(context) if context else None, timestamp
        ))
        
        flag_id = cursor.lastrowid
        conn.commit()
        
        return json.dumps({
            "success": True,
            "flag_id": flag_id,
            "message": f"FLAG CREATED: {flag_type} for {target_agent}",
            "from": source_agent,
            "to": target_agent,
            "priority": impact_level
        })
        
    except Exception as e:
        conn.rollback()
        return json.dumps({"error": str(e)})
    finally:
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agent_db.py [command] [args...]")
        print("Commands: init, create-agent, update-memory, get-memory, query, execute, create-flag, get_flags, update-health, get-health")
        print("TODO Commands: create-todo, update-todo-status, get-todos, create-todo-from-flag")
        print("NEW FLAGS Commands: get-workable-flags, get-agent-flags, complete-flag, lock-flag, unlock-flag, create-flag-for-agent")
        print("MAINTENANCE Commands: cleanup-jobs")
        sys.exit(1)
    
    command = sys.argv[1]
    
    try:
        if command == "init":
            print(init_database())
        
        elif command == "create-agent":
            if len(sys.argv) < 3:
                print("Usage: python agent_db.py create-agent [name]")
                sys.exit(1)
            name = sys.argv[2]
            print(create_agent(name))
        
        elif command == "update-memory":
            if len(sys.argv) < 5:
                print("Usage: python agent_db.py update-memory [agent-name] [memory-type] [content-json]")
                sys.exit(1)
            agent_name = sys.argv[2]
            memory_type = sys.argv[3]
            try:
                content = json.loads(sys.argv[4])
            except json.JSONDecodeError as e:
                print(json.dumps({"error": f"Invalid JSON: {e}"}))
                sys.exit(1)
            print(update_memory(agent_name, memory_type, content))
        
        elif command == "get-memory":
            if len(sys.argv) < 4:
                print("Usage: python agent_db.py get-memory [agent-name] [memory-type]")
                sys.exit(1)
            agent_name = sys.argv[2]
            memory_type = sys.argv[3]
            print(get_memory(agent_name, memory_type))
        
        elif command == "query":
            sql = sys.argv[2]
            try:
                params = json.loads(sys.argv[3]) if len(sys.argv) > 3 else None
            except json.JSONDecodeError as e:
                print(json.dumps({"error": f"Invalid JSON params: {e}"}))
                sys.exit(1)
            print(query(sql, params))
        
        elif command == "execute":
            sql = sys.argv[2]
            try:
                params = json.loads(sys.argv[3]) if len(sys.argv) > 3 else None
            except json.JSONDecodeError as e:
                print(json.dumps({"error": f"Invalid JSON params: {e}"}))
                sys.exit(1)
            print(execute(sql, params))
        
        elif command == "create-flag":
            # Parse arguments for the new flag structure
            import argparse
            parser = argparse.ArgumentParser()
            parser.add_argument('command')
            parser.add_argument('--flag_type', required=True)
            parser.add_argument('--source_agent', required=True)
            parser.add_argument('--target_agent', required=True)
            parser.add_argument('--change_description', required=True)
            parser.add_argument('--action_required', required=True)
            parser.add_argument('--impact_level', default='medium')
            parser.add_argument('--related_files', default=None)
            parser.add_argument('--code_location', default=None)
            parser.add_argument('--example_usage', default=None)
            
            args = parser.parse_args(sys.argv[1:])
            print(create_flag(
                args.flag_type, args.source_agent, args.target_agent,
                args.change_description, args.action_required,
                args.impact_level, args.related_files, args.code_location,
                args.example_usage
            ))
        
        elif command == "get_flags":
            target_agent = sys.argv[2] if len(sys.argv) > 2 else None
            print(get_pending_flags(target_agent))
        
        elif command == "update-health":
            # Parse arguments for health update
            import argparse
            parser = argparse.ArgumentParser()
            parser.add_argument('command')
            parser.add_argument('--agent_name', required=True)
            parser.add_argument('--drift_score', type=int, required=True)
            parser.add_argument('--status', required=True)
            parser.add_argument('--memory_size_kb', type=float, default=None)
            parser.add_argument('--file_count_current', type=int, default=None)
            parser.add_argument('--needs_compaction', type=bool, default=False)
            parser.add_argument('--largest_memory_type', default=None)
            parser.add_argument('--recommendations', default=None)
            
            args = parser.parse_args(sys.argv[1:])
            print(update_health(
                args.agent_name, args.drift_score, args.status,
                args.memory_size_kb, args.file_count_current, 
                args.needs_compaction, args.largest_memory_type,
                args.recommendations
            ))
        
        elif command == "get-health":
            health_agent_name: Optional[str] = sys.argv[2] if len(sys.argv) > 2 else None
            print(get_agent_health(health_agent_name))
        
        elif command == "create-todo":
            import argparse
            parser = argparse.ArgumentParser()
            parser.add_argument('command')
            parser.add_argument('--task', required=True)
            parser.add_argument('--priority', default='medium')
            parser.add_argument('--category', default=None)
            parser.add_argument('--module', default=None)
            parser.add_argument('--assigned_to', default=None)
            parser.add_argument('--due_date', default=None)
            parser.add_argument('--tags', default=None)
            
            args = parser.parse_args(sys.argv[1:])
            tags = json.loads(args.tags) if args.tags else None
            print(create_todo(
                args.task, args.priority, args.category, args.module,
                args.assigned_to, args.due_date, tags=tags
            ))
        
        elif command == "update-todo-status":
            if len(sys.argv) < 4:
                print("Usage: python agent_db.py update-todo-status [todo_id] [status]")
                sys.exit(1)
            todo_id = int(sys.argv[2])
            status = sys.argv[3]
            print(update_todo_status(todo_id, status))
        
        elif command == "get-todos":
            todos_status: Optional[str] = sys.argv[2] if len(sys.argv) > 2 else None
            print(get_todos(status=todos_status))
        
        elif command == "create-todo-from-flag":
            if len(sys.argv) < 3:
                print("Usage: python agent_db.py create-todo-from-flag [flag_id]")
                sys.exit(1)
            flag_id = int(sys.argv[2])
            print(create_todo_from_flag(flag_id))
        
        elif command == "timestamp":
            print(get_timestamp())
        
        # NEW FLAGS SYSTEM COMMANDS
        elif command == "get-workable-flags":
            print(get_workable_flags_summary())
        
        elif command == "get-agent-flags":
            if len(sys.argv) < 3:
                print("Usage: python agent_db.py get-agent-flags [@agent-name]")
                sys.exit(1)
            agent_name = sys.argv[2]
            print(get_agent_flags(agent_name))
        
        elif command == "complete-flag":
            if len(sys.argv) < 3:
                print("Usage: python agent_db.py complete-flag [flag_id] [optional: agent_name]")
                sys.exit(1)
            flag_id = int(sys.argv[2])
            agent_name = sys.argv[3] if len(sys.argv) > 3 else None
            print(complete_flag(flag_id, agent_name))
        
        elif command == "lock-flag":
            if len(sys.argv) < 3:
                print("Usage: python agent_db.py lock-flag [flag_id]")
                sys.exit(1)
            flag_id = int(sys.argv[2])
            print(lock_flag(flag_id))
        
        elif command == "unlock-flag":
            if len(sys.argv) < 3:
                print("Usage: python agent_db.py unlock-flag [flag_id]")
                sys.exit(1)
            flag_id = int(sys.argv[2])
            print(unlock_flag(flag_id))
        
        elif command == "list-agents":
            print(list_available_agents())
        
        elif command == "cleanup-jobs":
            print(cleanup_orphaned_jobs())
        
        elif command == "create-flag-for-agent":
            import argparse
            parser = argparse.ArgumentParser()
            parser.add_argument('command')
            parser.add_argument('--flag_type', required=True)
            parser.add_argument('--source_agent', required=True)
            parser.add_argument('--target_agent', required=True)
            parser.add_argument('--change_description', required=True)
            parser.add_argument('--action_required', required=True)
            parser.add_argument('--impact_level', default='medium')
            parser.add_argument('--related_files', default=None)
            parser.add_argument('--code_location', default=None)
            parser.add_argument('--example_usage', default=None)
            parser.add_argument('--context', default=None)
            parser.add_argument('--chain_origin_id', type=int, default=None)
            
            args = parser.parse_args(sys.argv[1:])
            context = json.loads(args.context) if args.context else None
            related_files = args.related_files.split(',') if args.related_files else None
            
            print(create_flag_for_agent(
                args.flag_type, args.source_agent, args.target_agent,
                args.change_description, args.action_required, args.impact_level,
                related_files, args.code_location, args.example_usage, context, args.chain_origin_id
            ))
        
        else:
            print(f"Unknown command: {command}")
            print("Commands: init, create-agent, update-memory, get-memory, query, execute, create-flag, get_flags, update-health, get-health")
            print("TODO Commands: create-todo, update-todo-status, get-todos, create-todo-from-flag")
            print("NEW FLAGS Commands: get-workable-flags, get-agent-flags, complete-flag, lock-flag, unlock-flag, create-flag-for-agent")
            sys.exit(1)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)