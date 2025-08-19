#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///

import json
import sys
import sqlite3
from pathlib import Path

def update_tool_log(tool_data):
    """Update tool log with results in SQLite"""
    try:
        db_path = Path.cwd() / '.claude' / 'memory' / 'project.db'
        if not db_path.exists():
            return  # Database not initialized yet
        
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # Extract tool info and results
        tool_name = tool_data.get('tool_name', 'unknown')
        tool_result = tool_data.get('tool_result', {})
        tool_error = tool_data.get('tool_error')
        
        # Determine success and extract summary
        success = tool_error is None
        error_message = str(tool_error) if tool_error else None
        
        # Create result summary based on tool type
        result_summary = None
        lines_changed = None
        bytes_processed = None
        
        if success and tool_result:
            if tool_name == 'Read':
                # Extract lines read and file size
                if isinstance(tool_result, str):
                    lines_changed = len(tool_result.splitlines())
                    bytes_processed = len(tool_result.encode('utf-8'))
                    result_summary = f"Read {lines_changed} lines"
            elif tool_name in ['Write', 'Edit', 'MultiEdit']:
                result_summary = "File modified successfully"
                if isinstance(tool_result, str) and 'lines' in tool_result:
                    # Try to extract line count from result message
                    import re
                    match = re.search(r'(\d+)\s+lines?', tool_result)
                    if match:
                        lines_changed = int(match.group(1))
            elif tool_name == 'Bash':
                if isinstance(tool_result, str):
                    bytes_processed = len(tool_result.encode('utf-8'))
                    result_summary = f"Command executed ({bytes_processed} bytes output)"
            elif tool_name in ['Grep', 'Glob']:
                if isinstance(tool_result, str):
                    match_count = len(tool_result.splitlines())
                    result_summary = f"Found {match_count} matches"
            elif tool_name == 'Task':
                result_summary = "Task delegated to subagent"
        
        # Update the most recent log entry for this tool in this session
        # (matches by tool_name and timestamp within last 60 seconds)
        cursor.execute("""
            UPDATE tool_logs
            SET success = ?,
                error_message = ?,
                result_summary = ?,
                lines_changed = ?,
                bytes_processed = ?
            WHERE id = (
                SELECT id FROM tool_logs
                WHERE tool_name = ?
                  AND datetime(timestamp) > datetime('now', '-60 seconds')
                ORDER BY id DESC
                LIMIT 1
            )
        """, (
            success, error_message, result_summary,
            lines_changed, bytes_processed,
            tool_name
        ))        
        conn.commit()
        conn.close()
        
    except Exception:
        pass  # Fail silently to not interrupt tool execution

def main():
    try:
        # Read JSON input from stdin
        input_data = json.load(sys.stdin)
        
        # Update tool log in SQLite
        update_tool_log(input_data)
        
        sys.exit(0)
        
    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Exit cleanly on any other error
        sys.exit(0)

if __name__ == '__main__':
    main()