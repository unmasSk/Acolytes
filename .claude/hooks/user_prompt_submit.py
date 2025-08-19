#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

import argparse
import json
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional


def log_user_prompt(session_id, input_data):
    """Log user prompt - disabled to avoid JSON storage."""
    # No longer saving to JSON, prompts are already in session transcript
    pass


def detect_work_type(prompt):
    """
    Detect if prompt suggests a new JOB (large multi-session work).
    Provides hints to Claude about potential work organization.
    """
    big_job_indicators = [
        "implement complete system",
        "total migration",
        "create from scratch",
        "complete refactor",
        "complete architecture", 
        "complete system",
        "build entire",
        "develop complete",
        "full implementation"
    ]
    
    prompt_lower = prompt.lower()
    
    # Check for obvious JOB indicators
    for indicator in big_job_indicators:
        if indicator in prompt_lower:
            # Hint to Claude about potential JOB
            print("POSSIBLE JOB DETECTED - Consider asking user:")
            print("Do you want to create a new JOB for this large task?")
            print("(Check active/paused jobs with /jobs)")
            return
    
    # If no JOB detected, Claude handles normally (TODOs, regular tasks)


def validate_prompt(prompt):
    """
    Validate the user prompt for security or policy violations.
    Returns tuple (is_valid, reason).
    """
    # Example validation rules (customize as needed)
    blocked_patterns = [
        # Add any patterns you want to block
        # Example: ('rm -rf /', 'Dangerous command detected'),
    ]
    
    prompt_lower = prompt.lower()
    
    for pattern, reason in blocked_patterns:
        if pattern.lower() in prompt_lower:
            return False, reason
    
    return True, None


def main():
    try:
        # Parse command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--validate', action='store_true', 
                          help='Enable prompt validation')
        parser.add_argument('--log-only', action='store_true',
                          help='Only log prompts, no validation or blocking')
        args = parser.parse_args()
        
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Extract session_id and prompt
        session_id = input_data.get('session_id', 'unknown')
        prompt = input_data.get('prompt', '')
        
        # Log the user prompt
        log_user_prompt(session_id, input_data)
        
        # Detect work type and provide hints to Claude
        detect_work_type(prompt)
        
        # Validate prompt if requested and not in log-only mode
        if args.validate and not args.log_only:
            is_valid, reason = validate_prompt(prompt)
            if not is_valid:
                # Exit code 2 blocks the prompt with error message
                print(f"Prompt blocked: {reason}", file=sys.stderr)
                sys.exit(2)
        
        # Add context information (optional)
        # You can print additional context that will be added to the prompt
        # Example: print(f"Current time: {datetime.now()}")
        
        # Success - prompt will be processed
        sys.exit(0)
        
    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)


if __name__ == '__main__':
    main()