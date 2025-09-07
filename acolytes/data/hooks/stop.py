#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import argparse
import json
import os
import sys
import subprocess
import platform
import time
from pathlib import Path

# Add path to scripts directory for db_locator
sys.path.append(str(Path(__file__).parent.parent / 'scripts'))
from db_locator import get_project_db_path, get_project_root

def play_stop_sound():
    """Play work complete sound at 20% volume when session stops"""
    try:
        # Path to work complete sound
        sound_file = Path('~/.claude/resources/sfx/ready-ogre.wav').expanduser()
        
        if sound_file.exists():
            system = platform.system()
            
            if system == "Windows":
                # Use PowerShell Media.SoundPlayer - no windows, volume control
                try:
                    ps_script = f'''
                    Add-Type -AssemblyName PresentationCore
                    $mediaPlayer = New-Object System.Windows.Media.MediaPlayer
                    $mediaPlayer.Open([System.Uri]::new("{sound_file}"))
                    $mediaPlayer.Volume = 0.2
                    $mediaPlayer.Play()
                    Start-Sleep -Milliseconds 2000
                    $mediaPlayer.Stop()
                    $mediaPlayer.Close()
                    '''
                    subprocess.run(
                        ['powershell', '-NoProfile', '-WindowStyle', 'Hidden', '-Command', ps_script],
                        capture_output=True,
                        creationflags=subprocess.CREATE_NO_WINDOW,
                        timeout=3
                    )
                    return
                except Exception:
                    # Fallback to winsound without volume control
                    try:
                        import winsound
                        winsound.PlaySound(str(sound_file), winsound.SND_FILENAME | winsound.SND_NOWAIT)
                        return
                    except Exception:
                        pass
            elif system == "Darwin":  # macOS
                # Use afplay with reduced volume (0.2 = 20%)
                subprocess.run(
                    ['afplay', '-v', '0.2', str(sound_file.resolve())],
                    capture_output=True,
                    timeout=3
                )
            elif system == "Linux":
                # Try paplay (PulseAudio) first, then aplay (ALSA)
                try:
                    # PulseAudio with 20% volume (32768 * 0.2 = 6554)
                    subprocess.run(
                        ['paplay', '--volume=6554', str(sound_file.resolve())],
                        capture_output=True,
                        timeout=3
                    )
                except (FileNotFoundError, subprocess.CalledProcessError):
                    try:
                        # Fallback to ALSA aplay
                        subprocess.run(
                            ['aplay', str(sound_file.resolve())],
                            capture_output=True,
                            timeout=3
                        )
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        pass  # No audio player available
            
    except Exception:
        # Silently fail if sound cannot play
        pass

def generate_markdown_transcript(conversation_file, session_id):
    """Generate a beautiful Markdown transcript from the JSON conversation."""
    try:
        if not conversation_file.exists():
            return
        
        # Read the conversation
        with open(conversation_file, "r", encoding="utf-8") as f:
            conversation = json.load(f)
        
        if not conversation:
            return
        
        # Generate markdown content
        md_content = []
        md_content.append(f"# 💬 Conversación {session_id}")
        md_content.append("")
        
        # Add session metadata
        first_msg = conversation[0]
        timestamp = first_msg.get("timestamp", "")
        if timestamp:
            date_part = timestamp.split("T")[0] if "T" in timestamp else timestamp
            md_content.append(f"**📅 Fecha:** {date_part}")
        md_content.append(f"**🆔 Sesión:** `{session_id}`")
        md_content.append(f"**💭 Total mensajes:** {len(conversation)}")
        md_content.append("")
        md_content.append("---")
        md_content.append("")
        
        # Add conversation
        for i, message in enumerate(conversation, 1):
            msg_type = message.get("type", "unknown")
            content = message.get("content", "")
            timestamp = message.get("timestamp", "")
            
            # Format timestamp
            time_part = ""
            if timestamp:
                if "T" in timestamp:
                    time_part = timestamp.split("T")[1].split(".")[0] if "T" in timestamp else ""
                    time_part = f" {time_part}" if time_part else ""
            
            if msg_type == "user":
                username = os.getenv("USERNAME", "Usuario")  # Get Windows username
                md_content.append("<div style=\"text-align: right;\">")
                md_content.append("")
                md_content.append(f"### <span style=\"color: #007bff;\">♾️ {username}</span>{time_part}")
                md_content.append("")
                md_content.append(content)
                md_content.append("")
                md_content.append("</div>")
                md_content.append("")
                md_content.append("---")
                md_content.append("")
                
            elif msg_type == "assistant":
                md_content.append(f"### <span style=\"color: #d2691e;\">🤖 Claude</span>{time_part}")
                md_content.append("")
                md_content.append(content)
                md_content.append("")
                md_content.append("---")
                md_content.append("")
                
            elif msg_type == "code_change":
                # Handle code changes with special formatting
                md_content.append(f"### 📝 Code Change{time_part}")
                md_content.append("")
                md_content.append(content)
                md_content.append("")
                md_content.append("---")
                md_content.append("")
        
        # Write markdown file
        md_file = conversation_file.parent / f"{session_id}.md"
        with open(md_file, "w", encoding="utf-8") as f:
            f.write("\n".join(md_content))
            
    except Exception as e:
        print(f"Markdown generation error: {e}", file=sys.stderr)

def ensure_session_log_dir(project_root=None):
    """Ensure chat directory exists and return path."""
    try:
        # Use centralized db_locator for finding project root
        project_root_path = get_project_root()
        chat_dir = project_root_path / '.claude' / 'memory' / 'chat'
    except SystemExit:
        # Fallback if no project found
        if project_root:
            chat_dir = Path(project_root) / '.claude' / 'memory' / 'chat'
        else:
            chat_dir = Path.cwd() / '.claude' / 'memory' / 'chat'
    chat_dir.mkdir(parents=True, exist_ok=True)
    return chat_dir

def main():
    try:
        # Parse command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("--sound", action="store_true", help="Play sound when stopping")
        args = parser.parse_args()
        
        # Read JSON input from stdin
        stdin_content = sys.stdin.read().strip()
        input_data = json.loads(stdin_content)

        # Extract required fields (only get what we actually use)
        project_cwd = input_data.get("cwd", "")

        # Get OUR session ID from SQLite
        import sqlite3
        # Use centralized db_locator for finding database
        try:
            db_path = get_project_db_path()
        except SystemExit:
            # Fallback if no project database found
            if project_cwd:
                db_path = Path(project_cwd) / '.claude' / 'memory' / 'project.db'
            else:
                db_path = Path.cwd() / '.claude' / 'memory' / 'project.db'
        # Fallback to hardcoded session ID if DB doesn't exist
        our_session_id = "session_ac01e7e4e110"  # Default hardcoded session
        
        if db_path.exists():
            try:
                conn = sqlite3.connect(str(db_path))
                cursor = conn.cursor()
                # Get current active session (the one that's still running)
                cursor.execute("SELECT id FROM sessions WHERE ended_at IS NULL ORDER BY created_at DESC LIMIT 1")
                result = cursor.fetchone()
                if result:
                    our_session_id = result[0]
                conn.close()
            except (sqlite3.Error, OSError, IOError):
                pass

        # Ensure chat directory exists
        log_dir = ensure_session_log_dir(project_cwd if project_cwd else None)

        # Process transcript to extract Claude's latest response
        if "transcript_path" in input_data:
            transcript_path = input_data["transcript_path"]
            if os.path.exists(transcript_path):
                try:
                    # Read transcript and find Claude's last response
                    with open(transcript_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    
                    # Find the last assistant message (skip divider lines)
                    last_claude_response = None
                    divider_line = "─" * 85  # The standard divider
                    
                    for line in reversed(lines):
                        line = line.strip()
                        if line:
                            try:
                                data = json.loads(line)
                                if data.get("type") == "assistant" and "message" in data:
                                    message = data.get("message", {})
                                    content = message.get("content", [])
                                    if content and len(content) > 0:
                                        text_content = content[0].get("text", "") if content[0].get("type") == "text" else ""
                                        # Skip if it's just the divider line
                                        if text_content and text_content.strip() != divider_line:
                                            last_claude_response = {
                                                "session_id": our_session_id,
                                                "timestamp": data.get("timestamp"),
                                                "content": text_content,
                                                "type": "assistant",
                                                "uuid": data.get("uuid")
                                            }
                                            break
                            except json.JSONDecodeError:
                                continue
                    
                    # Save Claude's response if found
                    if last_claude_response:
                        response_file = log_dir / f"{our_session_id}.json"
                        
                        # Read existing responses or create new list
                        responses = []
                        if response_file.exists():
                            try:
                                with open(response_file, "r", encoding="utf-8") as f:
                                    responses = json.load(f)
                            except (json.JSONDecodeError, OSError, IOError):
                                responses = []
                        
                        # Add new response
                        responses.append(last_claude_response)
                        
                        # Write back with lock
                        lock_file = log_dir / f"{our_session_id}.lock"
                        max_retries = 50
                        for retry in range(max_retries):
                            if not lock_file.exists():
                                try:
                                    lock_file.touch(exist_ok=False)
                                    break
                                except FileExistsError:
                                    pass
                            time.sleep(0.1)
                        else:
                            sys.exit(0)  # Timeout
                        
                        try:
                            temp_file = response_file.with_suffix('.tmp')
                            with open(temp_file, "w", encoding="utf-8") as f:
                                json.dump(responses, f, indent=2, ensure_ascii=False)
                            temp_file.replace(response_file)
                        finally:
                            if lock_file.exists():
                                lock_file.unlink()
                        
                        # Generate markdown transcript
                        generate_markdown_transcript(response_file, our_session_id)
                            
                except Exception as e:
                    print(f"Response extraction error: {e}", file=sys.stderr)

        # Play work complete sound before exiting (only if --sound flag is provided)
        if args.sound:
            play_stop_sound()
        
        sys.exit(0)

    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)


if __name__ == "__main__":
    main()