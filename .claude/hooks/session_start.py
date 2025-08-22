#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

"""
SESSION START HOOK - MANDATORY Complete Job Context Loader

This hook runs when Claude Code starts a new session and OBLIGATORILY:

1. FINDS existing ACTIVE session (ended_at IS NULL) and CONTINUES it
2. **MANDATORY**: LOADS COMPLETE context from entire job (all sessions)
3. **MANDATORY**: Shows detailed tool logs from last session (file modifications)
4. **MANDATORY**: Forces Claude to understand what was accomplished before
5. IF no active session exists, shows warning with available jobs
6. BUILDS context from session summaries (accomplishments, decisions, pending tasks)
7. LOADS CLAUDE.md project rules
8. **ENFORCES**: Claude MUST read complete context before starting work

Flow:
- Session starts → Hook finds active session → Loads COMPLETE job context
- Shows ALL accomplishments, decisions, bugs fixed from entire job
- Shows DETAILED tool logs and file modifications from last session
- FORCES Claude to query more details if needed before proceeding
- Claude continues existing work with FULL knowledge of previous sessions

CRITICAL: Claude CANNOT start working without understanding complete job context.
"""

import json
import sys
import sqlite3
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional


def backup_database():
    """Create database backup with timestamp and maintain max 10 files"""
    try:
        DB_PATH = Path(".claude/memory/project.db")
        if not DB_PATH.exists():
            return
        
        # Create backup directory
        backup_dir = Path(".claude/memory/backup")
        backup_dir.mkdir(exist_ok=True)
        
        # Create backup filename with timestamp (no seconds)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        backup_filename = f"project_{timestamp}.db"
        backup_path = backup_dir / backup_filename
        
        # Copy database to backup
        shutil.copy2(DB_PATH, backup_path)
        
        # Clean old backups - keep only 10 most recent
        backup_files = sorted(backup_dir.glob("project_*.db"), key=lambda f: f.stat().st_mtime)
        if len(backup_files) > 10:
            files_to_delete = backup_files[:-10]  # Remove all but last 10
            for old_file in files_to_delete:
                old_file.unlink()
                
    except (OSError, PermissionError, IOError) as e:
        # Backup failed but continue - don't break session start
        # Consider logging to a file for monitoring
        try:
            with open(".claude/memory/backup_errors.log", "a") as f:
                f.write(f"{datetime.now()}: Backup failed - {e}\n")
        except (OSError, PermissionError):
            # If we can't log, continue silently to avoid breaking session start
            pass



def find_active_session():
    """Find existing active session (ended_at IS NULL) and return session info"""
    try:
        # Backup database first
        backup_database()
        
        DB_PATH = Path(".claude/memory/project.db")
        if not DB_PATH.exists():
            return None, "Database not found"
            
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Find active session (ended_at IS NULL)
        cursor.execute("""
            SELECT id, job_id, created_at, claude_session_id 
            FROM sessions 
            WHERE ended_at IS NULL 
            ORDER BY created_at DESC 
            LIMIT 1
        """)
        
        active_session = cursor.fetchone()
        
        if not active_session:
            # No active session found - show available jobs
            cursor.execute("SELECT id, title, status FROM jobs WHERE status = 'paused' ORDER BY created_at DESC LIMIT 3")
            paused_jobs = cursor.fetchall()
            
            conn.close()
            
            context_parts = [
                "WARNING: NO ACTIVE SESSION FOUND",
                "=" * 50,
                "",
                "No active session to continue. Run /save first to create new session.",
                "OR activate an existing job to create session manually:",
                ""
            ]
            
            if paused_jobs:
                context_parts.append("AVAILABLE JOBS:")
                for job in paused_jobs:
                    title = job[1] or "No title"
                    context_parts.append(f"   - {job[0]} - {title} ({job[2]})")
                context_parts.append("")
                context_parts.append("To activate: UPDATE jobs SET status='active' WHERE id='job-id'")
            else:
                context_parts.append("No jobs available.")
            
            context_parts.append("")
            context_parts.append("Session flow: /save creates new session automatically")
            context_parts.append("=" * 50)
            
            return None, "\n".join(context_parts)
        
        session_info = {
            'session_id': active_session[0],
            'job_id': active_session[1],
            'created_at': active_session[2],
            'claude_session_id': active_session[3]
        }
        
        conn.close()
        return session_info, None
        
    except sqlite3.Error as e:
        return None, f"Database error: {str(e)}"
    except (OSError, IOError) as e:
        return None, f"File system error: {str(e)}"


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
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
        # Git not available or timeout
        return None, None
    except OSError:
        # System error running git
        return None, None


def load_job_context_from_db(session_info):
    """Load COMPLETE context from active session and its job
    
    MANDATORY CONTEXT LOADING - Claude MUST understand everything done in the job:
    1. Use the ACTIVE SESSION info provided
    2. Load ALL sessions from the same job for complete context
    3. Build context from session summaries (accomplishments, decisions, pending)
    4. **OBLIGATORIO**: Load detailed tool logs from last session for exact file changes
    5. **OBLIGATORIO**: Show modified files and code changes from previous sessions
    6. Show current session info and job progress
    
    Claude CANNOT start working without knowing the complete job context.
    This ensures Claude knows EXACTLY what was done and which files were modified.
    """
    try:
        DB_PATH = Path(".claude/memory/project.db")
        if not DB_PATH.exists():
            return None
            
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        context_parts = []
        
        # Get job info from active session
        if not session_info or not session_info.get('job_id'):
            conn.close()
            return "No job associated with current session"
        
        job_id = session_info['job_id']
        
        # Add header with current session info
        context_parts.append("=" * 60)
        context_parts.append(f"WORKING ON JOB: {job_id}")
        context_parts.append("=" * 60)
        
        # Get last completed session from this job for priority
        cursor.execute("""
            SELECT id, next_session_priority, breakthrough_moment, 
                   accomplishments, ended_at
            FROM sessions 
            WHERE job_id = ? AND ended_at IS NOT NULL
            ORDER BY created_at DESC 
            LIMIT 1
        """, (job_id,))
        
        last_session = cursor.fetchone()
        if last_session:
            context_parts.append("\nPREVIOUS SESSION SUMMARY:")
            
            # Show accomplishments from last session
            if last_session['accomplishments']:
                try:
                    accs = json.loads(last_session['accomplishments'])
                    if isinstance(accs, list) and accs:
                        context_parts.append("   Recent accomplishments:")
                        for acc in accs[:3]:  # Show max 3 from last session
                            context_parts.append(f"   • {acc}")
                except (json.JSONDecodeError, TypeError):
                    # Skip malformed accomplishments JSON
                    pass
            
            if last_session['next_session_priority']:
                context_parts.append("\nPRIORITY FOR THIS SESSION:")
                context_parts.append(f"   {last_session['next_session_priority']}")
            
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
        
        # Get ALL session data in single query
        cursor.execute("""
            SELECT accomplishments, decisions, bugs_fixed, created_at, ended_at 
            FROM sessions 
            WHERE job_id = ?
            ORDER BY created_at ASC
        """, (job_id,))
        
        all_accomplishments = []
        all_decisions = []
        all_bugs_fixed = []
        sessions_completed = 0
        
        # Helper function to parse JSON safely
        def parse_json_list(json_str):
            try:
                data = json.loads(json_str)
                return data if isinstance(data, list) else []
            except (json.JSONDecodeError, TypeError):
                return []
        
        for row in cursor.fetchall():
            if row['ended_at']:  # Only count completed sessions
                sessions_completed += 1
                
            if row['accomplishments']:
                all_accomplishments.extend(parse_json_list(row['accomplishments']))
            
            if row['decisions']:
                all_decisions.extend(parse_json_list(row['decisions']))
                    
            if row['bugs_fixed']:
                all_bugs_fixed.extend(parse_json_list(row['bugs_fixed']))
        
        # Show comprehensive job progress
        if all_accomplishments:
            context_parts.append(f"\nRECENT ACCOMPLISHMENTS ({len(all_accomplishments)} total):")
            for acc in all_accomplishments[-8:]:  # Show last 8
                context_parts.append(f"   • {acc}")
                
        if all_decisions:
            context_parts.append(f"\nKEY DECISIONS ({len(all_decisions)} total):")
            for dec in all_decisions[-3:]:  # Show last 3
                context_parts.append(f"   • {dec}")
                
        if all_bugs_fixed:
            context_parts.append(f"\nBUGS FIXED ({len(all_bugs_fixed)} total):")
            for bug in all_bugs_fixed[-3:]:  # Show last 3
                context_parts.append(f"   • {bug}")
                
        context_parts.append(f"\nSESSIONS PROGRESS: {sessions_completed} completed, 1 active")
        
        # **OBLIGATORIO**: Load detailed tool logs from last completed session
        if last_session:
            context_parts.append("\n" + "=" * 50)
            context_parts.append("MANDATORY: DETAILED LAST SESSION CONTEXT")
            context_parts.append("=" * 50)
            
            # Get tool logs from last session for file modifications
            cursor.execute("""
                SELECT tool_name, file_affected, success, timestamp
                FROM tool_logs 
                WHERE session_id = ? AND (tool_name IN ('Write', 'Edit', 'MultiEdit') OR file_affected IS NOT NULL)
                ORDER BY timestamp DESC
                LIMIT 15
            """, (last_session['id'],))
            
            tool_logs = cursor.fetchall()
            if tool_logs:
                context_parts.append("\nFILES MODIFIED IN LAST SESSION:")
                files_modified = set()
                md_files = set()
                
                for log in tool_logs:
                    if log['file_affected'] and log['success']:
                        file_path = log['file_affected']
                        files_modified.add(file_path)
                        file_name = Path(file_path).name
                        context_parts.append(f"   • {log['tool_name']}: {file_name}")
                        
                        # Track .md files for documentation changes
                        if file_path.endswith('.md'):
                            md_files.add(file_name)
                
                context_parts.append(f"\nTotal files modified: {len(files_modified)}")
                
                # Show key operations
                context_parts.append("\nKEY OPERATIONS FROM LAST SESSION:")
                for log in tool_logs[:5]:  # Show top 5 operations
                    if log['success']:
                        operation = f"{log['tool_name']}"
                        if log['file_affected']:
                            operation += f" on {Path(log['file_affected']).name}"
                        context_parts.append(f"   • {operation}")
                
                # Show documentation changes
                if md_files:
                    context_parts.append("\nMAJOR DOCUMENTATION CHANGES:")
                    for md_file in sorted(md_files):
                        context_parts.append(f"   • {md_file} - significant updates")
        
        # Check conversation history for additional context
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
        
    except sqlite3.Error as e:
        return f"Database error loading job context: {str(e)}"
    except (OSError, IOError) as e:
        return f"File system error loading job context: {str(e)}"
    except json.JSONDecodeError as e:
        return f"JSON parsing error in session data: {str(e)}"


def load_development_context():
    """Load git status and development context."""
    context_parts = []
    
    # Add git information
    branch, changes = get_git_status()
    if branch:
        context_parts.append(f"Git branch: {branch}")
        if changes and changes > 0:
            context_parts.append(f"Uncommitted changes: {changes} files")
    
    return "\n".join(context_parts) if context_parts else None


def main():
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Extract fields  
        source = input_data.get('source', 'unknown')  # "startup", "resume", or "clear"
        
        # Build context parts
        context_parts = []
        
        # CRITICAL: Set current date/time for Claude (2025 NOT 2024)
        current_time = datetime.now()
        context_parts.append("🕒 CRITICAL TIME CONTEXT FOR CLAUDE:")
        context_parts.append("=" * 50)
        context_parts.append(f"📅 TODAY'S DATE: {current_time.strftime('%A, %B %d, %Y')}")
        context_parts.append(f"⏰ CURRENT TIME: {current_time.strftime('%H:%M')} ({current_time.strftime('%Y-%m-%d %H:%M')})")
        context_parts.append(f"🗓️  YEAR: {current_time.year} (NOT 2024)")
        context_parts.append(f"📍 SESSION SOURCE: {source}")
        context_parts.append("=" * 50)
        
        # FIRST: Find ACTIVE SESSION (don't create new)
        session_info, error_msg = find_active_session()
        
        if error_msg:
            # No active session found or error
            context_parts.append(error_msg)
        else:
            # Found active session - load its context
            context_parts.append(f"Continuing session: {session_info['session_id']}")
            
            # Load context from active session and its job
            db_context = load_job_context_from_db(session_info)
            if db_context:
                context_parts.append(db_context)
        
        # Add project context AFTER session info
        if Path("CLAUDE.md").exists():
            context_parts.append("--- CLAUDE.md Project Rules Active ---")
        
        # Add git status
        dev_context = load_development_context()
        if dev_context:
            context_parts.append(dev_context)
        
        # FINAL: Mandatory instructions for Claude
        if session_info:
            context_parts.append("\n" + "!" * 60)
            context_parts.append("MANDATORY: CLAUDE MUST READ COMPLETE JOB CONTEXT")
            context_parts.append("!" * 60)
            context_parts.append("BEFORE starting any work, Claude MUST:")
            context_parts.append("1. Review the detailed tool logs above")
            context_parts.append("2. Query tool_logs table for complete session context if needed")
            context_parts.append("3. Understand exactly what was accomplished in previous sessions")
            context_parts.append("4. Query MESSAGES table for conversation details if needed")
            context_parts.append("5. Only then proceed with user's request")
            context_parts.append("!" * 60)
        
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
        # Invalid JSON input from Claude Code - exit cleanly
        sys.exit(0)
    except (sqlite3.Error, OSError, IOError):
        # Database or file system errors - exit cleanly to not break Claude
        sys.exit(0)
    except KeyboardInterrupt:
        # User interrupted - exit cleanly
        sys.exit(1)


if __name__ == '__main__':
    main()