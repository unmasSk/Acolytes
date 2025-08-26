#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///
"""
TodoWrite Sync Hook - Simple sync Claude TODOs with SQLite
Just copies whatever Claude puts in TodoWrite to the database
"""

import json
import sys
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path.cwd() / '.claude' / 'memory' / 'project.db'

def get_timestamp():
    """Get current timestamp without seconds"""
    return datetime.now().strftime('%Y-%m-%d %H:%M')

def sync_todo_to_sqlite(todo, session_id=None):
    """Simple sync: copy Claude TODO to SQLite"""
    if not DB_PATH.exists():
        return None
    
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    try:
        content = todo.get('content', '')
        status = todo.get('status', 'pending')
        claude_id = todo.get('id', '')
        
        timestamp = get_timestamp()
        completed_at = timestamp if status == 'completed' else None
        
        # Check if exists by claude_id in context JSON
        cursor.execute("SELECT id FROM todos WHERE json_extract(context, '$.claude_id') = ?", (claude_id,))
        existing = cursor.fetchone()
        
        if existing:
            # Update existing
            cursor.execute("""
                UPDATE todos SET 
                    task = ?, status = ?, updated_at = ?, completed_at = ?, updated_by = 'claude'
                WHERE id = ?
            """, (content, status, timestamp, completed_at, existing[0]))
        else:
            # Create new
            context = {'claude_id': claude_id, 'auto_synced': True}
            cursor.execute("""
                INSERT INTO todos (task, status, created_at, updated_at, completed_at, 
                                 created_by, context, auto_created, session_id)
                VALUES (?, ?, ?, ?, ?, 'claude', ?, 1, ?)
            """, (content, status, timestamp, timestamp, completed_at, 
                  json.dumps(context), session_id))
        
        conn.commit()
        return True
        
    except Exception as e:
        conn.rollback()
        print(f"Todo sync error: {e}", file=sys.stderr)
        return False
    finally:
        conn.close()

def get_current_session_id():
    """Get current session ID"""
    if not DB_PATH.exists():
        return None
    
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM sessions WHERE ended_at IS NULL ORDER BY created_at DESC LIMIT 1")
        session = cursor.fetchone()
        conn.close()
        return session[0] if session else None
    except Exception:
        return None

def process_todowrite(todos_data):
    """Simple process: sync all TODOs to SQLite"""
    todos = todos_data.get('todos', [])
    if not todos:
        return
    
    session_id = get_current_session_id()
    
    for todo in todos:
        sync_todo_to_sqlite(todo, session_id)

def main():
    """Main hook function"""
    try:
        # Read TodoWrite input
        input_data = json.load(sys.stdin)
        
        # Check if it's a TodoWrite call
        tool_name = input_data.get('tool_name', '')
        if tool_name == 'TodoWrite':
            tool_input = input_data.get('tool_input', {})
            process_todowrite(tool_input)
        
        # Let command pass without blocking
        sys.exit(0)
        
    except Exception as e:
        # Log error but don't block
        print(f"Todo sync error: {e}", file=sys.stderr)
        sys.exit(0)

if __name__ == '__main__':
    main()