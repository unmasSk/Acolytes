#!/usr/bin/env python3
"""
Update all agent files to include project context reading step.
Excludes: flags.agent, plan.strategy, and all setup.* agents
"""

import os
import re
from pathlib import Path

def should_skip_agent(filename):
    """Check if agent should be skipped from update."""
    skip_list = [
        'flags.agent.md',
        'plan.strategy.md',
        'flags-agent.md'  # Just in case there's a variant
    ]
    
    # Skip if in explicit skip list
    if filename in skip_list:
        return True
    
    # Skip if it's a setup agent (starts with setup.)
    if filename.startswith('setup.') or filename.startswith('setup-'):
        return True
    
    return False

def update_agent_workflow(file_path):
    """Update the workflow section in an agent file."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find the workflow section
    old_pattern = r'(\*\*MANDATORY: Agent workflow order:\*\*\n\n1\. Read your complete agent identity first\n)2\. Check pending FLAGS before new work\n3\. Handle the current request'
    
    # New workflow with project context
    new_workflow = r'\g<1>2. Read project context from `.claude/project/` documents:\n   - `vision.md` - Project vision and goals\n   - `architecture.md` - System architecture decisions\n   - `technical-decisions.md` - Technical choices and rationale\n   - `team-preferences.md` - Team coding standards and preferences\n   - `project-context.md` - Full project context and background\n3. Check pending FLAGS before new work\n4. Handle the current request'
    
    # Check if pattern exists in file
    if re.search(old_pattern, content):
        # Replace the workflow
        updated_content = re.sub(old_pattern, new_workflow, content)
        
        # Write back only if content changed
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
    
    return False

def main():
    """Main function to update all eligible agent files."""
    
    agents_dir = Path(r'C:\Users\bextia\Desktop\acolyte\ClaudeSquad\.claude\agents')
    
    if not agents_dir.exists():
        print(f"❌ Agents directory not found: {agents_dir}")
        return
    
    updated = []
    skipped = []
    already_updated = []
    
    # Process all .md files in agents directory
    for file_path in agents_dir.glob('*.md'):
        filename = file_path.name
        
        # Check if should skip
        if should_skip_agent(filename):
            skipped.append(filename)
            continue
        
        # Try to update the file
        if update_agent_workflow(file_path):
            updated.append(filename)
            print(f"[UPDATED] {filename}")
        else:
            # Check if already has the new format
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'Read project context from `.claude/project/` documents:' in content:
                    already_updated.append(filename)
                else:
                    print(f"[WARNING] No workflow section found: {filename}")
    
    # Print summary
    print("\n" + "="*50)
    print("UPDATE SUMMARY")
    print("="*50)
    
    if updated:
        print(f"\n[UPDATED] {len(updated)} agents:")
        for name in sorted(updated):
            print(f"   - {name}")
    
    if already_updated:
        print(f"\n[ALREADY UPDATED] {len(already_updated)} agents:")
        for name in sorted(already_updated)[:5]:  # Show first 5
            print(f"   - {name}")
        if len(already_updated) > 5:
            print(f"   ... and {len(already_updated) - 5} more")
    
    if skipped:
        print(f"\n[SKIPPED] {len(skipped)} agents:")
        for name in sorted(skipped):
            print(f"   - {name}")
    
    print(f"\n[TOTAL] Agents processed: {len(updated) + len(already_updated) + len(skipped)}")

if __name__ == "__main__":
    main()