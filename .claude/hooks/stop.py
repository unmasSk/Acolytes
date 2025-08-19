#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import argparse
import json
import sys
import subprocess
from datetime import datetime
from pathlib import Path

def play_notification_sound():
    """Play work complete sound at 50% volume when session stops"""
    try:
        # Path to work complete sound
        sound_file = Path('.claude/resources/sfx/work-complete.wav')
        
        if sound_file.exists():
            # Play the custom sound file at 50% volume using PowerShell
            powershell_cmd = f'''
            Add-Type -AssemblyName presentationCore
            $mediaPlayer = New-Object System.Windows.Media.MediaPlayer
            $mediaPlayer.Open([System.Uri]::new("{sound_file.resolve()}"))
            $mediaPlayer.Volume = 0.2
            $mediaPlayer.Play()
            Start-Sleep -Milliseconds 2000
            $mediaPlayer.Stop()
            $mediaPlayer.Close()
            '''
            
            subprocess.run(
                ['powershell', '-Command', powershell_cmd],
                capture_output=True,
                timeout=5
            )
        else:
            # Fallback to system sound if file not found
            subprocess.run(
                ['powershell', '-Command', '[System.Media.SystemSounds]::Asterisk.Play()'],
                capture_output=True,
                timeout=1
            )
            
    except subprocess.TimeoutExpired:
        pass  # Fail silently if timeout
    except Exception:
        pass  # Fail silently if sound doesn't work

def print_completion_line():
    """Print a visual completion line to the terminal."""
    try:
        # Get terminal width, default to 80 if not available
        try:
            import shutil
            terminal_width = shutil.get_terminal_size().columns
        except:
            terminal_width = 80
        
        # Ensure minimum width and cap maximum
        terminal_width = max(40, min(terminal_width, 120))
        
        # Create a fancy completion line
        line_char = "═"
        edge_char = "╬"
        middle_text = " CLAUDE COMPLETADO "
        
        # Calculate padding
        text_length = len(middle_text)
        if text_length >= terminal_width - 4:
            # If text is too long, use simpler format
            print("\n" + "═" * terminal_width)
            print("CLAUDE COMPLETADO".center(terminal_width))
            print("═" * terminal_width + "\n")
        else:
            # Calculate side lengths for proper centering
            remaining = terminal_width - text_length - 2  # -2 for edge chars
            left_side = remaining // 2
            right_side = remaining - left_side
            
            # Create completion line
            completion_line = (
                edge_char + 
                line_char * left_side + 
                middle_text + 
                line_char * right_side + 
                edge_char
            )
            
            print("\n" + completion_line + "\n")
        
        # Force flush output
        sys.stdout.flush()
        
    except Exception:
        # Fallback to simple line if anything fails
        try:
            print("\n" + "="*60)
            print("CLAUDE COMPLETADO".center(60))
            print("="*60 + "\n")
            sys.stdout.flush()
        except:
            pass  # Ultimate fallback - do nothing

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--chat', action='store_true', help='Enable chat mode with formatted output')
    args = parser.parse_args()
    
    try:
        # Read JSON input from stdin (validate format)
        input_data = sys.stdin.read()
        
        # Validate JSON
        json.loads(input_data)
        
        # Test simple print
        print("OKO OKOKOKOKO ESTA FUNCIONANDO HOSTIA")
        print("CLAUDE COMPLETADO")
        print("OKO OKOKOKOKO OKO OKO")
        sys.stdout.flush()
        
        # Start sound in background
        import threading
        sound_thread = threading.Thread(target=play_notification_sound)
        sound_thread.daemon = True
        sound_thread.start()
        
        # Give a moment for sound to start
        import time
        time.sleep(0.1)
        
    except json.JSONDecodeError:
        print("-" * 60, file=sys.stderr)
        print("Session completed (invalid JSON)", file=sys.stderr)
        sys.stderr.flush()
        
    except Exception as e:
        print(f"Stop hook error: {e}", file=sys.stderr)
        print("-" * 60, file=sys.stderr)
        print("Session completed (with errors)", file=sys.stderr)
        sys.stderr.flush()

if __name__ == '__main__':
    main()