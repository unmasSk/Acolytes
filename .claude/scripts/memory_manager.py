#!/usr/bin/env python3
"""
Memory Manager for ClaudeSquad
Manages persistent memory for agents between invocations
"""

import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path
import hashlib
from typing import Dict, List, Any, Optional

# Compile regex patterns once for performance
AGENT_NAME_PATTERN = re.compile(r'(?:I am|Agent:|agent:)\s*([a-z-]+(?:-agent|-engineer|-coordinator))')
FILE_PATH_PATTERN = re.compile(r'[\w\-/]+\.(?:php|js|py|ts|jsx|tsx|vue|json|md|yaml|yml)')

class MemoryManager:
    def __init__(self):
        self.base_path = Path(".claude/memory")
        self.agents_path = self.base_path / "agents"
        self.context_path = self.base_path / "context"
        self.flags_path = self.base_path / "flags"
        self.sessions_path = self.base_path / "sessions"
        
        # Crear estructura si no existe
        self._ensure_structure()
    
    def _ensure_structure(self):
        """Ensures the directory structure exists"""
        for path in [self.agents_path, self.context_path, self.flags_path, self.sessions_path]:
            path.mkdir(parents=True, exist_ok=True)
    
    def _get_agent_path(self, agent_name: str) -> Path:
        """Gets the memory path for an agent"""
        # Sanitize agent_name to prevent path traversal
        safe_name = agent_name.replace("..", "").replace("/", "_").replace("\\", "_")
        agent_dir = self.agents_path / safe_name.replace("-agent", "_agent")
        agent_dir.mkdir(parents=True, exist_ok=True)
        return agent_dir
    
    def save_agent_memory(self, agent_name: str, output: str):
        """
        Guarda la memoria de un agente después de su ejecución
        Called by SubagentStop hook
        """
        agent_dir = self._get_agent_path(agent_name)
        timestamp = datetime.now().isoformat()
        
        # Load existing memory
        knowledge_file = agent_dir / "knowledge.json"
        history_file = agent_dir / "history.json"
        patterns_file = agent_dir / "patterns.json"
        
        knowledge = self._load_json(knowledge_file, default={
            "module_info": {},
            "key_files": [],
            "conventions": [],
            "decisions": [],
            "last_updated": timestamp
        })
        
        history = self._load_json(history_file, default=[])
        patterns = self._load_json(patterns_file, default={})
        
        # Parse agent output to extract relevant information
        session_data = self._parse_agent_output(output, agent_name)
        
        # Actualizar knowledge
        if session_data.get("new_knowledge"):
            knowledge["module_info"].update(session_data["new_knowledge"])
            knowledge["last_updated"] = timestamp
        
        if session_data.get("files_modified"):
            for file in session_data["files_modified"]:
                if file not in knowledge["key_files"]:
                    knowledge["key_files"].append(file)
        
        if session_data.get("decisions"):
            knowledge["decisions"].extend(session_data["decisions"])
            # Limit decisions to last 500 to prevent infinite growth
            knowledge["decisions"] = knowledge["decisions"][-500:]
        
        # Add to history
        history_entry = {
            "timestamp": timestamp,
            "action": session_data.get("action", "unknown"),
            "details": session_data.get("details", {}),
            "files": session_data.get("files_modified", []),
            "success": session_data.get("success", True)
        }
        history.append(history_entry)
        
        # Actualizar patterns
        if session_data.get("patterns_detected"):
            for pattern, count in session_data["patterns_detected"].items():
                patterns[pattern] = patterns.get(pattern, 0) + count
        
        # Save updated files
        self._save_json(knowledge_file, knowledge)
        self._save_json(history_file, history[-100:])  # Keep last 100 entries
        self._save_json(patterns_file, patterns)
        
        # Process cross-domain flags if they exist
        if session_data.get("flags"):
            self._process_flags(session_data["flags"])
        
        print(f"✅ Memory saved for {agent_name}")
        return knowledge
    
    def load_agent_memory(self, agent_name: str) -> str:
        """
        Loads an agent's memory at the start of its invocation
        Called by SubagentStart hook
        IMPORTANT: For dynamic agents, loads ALL module context
        """
        agent_dir = self._get_agent_path(agent_name)
        knowledge_file = agent_dir / "knowledge.json"
        patterns_file = agent_dir / "patterns.json"
        
        # If it's a dynamic agent (ends with -agent), load complete module analysis
        if agent_name.endswith('-agent'):
            module_name = agent_name.replace('-agent', '')
            module_analysis_file = self.base_path / "modules" / f"{module_name}_analysis.json"
            
            if module_analysis_file.exists():
                # Load COMPLETE module analysis
                module_analysis = self._load_json(module_analysis_file)
                
                # Format MAXIMUM context for the dynamic agent
                memory_context = f"""
# 🧠 COMPLETE MODULE CONTEXT FOR {agent_name.upper()}
# ⚠️ MAXIMUM CONTEXT - {len(json.dumps(module_analysis)):,} characters

## 📁 COMPLETE MODULE STRUCTURE
```
{module_analysis.get('complete_structure', 'No structure available')}
```

## 📄 MAIN FILES AND THEIR CONTENT
{self._format_files_content(module_analysis.get('all_files', {}))}

## 🔗 DEPENDENCIES AND COMMUNICATION
### Internal Dependencies (other modules)
{chr(10).join('- ' + d for d in module_analysis.get('dependencies', {}).get('internal', []))}

### External Dependencies (packages)
{chr(10).join('- ' + d for d in module_analysis.get('dependencies', {}).get('external', []))}

### Events that Emits/Listens
{chr(10).join('- ' + e for e in module_analysis.get('dependencies', {}).get('events', []))}

## 🌐 COMMUNICATION WITH OTHER MODULES
### Endpoints it Exposes
{chr(10).join('- ' + e for e in module_analysis.get('communication', {}).get('endpoints', []))}

### APIs it Consumes
{chr(10).join('- ' + a for a in module_analysis.get('communication', {}).get('consumes', []))}

### Database Tables
{chr(10).join('- ' + t for t in module_analysis.get('communication', {}).get('database_tables', []))}

## 🎨 PATRONES Y CONVENCIONES
### Detected Patterns
{chr(10).join('- ' + p for p in module_analysis.get('patterns', []))}

### Project Conventions
{json.dumps(module_analysis.get('conventions', {}), indent=2)}

## 🏗️ DECISIONES ARQUITECTÓNICAS
{self._format_decisions(module_analysis.get('decisions', []))}

## ⚙️ CONFIGURACIÓN
{json.dumps(module_analysis.get('configuration', {}), indent=2)}

## 📊 TESTS
{json.dumps(module_analysis.get('tests', {}), indent=2)}

## ⚡ PERFORMANCE
{json.dumps(module_analysis.get('performance', {}), indent=2)}

## 📝 TODOs y FIXMEs
{self._format_todos(module_analysis.get('todos_and_fixmes', []))}

## 🕐 CAMBIOS RECIENTES
{chr(10).join('- ' + c for c in module_analysis.get('recent_changes', [])[:20])}
"""
                
                # Also add previous memory if it exists
                if knowledge_file.exists():
                    knowledge = self._load_json(knowledge_file)
                    patterns = self._load_json(patterns_file, default={})
                    
                    memory_context += f"""

## 🧠 MEMORIA ACUMULADA DE SESIONES ANTERIORES
### Previous Decisions
{chr(10).join('- ' + d for d in knowledge.get('decisions', [])[:20])}

### Previously Modified Files
{chr(10).join('- ' + f for f in knowledge.get('key_files', [])[:30])}

### Confirmed Patterns
{chr(10).join(f'- {p}: used {c} times' for p, c in list(patterns.items())[:20])}
"""
                
                return memory_context
            
        # If it's not a dynamic agent or there's no analysis, load normal memory
        if not knowledge_file.exists():
            return f"📝 No previous memory found for {agent_name}. Starting fresh."
        
        knowledge = self._load_json(knowledge_file)
        patterns = self._load_json(patterns_file, default={})
        
        # Format memory to inject into the agent
        memory_context = f"""
# 🧠 MEMORY CONTEXT FOR {agent_name.upper()}

## Previous Knowledge
Last updated: {knowledge.get('last_updated', 'unknown')}

### Module Information
{json.dumps(knowledge.get('module_info', {}), indent=2)}

### Key Files You've Worked With
{chr(10).join('- ' + f for f in knowledge.get('key_files', [])[:20])}

### Architectural Decisions Made
{chr(10).join('- ' + d for d in knowledge.get('decisions', [])[:10])}

### Patterns You've Identified
{chr(10).join(f'- {p}: used {c} times' for p, c in list(patterns.items())[:10])}

### Important Conventions
{chr(10).join('- ' + c for c in knowledge.get('conventions', [])[:10])}

## Instructions
- You have access to your previous knowledge above
- Use this context to maintain consistency
- Update your understanding based on new findings
- Flag any breaking changes or important discoveries
---
"""
        return memory_context
    
    def _format_files_content(self, files: Dict) -> str:
        """Formats file content for context"""
        if not files:
            return "No files analyzed"
        
        formatted = []
        for filepath, info in list(files.items())[:20]:  # Limit to 20 most important files
            if isinstance(info, dict) and 'content' in info:
                formatted.append(f"""
### 📄 {filepath}
- Lines: {info.get('lines', 0)}
- Functions: {', '.join(info.get('functions', [])[:10])}
- Classes: {', '.join(info.get('classes', [])[:10])}
- Complexity: {info.get('complexity', 0)}
""")
        
        return '\n'.join(formatted)
    
    def _format_decisions(self, decisions: List) -> str:
        """Formats architectural decisions"""
        if not decisions:
            return "No architectural decisions found"
        
        formatted = []
        for decision in decisions[:20]:
            if isinstance(decision, dict):
                formatted.append(f"- [{decision.get('type', 'NOTE')}] {decision.get('file', '')}: {decision.get('content', '')}")
        
        return '\n'.join(formatted)
    
    def _format_todos(self, todos: List) -> str:
        """Formats TODOs and FIXMEs"""
        if not todos:
            return "No TODOs found"
        
        formatted = []
        for todo in todos[:15]:
            if isinstance(todo, dict):
                formatted.append(f"- {todo.get('file', '')}:{todo.get('line', '')}: {todo.get('content', '')}")
        
        return '\n'.join(formatted)
    
    def _parse_agent_output(self, output: str, agent_name: str) -> Dict:
        """
        Parses agent output to extract structured information
        This is a basic parser that can be improved
        """
        session_data = {
            "action": "task_execution",
            "files_modified": [],
            "new_knowledge": {},
            "patterns_detected": {},
            "decisions": [],
            "flags": [],
            "success": True
        }
        
        lines = output.split('\n')
        
        for line in lines:
            # Detect mentioned files (more precise)
            # Use pre-compiled regex pattern for performance
            matches = FILE_PATH_PATTERN.findall(line)
            for match in matches:
                if not match.startswith('http') and not match.startswith('www.'):
                    session_data["files_modified"].append(match)
            
            # Detectar patterns (básico)
            if 'pattern' in line.lower() or 'repository' in line.lower() or 'service' in line.lower():
                if 'repository' in line.lower():
                    session_data["patterns_detected"]["Repository Pattern"] = 1
                if 'service' in line.lower():
                    session_data["patterns_detected"]["Service Pattern"] = 1
            
            # Detectar flags
            if 'FLAG:' in line or 'ATTENTION:' in line or 'WARNING:' in line:
                session_data["flags"].append(line)
            
            # Detectar decisiones
            if 'decided' in line.lower() or 'decision:' in line.lower():
                session_data["decisions"].append(line.strip())
        
        return session_data
    
    def _process_flags(self, flags: List[str]):
        """Processes cross-domain flags for other agents"""
        flags_file = self.flags_path / "pending.json"
        pending_flags = self._load_json(flags_file, default=[])
        
        for flag in flags:
            flag_entry = {
                "timestamp": datetime.now().isoformat(),
                "flag": flag,
                "processed": False
            }
            pending_flags.append(flag_entry)
        
        self._save_json(flags_file, pending_flags)
    
    def get_pending_flags(self) -> List[Dict]:
        """Gets pending flags to process"""
        flags_file = self.flags_path / "pending.json"
        return self._load_json(flags_file, default=[])
    
    def _load_json(self, filepath: Path, default=None) -> Any:
        """Loads a JSON file safely"""
        if not filepath.exists():
            return default if default is not None else {}
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error loading {filepath}: {e}")
            return default if default is not None else {}
    
    def _save_json(self, filepath: Path, data: Any):
        """Saves data in JSON format"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        except Exception as e:
            print(f"❌ Error saving {filepath}: {e}")
    
    def consolidate_memory(self, agent_name: str):
        """
        Consolidates an agent's memory, removing duplicates and
        organizing knowledge
        """
        agent_dir = self._get_agent_path(agent_name)
        knowledge_file = agent_dir / "knowledge.json"
        
        knowledge = self._load_json(knowledge_file)
        if knowledge:
            # Remove duplicates in key_files
            knowledge["key_files"] = list(set(knowledge.get("key_files", [])))
            
            # Remove duplicate decisions
            seen = set()
            unique_decisions = []
            for decision in knowledge.get("decisions", []):
                # Create a hashable key for comparison
                if isinstance(decision, dict):
                    decision_key = json.dumps(decision, sort_keys=True)
                else:
                    decision_key = str(decision)
                
                if decision_key not in seen:
                    seen.add(decision_key)
                    unique_decisions.append(decision)
            knowledge["decisions"] = unique_decisions
            
            self._save_json(knowledge_file, knowledge)
            print(f"✅ Memory consolidated for {agent_name}")


def extract_agent_name_from_stdin(data):
    """Extracts the agent name from stdin JSON"""
    try:
        json_data = json.loads(data)
        # The hook passes information about the agent in the JSON
        if 'agent' in json_data:
            return json_data['agent']
        elif 'name' in json_data:
            return json_data['name']
        elif 'subagent' in json_data:
            return json_data['subagent']
        # If we don't find it, try to extract from the output
        if 'output' in json_data:
            # Use pre-compiled regex pattern for performance
            match = AGENT_NAME_PATTERN.search(json_data['output'])
            if match:
                return match.group(1)
    except (json.JSONDecodeError, KeyError, TypeError, AttributeError) as e:
        print(f"⚠️ Error extracting agent name: {e}")
    return None

def main():
    """
    Entry point para el script
    Uso: 
    - python memory_manager.py save_from_stdin (lee JSON desde stdin)
    - python memory_manager.py track_file_change (rastrea cambios de archivos)
    - python memory_manager.py load [agent_name]
    - python memory_manager.py consolidate [agent_name]
    """
    if len(sys.argv) < 2:
        print("Usage: python memory_manager.py [save_from_stdin|track_file_change|load|consolidate] [agent_name]")
        sys.exit(1)
    
    action = sys.argv[1]
    manager = MemoryManager()
    
    if action == "save_from_stdin":
        # Read complete JSON from stdin
        stdin_data = sys.stdin.read()
        
        # Extract agent name and output from JSON
        agent_name = extract_agent_name_from_stdin(stdin_data)
        
        if agent_name:
            # Try to extract only the agent output
            try:
                json_data = json.loads(stdin_data)
                output = json_data.get('output', stdin_data)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"⚠️ Error parsing JSON: {e}")
                output = stdin_data
            
            manager.save_agent_memory(agent_name, output)
        else:
            print("⚠️ Could not determine agent name from stdin")
    
    elif action == "track_file_change":
        # Track file changes from PostToolUse
        stdin_data = sys.stdin.read()
        try:
            json_data = json.loads(stdin_data)
            file_path = json_data.get('file', json_data.get('path', 'unknown'))
            tool = json_data.get('tool', 'unknown')
            
            # Save to activity log
            activity_log = manager.context_path / "activity.log"
            with open(activity_log, 'a', encoding='utf-8') as f:
                f.write(f"[{datetime.now().isoformat()}] {tool}: {file_path}\n")
        except Exception as e:
            print(f"⚠️ Error tracking file change: {e}")
    
    elif action == "load":
        if len(sys.argv) < 3:
            print("Usage: python memory_manager.py load [agent_name]")
            sys.exit(1)
        agent_name = sys.argv[2]
        memory = manager.load_agent_memory(agent_name)
        print(memory)
    
    elif action == "consolidate":
        if len(sys.argv) < 3:
            print("Usage: python memory_manager.py consolidate [agent_name]")
            sys.exit(1)
        agent_name = sys.argv[2]
        manager.consolidate_memory(agent_name)
    
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)


if __name__ == "__main__":
    main()