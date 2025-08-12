# 📋 PROPUESTA DE RENOMBRADO DE AGENTES - v2

## 🎯 SISTEMA DE NOMBRES LARGOS (CATEGORÍA PRIMERO)

Formato: `[categoría]-[especialidad].md`

## 📊 CLASIFICACIÓN DEFINITIVA (71 agentes)

### COORDINADORES (9)
- backend-coordinator.md → `coordinator-backend.md`
- data-coordinator.md → `coordinator-data.md`
- database-coordinator.md → `coordinator-database.md`
- devops-coordinator.md → `coordinator-devops.md`
- frontend-coordinator.md → `coordinator-frontend.md`
- infrastructure-coordinator.md → `coordinator-infrastructure.md`
- migration-coordinator.md → `coordinator-migration.md`
- security-coordinator.md → `coordinator-security.md`
- testing-coordinator.md → `coordinator-testing.md`

### ENGINEERS - BACKEND (12)
- fastapi-engineer.md → `engineer-fastapi.md`
- graphql-engineer.md → `engineer-graphql.md`
- laravel-engineer.md → `engineer-laravel.md`
- message-queue-engineer.md → `engineer-message-queue.md`
- nodejs-engineer.md → `engineer-nodejs.md`
- cms-engineer.md → `engineer-cms.md`
- email-engineer.md → `engineer-email.md`
- notification-engineer.md → `engineer-notification.md`
- search-engineer.md → `engineer-search.md`
- weaviate-engineer.md → `engineer-weaviate.md`
- redis-engineer.md → `engineer-redis.md`
- git-engineer.md → `engineer-git.md`

### ENGINEERS - FRONTEND (5)
- angular-engineer.md → `engineer-angular.md`
- nextjs-engineer.md → `engineer-nextjs.md`
- react-engineer.md → `engineer-react.md`
- vue-engineer.md → `engineer-vue.md`
- ui-ux-engineer.md → `engineer-ui-ux.md`

### ENGINEERS - DATABASE (5)
- database-engineer.md → `engineer-database.md`
- mysql-engineer.md → `engineer-mysql.md`
- postgis-engineer.md → `engineer-postgis.md`
- postgres-engineer.md → `engineer-postgres.md`
- sqlite-engineer.md → `engineer-sqlite.md`

### ENGINEERS - AI/ML (4)
- ai-integration-engineer.md → `engineer-ai-integration.md`
- ml-engineer.md → `engineer-ml.md`
- prompt-engineer.md → `engineer-prompt.md`
- memory-engineer.md → `engineer-memory.md`

### ENGINEERS - ESPECIALISTAS (4)
- mapbox-engineer.md → `engineer-mapbox.md`
- billing-engineer.md → `engineer-billing.md`
- licensing-engineer.md → `engineer-licensing.md`
- system-engineer.md → `engineer-system.md`

### OPERATIONS (8)
- docker-engineer.md → `operations-docker.md`
- devops-troubleshooter.md → `operations-troubleshooter.md`
- incident-responder.md → `operations-incident.md`
- logging-engineer.md → `operations-logging.md`
- observability-engineer.md → `operations-observability.md`
- apm-engineer.md → `operations-apm.md`
- performance-tester.md → `operations-performance.md`
- debugging-engineer.md → `operations-debugging.md`

### ARCHITECTS (2)
- cloud-architect.md → `architect-cloud.md`
- architecture-engineer.md → `architect-system.md`

### ANALYSTS (7)
- business-analyst.md → `analyst-business.md`
- data-scientist.md → `analyst-data-scientist.md`
- metrics-analyst.md → `analyst-metrics.md`
- requirements-analyst.md → `analyst-requirements.md`
- risk-analyst.md → `analyst-risk.md`
- user-researcher.md → `analyst-user-research.md`
- tech-stack-selector.md → `analyst-tech-stack.md`

### AUDITORS (5)
- accessibility-auditor.md → `auditor-accessibility.md`
- compliance-auditor.md → `auditor-compliance.md`
- gdpr-compliance-engineer.md → `auditor-gdpr.md`
- security-auditor.md → `auditor-security.md`
- cost-optimizer.md → `auditor-cost.md`

### TESTING (3)
- e2e-engineer.md → `testing-e2e.md`
- test-automation-engineer.md → `testing-automation.md`
- quality-engineer.md → `testing-quality.md`

### PLANNING (2)
- project-engineer.md → `planning-project.md`
- project-planner.md → `planning-roadmap.md`

### DOCUMENTATION (3)
- docs-engineer.md → `documentation-technical.md`
- changelog-engineer.md → `documentation-changelog.md`
- clarification-engineer.md → `documentation-clarification.md`

### SPECIALIST (1)
- discovery-engineer.md → `specialist-discovery.md`

---

## 📝 SCRIPT DE RENOMBRADO

```bash
#!/bin/bash
# Script para renombrar todos los agentes

cd .claude/agents/

# COORDINADORES
mv backend-coordinator.md coordinator-backend.md
mv data-coordinator.md coordinator-data.md
mv database-coordinator.md coordinator-database.md
mv devops-coordinator.md coordinator-devops.md
mv frontend-coordinator.md coordinator-frontend.md
mv infrastructure-coordinator.md coordinator-infrastructure.md
mv migration-coordinator.md coordinator-migration.md
mv security-coordinator.md coordinator-security.md
mv testing-coordinator.md coordinator-testing.md

# ENGINEERS - BACKEND
mv fastapi-engineer.md engineer-fastapi.md
mv graphql-engineer.md engineer-graphql.md
mv laravel-engineer.md engineer-laravel.md
mv message-queue-engineer.md engineer-message-queue.md
mv nodejs-engineer.md engineer-nodejs.md
mv cms-engineer.md engineer-cms.md
mv email-engineer.md engineer-email.md
mv notification-engineer.md engineer-notification.md
mv search-engineer.md engineer-search.md
mv weaviate-engineer.md engineer-weaviate.md
mv redis-engineer.md engineer-redis.md
mv git-engineer.md engineer-git.md

# ENGINEERS - FRONTEND
mv angular-engineer.md engineer-angular.md
mv nextjs-engineer.md engineer-nextjs.md
mv react-engineer.md engineer-react.md
mv vue-engineer.md engineer-vue.md
mv ui-ux-engineer.md engineer-ui-ux.md

# ENGINEERS - DATABASE
mv database-engineer.md engineer-database.md
mv mysql-engineer.md engineer-mysql.md
mv postgis-engineer.md engineer-postgis.md
mv postgres-engineer.md engineer-postgres.md
mv sqlite-engineer.md engineer-sqlite.md

# ENGINEERS - AI/ML
mv ai-integration-engineer.md engineer-ai-integration.md
mv ml-engineer.md engineer-ml.md
mv prompt-engineer.md engineer-prompt.md
mv memory-engineer.md engineer-memory.md

# ENGINEERS - ESPECIALISTAS
mv mapbox-engineer.md engineer-mapbox.md
mv billing-engineer.md engineer-billing.md
mv licensing-engineer.md engineer-licensing.md
mv system-engineer.md engineer-system.md

# OPERATIONS
mv docker-engineer.md operations-docker.md
mv devops-troubleshooter.md operations-troubleshooter.md
mv incident-responder.md operations-incident.md
mv logging-engineer.md operations-logging.md
mv observability-engineer.md operations-observability.md
mv apm-engineer.md operations-apm.md
mv performance-tester.md operations-performance.md
mv debugging-engineer.md operations-debugging.md

# ARCHITECTS
mv cloud-architect.md architect-cloud.md
mv architecture-engineer.md architect-system.md

# ANALYSTS
mv business-analyst.md analyst-business.md
mv data-scientist.md analyst-data-scientist.md
mv metrics-analyst.md analyst-metrics.md
mv requirements-analyst.md analyst-requirements.md
mv risk-analyst.md analyst-risk.md
mv user-researcher.md analyst-user-research.md
mv tech-stack-selector.md analyst-tech-stack.md

# AUDITORS
mv accessibility-auditor.md auditor-accessibility.md
mv compliance-auditor.md auditor-compliance.md
mv gdpr-compliance-engineer.md auditor-gdpr.md
mv security-auditor.md auditor-security.md
mv cost-optimizer.md auditor-cost.md

# TESTING
mv e2e-engineer.md testing-e2e.md
mv test-automation-engineer.md testing-automation.md
mv quality-engineer.md testing-quality.md

# PLANNING
mv project-engineer.md planning-project.md
mv project-planner.md planning-roadmap.md

# DOCUMENTATION
mv docs-engineer.md documentation-technical.md
mv changelog-engineer.md documentation-changelog.md
mv clarification-engineer.md documentation-clarification.md

# SPECIALIST
mv discovery-engineer.md specialist-discovery.md

echo "✅ Renombrado completado!"
```

---

## ✅ VENTAJAS DE ESTE SISTEMA

1. **Organización clara**: Se ve inmediatamente qué tipo de agente es
2. **Alfabético útil**: Todos los coordinadores juntos, todos los engineers juntos, etc.
3. **Búsqueda fácil**: `coordinator-*` encuentra todos los coordinadores
4. **Sin ambigüedad**: Cada agente tiene su categoría clara
5. **Extensible**: Fácil agregar nuevas categorías

---

## 🚀 ¿PROCEDEMOS?

Si estás de acuerdo con esta clasificación, ejecutaré el renombrado automático.

Total de cambios: **71 archivos** renombrados con el formato `[categoría]-[especialidad].md`