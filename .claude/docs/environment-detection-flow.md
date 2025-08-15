# 🌍 Environment Detection Flow Documentation

## Overview

The Environment Detection System ensures ClaudeSquad agents work seamlessly across all platforms (Windows, WSL, macOS, Linux) by automatically detecting the shell environment and available commands.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  /detect-env Command                 │
│                                                      │
│  Detects: OS, Shell, Commands, Paths                │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│           .claude/memory/environment.json           │
│                                                      │
│  Persistent storage of detection results            │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│              All ClaudeSquad Agents                 │
│                                                      │
│  Read environment.json on invocation                │
│  Use appropriate commands based on detection        │
└─────────────────────────────────────────────────────┘
```

## Detection Flow

### 1. Initial Setup Phase

When `/setup` is executed:

```yaml
Phase 0: Environment Verification
  └── Check prerequisites (Git, Node, Python, etc.)
  
Phase 0.5: Environment Detection [NEW]
  └── Execute /detect-env command
      └── Creates .claude/memory/environment.json
      
Phase 1: Parallel Analysis
  └── 4 setup agents read environment.json
      └── Use appropriate commands for the environment
```

### 2. Detection Process

The `/detect-env` command performs:

```bash
1. OS Detection
   ├── Check $OSTYPE variable
   ├── Check for WSL (/proc/sys/kernel/osrelease)
   ├── Check for Windows ($WINDIR)
   └── Determine: Windows/WSL/Linux/macOS

2. Shell Detection
   ├── Check $MSYSTEM (Git Bash: MINGW64/MINGW32/MSYS)
   ├── Check $WSL_DISTRO_NAME (WSL)
   ├── Check $SHELL (Bash/Zsh)
   └── Determine shell environment

3. Command Availability
   ├── Test Unix commands (ls, grep, find, cat)
   ├── Test PowerShell (powershell.exe, pwsh)
   ├── Test Git availability
   └── Determine available toolchains

4. Save Results
   └── Write to .claude/memory/environment.json
```

### 3. Environment Detection Results

```json
{
  "detected_at": "2025-01-14T18:00:00Z",
  "os_type": "Windows (Unix-like)",
  "shell_env": "Git Bash (MINGW64)",
  "unix_available": true,
  "powershell_available": true,
  "msystem": "MINGW64",
  "recommendations": {
    "use_unix_commands": true,
    "path_separator": "/",
    "line_endings": "LF"
  }
}
```

## Agent Integration

### Auto-Loading Environment

All agents MUST include this at the beginning of their execution:

```markdown
## Auto-Load Environment Detection
**MANDATORY FIRST ACTION**: When invoked, I MUST first read the environment detection:
```bash
# Read .claude/memory/environment.json to know which commands to use
# If file doesn't exist, use Unix commands as default (most compatible)
```
```

### Using Detection Results

Agents adapt their commands based on detection:

```bash
# Read environment detection
ENV_JSON=".claude/memory/environment.json"
if [[ -f "$ENV_JSON" ]]; then
    USE_UNIX=$(grep '"use_unix_commands":true' "$ENV_JSON")
    if [[ -n "$USE_UNIX" ]]; then
        # Use Unix commands
        ls -la
        grep "pattern" file
        find . -name "*.txt"
    else
        # Use PowerShell commands
        powershell -Command "Get-ChildItem"
        powershell -Command "Select-String -Pattern 'pattern' -Path file"
        powershell -Command "Get-ChildItem -Recurse -Filter '*.txt'"
    fi
else
    # Default to Unix (most compatible)
    ls -la
fi
```

## Environment Types

### 1. Git Bash (MINGW64/MINGW32)
- **Detected by**: `$MSYSTEM` variable
- **Commands**: Full Unix toolchain available
- **Paths**: Use forward slashes (/)
- **Special considerations**: Native Windows paths accessible via `/c/Users/`

### 2. WSL (Windows Subsystem for Linux)
- **Detected by**: `/proc/sys/kernel/osrelease` contains "Microsoft" or "WSL"
- **Commands**: Full Linux environment
- **Paths**: Unix paths, Windows drives mounted at `/mnt/c/`
- **Special considerations**: Can execute Windows binaries

### 3. PowerShell
- **Detected by**: `$PSVersionTable` variable
- **Commands**: PowerShell cmdlets
- **Paths**: Use backslashes (\) or forward slashes
- **Special considerations**: Different command syntax

### 4. Native Linux/macOS
- **Detected by**: `$OSTYPE` variable
- **Commands**: Standard Unix commands
- **Paths**: Unix paths (/)
- **Special considerations**: No Windows-specific features

## Command Equivalents

| Operation | Unix/Git Bash | PowerShell |
|-----------|--------------|------------|
| List files | `ls -la` | `Get-ChildItem -Force` |
| Search text | `grep "pattern" file` | `Select-String -Pattern "pattern" -Path file` |
| Find files | `find . -name "*.txt"` | `Get-ChildItem -Recurse -Filter "*.txt"` |
| Read file | `cat file` | `Get-Content file` |
| Create directory | `mkdir -p dir/subdir` | `New-Item -ItemType Directory -Force -Path "dir\subdir"` |
| Check file exists | `[[ -f file ]]` | `Test-Path file` |
| First 10 lines | `head -n 10` | `Select-Object -First 10` |

## Benefits

### 1. Cross-Platform Compatibility
- Works on Windows (Git Bash, PowerShell, WSL)
- Works on macOS and Linux
- No manual configuration needed

### 2. Error Prevention
- No more "command not found" errors
- Appropriate commands for each environment
- Fallback strategies

### 3. Performance Optimization
- Use native commands when available
- Avoid unnecessary command translation
- Efficient execution paths

### 4. Developer Experience
- Automatic detection
- Persistent across sessions
- Clear recommendations

## Troubleshooting

### Issue: Detection Not Working

**Solution**: Run manually
```bash
claude /detect-env
```

### Issue: Wrong Environment Detected

**Solution**: Check environment variables
```bash
echo $MSYSTEM
echo $OSTYPE
echo $SHELL
uname -s
```

### Issue: Agents Not Reading Detection

**Solution**: Verify file exists
```bash
cat .claude/memory/environment.json
```

### Issue: Commands Still Failing

**Solution**: Force regeneration
```bash
rm .claude/memory/environment.json
claude /detect-env
```

## Implementation Checklist

- [x] Create `/detect-env` command
- [x] Add Phase 0.5 to `/setup` workflow
- [x] Update agents to auto-read environment.json
- [x] Document command equivalents
- [x] Test on multiple platforms

## Future Enhancements

1. **Auto-detection on first command failure**
2. **Environment-specific optimizations**
3. **Custom command mappings**
4. **Performance metrics per environment**
5. **Automatic updates when environment changes**

---

*Documentation created by ClaudeSquad-commands-specialist*
*Last updated: 2025-01-14*