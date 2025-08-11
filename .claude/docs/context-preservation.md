# ⚡ CRITICAL: Context Window Preservation Strategy

## The Problem We Solved

### ❌ WRONG APPROACH (What I initially proposed)

```
Orchestrator reads 10 memory files → Uses 50KB of context
Passes content to specialist → More context used
Orchestrator runs out of context quickly → System fails
```

### ✅ CORRECT APPROACH (Your improvement)

```
Orchestrator: "Read these 3 files" → Uses 200 bytes
Specialist reads files directly → Uses THEIR context
Each agent preserves their context → System scales
```

## Why This Matters

Each agent in Claude Code has **200K tokens** of context. If the orchestrator reads all memory files:

- Orchestrator loses 20-50KB per delegation
- After 5 delegations, orchestrator is full
- System becomes unusable

With the instruction approach:

- Orchestrator uses ~500 bytes per delegation
- Can coordinate 100+ specialists
- Each specialist has full 200K for their work

## Implementation Pattern

### Orchestrator Code

```yaml
# WRONG - Don't do this
orchestrator:
  reads: laravel.md (10KB consumed)
  passes_to: specialist

# RIGHT - Do this
orchestrator:
  instruction: "Read .claude/memory/backend/laravel.md"
  specialist: *reads file themselves*
```

### Specialist Code

```markdown
## When invoked by orchestrator

1. FIRST ACTION: Read files specified
   - Use MY context window
   - cat .claude/memory/[specified].md
2. WORK: With full context available

3. RETURN: Summary only (not file contents)
```

## Benefits

1. **Infinite Scalability**: Orchestrator never fills up
2. **Better Performance**: Each agent uses full capacity
3. **Clean Separation**: Memory stays distributed
4. **Git Friendly**: Memory files can be large

## Rule of Thumb

> "The orchestrator is a traffic director pointing to memory, not a librarian reading everything aloud"

---

This is THE KEY INSIGHT that makes the entire multi-agent system viable at scale.
