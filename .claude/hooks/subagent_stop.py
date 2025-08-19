#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
Minimal stub for subagent_stop hook to prevent Claude Code errors.
This hook was removed but Claude Code still references it.
Since hooks are disabled in settings.json, this does nothing.
"""

def main():
    """Do nothing - hooks are disabled"""
    pass

if __name__ == "__main__":
    main()