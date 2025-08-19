#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

"""
SESSION START HOOK - SQLite Context Loader

This hook runs when Claude Code starts a new session and:

1. CREATES new session with hexadecimal ID
2. READS the previous session from SQLite (sessions table)
3. IF that session belongs to a job, LOADS ALL sessions from that job
4. BUILDS context from session summaries (accomplishments, decisions, pending tasks)
5. LOADS CLAUDE.md project rules

Flow:
- Session starts → Hook creates new session ID → Loads previous context
- Shows recent accomplishments and pending tasks from job
- Claude gets complete context to continue work seamlessly
"""

import json
import sys
import sqlite3
import subprocess
import secrets
import time
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional


def create_new_session():
    """Create new session at start and return session_id for hooks"""
    try:
        DB_PATH = Path(".claude/memory/project.db")
        if not DB_PATH.exists():
            return None
            
        # Generate new session ID
        session_id = f"session_{secrets.token_hex(6)}"
        
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Get active job or create default
        cursor.execute("SELECT id FROM jobs WHERE status = 'active' ORDER BY created_at DESC LIMIT 1")
        active_job = cursor.fetchone()
        job_id = active_job[0] if active_job else "project-closure"
        
        # Create initial session record
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        cursor.execute("""
            INSERT INTO sessions (id, job_id, created_at)
            VALUES (?, ?, ?)
        """, (session_id, job_id, timestamp))
        
        conn.commit()
        conn.close()
        
        
        return session_id
        
    except Exception:
        return None


def get_git_status():
    """Get current git status information."""
    try:
        # Get current branch
        branch_result = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True,
            text=True,
            timeout=5
        )
        current_branch = branch_result.stdout.strip() if branch_result.returncode == 0 else "unknown"
        
        # Get uncommitted changes count
        status_result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if status_result.returncode == 0:
            changes = status_result.stdout.strip().split('\n') if status_result.stdout.strip() else []
            uncommitted_count = len(changes)
        else:
            uncommitted_count = 0
        
        return current_branch, uncommitted_count
    except Exception:
        return None, None


def load_job_context_from_db():
    """Load context from database following this strategy:
    
    1. FIRST: Read the PREVIOUS SESSION from SQLite (sessions table)  
    2. IF that session belongs to a job, THEN load ALL sessions from that job
    3. Build context from session summaries (accomplishments, decisions, pending)
    4. If Claude needs more detail, can query MESSAGES table for full conversation
    
    This ensures Claude always knows what was done before and can continue work seamlessly.
    """
    try:
        DB_PATH = Path(".claude/memory/project.db")
        if not DB_PATH.exists():
            return None
            
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        context_parts = []
        
        # FIRST: Always load the PREVIOUS session to see what was done
        cursor.execute("""
            SELECT s.*, j.id as job_id, j.status as job_status
            FROM sessions s
            LEFT JOIN jobs j ON s.job_id = j.id
            WHERE s.ended_at IS NOT NULL
            ORDER BY s.created_at DESC
            LIMIT 1
        """)
        
        last_session = cursor.fetchone()
        
        if not last_session:
            # No previous sessions found
            conn.close()
            return None
        
        # Check if last session belongs to a job
        if last_session['job_id'] and last_session['job_status'] == 'active':
            job_id = last_session['job_id']
            # Now load ALL sessions from this job
        else:
            # Just show last session info without job context
            context_parts.append("=" * 60)
            context_parts.append("CONTINUING FROM LAST SESSION")
            context_parts.append("=" * 60)
            
            if last_session['next_session_priority']:
                context_parts.append("\nPRIORITY:")
                context_parts.append(f"   {last_session['next_session_priority']}")
            
            if last_session['pending']:
                pending_items = json.loads(last_session['pending'])
                if pending_items:
                    context_parts.append(f"\nPENDING ({len(pending_items)}):")
                    for item in pending_items[:3]:
                        context_parts.append(f"   • {item}")
            
            context_parts.append("=" * 60)
            conn.close()
            return "\n".join(context_parts) if context_parts else None
        
        # Add nice header
        context_parts.append("=" * 60)
        context_parts.append(f"WORKING ON JOB: {job_id}")
        context_parts.append("=" * 60)
        
        
        # Get last session info from this job
        cursor.execute("""
            SELECT id, title, next_session_priority, breakthrough_moment, 
                   pending, accomplishments, ended_at
            FROM sessions 
            WHERE job_id = ? AND ended_at IS NOT NULL
            ORDER BY created_at DESC 
            LIMIT 1
        """, (job_id,))
        
        last_session = cursor.fetchone()
        if last_session:
            context_parts.append("\nPREVIOUS SESSION SUMMARY:")
            
            if last_session['next_session_priority']:
                context_parts.append("\nPRIORITY FOR THIS SESSION:")
                context_parts.append(f"   {last_session['next_session_priority']}")
            
            if last_session['pending']:
                pending_items = json.loads(last_session['pending'])
                if pending_items:
                    context_parts.append(f"\nPENDING TASKS ({len(pending_items)}):")
                    for item in pending_items[:5]:  # Show max 5
                        context_parts.append(f"   • {item}")
            
            if last_session['breakthrough_moment']:
                context_parts.append("\nLAST BREAKTHROUGH:")
                context_parts.append(f"   {last_session['breakthrough_moment']}")
        
        # Get total sessions count for this job
        cursor.execute("""
            SELECT COUNT(*) as count, MIN(created_at) as started
            FROM sessions 
            WHERE job_id = ?
        """, (job_id,))
        
        stats = cursor.fetchone()
        if stats and stats['count'] > 0:
            context_parts.append("\nJOB STATS:")
            context_parts.append(f"   Sessions: {stats['count']}")
            context_parts.append(f"   Started: {stats['started']}")
        
        # Get recent accomplishments across all sessions
        cursor.execute("""
            SELECT accomplishments 
            FROM sessions 
            WHERE job_id = ? AND accomplishments IS NOT NULL
            ORDER BY created_at DESC 
            LIMIT 3
        """, (job_id,))
        
        all_accomplishments = []
        for row in cursor.fetchall():
            if row['accomplishments']:
                accs = json.loads(row['accomplishments'])
                all_accomplishments.extend(accs)
        
        if all_accomplishments:
            context_parts.append("\nRECENT ACCOMPLISHMENTS:")
            for acc in all_accomplishments[:5]:  # Show max 5
                context_parts.append(f"   • {acc}")
        
        # Check if we need more detail from MESSAGES table
        cursor.execute("""
            SELECT COUNT(*) as msg_count 
            FROM messages 
            WHERE session_id IN (
                SELECT id FROM sessions WHERE job_id = ?
            )
        """, (job_id,))
        
        msg_count = cursor.fetchone()
        if msg_count and msg_count['msg_count'] > 0:
            context_parts.append(f"\nFull conversation history available: {msg_count['msg_count']} messages")
            context_parts.append("   (Claude can query MESSAGES table if more detail needed)")
        
        context_parts.append("=" * 60)
        
        conn.close()
        return "\n".join(context_parts)
        
    except Exception:
        return None


def load_development_context(source):
    """Load relevant development context based on session source."""
    context_parts = []
    
    # Add simple timestamp
    current_time = datetime.now()
    timestamp_str = current_time.strftime('%Y-%m-%d %H:%M')
    context_parts.append(f"Current time: {timestamp_str}")
    context_parts.append(f"Today is: {current_time.strftime('%A, %B %d, %Y')}")
    context_parts.append(f"Session source: {source}")
    
    # Add git information
    branch, changes = get_git_status()
    if branch:
        context_parts.append(f"Git branch: {branch}")
        if changes > 0:
            context_parts.append(f"Uncommitted changes: {changes} files")
    
    # Load project-specific context files if they exist
    context_files = [
        ".claude/CONTEXT.md",
        ".claude/TODO.md",
        "TODO.md",
        ".github/ISSUE_TEMPLATE.md"
    ]
    
    for file_path in context_files:
        if Path(file_path).exists():
            try:
                with open(file_path, 'r') as f:
                    content = f.read().strip()
                    if content:
                        context_parts.append(f"\n--- Content from {file_path} ---")
                        context_parts.append(content[:1000])  # Limit to first 1000 chars
            except Exception:
                pass
    
    return "\n".join(context_parts)


def main():
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Extract fields  
        source = input_data.get('source', 'unknown')  # "startup", "resume", or "clear"
        
        # Build context parts
        context_parts = []
        
        # FIRST: Create NEW SESSION only if not resuming
        if source != 'resume':
            session_id = create_new_session()
            if session_id:
                context_parts.append(f"New session created: {session_id}")
        else:
            context_parts.append("Resuming existing session")
        
        # THEN: Load PREVIOUS SESSION context  
        # If that session belongs to a job, then load all job sessions
        db_context = load_job_context_from_db()
        if db_context:
            context_parts.append(db_context)
        
        # Add simplified reference to CLAUDE.md rules
        if Path("CLAUDE.md").exists():
            context_parts.append("--- CLAUDE.md Project Rules Active ---")
        
        # Add development context
        dev_context = load_development_context(source)
        if dev_context:
            context_parts.append(dev_context)
        
        # If we have any context, output it
        if context_parts:
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": "\n".join(context_parts)
                }
            }
            print(json.dumps(output))
            sys.exit(0)
        
        # Success
        sys.exit(0)
        
    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)


if __name__ == '__main__':
    main()