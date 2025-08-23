# FIX - Post-Creation Audit Checklist

## Final Review Tasks

Once all agents/prompts are created and individually audited, run a final sweep to:

### 1. Clean Formatting
- [ ] Remove all emojis from agent documents
- [ ] Ensure consistent markdown formatting
- [ ] Fix any encoding issues
- revisar si las comillas acaban bien en todos los documentos, veo muchos errores de triples comillas

### 2. Technical Validation
- [ ] Verify all variables are properly defined
- [ ] Check all file paths are absolute, not relative
- [ ] Validate SQLite database paths
- [ ] Ensure Python script paths use `~/.claude/scripts/`
- mirar las dos ultimas lineas filosofia y lo otro
- revisar tb en los documentos que no exista cosas de MCPS no pueden acceder a el ni de memoria solo flags si procede
- revisar que cada angente pueda hacer cosas, pero no anticiparse, como VUE que tiene -precommit, para que quiere precommit si el no va a commitear. cosas asi.
- si hay timers, es decir como roadmpas o chronograma quitarlos.
- revisar que todos tienes las flags correctas, no la version resumida.
- OJO cambiar en todos FLAGS NUEVAS

-instalar pupeeteer

### 3. Color Standardization by Role
```yaml
color_scheme:
  coordinators: blue  🪙    # Strategic orchestrators
  backend: purple         # Backend specialists
  frontend: orange         # Frontend specialists
  database: green        # Data management
  service: cyan          # External services
  business: gold         # Business logic
  ops: red              # Operations/DevOps
  setup: gray     🩶      # Configuration/setup
  docs: yellow          # Documentation
```

### 4. Routing Validation
- [ ] Verify all agents in `agent-routing.md` match actual files
- [ ] Update line counts in routing document
- [ ] Ensure "When:" conditions are clear and non-overlapping
- [ ] Validate agent handles follow naming convention

### 5. Final Checks
- [ ] All agents have proper frontmatter (name, description, model, color)
- [ ] Philosophy and Remember sections at end (where applicable)
- [ ] No duplicate agent responsibilities
- [ ] FLAGS section only in non-coordinator agents

## Execution
Run this as final QA before considering agent system production-ready.