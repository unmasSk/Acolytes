#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

import json
import sys
import subprocess
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional


def execute_save_command():
    """Execute save_session.py to close session before compaction"""
    try:
        # Path to save session script
        save_script = Path(".claude/scripts/save_session.py")
        
        if not save_script.exists():
            print("[WARNING] save_session.py not found - session will not be saved before compaction")
            return False
        
        # Execute save command
        result = subprocess.run(
            ['uv', 'run', str(save_script)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("Session closed successfully before compaction")
            # Print save output if available
            if result.stdout.strip():
                print("Save output:")
                print(result.stdout)
            return True
        else:
            print(f"ERROR: Failed to close session before compaction: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("TIMEOUT: Session close timed out - proceeding with compaction")
        return False
    except Exception as e:
        print(f"ERROR: Error executing session close: {e}")
        return False


def main():
    try:
        # Read JSON input from stdin  
        input_data = json.loads(sys.stdin.read())
        
        # Extract trigger and custom instructions
        trigger = input_data.get('trigger', 'unknown')  # "manual" or "auto"
        custom_instructions = input_data.get('custom_instructions', '')
        
        # FIRST: Execute save session before compaction
        execute_save_command()
        
        # THEN: Provide feedback based on trigger type
        if trigger == "manual":
            message = "Preparing for manual compaction"
            if custom_instructions:
                message += f"\nCustom instructions: {custom_instructions[:100]}..."
        else:  # auto
            message = "Auto-compaction triggered due to full context window"
        
        print(message)
        print("Session closed before compaction.")
        
        # Success - compaction will proceed
        sys.exit(0)
        
    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)


if __name__ == '__main__':
    main()