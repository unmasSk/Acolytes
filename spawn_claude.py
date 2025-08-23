#!/usr/bin/env python3
"""
🚀 Multi-Claude Spawner for ClaudeSquad
Spawns specialized Claude instances with specific contexts
"""
import subprocess
import sys
import json
from pathlib import Path

def spawn_claude(context_type, prompt, agent_name=None):
    """
    Spawn a new Claude instance with specialized context
    
    Args:
        context_type: Type of specialization (auth, database, frontend, etc.)
        prompt: The task prompt for the specialized Claude
        agent_name: Optional agent name for context
    """
    
    # Project directory
    project_dir = Path(__file__).parent
    
    # Context templates for different specializations
    contexts = {
        "auth": {
            "role": "Authentication Specialist Claude",
            "expertise": "JWT, OAuth, session management, password hashing, security",
            "focus": "All authentication and authorization related tasks"
        },
        "database": {
            "role": "Database Specialist Claude", 
            "expertise": "PostgreSQL, SQLite, Redis, schemas, optimization, migrations",
            "focus": "All database design, queries, and performance tasks"
        },
        "frontend": {
            "role": "Frontend Specialist Claude",
            "expertise": "Vue.js, React, HTML, CSS, JavaScript, UI/UX",
            "focus": "All user interface and frontend development tasks"
        },
        "backend": {
            "role": "Backend Specialist Claude",
            "expertise": "Node.js, Python, APIs, microservices, architecture", 
            "focus": "All backend development and API design tasks"
        },
        "flags": {
            "role": "FLAGS System Orchestrator Claude",
            "expertise": "Inter-agent communication, task coordination, workflow management",
            "focus": "Managing FLAGS system and coordinating other Claude instances"
        },
        "general": {
            "role": "General Purpose Claude",
            "expertise": "Multi-domain problem solving",
            "focus": "General development tasks"
        }
    }
    
    # Get context or use general
    context = contexts.get(context_type, contexts["general"])
    
    # Build the full context prompt
    full_prompt = f"""PARALLEL CLAUDE INSTANCE - {context['role']}

SPECIALIZATION:
- Expertise: {context['expertise']}
- Focus: {context['focus']}
- Agent Name: {agent_name or '@' + context_type + '-claude'}

COMMUNICATION:
- You are Claude instance #{context_type.upper()}
- Main Claude is coordinating multiple parallel instances
- Use claude-claude.md for inter-Claude chat communication
- Format: [TIMESTAMP] [CLAUDE-{context_type.upper()}] your message
- SQLite database at .claude/memory/project.db for FLAGS
- Check FLAGS with: uv run python .claude/scripts/agent_db.py get-agent-flags "@{agent_name or context_type}-agent"
- FIRST ACTION: Write to claude-claude.md that you are active and ready
- AFTER EVERY TASK: Check claude-commands.md for new commands directed to you
- EXECUTE any commands in claude-commands.md marked [FOR: CLAUDE-{context_type.upper()}] or [FOR: ANY]

CURRENT TASK:
{prompt}

IMPORTANT:
- This is ClaudeSquad project - multi-agent architecture system
- You are a specialized Claude working in parallel with other Claudes
- Focus ONLY on your specialization area
- Use SQLite database for inter-Claude communication
- When done, update FLAGS status in database

Ready to execute your specialized task!
"""

    try:
        # Work DIRECTLY in project directory (no isolation)
        # Create the batch file with --print mode for testing
        batch_content = f'''@echo off
cd /d "{project_dir}"
echo === ARTHUR AGENT TEST ===
echo Working in: %CD%
echo.
claude --print "Your name is ARTHUR. You are a specialized agent. Your tasks: 1) Fix all typos in mixed-test-file.md following @typo-fixer rules from .claude/agents/typo-fixer.md, 2) If you detect Python code with issues, create a FLAG for @backend.python agent using MCP SQLite tools, 3) Answer who you are and save your response to arthur-response.md in the root. Do all 3 tasks and report results." --dangerously-skip-permissions --output-format json
echo.
echo === ARTHUR COMPLETE ===
pause
'''
        
        # Write batch file in project directory
        batch_file = project_dir / f"direct_claude_{context_type}.bat"
        with open(batch_file, 'w') as f:
            f.write(batch_content)
        
        # Execute batch file in new window (INTERACTIVE MODE)
        process = subprocess.Popen(
            f'start "INTERACTIVE Claude {context_type}" "{batch_file.absolute()}"',
            shell=True,
            cwd=str(project_dir)
        )
        
        print(f"[OK] Spawned {context['role']} (PID: {process.pid})")
        print(f"[INFO] Specialization: {context['expertise']}")
        print(f"[TASK] Task: {prompt[:60]}...")
        
        return {
            "success": True,
            "pid": process.pid,
            "context_type": context_type,
            "role": context['role']
        }
        
    except Exception as e:
        print(f"[ERROR] Error spawning {context_type} Claude: {e}")
        return {
            "success": False,
            "error": str(e),
            "context_type": context_type
        }

def spawn_multiple_claudes(tasks):
    """
    Spawn multiple Claude instances for parallel processing
    
    Args:
        tasks: List of dicts with 'context_type', 'prompt', 'agent_name'
    """
    results = []
    
    print(f"[SPAWN] Starting {len(tasks)} parallel Claude instances...")
    print("=" * 60)
    
    for i, task in enumerate(tasks):
        print(f"\n[INSTANCE] {i+1}/{len(tasks)}:")
        result = spawn_claude(
            task.get('context_type', 'general'),
            task.get('prompt', 'Execute pending tasks'),
            task.get('agent_name')
        )
        results.append(result)
    
    print("\n" + "=" * 60)
    print("[SUMMARY] PARALLEL CLAUDE DEPLOYMENT SUMMARY:")
    
    for result in results:
        if result['success']:
            print(f"[OK] {result['role']} - PID: {result['pid']}")
        else:
            print(f"[ERROR] {result['context_type']} - Error: {result['error']}")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python spawn_claude.py [context_type] [prompt] [optional: agent_name]")
        print("Context types: auth, database, frontend, backend, flags, general")
        print("\nExample:")
        print("python spawn_claude.py auth 'Review JWT implementation' '@auth-specialist'")
        print("\nOr for multiple:")
        print("python spawn_claude.py multi '[{\"context_type\":\"auth\",\"prompt\":\"Fix auth\"}]'")
        sys.exit(1)
    
    if sys.argv[1] == "multi":
        # Multiple Claude spawning
        try:
            tasks = json.loads(sys.argv[2])
            spawn_multiple_claudes(tasks)
        except json.JSONDecodeError:
            print("❌ Invalid JSON format for multiple tasks")
            sys.exit(1)
    else:
        # Single Claude spawning
        context_type = sys.argv[1]
        prompt = sys.argv[2]
        agent_name = sys.argv[3] if len(sys.argv) > 3 else None
        
        result = spawn_claude(context_type, prompt, agent_name)
        if not result['success']:
            sys.exit(1)