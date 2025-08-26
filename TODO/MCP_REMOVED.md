# MCP Servers Removed from Configuration

This document lists all MCP servers that have been removed from the active configuration to optimize token usage. These can be reinstalled if needed for specific tasks.

## Removed MCP Servers

### 1. **n8n-mcp** 
- **Tokens used**: ~10k tokens
- **Purpose**: n8n workflow automation and node management
- **Used by agents**: service.integrations (only)
- **Reinstall if**: You need to work with n8n workflows or automation
- **Installation**: Add back to claude_desktop_config.json

### 2. **voice-mode**
- **Tokens used**: ~25k tokens  
- **Purpose**: Voice interaction, TTS, STT, audio capabilities
- **Used by agents**: None currently assigned
- **Reinstall if**: You need voice interaction features
- **Installation**: Add back to claude_desktop_config.json

### 3. **server-git**
- **Tokens used**: ~5.5k tokens
- **Purpose**: Git operations via MCP (status, diff, commit, branch)
- **Used by agents**: service.auth, ops.git
- **Reinstall if**: You prefer MCP git operations over bash commands
- **Installation**: Add back to claude_desktop_config.json
- **Note**: Bash git commands work perfectly fine as alternative

### 4. **puppeteer** 
- **Tokens used**: ~8k tokens
- **Purpose**: Browser automation and testing
- **Used by agents**: Various testing and frontend agents
- **Reinstall if**: Never - use playwright instead
- **Installation**: Not recommended

### 5. **chrome-devtools**
- **Tokens used**: ~55k tokens (huge!)
- **Purpose**: Chrome DevTools Protocol operations
- **Used by agents**: Various debugging and testing agents  
- **Reinstall if**: Never - use playwright instead
- **Installation**: Not recommended

## Total Tokens Freed

**~103,500 tokens** freed from context (approximately 52% of total context!)

## Current Session Usage

These MCPs were minimally used in recent sessions:
- n8n-mcp: 5 tool calls
- voice-mode: 4 tool calls  
- server-git: 2 tool calls

## How to Reinstall

To reinstall any of these MCP servers:

1. Edit `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the server configuration back to the `mcpServers` section
3. Restart Claude Desktop

## Recommended Alternatives

- **n8n-mcp** → Use direct API calls or n8n's web interface
- **voice-mode** → Not critical for current project phase
- **server-git** → Use bash git commands (git status, git diff, etc.)

## Impact on Agents

Agents that referenced these MCPs will need to be updated:
- service.integrations (remove n8n-mcp)
- service.auth (remove server-git)
- ops.git (remove server-git)

---

*Document created: 2025-08-27*
*Reason: Context optimization - freeing ~40k tokens for more productive use*