#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

import sqlite3
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

def backup_database():
    """Create database backup with timestamp and maintain max 10 files"""
    try:
        db_path = Path(".claude/memory/project.db")
        if not db_path.exists():
            print("WARNING: Database does not exist, skipping backup")
            return False
        
        # Create backup directory
        backup_dir = Path(".claude/memory/backup")
        backup_dir.mkdir(exist_ok=True)
        
        # Create backup filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        backup_filename = f"project_{timestamp}.db"
        backup_path = backup_dir / backup_filename
        
        # Copy database to backup
        shutil.copy2(db_path, backup_path)
        
        # Clean old backups - keep only 10 most recent
        backup_files = sorted(backup_dir.glob("project_*.db"), key=lambda f: f.stat().st_mtime)
        if len(backup_files) > 10:
            files_to_delete = backup_files[:-10]
            for old_file in files_to_delete:
                old_file.unlink()
        
        return True
    except Exception as e:
        print(f"ERROR: Critical backup failure: {e}")
        return False

def parse_arguments():
    """Parse command line arguments manually"""
    import sys
    
    args = sys.argv[1:]
    if len(args) < 4 or '-session' not in args or '-message' not in args:
        print(json.dumps({
            "error": "Usage: script.py -session 'session_data' -message 'message_data'",
            "example": "script.py -session 'accomplishments: Fixed bug. decisions: Chose X.' -message 'conversation_flow: Q: What? A: Fixed bug. total_exchanges: 10 duration_minutes: 30'"
        }))
        return None, None
    
    try:
        session_idx = args.index('-session') + 1
        message_idx = args.index('-message') + 1
        return args[session_idx], args[message_idx]
    except (IndexError, ValueError):
        print(json.dumps({"error": "Invalid arguments format"}))
        return None, None

def parse_field(text, field_name):
    """Extract field content from text"""
    # Clean emojis with simple regex
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # Extract field content
    pattern = rf"{field_name}:\s*(.*?)(?=\s+(?:accomplishments|decisions|bugs_fixed|errors_encountered|breakthrough_moment|next_session_priority|conversation_flow|total_exchanges|duration_minutes):|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    
    if match:
        content = match.group(1).strip()
        if content and content.lower() not in ['none', 'n/a', 'nothing', 'empty']:
            # Add line breaks for readability
            content = content.replace('. ', '.\n').replace('? ', '?\n').replace('! ', '!\n')
            content = re.sub(r'\n\s*\n', '\n', content)
            return content.strip()
    return ""

def get_current_session():
    """Get current active session"""
    try:
        conn = sqlite3.connect(".claude/memory/project.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, job_id, created_at FROM sessions WHERE ended_at IS NULL ORDER BY created_at DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        
        if not result:
            raise Exception("No active session found")
        return {'session_id': result[0], 'job_id': result[1], 'created_at': result[2]}
    except Exception as e:
        raise Exception(f"Failed to get session: {e}")

def save_to_database(session_data, session_text, message_text):
    """Save session data to database"""
    try:
        # Parse session fields
        accomplishments_text = parse_field(session_text, 'accomplishments')
        decisions_text = parse_field(session_text, 'decisions') 
        bugs_text = parse_field(session_text, 'bugs_fixed')
        errors_text = parse_field(session_text, 'errors_encountered')
        breakthrough = parse_field(session_text, 'breakthrough_moment')
        next_priority = parse_field(session_text, 'next_session_priority')
        
        # Convert to arrays for database
        accomplishments = [s.strip() for s in accomplishments_text.split('\n') if s.strip()] if accomplishments_text else []
        decisions = [s.strip() for s in decisions_text.split('\n') if s.strip()] if decisions_text else []
        bugs_fixed = [s.strip() for s in bugs_text.split('\n') if s.strip()] if bugs_text else []
        errors = [s.strip() for s in errors_text.split('\n') if s.strip()] if errors_text else []
        
        # Parse message fields
        conversation_flow = parse_field(message_text, 'conversation_flow')
        
        # Extract numbers
        exchanges_match = re.search(r'total_exchanges:\s*(\d+)', message_text, re.IGNORECASE)
        total_exchanges = int(exchanges_match.group(1)) if exchanges_match else len(accomplishments) + len(errors)
        
        # duration_minutes is parsed but actual duration calculated from database timestamps
        
        # Calculate actual duration from database
        start_time = datetime.strptime(session_data['created_at'], '%Y-%m-%d %H:%M')
        actual_duration = int((datetime.now() - start_time).total_seconds() / 60)
        
        # Basic validation
        if not accomplishments and not decisions and not bugs_fixed:
            raise Exception("Session must have some accomplishments, decisions, or bugs fixed")
        
        if conversation_flow and len(conversation_flow) > 20:
            if "Q:" not in conversation_flow or "A:" not in conversation_flow:
                raise Exception("conversation_flow must contain Q&A format")
        
        if len(conversation_flow) > 5000:
            raise Exception("conversation_flow too long (>5000 chars)")
        
        # Calculate quality score (simplified)
        score = 5  # neutral base
        score += min(3, len(accomplishments))  # +1-3 for accomplishments
        score -= min(2, len(errors))  # -1-2 for errors  
        if breakthrough and len(breakthrough) > 30:
            score += 1  # breakthrough bonus
        if sum(len(str(x)) for x in accomplishments) + len(breakthrough) > 500:
            score += 1  # rich content
        quality_score = max(1, min(10, score))
        
        # Save to database
        conn = sqlite3.connect(".claude/memory/project.db")
        cursor = conn.cursor()
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        # Update session
        cursor.execute("""
            UPDATE sessions SET
                accomplishments = ?, decisions = ?, bugs_fixed = ?, errors_encountered = ?,
                breakthrough_moment = ?, next_session_priority = ?, quality_score = ?, ended_at = ?
            WHERE id = ?
        """, (
            json.dumps(accomplishments), json.dumps(decisions), 
            json.dumps(bugs_fixed), json.dumps(errors),
            breakthrough, next_priority, quality_score, timestamp,
            session_data['session_id']
        ))
        
        # Insert message
        cursor.execute("""
            INSERT INTO messages (session_id, conversation_flow, total_exchanges, duration_minutes, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (session_data['session_id'], conversation_flow, total_exchanges, actual_duration, timestamp))
        
        message_id = cursor.lastrowid
        
        # Create next session
        import secrets
        new_session_id = f"session_{secrets.token_hex(6)}"
        cursor.execute("""
            INSERT INTO sessions (id, job_id, created_at)
            VALUES (?, ?, ?)
        """, (new_session_id, session_data['job_id'], timestamp))
        
        conn.commit()
        conn.close()
        
        return {
            'session_id': session_data['session_id'],
            'job_id': session_data['job_id'],
            'quality_score': quality_score,
            'duration_minutes': actual_duration,
            'total_exchanges': total_exchanges,
            'accomplishments': accomplishments,
            'decisions': decisions,
            'bugs_fixed': bugs_fixed,
            'errors': errors,
            'breakthrough_moment': breakthrough,
            'next_session_priority': next_priority,
            'message_id': message_id,
            'timestamp': timestamp,
            'new_session_id': new_session_id,
            'next_session_ready': True
        }
        
    except Exception as e:
        raise Exception(f"Database save failed: {e}")

def main():
    """Main function - simple and direct"""
    try:
        # Backup database first - critical step
        backup_success = backup_database()
        if not backup_success:
            print(json.dumps({
                "error": "Failed to create database backup",
                "recommendation": "Check database file permissions and disk space"
            }))
            return 1
        
        # Parse arguments
        session_text, message_text = parse_arguments()
        if not session_text or not message_text:
            return 1
        
        # Get current session
        session_data = get_current_session()
        
        # Save everything
        result = save_to_database(session_data, session_text, message_text)
        
        # Output result
        print(json.dumps(result))
        return 0
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        return 1

if __name__ == "__main__":
    exit(main())