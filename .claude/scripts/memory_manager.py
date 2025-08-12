#!/usr/bin/env python3
"""
Memory Manager for ClaudeSquad
Gestiona la memoria persistente de los agentes entre invocaciones
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
import hashlib
from typing import Dict, List, Any, Optional

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
        """Asegura que existe la estructura de directorios"""
        for path in [self.agents_path, self.context_path, self.flags_path, self.sessions_path]:
            path.mkdir(parents=True, exist_ok=True)
    
    def _get_agent_path(self, agent_name: str) -> Path:
        """Obtiene el path de memoria de un agente"""
        agent_dir = self.agents_path / agent_name.replace("-agent", "_agent")
        agent_dir.mkdir(exist_ok=True)
        return agent_dir
    
    def save_agent_memory(self, agent_name: str, output: str):
        """
        Guarda la memoria de un agente después de su ejecución
        Llamado por SubagentStop hook
        """
        agent_dir = self._get_agent_path(agent_name)
        timestamp = datetime.now().isoformat()
        
        # Cargar memoria existente
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
        
        # Parsear output del agente para extraer información relevante
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
        
        # Añadir a history
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
        
        # Guardar archivos actualizados
        self._save_json(knowledge_file, knowledge)
        self._save_json(history_file, history[-100:])  # Mantener últimas 100 entradas
        self._save_json(patterns_file, patterns)
        
        # Procesar flags cross-domain si existen
        if session_data.get("flags"):
            self._process_flags(session_data["flags"])
        
        print(f"✅ Memory saved for {agent_name}")
        return knowledge
    
    def load_agent_memory(self, agent_name: str) -> str:
        """
        Carga la memoria de un agente al inicio de su invocación
        Llamado por SubagentStart hook
        IMPORTANTE: Para agentes dinámicos, carga TODO el contexto del módulo
        """
        agent_dir = self._get_agent_path(agent_name)
        knowledge_file = agent_dir / "knowledge.json"
        patterns_file = agent_dir / "patterns.json"
        
        # Si es un agente dinámico (termina en -agent), cargar análisis completo del módulo
        if agent_name.endswith('-agent'):
            module_name = agent_name.replace('-agent', '')
            module_analysis_file = self.base_path / "modules" / f"{module_name}_analysis.json"
            
            if module_analysis_file.exists():
                # Cargar análisis COMPLETO del módulo
                module_analysis = self._load_json(module_analysis_file)
                
                # Formatear contexto MÁXIMO para el agente dinámico
                memory_context = f"""
# 🧠 COMPLETE MODULE CONTEXT FOR {agent_name.upper()}
# ⚠️ CONTEXTO MÁXIMO - {len(json.dumps(module_analysis)):,} caracteres

## 📁 ESTRUCTURA COMPLETA DEL MÓDULO
```
{module_analysis.get('complete_structure', 'No structure available')}
```

## 📄 ARCHIVOS PRINCIPALES Y SU CONTENIDO
{self._format_files_content(module_analysis.get('all_files', {}))}

## 🔗 DEPENDENCIAS Y COMUNICACIÓN
### Dependencias Internas (otros módulos)
{chr(10).join('- ' + d for d in module_analysis.get('dependencies', {}).get('internal', []))}

### Dependencias Externas (paquetes)
{chr(10).join('- ' + d for d in module_analysis.get('dependencies', {}).get('external', []))}

### Eventos que Emite/Escucha
{chr(10).join('- ' + e for e in module_analysis.get('dependencies', {}).get('events', []))}

## 🌐 COMUNICACIÓN CON OTROS MÓDULOS
### Endpoints que Expone
{chr(10).join('- ' + e for e in module_analysis.get('communication', {}).get('endpoints', []))}

### APIs que Consume
{chr(10).join('- ' + a for a in module_analysis.get('communication', {}).get('consumes', []))}

### Tablas de Base de Datos
{chr(10).join('- ' + t for t in module_analysis.get('communication', {}).get('database_tables', []))}

## 🎨 PATRONES Y CONVENCIONES
### Patrones Detectados
{chr(10).join('- ' + p for p in module_analysis.get('patterns', []))}

### Convenciones del Proyecto
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
                
                # Añadir también la memoria previa si existe
                if knowledge_file.exists():
                    knowledge = self._load_json(knowledge_file)
                    patterns = self._load_json(patterns_file, default={})
                    
                    memory_context += f"""

## 🧠 MEMORIA ACUMULADA DE SESIONES ANTERIORES
### Decisiones Previas
{chr(10).join('- ' + d for d in knowledge.get('decisions', [])[:20])}

### Archivos Modificados Previamente
{chr(10).join('- ' + f for f in knowledge.get('key_files', [])[:30])}

### Patrones Confirmados
{chr(10).join(f'- {p}: usado {c} veces' for p, c in list(patterns.items())[:20])}
"""
                
                return memory_context
            
        # Si no es agente dinámico o no hay análisis, cargar memoria normal
        if not knowledge_file.exists():
            return f"📝 No previous memory found for {agent_name}. Starting fresh."
        
        knowledge = self._load_json(knowledge_file)
        patterns = self._load_json(patterns_file, default={})
        
        # Formatear memoria para inyectar al agente
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
        """Formatea el contenido de archivos para el contexto"""
        if not files:
            return "No files analyzed"
        
        formatted = []
        for filepath, info in list(files.items())[:20]:  # Limitar a 20 archivos más importantes
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
        """Formatea decisiones arquitectónicas"""
        if not decisions:
            return "No architectural decisions found"
        
        formatted = []
        for decision in decisions[:20]:
            if isinstance(decision, dict):
                formatted.append(f"- [{decision.get('type', 'NOTE')}] {decision.get('file', '')}: {decision.get('content', '')}")
        
        return '\n'.join(formatted)
    
    def _format_todos(self, todos: List) -> str:
        """Formatea TODOs y FIXMEs"""
        if not todos:
            return "No TODOs found"
        
        formatted = []
        for todo in todos[:15]:
            if isinstance(todo, dict):
                formatted.append(f"- {todo.get('file', '')}:{todo.get('line', '')}: {todo.get('content', '')}")
        
        return '\n'.join(formatted)
    
    def _parse_agent_output(self, output: str, agent_name: str) -> Dict:
        """
        Parsea el output del agente para extraer información estructurada
        Este es un parser básico que puede ser mejorado
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
            # Detectar archivos mencionados
            if '.php' in line or '.js' in line or '.py' in line:
                words = line.split()
                for word in words:
                    if '.' in word and '/' in word:
                        session_data["files_modified"].append(word.strip(',').strip('"'))
            
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
        """Procesa flags cross-domain para otros agentes"""
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
        """Obtiene flags pendientes de procesar"""
        flags_file = self.flags_path / "pending.json"
        return self._load_json(flags_file, default=[])
    
    def _load_json(self, filepath: Path, default=None) -> Any:
        """Carga un archivo JSON de forma segura"""
        if not filepath.exists():
            return default if default is not None else {}
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error loading {filepath}: {e}")
            return default if default is not None else {}
    
    def _save_json(self, filepath: Path, data: Any):
        """Guarda datos en formato JSON"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        except Exception as e:
            print(f"❌ Error saving {filepath}: {e}")
    
    def consolidate_memory(self, agent_name: str):
        """
        Consolida la memoria de un agente, eliminando duplicados y 
        organizando el conocimiento
        """
        agent_dir = self._get_agent_path(agent_name)
        knowledge_file = agent_dir / "knowledge.json"
        
        knowledge = self._load_json(knowledge_file)
        if knowledge:
            # Eliminar duplicados en key_files
            knowledge["key_files"] = list(set(knowledge.get("key_files", [])))
            
            # Eliminar decisiones duplicadas
            seen = set()
            unique_decisions = []
            for decision in knowledge.get("decisions", []):
                if decision not in seen:
                    seen.add(decision)
                    unique_decisions.append(decision)
            knowledge["decisions"] = unique_decisions
            
            self._save_json(knowledge_file, knowledge)
            print(f"✅ Memory consolidated for {agent_name}")


def extract_agent_name_from_stdin(data):
    """Extrae el nombre del agente del JSON de stdin"""
    try:
        json_data = json.loads(data)
        # El hook pasa información sobre el agente en el JSON
        if 'agent' in json_data:
            return json_data['agent']
        elif 'name' in json_data:
            return json_data['name']
        elif 'subagent' in json_data:
            return json_data['subagent']
        # Si no encontramos, intentar extraer del output
        if 'output' in json_data:
            # Buscar patrones como "I am dream-agent" o similar
            import re
            match = re.search(r'(?:I am|Agent:|agent:)\s*([a-z-]+(?:-agent|-engineer|-coordinator))', json_data['output'])
            if match:
                return match.group(1)
    except:
        pass
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
        # Leer JSON completo desde stdin
        stdin_data = sys.stdin.read()
        
        # Extraer nombre del agente y output del JSON
        agent_name = extract_agent_name_from_stdin(stdin_data)
        
        if agent_name:
            # Intentar extraer solo el output del agente
            try:
                json_data = json.loads(stdin_data)
                output = json_data.get('output', stdin_data)
            except:
                output = stdin_data
            
            manager.save_agent_memory(agent_name, output)
        else:
            print("⚠️ Could not determine agent name from stdin")
    
    elif action == "track_file_change":
        # Rastrear cambios de archivos desde PostToolUse
        stdin_data = sys.stdin.read()
        try:
            json_data = json.loads(stdin_data)
            file_path = json_data.get('file', json_data.get('path', 'unknown'))
            tool = json_data.get('tool', 'unknown')
            
            # Guardar en activity log
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