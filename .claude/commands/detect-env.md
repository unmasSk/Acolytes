---
name: detect-env
description: Detects the current shell environment and OS for cross-platform compatibility
version: 1.0.0
author: ClaudeSquad-commands-specialist
---

# /detect-env - Environment Detection Command

## Purpose
Detects the current operating system, shell environment, and terminal type to help agents use the correct commands for cross-platform compatibility.

## Usage
```
claude /detect-env
```

## Detection Process

The command performs multiple checks to accurately identify the environment:

### 1. Primary OS Detection
```bash
# Check if running in Windows native
if [[ -n "$SYSTEMROOT" ]] && [[ -n "$WINDIR" ]]; then
    OS_TYPE="Windows"
fi

# Check for WSL
if grep -qEi "(Microsoft|WSL)" /proc/sys/kernel/osrelease 2>/dev/null; then
    OS_TYPE="WSL"
fi

# Check for macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macOS"
fi

# Check for Linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="Linux"
fi
```

### 2. Shell/Terminal Detection
```bash
# Check for Git Bash / MSYS2 / MinGW
if [[ -n "$MSYSTEM" ]]; then
    case "$MSYSTEM" in
        MINGW64)
            SHELL_ENV="Git Bash (MINGW64)"
            UNIX_TOOLS="Available"
            ;;
        MINGW32)
            SHELL_ENV="Git Bash (MINGW32)"
            UNIX_TOOLS="Available"
            ;;
        MSYS)
            SHELL_ENV="MSYS"
            UNIX_TOOLS="Available"
            ;;
        UCRT64)
            SHELL_ENV="UCRT64"
            UNIX_TOOLS="Available"
            ;;
        *)
            SHELL_ENV="Unknown MSYS variant"
            UNIX_TOOLS="Maybe"
            ;;
    esac
fi

# Check for PowerShell
if [[ -n "$PSVersionTable" ]]; then
    SHELL_ENV="PowerShell"
    UNIX_TOOLS="Not Available"
fi

# Check for Command Prompt
if [[ "$COMSPEC" == *"cmd.exe"* ]] && [[ -z "$MSYSTEM" ]]; then
    SHELL_ENV="Command Prompt"
    UNIX_TOOLS="Not Available"
fi

# Check for WSL Bash
if [[ -f "/etc/wsl.conf" ]]; then
    SHELL_ENV="WSL Bash"
    UNIX_TOOLS="Available"
fi

# Check uname for additional info
UNAME_OUTPUT=$(uname -s 2>/dev/null || echo "Not Available")
```

### 3. Command Availability Check
```bash
# Test if Unix commands are available
check_unix_commands() {
    local commands_available=true
    
    for cmd in ls grep find cat head tail mkdir; do
        if ! command -v $cmd >/dev/null 2>&1; then
            commands_available=false
            break
        fi
    done
    
    if $commands_available; then
        echo "Unix commands: Available"
    else
        echo "Unix commands: Not Available"
    fi
}

# Test if PowerShell is available
check_powershell() {
    if command -v powershell >/dev/null 2>&1 || command -v pwsh >/dev/null 2>&1; then
        echo "PowerShell: Available"
    else
        echo "PowerShell: Not Available"
    fi
}
```

## Output Format

```yaml
ENVIRONMENT_DETECTION:
  os:
    type: "Windows|WSL|macOS|Linux"
    version: "version if available"
    architecture: "x64|x86|arm64"
    
  shell:
    type: "Git Bash|PowerShell|Bash|Zsh|Command Prompt"
    variant: "MINGW64|MINGW32|MSYS|WSL"
    terminal: "Windows Terminal|mintty|cmd.exe|iTerm2"
    
  environment:
    MSYSTEM: "MINGW64|MINGW32|MSYS|null"
    PATH_SEPARATOR: ";|:"
    HOME: "/home/user|C:\Users\user"
    SHELL: "/bin/bash|null"
    
  commands:
    unix_tools: "Available|Not Available"
    powershell: "Available|Not Available"
    git: "Available|Not Available"
    python: "Available|Not Available"
    node: "Available|Not Available"
    
  recommendations:
    preferred_commands: "Unix|PowerShell|Mixed"
    path_format: "Unix (/)|Windows (\)"
    line_endings: "LF|CRLF"
```

## Implementation

```bash
#!/bin/bash

echo "🔍 Detecting Environment..."
echo "=========================="

# OS Detection
OS_TYPE="Unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if grep -qEi "(Microsoft|WSL)" /proc/sys/kernel/osrelease 2>/dev/null; then
        OS_TYPE="WSL"
    else
        OS_TYPE="Linux"
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macOS"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    OS_TYPE="Windows (Unix-like)"
elif [[ -n "$WINDIR" ]]; then
    OS_TYPE="Windows"
else
    OS_TYPE="Unknown"
fi

# Shell Detection
SHELL_ENV="Unknown"
if [[ -n "$MSYSTEM" ]]; then
    SHELL_ENV="Git Bash ($MSYSTEM)"
elif [[ -n "$WSL_DISTRO_NAME" ]]; then
    SHELL_ENV="WSL ($WSL_DISTRO_NAME)"
elif [[ "$SHELL" == *"bash"* ]]; then
    SHELL_ENV="Bash"
elif [[ "$SHELL" == *"zsh"* ]]; then
    SHELL_ENV="Zsh"
elif [[ -n "$PSVersionTable" ]]; then
    SHELL_ENV="PowerShell"
fi

# Command Availability
UNIX_CMDS="❌"
if command -v ls >/dev/null 2>&1 && command -v grep >/dev/null 2>&1; then
    UNIX_CMDS="✅"
fi

PWSH_CMDS="❌"
if command -v powershell >/dev/null 2>&1 || command -v pwsh >/dev/null 2>&1; then
    PWSH_CMDS="✅"
fi

# Output Results
echo ""
echo "📊 DETECTION RESULTS:"
echo "====================="
echo "🖥️  OS Type:        $OS_TYPE"
echo "🐚 Shell:          $SHELL_ENV"
echo "📁 Home:           $HOME"
echo "🔧 Unix Commands:  $UNIX_CMDS"
echo "🔷 PowerShell:     $PWSH_CMDS"
echo ""

# Recommendations
echo "💡 RECOMMENDATIONS:"
echo "==================="
if [[ "$SHELL_ENV" == *"Git Bash"* ]] || [[ "$SHELL_ENV" == *"WSL"* ]]; then
    echo "✅ Use Unix commands (ls, grep, find, etc.)"
    echo "✅ Use forward slashes (/) for paths"
    echo "✅ Line endings: LF"
elif [[ "$OS_TYPE" == "Windows" ]] && [[ "$UNIX_CMDS" == "❌" ]]; then
    echo "✅ Use PowerShell commands"
    echo "✅ Use backslashes (\) for paths"
    echo "✅ Line endings: CRLF"
else
    echo "✅ Unix commands available"
    echo "✅ Use forward slashes (/) for paths"
fi

# Store results for agents
cat > .claude/memory/environment.json << EOF
{
  "detected_at": "$(date -Iseconds)",
  "os_type": "$OS_TYPE",
  "shell_env": "$SHELL_ENV",
  "unix_available": $([ "$UNIX_CMDS" == "✅" ] && echo "true" || echo "false"),
  "powershell_available": $([ "$PWSH_CMDS" == "✅" ] && echo "true" || echo "false"),
  "msystem": "${MSYSTEM:-null}",
  "recommendations": {
    "use_unix_commands": $([ "$UNIX_CMDS" == "✅" ] && echo "true" || echo "false"),
    "path_separator": "$([ "$OS_TYPE" == "Windows" ] && echo "\\\\" || echo "/")"
  }
}
EOF

echo ""
echo "✅ Environment detection complete!"
echo "📄 Results saved to .claude/memory/environment.json"
```

## Integration with Agents

Agents can read the environment detection results:

```bash
# In any agent, first check environment
ENV_DATA=$(cat .claude/memory/environment.json 2>/dev/null)
if [[ -n "$ENV_DATA" ]]; then
    USE_UNIX=$(echo "$ENV_DATA" | grep -o '"use_unix_commands":[^,}]*' | cut -d: -f2)
    if [[ "$USE_UNIX" == "true" ]]; then
        # Use Unix commands
        ls -la
    else
        # Use PowerShell
        powershell -Command "Get-ChildItem"
    fi
fi
```

## Error Handling

- If detection fails, defaults to Unix commands (most compatible)
- Stores last successful detection for offline use
- Provides manual override option via environment variables

## Benefits

1. **Automatic Detection**: No manual configuration needed
2. **Cross-Platform**: Works on Windows, WSL, macOS, Linux
3. **Agent Integration**: Results available to all agents
4. **Persistent**: Saves results for future sessions
5. **Smart Recommendations**: Suggests best commands for environment

---

*Command created by ClaudeSquad-commands-specialist for optimal cross-platform compatibility*