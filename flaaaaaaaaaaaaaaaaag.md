## 🚩 FLAG System - Inter-Agent Communication

### What are FLAGS?

FLAGS are asynchronous coordination messages between agents stored in SQLite database.

- When you modify code/config affecting other modules → create FLAG for them
- When others modify things affecting you → they create FLAG for you
- FLAGS ensure system-wide consistency across all agents

### On Invoked - ALWAYS Check FLAGS First

```bash
# MANDATORY: Check pending flags before ANY work
uv run python ~/.claude/scripts/agent_db.py get-agent-flags "@service.ai"
# Returns only status='pending' flags automatically
```

### FLAG Processing Decision Tree

```python
# EXPLICIT DECISION LOGIC - No ambiguity
flags = get_agent_flags("@service.ai")

if flags.empty:
    proceed_with_primary_request()
else:
    # Process by priority: critical → high → medium → low
    for flag in flags:
        if flag.locked == True:
            # Another agent handling or awaiting response
            skip_flag()

        elif flag.change_description.contains("schema change"):
            # Database structure changed
            update_ai_models_schema()
            complete_flag(flag.id)

        elif flag.change_description.contains("API endpoint"):
            # API routes changed
            update_service_integrations()
            complete_flag(flag.id)

        elif flag.change_description.contains("authentication"):
            # Auth system modified
            update_ml_auth_middleware()
            complete_flag(flag.id)

        elif need_more_context(flag):
            # Need clarification
            lock_flag(flag.id)
            create_information_request_flag()

        elif not_ai_ml_related(flag):
            # Not your domain
            complete_flag(flag.id, note="Not applicable to AI/ML services")
```

### FLAG Processing Examples

**Example 1: Database Schema Change**

```
Received FLAG: "users table added 'ml_preferences' JSON column for AI personalization"
Your Action:
1. Update data loaders to handle new column
2. Modify feature extractors if using user data
3. Update model training pipelines
4. Test with new schema
5. complete-flag [FLAG_ID] "@service.ai"
```

**Example 2: API Breaking Change**

```
Received FLAG: "POST /api/predict deprecated, use /api/v2/inference with new auth headers"
Your Action:
1. Update all prediction service calls
2. Implement new auth header format
3. Update integration tests
4. Update documentation
5. complete-flag [FLAG_ID] "@service.ai"
```

**Example 3: Need More Information**

```
Received FLAG: "Switching to new vector database for embeddings"
Your Action:
1. lock-flag [FLAG_ID]
2. create-flag --flag_type "information_request" \
   --target_agent "@database.vector" \
   --change_description "Need specs for FLAG #[ID]: vector DB migration" \
   --action_required "Provide: 1) New DB connection details 2) Migration timeline 3) Embedding format changes 4) Backward compatibility plan"
3. Wait for response FLAG
4. Implement based on response
5. unlock-flag [FLAG_ID]
6. complete-flag [FLAG_ID] "@service.ai"
```

### Complete FLAG After Processing

```bash
# Mark as done when implementation complete
uv run python ~/.claude/scripts/agent_db.py complete-flag [FLAG_ID] "@service.ai"
```

### Lock/Unlock for Bidirectional Communication

```bash
# Lock when need clarification
uv run python ~/.claude/scripts/agent_db.py lock-flag [FLAG_ID]

# Create information request
uv run python ~/.claude/scripts/agent_db.py create-flag \
  --flag_type "information_request" \
  --source_agent "@service.ai" \
  --target_agent "@[EXPERT]" \
  --change_description "Need clarification on FLAG #[FLAG_ID]: [specific question]" \
  --action_required "Please provide: [detailed list of needed information]" \
  --impact_level "high"

# After receiving response
uv run python ~/.claude/scripts/agent_db.py unlock-flag [FLAG_ID]
uv run python ~/.claude/scripts/agent_db.py complete-flag [FLAG_ID] "@service.ai"
```

### Create FLAG When Your Changes Affect Others

```bash
uv run python ~/.claude/scripts/agent_db.py create-flag \
  --flag_type "[type]" \
  --source_agent "@service.ai" \
  --target_agent "@[TARGET]" \
  --change_description "[what changed - min 50 chars with specifics]" \
  --action_required "[exact steps they need to take - min 100 chars]" \
  --impact_level "[level]" \
  --related_files "[file1.py,file2.js,config.json]" \
  --chain_origin_id "[original_flag_id_if_chain]"
```

### Advanced FLAG Parameters

**related_files**: Comma-separated list of affected files

- Helps agents identify scope of changes
- Used for conflict detection between parallel FLAGS
- Example: `--related_files "models/user.py,api/endpoints.py,config/ml.json"`

**chain_origin_id**: Track FLAG chains for complex workflows

- Use when your FLAG is result of another FLAG
- Maintains traceability of cascading changes
- Example: `--chain_origin_id "123"` if FLAG #123 triggered this new FLAG
- Helps detect circular dependencies

### When to Create FLAGS

**ALWAYS create FLAG when you:**

- Changed AI model API endpoints
- Modified ML pipeline outputs
- Updated vector database schemas
- Changed authentication for AI services
- Deprecated AI/ML features
- Added new AI capabilities
- Modified shared configuration files
- Changed data formats or schemas

**flag_type Options:**

- `breaking_change`: Existing integrations will break
- `new_feature`: New AI capability available
- `refactor`: Internal changes, external API same
- `deprecation`: Feature being removed
- `information_request`: Need clarification

**impact_level Guide:**

- `critical`: System breaks without immediate action
- `high`: Functionality degraded, action needed soon
- `medium`: Standard coordination, handle normally
- `low`: FYI, handle when convenient

### FLAG Chain Example

```bash
# Original FLAG #100: "Migrating to new ML framework"
# You need to update models, which affects API

# Create chained FLAG
uv run python ~/.claude/scripts/agent_db.py create-flag \
  --flag_type "breaking_change" \
  --source_agent "@service.ai" \
  --target_agent "@backend.api" \
  --change_description "ML models output format changed due to framework migration" \
  --action_required "Update API response handlers for /predict and /classify endpoints to handle new tensor format" \
  --impact_level "high" \
  --related_files "models/predictor.py,models/classifier.py,api/ml_endpoints.py" \
  --chain_origin_id "100"
```

### After Processing All FLAGS

- Continue with original user request
- FLAGS have priority over new work
- Document changes made due to FLAGS
- If FLAGS caused major changes, create new FLAGS for affected agents

### CRITICAL RULES

1. FLAGS are the ONLY way agents communicate
2. No direct agent-to-agent calls
3. Always process FLAGS before new work
4. Complete or lock every FLAG (never leave hanging)
5. Create FLAGS for ANY change affecting other modules
6. Use related_files for better coordination
7. Use chain_origin_id to track cascading changes
