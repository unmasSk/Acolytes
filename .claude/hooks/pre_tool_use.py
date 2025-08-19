#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///

# BACKUP: This is the original pre_tool_use.py content

import json
import sys
import re
import sqlite3
from datetime import datetime
from pathlib import Path

def is_dangerous_rm_command(command):
    """
    Comprehensive detection of dangerous rm commands.
    Matches various forms of rm -rf and similar destructive patterns.
    """
    # Normalize command by removing extra spaces and converting to lowercase
    normalized = ' '.join(command.lower().split())
    
    # Pattern 1: Standard rm -rf variations
    patterns = [
        r'\brm\s+.*-[a-z]*r[a-z]*f',  # rm -rf, rm -fr, rm -Rf, etc.
        r'\brm\s+.*-[a-z]*f[a-z]*r',  # rm -fr variations
        r'\brm\s+--recursive\s+--force',  # rm --recursive --force
        r'\brm\s+--force\s+--recursive',  # rm --force --recursive
        r'\brm\s+-r\s+.*-f',  # rm -r ... -f
        r'\brm\s+-f\s+.*-r',  # rm -f ... -r
    ]
    
    # Check for dangerous patterns
    for pattern in patterns:
        if re.search(pattern, normalized):
            return True
    
    # Pattern 2: Check for rm with recursive flag targeting dangerous paths
    dangerous_paths = [
        r'/',           # Root directory
        r'/\*',         # Root with wildcard
        r'~',           # Home directory
        r'~/',          # Home directory path
        r'\$HOME',      # Home environment variable
        r'\.\.',        # Parent directory references
        r'\*',          # Wildcards in general rm -rf context
        r'\.',          # Current directory
        r'\.\s*$',      # Current directory at end of command
    ]
    
    if re.search(r'\brm\s+.*-[a-z]*r', normalized):  # If rm has recursive flag
        for path in dangerous_paths:
            if re.search(path, normalized):
                return True
    
    return False

def is_any_delete_command(command):
    """
    Block ALL deletion commands - rm, rmdir, del, unlink, etc.
    Complete protection against any file/folder deletion.
    """
    # Normalize command
    normalized = ' '.join(command.lower().split())
    
    # All deletion command patterns
    delete_patterns = [
        r'\brm\b',           # ANY rm command
        r'\brmdir\b',        # Remove directory
        r'\bdel\b',          # Windows delete
        r'\bdelete\b',       # Delete command
        r'\bunlink\b',       # Unlink files
        r'\btrash\b',        # Move to trash
        r'\bshred\b',        # Secure delete
        r'\bwipe\b',         # Wipe files
        r'>\s*[^|]',         # Overwrite file with >
        r'>\s*>',            # Truncate file with >>
        r'\btruncate\b',     # Truncate command
    ]
    
    # Check for any deletion pattern
    for pattern in delete_patterns:
        if re.search(pattern, normalized):
            return True
    
    # Also block git clean (removes untracked files)
    if re.search(r'\bgit\s+clean', normalized):
        return True
    
    # Block find with -delete flag
    if re.search(r'\bfind\b.*-delete', normalized):
        return True
    
    # Block xargs rm combinations
    if 'xargs' in normalized and 'rm' in normalized:
        return True
    
    return False

def is_env_file_access(tool_name, tool_input):
    """
    Check if any tool is trying to access .env files containing sensitive data.
    """
    if tool_name in ['Read', 'Edit', 'MultiEdit', 'Write', 'Bash']:
        # Check file paths for file-based tools
        if tool_name in ['Read', 'Edit', 'MultiEdit', 'Write']:
            file_path = tool_input.get('file_path', '')
            if '.env' in file_path and not file_path.endswith('.env.sample'):
                return True
        
        # Check bash commands for .env file access
        elif tool_name == 'Bash':
            command = tool_input.get('command', '')
            # Pattern to detect .env file access (but allow .env.sample)
            env_patterns = [
                r'\b\.env\b(?!\.sample)',  # .env but not .env.sample
                r'cat\s+.*\.env\b(?!\.sample)',  # cat .env
                r'echo\s+.*>\s*\.env\b(?!\.sample)',  # echo > .env
                r'touch\s+.*\.env\b(?!\.sample)',  # touch .env
                r'cp\s+.*\.env\b(?!\.sample)',  # cp .env
                r'mv\s+.*\.env\b(?!\.sample)',  # mv .env
            ]
            
            for pattern in env_patterns:
                if re.search(pattern, command):
                    return True
    
    return False

def is_dangerous_git_operation(tool_name, tool_input):
    """Check if git MCP operation could expose .git directory."""
    if tool_name != 'mcp__server-git__git_add':
        return False
    
    # Check if trying to add everything including .git
    if isinstance(tool_input, dict):
        files = tool_input.get('files', [])
        if files:
            # Convert to string to handle various formats
            files_str = str(files).lower()
            # Dangerous patterns that could include .git
            dangerous_patterns = ['.', '*', 'all', '.git']
            return any(pattern in files_str for pattern in dangerous_patterns)
    
    return False

def log_to_sqlite(tool_data, blocked=False, block_reason=None):
    """Log tool usage to SQLite database"""
    try:
        db_path = Path.cwd() / '.claude' / 'memory' / 'project.db'
        if not db_path.exists():
            return  # Database not initialized yet
        
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # Get current session_id
        cursor.execute("SELECT id FROM sessions WHERE ended_at IS NULL ORDER BY created_at DESC LIMIT 1")
        session = cursor.fetchone()
        session_id = session[0] if session else None
        
        # Extract tool info
        tool_name = tool_data.get('tool_name', 'unknown')
        parameters = json.dumps(tool_data.get('tool_input', {}))
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Determine tool category
        tool_category = 'unknown'
        if tool_name in ['Read', 'Write', 'Edit', 'MultiEdit']:
            tool_category = 'file'
        elif tool_name in ['Grep', 'Glob', 'LS']:
            tool_category = 'search'
        elif tool_name in ['Bash', 'BashOutput', 'KillBash']:
            tool_category = 'execution'
        elif tool_name in ['Task', 'WebSearch', 'WebFetch', 'TodoWrite']:
            tool_category = 'ai'
        elif tool_name.startswith('mcp__'):
            tool_category = 'mcp'
        
        # Extract file if applicable
        file_affected = None
        tool_input = tool_data.get('tool_input', {})
        if 'file_path' in tool_input:
            file_affected = tool_input['file_path']
        elif 'path' in tool_input:
            file_affected = tool_input['path']
        
        # Insert pre-tool log (will be updated in post_tool_use)
        cursor.execute("""
            INSERT INTO tool_logs (
                session_id, tool_name, tool_category, parameters,
                file_affected, blocked_by_hook, hook_message, 
                success, timestamp
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            session_id, tool_name, tool_category, parameters,
            file_affected, blocked, block_reason,
            0 if blocked else 1, timestamp
        ))
        
        conn.commit()
        conn.close()
        
    except Exception:
        pass  # Fail silently to not interrupt tool execution

def main():
    try:
        # Read JSON input from stdin
        input_data = json.load(sys.stdin)
        
        tool_name = input_data.get('tool_name', '')
        tool_input = input_data.get('tool_input', {})
        
        # Block delete_file tool completely
        if tool_name == 'delete_file':
            log_to_sqlite(input_data, blocked=True, block_reason="delete_file tool is blocked")
            print("BLOCKED: The delete_file tool is disabled. File deletion is not allowed.", file=sys.stderr)
            sys.exit(2)  # Exit code 2 blocks tool call and shows error to Claude
        
        # Check for .env file access (blocks access to sensitive environment files)
        if is_env_file_access(tool_name, tool_input):
            log_to_sqlite(input_data, blocked=True, block_reason="Access to .env files not allowed")
            print("BLOCKED: Access to .env files containing sensitive data is prohibited", file=sys.stderr)
            print("Use .env.sample for template files instead", file=sys.stderr)
            sys.exit(2)  # Exit code 2 blocks tool call and shows error to Claude
        
        # Check for dangerous Git MCP operations
        if is_dangerous_git_operation(tool_name, tool_input):
            log_to_sqlite(input_data, blocked=True, block_reason="Git MCP operation could expose .git directory")
            print("BLOCKED: Git MCP operation with '.' or '*' could commit .git directory", file=sys.stderr)
            print("Use 'git add -A' via Bash tool instead for safety", file=sys.stderr)
            sys.exit(2)
        
        # Check for ANY deletion commands
        if tool_name == 'Bash':
            command = tool_input.get('command', '')
            
            # Block ALL deletion commands - complete protection
            if is_any_delete_command(command):
                log_to_sqlite(input_data, blocked=True, block_reason="Deletion command blocked - ALL deletions are prohibited")
                print("BLOCKED: Deletion commands are not allowed. ALL file/folder deletion is prohibited.", file=sys.stderr)
                print("Protected commands include: rm, rmdir, del, unlink, trash, shred, git clean, etc.", file=sys.stderr)
                sys.exit(2)  # Exit code 2 blocks tool call and shows error to Claude
            
            # Also check for dangerous rm -rf patterns (redundant but kept for specific logging)
            elif is_dangerous_rm_command(command):
                log_to_sqlite(input_data, blocked=True, block_reason="Dangerous rm command detected")
                print("BLOCKED: Dangerous rm command detected and prevented", file=sys.stderr)
                sys.exit(2)  # Exit code 2 blocks tool call and shows error to Claude
        
        # Log successful pre-tool call to SQLite
        log_to_sqlite(input_data)
        
        # Special handling for TodoWrite
        if tool_name == 'TodoWrite':
            try:
                from todo_sync import process_todowrite
                result = process_todowrite(tool_input)
            except Exception as e:
                print(f"TodoWrite sync error: {e}", file=sys.stderr)
        
        sys.exit(0)
        
    except json.JSONDecodeError:
        # Gracefully handle JSON decode errors
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)

if __name__ == '__main__':
    main()