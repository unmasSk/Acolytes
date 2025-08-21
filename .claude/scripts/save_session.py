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

def clean_emojis(text):
    """Remove problematic emojis from text to avoid encoding issues"""
    import re
    # Remove emoji and problematic unicode characters
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"  # dingbats
                               u"\U000024C2-\U0001F251"
                               u"\U0001F900-\U0001F9FF"  # supplemental symbols
                               u"\U00002600-\U000026FF"  # misc symbols
                               u"\U00002700-\U000027BF"  # dingbats
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub('', text)

def parse_analysis_from_stdin():
    """Parse Claude's analysis from stdin"""
    try:
        import sys
        analysis_data = sys.stdin.read()
        if analysis_data.strip():
            return json.loads(analysis_data)
    except Exception:
        pass
    return None

def get_claude_analysis():
    """Get Claude's manual analysis from stdin or use fallback with ENGLISH data"""
    
    # Try to get Claude's analysis from stdin first
    claude_analysis = parse_analysis_from_stdin()
    
    if not claude_analysis:
        # NO FALLBACK - Claude MUST provide analysis
        print(json.dumps({
            "error": "No analysis provided via stdin. Claude must analyze conversation manually and provide JSON data.",
            "required_format": {
                "accomplishments": ["list of actual accomplishments"],
                "decisions": ["list of key decisions made"],
                "bugs_fixed": ["list of bugs actually fixed"],
                "errors": ["list of errors encountered"],
                "breakthrough_moment": "key insight that unlocked progress",
                "next_session_priority": "what should be done next",
                "conversation_flow": "brief conversation summary"
            }
        }))
        return None
    else:
        # Clean emojis from provided analysis
        for key in ['accomplishments', 'decisions', 'bugs_fixed', 'errors']:
            if key in claude_analysis:
                claude_analysis[key] = [clean_emojis(item) for item in claude_analysis[key]]
        
        for key in ['breakthrough_moment', 'next_session_priority', 'conversation_flow']:
            if key in claude_analysis:
                claude_analysis[key] = clean_emojis(claude_analysis[key])
    
    return claude_analysis

def create_new_session_for_next_time(job_id):
    """Create new session for next conversation after closing current one"""
    try:
        import secrets
        
        # Generate new session ID
        new_session_id = f"session_{secrets.token_hex(6)}"
        
        DB_PATH = Path(".claude/memory/project.db")
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Create new session with same job_id
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        cursor.execute("""
            INSERT INTO sessions (id, job_id, created_at)
            VALUES (?, ?, ?)
        """, (new_session_id, job_id, timestamp))
        
        conn.commit()
        conn.close()
        
        return new_session_id
        
    except Exception:
        return None

def main():
    """Main session save function - closes current session and creates new one"""
    
    try:
        # Backup database first
        backup_database()
        
        # Get current active session
        session_data = get_current_session_data()
        
        # Get technical metrics
        technical_metrics = get_technical_metrics(session_data['session_id'])
        duration_minutes = calculate_session_duration(session_data)
        
        # Get Claude's manual analysis
        claude_analysis = get_claude_analysis()
        if not claude_analysis:
            return 1  # Exit with error if no analysis provided
        claude_analysis['total_exchanges'] = technical_metrics['total_tools'] * 2  # Estimate
        
        # Save to database (this closes the session by setting ended_at)
        quality_score, message_id, timestamp = save_session_to_database(
            session_data, claude_analysis, technical_metrics, duration_minutes
        )
        
        # Create new session for next conversation
        new_session_id = create_new_session_for_next_time(session_data['job_id'])
        
        # Output results for Claude to format
        result = {
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
        }
        
        if new_session_id:
            result['new_session_id'] = new_session_id
            result['next_session_ready'] = True
        else:
            result['next_session_ready'] = False
        
        print(json.dumps(result))
        
        return 0
        
    except Exception as e:
        print(f"ERROR: {e}")
        return 1

if __name__ == "__main__":
    exit(main())