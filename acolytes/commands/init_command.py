"""
Init command for Acolytes - System initialization.

Initializes the Acolytes system with default configuration.
"""

import sys
import json
import shutil
import subprocess
import platform
from pathlib import Path
from typing import Dict, Any
from datetime import datetime
try:
    from importlib.resources import files
    use_importlib = True
except ImportError:
    # Fallback for older Python versions
    import pkg_resources
    use_importlib = False


def run() -> None:
    """
    Initialize Acolytes system in local .claude directory.

    Creates the complete Acolytes infrastructure in the current project's
    .claude directory instead of the global .claude location.

    Raises:
        SystemExit: If initialization fails
    """
    print("Initializing Acolytes system...")
    
    try:
        # Step 1: Install uv if not present
        _install_uv_if_needed()
        
        # Step 2: Copy data files to .claude/
        _copy_data_files()
        
        # Step 3: Generate settings.json
        _generate_settings_json()
        
        # Step 4: Create local project structure
        _create_local_project_structure()
        
        # Step 5: Show final status
        _show_final_status()
        
        print("[OK] Initialization complete!")
        
    except Exception as e:
        print(f"[ERROR] Initialization failed: {e}")
        sys.exit(1)


def _install_uv_if_needed() -> None:
    """
    Install uv package manager if not present on the system.

    Attempts to install uv using platform-specific methods:
    - Windows: winget or PowerShell
    - Unix-like: curl installer

    Raises:
        subprocess.CalledProcessError: If installation fails
    """
    print("Checking for uv installation...")
    
    # Check if uv is already installed
    try:
        subprocess.run(["uv", "--version"], check=True, capture_output=True, text=True)
        print("[OK] uv is already installed")
        return
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("uv not found, installing...")
    
    system = platform.system().lower()
    
    try:
        if system == "windows":
            _install_uv_windows()
        else:
            _install_uv_unix()
        print("[OK] uv installed successfully")
    except Exception as e:
        print(f"[WARNING] Could not install uv automatically: {e}")
        print("Please install uv manually from https://github.com/astral-sh/uv")


def _install_uv_windows() -> None:
    """
    Install uv on Windows using winget or PowerShell fallback.

    Tries winget first, then falls back to PowerShell installer.

    Raises:
        subprocess.CalledProcessError: If both installation methods fail
    """
    # Try winget first
    try:
        print("Attempting installation with winget...")
        subprocess.run(["winget", "install", "astral-sh.uv"], check=True, capture_output=True)
        return
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    # Fallback to PowerShell installer
    print("Attempting installation with PowerShell...")
    powershell_cmd = [
        "powershell", "-Command",
        "Invoke-RestMethod https://astral.sh/uv/install.ps1 | Invoke-Expression"
    ]
    subprocess.run(powershell_cmd, check=True)


def _install_uv_unix() -> None:
    """
    Install uv on Linux/Mac using curl installer.

    Downloads and executes the official uv installer script.

    Raises:
        subprocess.CalledProcessError: If installation fails
    """
    print("Installing uv with curl...")
    curl_cmd = [
        "curl", "-LsSf", "https://astral.sh/uv/install.sh"
    ]
    sh_cmd = ["sh"]
    
    # Pipe curl output to sh
    curl_process = subprocess.Popen(curl_cmd, stdout=subprocess.PIPE)
    subprocess.run(sh_cmd, stdin=curl_process.stdout, check=True)
    curl_process.wait()


def _copy_data_files() -> None:
    """
    Copy data files to local .claude/ directory.

    Copies all necessary files from the acolytes package data directory
    to the current project's .claude directory instead of global .claude.

    Creates the following structure:
    - .claude/agents/
    - .claude/commands/
    - .claude/scripts/
    - .claude/hooks/
    - .claude/resources/

    Raises:
        FileNotFoundError: If source data directory cannot be located
        PermissionError: If unable to create target directories
    """
    print("Copying data files to .claude/...")

    # Get target directory - LOCAL .claude in current project
    claude_dir = Path.cwd() / ".claude"
    claude_dir.mkdir(exist_ok=True)
    
    # Get package data directory
    try:
        if use_importlib:
            # Modern way using importlib.resources
            data_dir = Path(str(files('acolytes') / 'data'))
        else:
            # Fallback using pkg_resources
            data_dir = Path(pkg_resources.resource_filename('acolytes', 'data'))
    except Exception:
        # Fallback for development/editable installs
        current_dir = Path(__file__).parent.parent
        data_dir = current_dir / "data"
    
    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")
    
    # Define directories to copy
    directories_to_copy = ['agents', 'commands', 'scripts', 'hooks', 'resources']
    total_files_copied = 0

    for dir_name in directories_to_copy:
        source_dir = data_dir / dir_name
        target_dir = claude_dir / dir_name
        
        if source_dir.exists():
            print(f"  [DIR] Copying {dir_name}/...")
            
            # Create target directory
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # Copy files recursively
            files_copied = _copy_directory_contents(source_dir, target_dir)
            total_files_copied += files_copied
            print(f"    [OK] {files_copied} files copied")
        else:
            print(f"  [WARNING] Directory not found: {source_dir}")
    
    # Note: All agents (including setup.*, flags, plan) are now in the agents directory
    # No need for separate internal agents handling
    
    print(f"[OK] Total files copied: {total_files_copied}")


def _copy_directory_contents(source: Path, target: Path) -> int:
    """
    Copy directory contents recursively and return file count.

    Args:
        source: Source directory path
        target: Target directory path

    Returns:
        Number of files copied

    Raises:
        PermissionError: If unable to copy files
        OSError: If file system operation fails
    """
    files_copied = 0
    
    for item in source.rglob('*'):
        if item.is_file():
            # Calculate relative path
            rel_path = item.relative_to(source)
            target_file = target / rel_path
            
            # Create parent directories if needed
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy file
            shutil.copy2(item, target_file)
            files_copied += 1
    
    return files_copied


def _generate_settings_json() -> None:
    """
    Generate settings.json configuration file with local paths.

    Creates settings.json in the local .claude directory with all paths
    configured to use the local .claude structure instead of global .claude.

    Raises:
        PermissionError: If unable to write settings file
        OSError: If file system operation fails
    """
    print("Generating settings.json...")

    claude_dir = Path.cwd() / ".claude"
    settings_file = claude_dir / "settings.json"
    
    # Detect Python command
    python_cmd = _detect_python_command()
    
    # Check if uv is available
    uv_available = _is_uv_available()
    
    # Generate settings
    settings = _create_settings_config(python_cmd, uv_available)
    
    # Write settings file
    with open(settings_file, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Settings saved to {settings_file}")


def _detect_python_command() -> str:
    """
    Detect the best Python command to use on this system.

    Tests various Python command candidates and returns the first
    one that supports Python 3.

    Returns:
        Python command string (e.g., 'python3', 'python', 'py -3')
    """
    # List of candidates: can be single command or command with args
    candidates = [
        ['python3', '--version'],
        ['python', '--version'],
        ['py', '-3', '--version'],  # Windows launcher with Python 3
        ['py', '--version']          # Windows launcher fallback
    ]
    
    for cmd_list in candidates:
        try:
            result = subprocess.run(cmd_list, 
                                  capture_output=True, text=True, check=True)
            # Check both stdout and stderr (some versions print to stderr)
            output = result.stdout + result.stderr
            if 'Python 3' in output:
                # Return the command part (without --version)
                if cmd_list[0] == 'py' and len(cmd_list) > 2:
                    return 'py -3'  # Return Windows launcher with -3 flag
                return cmd_list[0]
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    
    # Default fallback
    return 'python'


def _is_uv_available() -> bool:
    """
    Check if uv package manager is available on the system.

    Returns:
        True if uv is available, False otherwise
    """
    try:
        subprocess.run(['uv', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def _create_settings_config(python_cmd: str, uv_available: bool) -> Dict[str, Any]:
    """
    Create the settings configuration dictionary in Claude Code format.

    Generates a complete Claude Code settings configuration with hooks,
    permissions, and commands configured for local .claude directory.

    Args:
        python_cmd: Python command to use (e.g., 'python3')
        uv_available: Whether uv package manager is available

    Returns:
        Settings dictionary ready for JSON serialization
    """
    
    # Base Python command
    if uv_available:
        base_cmd = "uv run python"
    else:
        base_cmd = python_cmd
    
    # Get the correct path format based on OS
    # IMPORTANT: The hooks are installed in .claude/ (local project directory)
    # Windows doesn't expand relative paths in some contexts, so we need absolute paths
    if platform.system() == 'Windows':
        # Windows needs full absolute path with forward slashes
        claude_path = str(Path.cwd() / ".claude").replace('\\', '/')
        script_prefix = claude_path
    else:
        # Unix-like systems can use absolute path
        script_prefix = str(Path.cwd() / ".claude")
    
    settings = {
        "permissions": {
            "allow": [
                "Bash(mkdir:*)",
                "Bash(uv:*)",
                "Bash(find:*)",
                "Bash(mv:*)",
                "Bash(grep:*)",
                "Bash(npm:*)",
                "Bash(ls:*)",
                "Bash(cp:*)",
                "Write",
                "Edit",
                "Bash(chmod:*)",
                "Bash(touch:*)"
            ],
            "deny": []
        },
        "statusLine": {
            "type": "command",
            "command": f"{base_cmd} {script_prefix}/scripts/status_line.py",
            "padding": 0
        },
        "disableAllHooks": False,
        "hooks": {
            "SessionStart": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": f"{base_cmd} {script_prefix}/hooks/session_start.py"
                        }
                    ]
                }
            ],
            "PostToolUse": [
            {
                "matcher": "",
                "hooks": [
                {
                    "type": "command",
                    "command": f"{base_cmd} {script_prefix}/hooks/post_tool_use.py"
                }
                ]
            },
            {
                "matcher": "TodoWrite",
                "hooks": [
                {
                    "type": "command",
                    "command": f"{base_cmd} {script_prefix}/hooks/post_tool_use.py --todowrite"
                }
                ]
            },
            {
                "matcher": "Edit|Write|MultiEdit|Update",
                "hooks": [
                {
                    "type": "command",
                    "command": f"{base_cmd} {script_prefix}/hooks/capture_code_changes.py"
                }
                ]
            }
            ],
            "PreCompact": [
                {
                    "matcher": "",
                    "hooks": [
                        {
                            "type": "command",
                            "command": f"{base_cmd} {script_prefix}/hooks/pre_compact.py"
                        }
                    ]
                }
            ],
            "PreToolUse": [
                {
                    "matcher": "",
                    "hooks": [
                        {
                            "type": "command",
                            "command": f"{base_cmd} {script_prefix}/hooks/pre_tool_use.py"
                        }
                    ]
                }
            ],
            "UserPromptSubmit": [
                {
                    "matcher": "",
                    "hooks": [
                        {
                            "type": "command",
                            "command": f"{base_cmd} {script_prefix}/hooks/user_prompt_submit.py"
                        }
                    ]
                }
            ],
            "Stop": [
                {
                    "matcher": "",
                    "hooks": [
                        {
                            "type": "command",
                            "command": f"{base_cmd} {script_prefix}/hooks/stop.py --sound"
                        }
                    ]
                }
            ],
            "SubagentStop": [
                {
                    "matcher": "",
                    "hooks": [
                        {
                            "type": "command",
                            "command": f"{base_cmd} {script_prefix}/hooks/subagent_stop.py --sound"
                        }
                    ]
                }
            ]
        }
    }
    
    return settings


def _create_local_project_structure() -> None:
    """
    Create local .claude/ structure in current project directory.

    Creates the complete directory structure needed for local project operation:
    - .claude/project/ (for project documentation)
    - .claude/memory/ (for persistent data)
    - .claude/memory/chat/ (for session history)
    - .claude/agents/ (for project-specific acolytes)

    Also creates initial session files to ensure hooks work properly.

    Raises:
        PermissionError: If unable to create directories
        OSError: If file system operation fails
    """
    print("[LOCAL] Creating local project structure...")
    
    # Get current working directory
    project_dir = Path.cwd()
    claude_project_dir = project_dir / ".claude"
    
    # Create main .claude directory
    claude_project_dir.mkdir(exist_ok=True)
    
    # Create subdirectories
    directories = {
        'project': claude_project_dir / 'project',
        'memory': claude_project_dir / 'memory',
        'memory_chat': claude_project_dir / 'memory' / 'chat',
        'agents': claude_project_dir / 'agents',  # Para acólitos activos del proyecto
        'resources_agents': claude_project_dir / 'resources' / 'agents'  # Pool de agentes no activos
    }
    
    for name, path in directories.items():
        path.mkdir(parents=True, exist_ok=True)
        if name == 'memory_chat':
            print("  [OK] Created memory/chat/")
        elif name == 'resources_agents':
            print("  [OK] Created resources/agents/")
        else:
            print(f"  [OK] Created {name}/")
    
    # Create initial session files - ALWAYS use these hardcoded IDs
    # This ensures hooks work even before database exists
    chat_dir = directories['memory_chat']
    
    # Find available filenames with uniqueness guard
    base_name = "session_ac01e7e4e110"
    json_file = chat_dir / f"{base_name}.json"
    md_file = chat_dir / f"{base_name}.md"
    
    # If files exist, find next available number
    counter = 1
    while json_file.exists() or md_file.exists():
        json_file = chat_dir / f"{base_name}_{counter}.json"
        md_file = chat_dir / f"{base_name}_{counter}.md"
        counter += 1
    
    # Create JSON file with ISO timestamp
    timestamp = datetime.utcnow().isoformat() + "Z"
    json_content = {
        "session_id": "session_ac01e7e4e110",
        "job_id": "job_5e770c0deba5e",
        "created_at": timestamp,
        "messages": []
    }
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_content, f, indent=2, ensure_ascii=False)
    print(f"  [OK] Created {json_file.name}")
    
    # Create MD file
    md_content = f"""# Session: session_ac01e7e4e110

## Job: Project Setup (job_5e770c0deba5e)

### Session Start
- **Created**: {timestamp}
- **Purpose**: Acolytes for Claude Code initialization

### Notes
This is the initial session created during project setup.

---
"""
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"  [OK] Created {md_file.name}")
    
    print(f"  [PATH] Project structure created at: {claude_project_dir}")


def _show_final_status() -> None:
    """
    Show final status and requirements check.

    Displays a comprehensive status report including:
    - Directory structure verification
    - Settings file confirmation
    - Python and uv availability
    - Next steps for user
    """
    print("\n[STATUS] Final Status Check:")

    claude_dir = Path.cwd() / ".claude"
    
    # Check directory structure
    required_dirs = ['agents', 'commands', 'scripts', 'hooks', 'resources']
    for dir_name in required_dirs:
        dir_path = claude_dir / dir_name
        if dir_path.exists():
            file_count = len(list(dir_path.rglob('*')))
            print(f"  [OK] {dir_name}/ ({file_count} files)")
        else:
            print(f"  [ERROR] {dir_name}/ (missing)")
    
    # Check settings file
    settings_file = claude_dir / "settings.json"
    if settings_file.exists():
        print("  [OK] settings.json")
    else:
        print("  [ERROR] settings.json (missing)")
    
    # Check Python and uv
    python_cmd = _detect_python_command()
    uv_available = _is_uv_available()
    
    print(f"  [OK] Python: {python_cmd}")
    if uv_available:
        print("  [OK] uv: available")
    else:
        print("  [WARNING] uv: not available (recommended)")
    
    print("\nNext steps:")
    print("  1. Go to the path to your project")
    print("  2. Run: claude --dangerously-skip-permissions")
    print("  3. Type: /setup")
    print("  4. Y déjate fluir...")