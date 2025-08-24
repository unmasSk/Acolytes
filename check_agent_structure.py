#!/usr/bin/env python3
"""
Script to check which agent files are missing Core Identity or Core Responsibilities sections
"""

import os
import glob

def check_agent_file(filepath):
    """Check if an agent file has both required sections"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    has_core_identity = '## Core Identity' in content
    has_core_responsibilities = '## Core Responsibilities' in content
    
    return {
        'file': filename,
        'has_identity': has_core_identity,
        'has_responsibilities': has_core_responsibilities,
        'both': has_core_identity and has_core_responsibilities
    }

def main():
    # Get all agent markdown files
    agent_files = glob.glob('.claude/agents/*.md')
    
    # Filter out setup files and flags-related files
    excluded_prefixes = ['setup.', 'flags-updater', 'flags.agent']
    agent_files = [f for f in agent_files if not any(
        os.path.basename(f).startswith(prefix) for prefix in excluded_prefixes
    )]
    
    results = []
    for filepath in sorted(agent_files):
        result = check_agent_file(filepath)
        results.append(result)
    
    # Print results
    print("=" * 80)
    print("AGENT FILES STRUCTURE CHECK")
    print("=" * 80)
    
    # Files with both sections (ready for FLAGS update)
    print("\n[OK] FILES WITH BOTH SECTIONS (Ready for FLAGS update):")
    ready_files = [r for r in results if r['both']]
    for r in ready_files:
        print(f"  - {r['file']}")
    print(f"  Total: {len(ready_files)} files")
    
    # Files missing Core Identity
    print("\n[X] FILES MISSING CORE IDENTITY:")
    missing_identity = [r for r in results if not r['has_identity']]
    if missing_identity:
        for r in missing_identity:
            print(f"  - {r['file']}")
        print(f"  Total: {len(missing_identity)} files")
    else:
        print("  None")
    
    # Files missing Core Responsibilities
    print("\n[X] FILES MISSING CORE RESPONSIBILITIES:")
    missing_responsibilities = [r for r in results if not r['has_responsibilities']]
    if missing_responsibilities:
        for r in missing_responsibilities:
            print(f"  - {r['file']}")
        print(f"  Total: {len(missing_responsibilities)} files")
    else:
        print("  None")
    
    # Files missing both
    print("\n[!!] FILES MISSING BOTH SECTIONS:")
    missing_both = [r for r in results if not r['has_identity'] and not r['has_responsibilities']]
    if missing_both:
        for r in missing_both:
            print(f"  - {r['file']}")
        print(f"  Total: {len(missing_both)} files")
    else:
        print("  None")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY:")
    print(f"  Total agent files checked: {len(results)}")
    print(f"  Ready for FLAGS update: {len(ready_files)}")
    print(f"  Need fixes: {len(results) - len(ready_files)}")
    print("=" * 80)

if __name__ == "__main__":
    main()