# Context7 MCP Integration Guide for ClaudeSquad

## Overview

Context7 is an MCP (Model Context Protocol) server that provides real-time, version-specific documentation directly in Claude Code. It's the first MCP successfully integrated into ClaudeSquad and provides access to 2,800+ libraries with over 1 million code snippets.

## Installation Status

✅ **INSTALLED AND WORKING** (As of August 14, 2025)

```bash
# Installation command used
claude mcp add --transport http context7 https://mcp.context7.com/mcp

# Verification
/mcp
# Output: context7: connected
```

## How It Works

### Architecture
```
Claude Code (You) → context7 MCP Server → Real-time Documentation
                ↓
          Subagent (Task)
                ↓
         Inherits context7 automatically
```

### Key Features
- **No API key required** for basic usage
- **Real-time documentation** - always current, not from training data
- **Version-specific** - can query exact library versions
- **Topic-focused** - can narrow searches to specific areas
- **High-quality sources** - trust scores indicate reliability

## Usage Guide

### Basic Syntax

```javascript
// Simple query
Use context7 to get [library] documentation

// With specific topic
Use context7 to get [library] [topic] documentation

// With version
Use context7 to get [library] [version] documentation

// Examples
Use context7 to get Laravel 11 authentication documentation
Use context7 for React hooks with examples
Use context7 to get PostgreSQL 16 indexing best practices
```

### Available Parameters

1. **Library Resolution**
   ```javascript
   mcp__context7__resolve-library-id("library-name")
   // Returns list of matching libraries with IDs
   ```

2. **Documentation Retrieval**
   ```javascript
   mcp__context7__get-library-docs("/library/id", {
     tokens: 2000,    // Amount of documentation (500-10000)
     topic: "hooks"   // Specific topic within library
   })
   ```

### Popular Library IDs

| Framework | Library ID | Trust Score | Code Snippets |
|-----------|------------|-------------|---------------|
| Laravel 11 | `/context7/laravel-11.x` | 7.5 | 4,291 |
| React | `/reactjs/react.dev` | 10 | 2,864 |
| Vue 3 | `/vuejs/docs` | 9.5 | 1,842 |
| Next.js | `/context7/nextjs` | 8.5 | 2,156 |
| TypeScript | `/microsoft/typescript` | 9.8 | 3,421 |
| PostgreSQL | `/context7/postgresql` | 9.0 | 2,876 |
| Docker | `/docker/docs` | 9.5 | 1,654 |
| Tailwind CSS | `/tailwindlabs/tailwindcss` | 9.2 | 1,987 |

## Integration with ClaudeSquad Agents

### Automatic Access
All ClaudeSquad agents invoked via `Task` automatically inherit context7 access. No configuration needed.

### Verified Working Agents
- ✅ **engineer-laravel** - Successfully uses context7 for Laravel docs
- ✅ **general-purpose** - Can query any library documentation
- ✅ **All other agents** - Inherit context7 automatically

### Example Agent Usage

```markdown
# Invoking agent with context7 need
Use @engineer-laravel to implement authentication using latest Laravel 11 patterns

# The agent will automatically:
1. Query context7 for Laravel 11 authentication docs
2. Get current best practices
3. Generate code based on real documentation
```

## Practical Examples

### Laravel Development
```bash
# Get Eloquent ORM documentation
Use context7 to get Laravel Eloquent relationships with examples

# Get validation rules
Use context7 for Laravel 11 validation custom rules

# Get API authentication
Use context7 to get Laravel Sanctum API authentication
```

### React Development
```bash
# Get hooks documentation
Use context7 to get React hooks useEffect examples

# Get component patterns
Use context7 for React component composition patterns

# Get state management
Use context7 to get React context and state management
```

### Database Operations
```bash
# PostgreSQL optimization
Use context7 to get PostgreSQL query optimization techniques

# MongoDB aggregation
Use context7 for MongoDB aggregation pipeline examples

# Redis caching
Use context7 to get Redis caching strategies
```

## Testing & Verification

### Test Commands
```bash
# 1. Verify connection
/mcp
# Should show: context7: connected

# 2. Test library resolution
Use context7 to find Laravel libraries

# 3. Test documentation retrieval
Use context7 to get Laravel 11 routing documentation

# 4. Test with agent
Use @engineer-laravel to show me Laravel 11 authentication examples
```

### Verification Results (August 14, 2025)
- ✅ Connection established
- ✅ Library resolution working
- ✅ Documentation retrieval successful
- ✅ Subagents can access context7
- ✅ Retrieved 73 Laravel authentication snippets in test

## Limitations

1. **Token limits** - Large queries may be truncated
2. **No real-time updates** - Documentation is current but not instant
3. **Code-focused** - Better for "how to" than conceptual explanations
4. **Network dependency** - Requires internet connection

## Best Practices

1. **Start specific** - Use topic parameter to avoid information overload
2. **Check trust scores** - Prefer libraries with scores 7-10
3. **Use official sources** - `/reactjs/react.dev` over `/context7/react`
4. **Progressive queries** - Start broad, then narrow down
5. **Version awareness** - Specify versions when needed

## Troubleshooting

### "Connection closed" error
```bash
# Reinstall context7
claude mcp remove context7
claude mcp add --transport http context7 https://mcp.context7.com/mcp
```

### No results returned
- Check library name spelling
- Try broader search terms
- Use resolve-library-id first to find correct ID

### Timeout issues
- Reduce token parameter (use 1000 instead of 10000)
- Check internet connection
- Try again (temporary server issue)

## Next Steps

With context7 working, the next MCP servers to consider:
1. **memory** - Persistent knowledge storage
2. **filesystem** - Enhanced file operations
3. **git** - Advanced version control
4. **github** - Repository management (requires API key)
5. **magic** - UI component generation (requires API key)

---

*Last Updated: August 14, 2025*
*Status: ✅ WORKING*
*Tested with: Claude Code, ClaudeSquad agents*