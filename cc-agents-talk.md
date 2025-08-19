## 🎯 **PROPUESTA DE EXTENSIÓN DEL SISTEMA FLAGS**

### 1. **NUEVO CAMPO: `target_agent`**

```sql
-- Añadir columna para dirigir flags a agentes específicos
ALTER TABLE flags ADD COLUMN target_agent TEXT;

-- Índice para búsquedas rápidas por agente
CREATE INDEX idx_flags_target_agent ON flags(target_agent, status);
```

### 2. **CONVENCIÓN DE NOMBRADO**

```yaml
TIPOS_DE_DESTINO:
  módulo_normal: "auth"              # Va al módulo auth
  agente_dinámico: "@auth-agent"     # Va al agente dinámico auth-agent
  especialista: "@specialist.laravel" # Va al especialista laravel
  coordinador: "@coordinator.backend" # Va al coordinador backend
  múltiple: "@auth-agent,@api-agent" # Va a varios agentes
```

### 3. **FUNCIONES PYTHON ACTUALIZADAS**

```python
def create_flag_extended(flag_type, source_module, source_agent, 
                        affected_modules=None, target_agent=None,
                        change_description, action_required, 
                        impact_level='medium', **kwargs):
    """
    Versión extendida que soporta target_agent
    
    Ejemplos:
    - target_agent="@auth-agent" → Flag para agente dinámico
    - target_agent="@specialist.laravel" → Flag para especialista
    - affected_modules="auth,api" → Flag tradicional para módulos
    """
    
    # Si hay target_agent, puede no haber affected_modules
    if target_agent and not affected_modules:
        affected_modules = target_agent  # Para mantener compatibilidad
    
    # Resto del código actual...

def get_agent_flags(agent_name):
    """
    Obtiene flags pendientes para un agente específico
    
    Ejemplo: get_agent_flags("@auth-agent")
    """
    sql = """
        SELECT * FROM flags 
        WHERE status = 'pending'
        AND (
            target_agent = ? 
            OR target_agent LIKE ? || ',%'
            OR target_agent LIKE '%,' || ?
            OR target_agent LIKE '%,' || ? || ',%'
        )
        ORDER BY 
            CASE impact_level 
                WHEN 'critical' THEN 1 
                WHEN 'high' THEN 2 
                WHEN 'medium' THEN 3 
                ELSE 4 
            END,
            created_at ASC
    """
    return query(sql, [agent_name, agent_name, agent_name, agent_name])
```

### 4. **PROTOCOLO PARA CLAUDE CODE**

```yaml
ACTIVACIÓN_DE_AGENTE:
  # 1. Claude detecta que necesita un agente
  trigger: "Voy a trabajar con el módulo auth"
  
  # 2. Revisa flags automáticamente
  comando: |
    python agent_db.py get-agent-flags "@auth-agent"
  
  # 3. Si hay flags, las procesa ANTES del trabajo
  respuesta:
    - flag_id: 45
      from: "@api-agent"
      message: "Nuevo endpoint /verify requiere método"
      action: "Crear verifyUser() en AuthService"
    
  # 4. Agente incorpora requirements de flags
  acción: "Incluye en contexto todas las flags antes de trabajar"

CREACIÓN_DE_FLAG:
  # Cuando agente detecta dependencia externa
  trigger: "auth-agent modificó interface que usa api"
  
  comando: |
    python agent_db.py create-flag \
      --flag_type "interface_change" \
      --source_module "auth" \
      --source_agent "@auth-agent" \
      --target_agent "@api-agent" \
      --change_description "Added 'verified' field to user object" \
      --action_required "Update user type interface" \
      --impact_level "high" \
      --example_usage "user.verified: boolean"

FLAG_PARA_ESPECIALISTA:
  # Cuando necesita ayuda de especialista
  trigger: "auth-agent necesita optimizar queries Laravel"
  
  comando: |
    python agent_db.py create-flag \
      --flag_type "optimization_needed" \
      --source_agent "@auth-agent" \
      --target_agent "@specialist.laravel" \
      --change_description "N+1 queries in user loading" \
      --action_required "Need eager loading strategy" \
      --context '{"file": "UserController.php", "method": "index"}'
```

### 5. **FLUJO COMPLETO ANTI-FALLOS**

```python
# En el system prompt de CADA agente dinámico:
"""
ON_ACTIVATION:
  1. CHECK FLAGS:
     result = bash('python agent_db.py get-agent-flags "@{self.name}"')
     if result.has_flags:
         self.context.add_all(result.flags)
         self.priority_tasks = result.critical_flags
  
  2. PROCESS WORK:
     # Normal work + flag requirements
  
  3. CREATE FLAGS IF NEEDED:
     if self.found_external_dependency:
         bash(f'''python agent_db.py create-flag \
           --source_agent "@{self.name}" \
           --target_agent "@{dependent_agent}" \
           --change_description "{what_changed}" \
           --action_required "{what_they_need_to_do}"
         ''')
  
  4. COMPLETE FLAGS:
     for flag in self.processed_flags:
         bash(f'python agent_db.py execute \
           "UPDATE flags SET status=\'completed\', \
            completed_at=\'{timestamp}\', \
            completed_by=\'@{self.name}\' \
            WHERE id={flag.id}"')
"""
```

### 6. **VIEWS ADICIONALES ÚTILES**

```sql
-- Flags pendientes por agente
CREATE VIEW pending_agent_flags AS
SELECT 
    target_agent,
    COUNT(*) as pending_count,
    MAX(CASE WHEN impact_level = 'critical' THEN 1 ELSE 0 END) as has_critical
FROM flags
WHERE status = 'pending'
AND target_agent IS NOT NULL
GROUP BY target_agent;

-- Comunicación entre agentes (quién habla con quién)
CREATE VIEW agent_communication_matrix AS
SELECT 
    source_agent,
    target_agent,
    COUNT(*) as message_count,
    AVG(CASE 
        WHEN status = 'completed' THEN 
            julianday(completed_at) - julianday(created_at) 
        ELSE NULL 
    END) as avg_resolution_time_days
FROM flags
WHERE source_agent LIKE '@%'
AND target_agent LIKE '@%'
GROUP BY source_agent, target_agent;
```

### 7. **REGLAS PARA EVITAR PROBLEMAS**

```yaml
ANTI_LOOP:
  # En agent_db.py, añadir validación
  def validate_flag_creation(source, target):
      # No auto-flags
      if source == target:
          return False, "Cannot flag yourself"
      
      # Check recent reverse flags
      recent = query("""
          SELECT COUNT(*) as cnt FROM flags 
          WHERE source_agent = ? AND target_agent = ?
          AND created_at > datetime('now', '-5 minutes')
      """, [target, source])
      
      if recent[0]['cnt'] > 2:
          return False, "Possible flag loop detected"
      
      return True, "OK"

AUTO_CLEANUP:
  # Cron job o trigger
  - Flags > 7 días sin acknowledge → status='expired'
  - Flags de sesiones viejas → archive
  - Flags con agentes no existentes → status='orphaned'

PRIORIDAD_INTELIGENTE:
  critical: "Bloquea todo trabajo del agente"
  high: "Procesar antes que trabajo normal"  
  medium: "Mezclar con trabajo normal"
  low: "Solo cuando no hay más trabajo"
```

### 8. **COMANDO SIMPLIFICADO PARA CLAUDE**

```bash
# Alias simples para Claude Code
alias flag-check='python agent_db.py get-agent-flags'
alias flag-create='python agent_db.py create-flag'
alias flag-complete='python agent_db.py execute "UPDATE flags SET status=\"completed\" WHERE id="'

# Uso en Claude:
flag-check "@auth-agent"
flag-create --target_agent "@api-agent" --message "Interface changed"
flag-complete 45
```

## ✅ **BENEFICIOS DE ESTA EXTENSIÓN**

1. **Usa infraestructura existente** - No reinventamos la rueda
2. **Retrocompatible** - Los flags actuales siguen funcionando
3. **Simple para Claude** - Comandos claros y determinísticos
4. **Trazable** - Todo queda en la DB
5. **Escalable** - Funciona con N agentes

¡**EXCELENTE PUNTO**! Las flags necesitan poder orquestar **workflows complejos**. Aquí está mi propuesta:

## 🔄 **SISTEMA DE FLAGS CON WORKFLOWS**

### 1. **NUEVOS CAMPOS EN LA DB**

```sql
-- Añadir campos para workflows complejos
ALTER TABLE flags ADD COLUMN workflow_type TEXT DEFAULT 'single';  
-- 'single' | 'parallel' | 'sequential' | 'cascade'

ALTER TABLE flags ADD COLUMN workflow_steps JSON;
-- JSON con el workflow completo

ALTER TABLE flags ADD COLUMN parent_flag_id INTEGER;
-- Para flags que dependen de otras

ALTER TABLE flags ADD COLUMN step_number INTEGER DEFAULT 1;
-- Orden en workflow secuencial

ALTER TABLE flags ADD COLUMN dependencies JSON;
-- IDs de flags que deben completarse antes
```

### 2. **TIPOS DE WORKFLOWS**

```yaml
SINGLE (actual):
  target: "@auth-agent"
  action: "Update interface"

PARALLEL (todos a la vez):
  targets: ["@auth-agent", "@api-agent", "@frontend-agent"]
  action: "All update user model"
  completion: "when_all_done"

SEQUENTIAL (uno tras otro):
  steps:
    1: {target: "@auth-agent", action: "Implement feature"}
    2: {target: "@test.quality", action: "Define test strategy"}  
    3: {target: "@audit.security", action: "Security review"}
    4: {target: "@ops.deployment", action: "Deploy to staging"}
  completion: "when_last_done"

CASCADE (genera más flags):
  initial: "@database.postgres"
  triggers:
    on_complete: [
      {target: "@all-backend-agents", action: "Update queries"},
      {target: "@test.quality", action: "Update test fixtures"}
    ]
```

### 3. **ESTRUCTURA JSON PARA WORKFLOWS**

```json
{
  "workflow_type": "sequential",
  "steps": [
    {
      "step": 1,
      "target": "@payment-agent",
      "action": "Implement Stripe integration",
      "priority": "high",
      "estimated_hours": 4
    },
    {
      "step": 2,
      "target": "@test.quality",
      "action": "Define payment test scenarios",
      "priority": "high",
      "dependencies": ["step_1_complete"]
    },
    {
      "step": 3,
      "targets": ["@audit.security", "@audit.compliance"],
      "action": "Review payment implementation",
      "type": "parallel",
      "dependencies": ["step_2_complete"]
    },
    {
      "step": 4,
      "target": "@ops.deployment",
      "action": "Deploy to staging with feature flag",
      "dependencies": ["step_3_all_complete"]
    }
  ],
  "completion_criteria": "all_steps",
  "timeout_hours": 48,
  "on_failure": "rollback"
}
```

### 4. **FUNCIONES PYTHON MEJORADAS**

```python
def create_workflow_flag(workflow_type, steps, change_description, 
                         source_agent, priority='high'):
    """
    Crea un workflow complejo de flags
    """
    timestamp = get_timestamp()
    conn = sqlite3.connect(DB_PATH)
    
    # Crear flag padre (maestro)
    master_flag = {
        "flag_type": "workflow",
        "workflow_type": workflow_type,
        "source_agent": source_agent,
        "change_description": change_description,
        "status": "in_progress",
        "created_at": timestamp
    }
    
    cursor = conn.execute("""
        INSERT INTO flags (flag_type, workflow_type, source_agent, 
                          change_description, workflow_steps, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        "workflow", workflow_type, source_agent, 
        change_description, json.dumps(steps), 
        "in_progress", timestamp
    ))
    
    master_id = cursor.lastrowid
    
    # Crear flags hijas según el tipo
    if workflow_type == "parallel":
        for step in steps:
            create_child_flag(conn, master_id, step, step_number=None)
            
    elif workflow_type == "sequential":
        # Solo crear la primera, las demás se crean al completar
        create_child_flag(conn, master_id, steps[0], step_number=1)
        
    elif workflow_type == "cascade":
        # Crear inicial, esperar completion para triggers
        create_child_flag(conn, master_id, steps["initial"])
    
    conn.commit()
    conn.close()
    
    return json.dumps({
        "workflow_id": master_id,
        "type": workflow_type,
        "steps": len(steps),
        "status": "initiated"
    })

def complete_workflow_step(flag_id, completed_by):
    """
    Completa un paso y activa el siguiente si es secuencial
    """
    conn = sqlite3.connect(DB_PATH)
    
    # Marcar actual como completado
    conn.execute("""
        UPDATE flags 
        SET status = 'completed', 
            completed_at = ?,
            completed_by = ?
        WHERE id = ?
    """, (get_timestamp(), completed_by, flag_id))
    
    # Buscar si es parte de workflow
    cursor = conn.execute("""
        SELECT parent_flag_id, step_number 
        FROM flags 
        WHERE id = ?
    """, (flag_id,))
    
    row = cursor.fetchone()
    if row and row[0]:  # Es parte de workflow
        parent_id = row[0]
        current_step = row[1]
        
        # Obtener workflow info
        cursor = conn.execute("""
            SELECT workflow_type, workflow_steps 
            FROM flags 
            WHERE id = ?
        """, (parent_id,))
        
        parent = cursor.fetchone()
        if parent:
            workflow_type = parent[0]
            steps = json.loads(parent[1])
            
            if workflow_type == "sequential" and current_step:
                # Activar siguiente paso
                next_step = current_step + 1
                if next_step <= len(steps):
                    create_child_flag(conn, parent_id, 
                                    steps[next_step - 1], 
                                    step_number=next_step)
                else:
                    # Workflow completo
                    conn.execute("""
                        UPDATE flags 
                        SET status = 'completed',
                            completed_at = ?
                        WHERE id = ?
                    """, (get_timestamp(), parent_id))
            
            elif workflow_type == "parallel":
                # Verificar si todos completados
                cursor = conn.execute("""
                    SELECT COUNT(*) 
                    FROM flags 
                    WHERE parent_flag_id = ? 
                    AND status != 'completed'
                """, (parent_id,))
                
                pending = cursor.fetchone()[0]
                if pending == 0:
                    conn.execute("""
                        UPDATE flags 
                        SET status = 'completed',
                            completed_at = ?
                        WHERE id = ?
                    """, (get_timestamp(), parent_id))
    
    conn.commit()
    conn.close()
```

### 5. **CASOS DE USO REALES**

```yaml
CASO_1_NUEVO_FEATURE_COMPLETO:
  workflow: "sequential"
  steps:
    1: "@payment-agent: Implement Stripe"
    2: "@frontend-agent: Add payment UI"
    3: "@test.quality: Test strategy"
    4: "@audit.security: Security review"
    5: "@audit.compliance: PCI compliance check"
    6: "@ops.deployment: Deploy to staging"
    7: "@test.quality: E2E tests"
    8: "@ops.deployment: Deploy to production"

CASO_2_CAMBIO_BREAKING:
  workflow: "parallel_then_sequential"
  phase1_parallel:
    - "@all-backend-agents: Update to new API"
    - "@all-frontend-agents: Update to new API"
  phase2_sequential:
    - "@test.quality: Integration tests"
    - "@ops.deployment: Staged rollout"

CASO_3_SECURITY_FIX:
  workflow: "cascade"
  initial: "@audit.security: Critical vulnerability found"
  triggers:
    immediate: 
      - "@auth-agent: Apply security patch"
      - "@ops.monitoring: Add detection rules"
    after_patch:
      - "@test.quality: Regression tests"
      - "@ops.deployment: Emergency deploy"
    post_deploy:
      - "@audit.security: Verify fix"
      - "@docs.changelog: Document fix"
```

### 6. **COMANDO SIMPLIFICADO PARA CLAUDE**

```bash
# Crear workflow complejo
python agent_db.py create-workflow \
  --type "sequential" \
  --steps '[
    {"target": "@auth-agent", "action": "Add 2FA"},
    {"target": "@test.quality", "action": "Test 2FA"},
    {"target": "@audit.security", "action": "Review 2FA"}
  ]'

# Ver estado del workflow
python agent_db.py workflow-status 123

# Output:
{
  "workflow_id": 123,
  "status": "in_progress",
  "completed_steps": 1,
  "total_steps": 3,
  "current_step": {
    "target": "@test.quality",
    "action": "Test 2FA",
    "assigned_at": "2024-01-15 10:30"
  },
  "estimated_completion": "2024-01-15 18:00"
}
```

### 7. **VISUALIZACIÓN DEL WORKFLOW**

```sql
-- Vista para ver workflows activos
CREATE VIEW active_workflows AS
SELECT 
    f.id as workflow_id,
    f.workflow_type,
    f.change_description,
    f.created_at,
    COUNT(DISTINCT c.id) as total_steps,
    COUNT(DISTINCT CASE WHEN c.status = 'completed' THEN c.id END) as completed_steps,
    GROUP_CONCAT(
        CASE WHEN c.status = 'pending' 
        THEN c.target_agent 
        END, ', '
    ) as pending_agents,
    MAX(c.impact_level) as max_impact
FROM flags f
LEFT JOIN flags c ON f.id = c.parent_flag_id
WHERE f.workflow_type IS NOT NULL
AND f.status != 'completed'
GROUP BY f.id;
```

### 8. **SISTEMA ANTI-DEADLOCK**

```python
def detect_circular_dependencies(workflow_steps):
    """
    Detecta dependencias circulares antes de crear workflow
    """
    graph = {}
    for step in workflow_steps:
        if 'dependencies' in step:
            graph[step['id']] = step['dependencies']
    
    def has_cycle(node, visited, stack):
        visited.add(node)
        stack.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if has_cycle(neighbor, visited, stack):
                    return True
            elif neighbor in stack:
                return True
        
        stack.remove(node)
        return False
    
    visited = set()
    for node in graph:
        if node not in visited:
            if has_cycle(node, visited, set()):
                raise ValueError("Circular dependency detected!")
    
    return True
```

## ✅ **VENTAJAS DEL SISTEMA DE WORKFLOWS**

1. **Orquestación compleja** sin que Claude tenga que microgestionar
2. **Visibilidad total** del estado del workflow
3. **Recuperación automática** si falla un paso
4. **Prevención de deadlocks** y dependencias circulares
5. **Trazabilidad completa** de quién hizo qué y cuándo
