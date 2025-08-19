#!/usr/bin/env python3
"""
Setup MCP SQLite for the project.
This script configures the MCP server to point to project.db
"""
import os
import sys
import subprocess
from pathlib import Path

def setup_mcp_sqlite():
    """Configure MCP SQLite server for the project"""
    
    # 1. Get current directory and verify we're in project root
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    # Check for .claude directory
    claude_dir = current_dir / ".claude"
    if not claude_dir.exists():
        print("ERROR: .claude directory not found!")
        print("Please run this from your project root directory")
        return False
    
    # 2. Ensure memory directory exists
    memory_dir = claude_dir / "memory"
    memory_dir.mkdir(exist_ok=True)
    
    # 3. Set database path
    db_name = "project.db"
    db_path = memory_dir / db_name
    
    # 4. Create database if it doesn't exist
    if not db_path.exists():
        print(f"Creating database: {db_path}")
        # Initialize with schema
        init_sql = claude_dir / "scripts" / "init_db.sql"
        if init_sql.exists():
            import sqlite3
            conn = sqlite3.connect(str(db_path))
            with open(init_sql, 'r') as f:
                conn.executescript(f.read())
            conn.commit()
            conn.close()
            print("Database created with schema")
        else:
            # Create empty database
            open(db_path, 'a').close()
            print("Empty database created")
    
    # 5. Get absolute path for MCP configuration
    absolute_db_path = str(db_path.absolute())
    
    # For Windows, ensure proper path format
    if os.name == 'nt':
        # Windows path - use forward slashes or escaped backslashes
        absolute_db_path = absolute_db_path.replace('\\', '\\\\')
    
    print(f"\nDatabase path: {absolute_db_path}")
    
    # 6. Build MCP command
    # The command needs the full JSON configuration
    import json
    
    # Create the configuration JSON
    config = {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-sqlite", str(db_path.absolute())]
    }
    config_json = json.dumps(config)
    
    mcp_args = [
        "claude", "mcp", "add",
        "--transport", "stdio",
        "sqlite",
        config_json
    ]
    
    print("\nConfiguring MCP SQLite...")
    print(f"Command: {' '.join(map(str, mcp_args))}")
    
    # 7. Execute the command
    try:
        result = subprocess.run(
            mcp_args,
            capture_output=True,
            text=True,
            shell=False  # Always pass args as a list to avoid shell quoting issues
        )
        
        if result.returncode == 0:
            print("\n[SUCCESS] MCP SQLite configured!")
            print("\n[IMPORTANT] Please restart Claude Code for changes to take effect")
            print(f"\n[INFO] Your database is at: .claude/memory/{db_name}")
            return True
        else:
            # Check if it's because the server already exists
            if "already exists" in result.stderr:
                print("\n[INFO] MCP SQLite server already exists")
                print("[ACTION] To update it, first remove with: claude mcp remove sqlite")
                print("[ACTION] Then run this script again")
                return True  # Consider it a success since it's configured
            
            print("\n[ERROR] Failed to configure MCP")
            if result.stderr:
                print(f"Error details: {result.stderr}")
            if result.stdout:
                print(f"Output: {result.stdout}")
            
            # Provide manual fallback instructions
            print("\n[MANUAL] Configuration instructions:")
            print("Add this to your claude_desktop_config.json:")
            print(f'''
"sqlite": {{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-sqlite", "{absolute_db_path}"]
}}
''')
            return False
            
    except FileNotFoundError:
        print("\n[ERROR] 'claude' command not found")
        print("Is Claude Code CLI installed and in PATH?")
        
        # Provide manual instructions
        print("\n[MANUAL] Configuration required:")
        print("1. Open: %APPDATA%\\Claude\\claude_desktop_config.json")
        print("2. Add the sqlite server configuration:")
        print(f'''
"sqlite": {{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-sqlite", "{absolute_db_path}"]
}}
''')
        print("3. Restart Claude Code")
        return False
    
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = setup_mcp_sqlite()
    sys.exit(0 if success else 1)