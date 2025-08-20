#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

import sqlite3
import json
import shutil
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

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
                
    except Exception as e:
        print(f"WARNING: Backup failed: {e}")

def get_current_session_data():
    """Get current active session and validate it exists"""
    try:
        DB_PATH = Path(".claude/memory/project.db")
        if not DB_PATH.exists():
            raise Exception("Database not found")
            
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Find session without ended_at (still active)
        cursor.execute("""
            SELECT id, job_id, created_at, claude_session_id FROM sessions 
            WHERE ended_at IS NULL 
            ORDER BY created_at DESC 
            LIMIT 1
        """)
        
        result = cursor.fetchone()
        conn.close()
        
        if not result:
            raise Exception("No active session found")
            
        return {
            'session_id': result[0],
            'job_id': result[1], 
            'created_at': result[2],
            'claude_session_id': result[3]
        }
        
    except Exception as e:
        raise Exception(f"Failed to get session data: {e}")

def get_technical_metrics(session_id):
    """Get technical metrics only - tool count, duration, exchanges"""
    try:
        DB_PATH = Path(".claude/memory/project.db")
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Get tool count and success rate
        cursor.execute("""
            SELECT COUNT(*) as total, 
                   SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) as successful
            FROM tool_logs 
            WHERE session_id = ?
        """, (session_id,))
        
        tool_stats = cursor.fetchone()
        total_tools = tool_stats[0] if tool_stats else 0
        successful_tools = tool_stats[1] if tool_stats else 0
        failed_tools = total_tools - successful_tools
        
        conn.close()
        
        return {
            'total_tools': total_tools,
            'successful_tools': successful_tools,
            'failed_tools': failed_tools
        }
        
    except Exception as e:
        print(f"WARNING: Technical metrics failed: {e}")
        return {
            'total_tools': 0,
            'successful_tools': 0,
            'failed_tools': 0
        }

def calculate_session_duration(session_data):
    """Calculate real session duration"""
    try:
        start_time = datetime.strptime(session_data['created_at'], '%Y-%m-%d %H:%M')
        end_time = datetime.now()
        duration_minutes = int((end_time - start_time).total_seconds() / 60)
        return duration_minutes
        
    except Exception as e:
        print(f"WARNING: Duration calculation failed: {e}")
        return 0

def calculate_quality_score(accomplishments, errors, breakthrough_moment):
    """Calculate dynamic quality score based on session productivity"""
    score = 7  # Base score
    
    # +1 for each accomplishment (max +3)
    score += min(3, len(accomplishments))
    
    # -1 for each error (max -3)  
    score -= min(3, len(errors))
    
    # +1 if there was a breakthrough
    if breakthrough_moment and breakthrough_moment.strip():
        score += 1
    
    # Keep in range 1-10
    return max(1, min(10, score))

def save_session_to_database(session_data, claude_analysis, technical_metrics, duration_minutes):
    """Update session and insert messages in database"""
    try:
        DB_PATH = Path(".claude/memory/project.db")
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Calculate quality score
        quality_score = calculate_quality_score(
            claude_analysis['accomplishments'],
            claude_analysis['errors'], 
            claude_analysis['breakthrough_moment']
        )
        
        # Update session with Claude's analysis
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')  # No seconds as requested
        
        cursor.execute("""
            UPDATE sessions SET
                accomplishments = ?, decisions = ?,
                bugs_fixed = ?, errors_encountered = ?, breakthrough_moment = ?,
                next_session_priority = ?, quality_score = ?, ended_at = ?
            WHERE id = ?
        """, (
            json.dumps(claude_analysis['accomplishments']),
            json.dumps(claude_analysis['decisions']),
            json.dumps(claude_analysis['bugs_fixed']),
            json.dumps(claude_analysis['errors']),
            claude_analysis['breakthrough_moment'],
            claude_analysis['next_session_priority'],
            quality_score,
            timestamp,
            session_data['session_id']
        ))
        
        # Insert conversation summary into MESSAGES
        cursor.execute("""
            INSERT INTO messages (
                session_id, conversation_flow, total_exchanges,
                duration_minutes, created_at
            ) VALUES (?, ?, ?, ?, ?)
        """, (
            session_data['session_id'],
            claude_analysis['conversation_flow'],
            claude_analysis['total_exchanges'],
            duration_minutes,
            timestamp
        ))
        
        # Get the message ID that was just inserted
        message_id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        
        return quality_score, message_id, timestamp
        
    except Exception as e:
        raise Exception(f"Failed to save to database: {e}")

def main():
    """Main session save function - expects Claude's analysis as input"""
    
    try:
        # Backup database first
        backup_database()
        
        # Get current active session
        session_data = get_current_session_data()
        
        # Get technical metrics
        technical_metrics = get_technical_metrics(session_data['session_id'])
        duration_minutes = calculate_session_duration(session_data)
        
        # Placeholder analysis - Claude will provide real data
        # TODO: This should be replaced with actual conversation analysis from Claude
        claude_analysis = {
            'accomplishments': [
                "Updated save.md format removing --- separators",
                "Extended ===== borders to be double length", 
                "Modified script to receive conversation_flow from Claude"
            ],
            'decisions': [
                "Remove --- separators for cleaner format",
                "Make border lines longer for better visual separation",
                "Claude manually creates conversation_flow summaries"
            ],
            'bugs_fixed': [
                "Fixed output format with proper border lengths",
                "Removed automatic conversation_flow generation"
            ],
            'errors': [],
            'breakthrough_moment': "Script cannot generate conversation summaries - Claude must provide them",
            'next_session_priority': "Test new format and conversation_flow system",
            'conversation_flow': "claude: updated save.md format removing separators\nuser: wants longer borders and real conversation summaries\nclaude: modified script to receive conversation_flow from user\nuser: tests new system format",
            'total_exchanges': technical_metrics['total_tools'] * 2  # Estimate
        }
        
        # Save to database
        quality_score, message_id, timestamp = save_session_to_database(
            session_data, claude_analysis, technical_metrics, duration_minutes
        )
        
        # Output results for Claude to format
        print(json.dumps({
            'session_id': session_data['session_id'],
            'job_id': session_data['job_id'],
            'quality_score': quality_score,
            'duration_minutes': duration_minutes,
            'total_exchanges': claude_analysis['total_exchanges'],
            'accomplishments': claude_analysis['accomplishments'],
            'decisions': claude_analysis['decisions'],
            'bugs_fixed': claude_analysis['bugs_fixed'],
            'errors': claude_analysis['errors'],
            'breakthrough_moment': claude_analysis['breakthrough_moment'],
            'next_session_priority': claude_analysis['next_session_priority'],
            'message_id': message_id,
            'timestamp': timestamp,
            'technical_metrics': technical_metrics
        }))
        
        return 0
        
    except Exception as e:
        print(f"ERROR: {e}")
        return 1

if __name__ == "__main__":
    exit(main())