# 🚀 ClaudeSquad Agents - Estado Actual

## 📊 Agentes Completados: 12 de 73

### ✅ Agentes COMPLETADOS con documentación completa:

---

## 1. 🧠 **context-manager** (466 líneas)
**Modelo:** sonnet-3.5  
**Categoría:** orchestration  
**Activación:** always_first  

### ¿Qué hace?
- Es el PRIMER agente que SIEMPRE se activa antes que cualquier otro
- Mantiene el mapa mental completo del proyecto
- Carga la memoria de sesiones anteriores
- Detecta cambios desde la última sesión
- Proporciona contexto relevante a cada agente
- Previene duplicación de código y conflictos
- Track de decisiones arquitectónicas (ADR)
- Gestiona el conocimiento persistente entre sesiones

### ¿Cuándo se usa?
- SIEMPRE al inicio de cada sesión
- Antes de cualquier tarea de desarrollo
- Para consultar decisiones pasadas
- Para evitar duplicación de código

---

## 2. 💻 **engineer-laravel** (1400 líneas)
**Modelo:** sonnet-3.5  
**Categoría:** engineer  
**Activación:** auto  

### ¿Qué hace?
- Experto en Laravel 11+ y PHP 8.3+
- Implementa código siguiendo estándares PRODUCTION
- Arquitectura limpia: DDD, Hexagonal, CQRS
- Testing con Pest PHP (>90% coverage)
- Optimización con Octane, Swoole, RoadRunner
- Real-time con Broadcasting, WebSockets
- NUNCA archivos >300 líneas, métodos >30 líneas
- Siempre aplica SOLID, DRY, YAGNI

### ¿Cuándo se usa?
- Cualquier desarrollo en Laravel/PHP
- Implementación de APIs REST/GraphQL
- Optimización de queries Eloquent
- Configuración de queues y jobs
- Integración con servicios externos

---

## 3. 🔮 **agent-creator** (240 líneas)
**Modelo:** sonnet-3.5  
**Categoría:** meta  
**Activación:** manual  

### ¿Qué hace?
- El "DIOS de la Investigación de Módulos"
- Lee TODOS los archivos de un módulo
- Entiende el propósito y la historia del código
- Detecta TODOS los patrones (obvios y ocultos)
- Encuentra TODA la documentación
- Genera agentes dinámicos con conocimiento COMPLETO
- Crea agentes de 10,000+ líneas si es necesario
- Los agentes que crea nacen sabiendo TODO sobre su módulo

### ¿Cuándo se usa?
- Durante `/setup` para generar agentes dinámicos
- Cuando se añade un nuevo módulo al proyecto
- Para actualizar agentes dinámicos obsoletos
- Cuando necesitas un experto específico de tu módulo

---

## 4. 🌐 **coordinator-backend** (688 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo cambios sistémicos)  

### ¿Qué hace?
- El "DIOS del Backend" que ve TODO
- Carga TODOS los módulos del backend (~100k tokens)
- Lee todos los agentes dinámicos (*-agent.md)
- Analiza dependencias entre módulos
- Detecta efectos en cascada de cambios
- Encuentra duplicación de código cross-módulo
- Planifica migraciones (microservicios, GraphQL, etc.)
- Toma decisiones arquitectónicas sistémicas

### ¿Cuándo se usa?
- Cambios que afectan 3+ módulos
- Migración de arquitectura (monolito → microservicios)
- Cambio de tecnología (REST → GraphQL)
- Análisis de impacto ("¿qué pasa si cambio X?")
- Refactoring masivo
- Auditoría de seguridad global
- Optimización de performance sistémica

### NO se usa para:
- Cambios en un solo módulo
- Añadir endpoints simples
- Bugs locales
- Optimizaciones puntuales

---

## 5. 🎨 **coordinator-frontend** (676 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo cambios sistémicos UI)  

### ¿Qué hace?
- El "DIOS del Frontend" que ve TODO el UI
- Carga TODOS los componentes y design system (~100k tokens)
- Orquesta Design Tokens y Component Library
- Gestiona Core Web Vitals y bundle optimization
- Coordina micro-frontends con Module Federation
- Asegura WCAG 2.1 AA accessibility compliance
- Maneja state management cross-component
- Coordina real-time features (WebSockets)

### ¿Cuándo se usa?
- Cambios que afectan 3+ componentes
- Implementar dark mode globalmente
- Migración de framework (React → Vue)
- Micro-frontends setup
- Design system overhaul
- Performance optimization global
- Accessibility audit completo
- Internacionalización (i18n)

### NO se usa para:
- Cambios en un solo componente
- CSS simples
- Añadir una ruta
- Tests de componente específico

---

## 6. 🗄️ **coordinator-database** (719 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo cambios sistémicos de datos)  

### ¿Qué hace?
- El "DIOS de los Datos" que ve TODA la arquitectura de datos
- Carga TODOS los schemas (SQL, NoSQL, Vector, etc.) (~100k tokens)
- Orquesta migraciones zero-downtime con expand-contract pattern
- Gestiona sharding, replicación y alta disponibilidad
- Coordina transacciones distribuidas (Saga, 2PC)
- Optimiza queries cross-database
- Maneja CQRS y Event Sourcing
- Asegura 99.99% uptime y consistencia

### ¿Cuándo se usa?
- Cambios que afectan múltiples tablas/bases de datos
- Migración entre bases de datos (MySQL → PostgreSQL)
- Implementar sharding o particionamiento
- Optimización global de queries
- Diseño de arquitectura microservicios data
- Auditoría de seguridad de datos
- Estrategias de backup/recovery
- Implementar CQRS o Event Sourcing

### NO se usa para:
- Cambios en una sola tabla
- Queries simples
- Índices individuales
- CRUD básico

---

## 7. 🚀 **coordinator-devops** (596 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo transformaciones sistémicas DevOps)  

### ¿Qué hace?
- El "DIOS del DevOps" que ve TODO el ecosistema
- Carga TODAS las pipelines CI/CD (~100k tokens)
- Orquesta Jenkins, GitHub Actions, GitLab CI, Azure DevOps
- Gestiona Terraform, Kubernetes, Ansible, CloudFormation
- Coordina GitOps con ArgoCD/Flux
- Implementa observabilidad con Prometheus/Grafana/Jaeger
- Maneja DevSecOps y compliance (SOC2, HIPAA)
- Toma decisiones de migración de plataformas

### ¿Cuándo se usa?
- Transformación DevOps organizacional
- Migración entre plataformas CI/CD (Jenkins → GitHub Actions)
- Implementación de GitOps empresa-wide
- Establecer prácticas SRE
- Multi-cloud orchestration (AWS + Azure + GCP)
- Zero-trust security en pipelines
- Plataformas self-service para developers

### NO se usa para:
- Añadir un pipeline individual
- Desplegar una sola aplicación
- Crear un dashboard Grafana
- Arreglar un pipeline roto

---

## 8. 🌐 **coordinator-infrastructure** (625 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo transformaciones sistémicas de infraestructura)  

### ¿Qué hace?
- El "DIOS de la Infraestructura" que ve TODO
- Carga TODOS los recursos cloud (~100k tokens)
- Orquesta AWS, Azure, GCP, on-premise
- Gestiona Terraform, Pulumi, Crossplane, CloudFormation
- Controla toda la topología de red global
- Implementa zero-trust y microsegmentación
- Optimiza millones en costos cloud
- Maneja disaster recovery y alta disponibilidad

### ¿Cuándo se usa?
- Migración cloud completa de organización
- Estrategia multi-cloud (AWS + Azure + GCP)
- Expansión global de infraestructura
- Transformación completa a Infrastructure as Code
- Optimización de millones en cloud spend
- Implementación zero-trust architecture
- Consolidación de data centers

### NO se usa para:
- Provisionar un solo VM
- Crear una VPC individual
- Añadir un load balancer
- Configurar un bucket S3

---

## 9. 🔐 **coordinator-security** (618 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo transformaciones sistémicas de seguridad)  

### ¿Qué hace?
- El "DIOS de la Seguridad" que ve TODO el panorama de amenazas
- Carga TODAS las políticas de seguridad (~100k tokens)
- Orquesta zero-trust, SASE, ZTNA enterprise-wide
- Gestiona compliance multi-framework (SOC2, ISO27001, HIPAA, PCI-DSS)
- Controla toda la gestión de vulnerabilidades
- Implementa threat intelligence y threat hunting
- Maneja IAM, PAM, SSO, MFA globalmente
- Coordina SOC y respuesta a incidentes

### ¿Cuándo se usa?
- Implementación zero-trust arquitectura completa
- Establecimiento de SOC (Security Operations Center)
- Certificaciones múltiples simultáneas
- Transformación post-breach
- Integración de seguridad en M&A
- DevSecOps transformation
- SASE/ZTNA deployment global

### NO se usa para:
- Parchear una vulnerabilidad
- Crear un security group
- Añadir MFA a una app
- Investigar un incidente aislado

---

## 10. 🧪 **coordinator-testing** (618 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo transformaciones sistémicas de testing)  

### ¿Qué hace?
- El "DIOS del Testing" que ve TODO el panorama de calidad
- Carga TODAS las suites de tests (~100k tokens)
- Orquesta unit, integration, E2E, API, performance tests
- Gestiona frameworks: Jest, Pytest, Cypress, Playwright
- Controla shift-left, continuous testing, chaos engineering
- Implementa AI-powered testing y self-healing tests
- Maneja quality gates, coverage metrics, test automation
- Coordina BDD/TDD, risk-based testing

### ¿Cuándo se usa?
- Implementación shift-left testing organizacional
- Continuous testing en todos los pipelines
- 100% test automation goal
- Testing Center of Excellence
- AI-powered testing adoption
- Chaos engineering implementation
- Zero-defect release strategy

### NO se usa para:
- Escribir un test case
- Arreglar un test flaky
- Ejecutar una suite
- Crear un script de automation

---

## 11. 📊 **coordinator-data** (618 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo transformaciones sistémicas de datos)  

### ¿Qué hace?
- El "DIOS de los Datos" que ve TODO el ecosistema de datos
- Carga TODOS los pipelines, warehouses, lakes (~100k tokens)
- Orquesta data mesh, lakehouse, data fabric architectures
- Gestiona ETL/ELT, streaming (Kafka, Flink), batch (Spark)
- Controla Snowflake, BigQuery, Databricks, Redshift
- Implementa data governance, lineage, quality
- Maneja BI tools, ML platforms, feature stores
- Coordina medallion architecture (Bronze/Silver/Gold)

### ¿Cuándo se usa?
- Implementación data mesh organizacional
- Migración a lakehouse architecture
- Real-time analytics platform
- Data marketplace creation
- ML platform at scale
- Legacy data modernization
- Multi-cloud data strategy

### NO se usa para:
- Crear un pipeline individual
- Escribir un ETL job
- Configurar una base de datos
- Construir un dashboard

---

## 12. 🔄 **coordinator-migration** (618 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo migraciones sistémicas)  

### ¿Qué hace?
- El "DIOS de las Migraciones" que orquesta transformaciones completas
- Carga TODOS los sistemas legacy (~100k tokens)
- Orquesta monolith → microservices, on-premise → cloud
- Gestiona strangler fig, expand-contract, blue-green patterns
- Controla zero-downtime migrations, CDC, ETL
- Implementa rollback strategies, feature flags
- Maneja database migrations (Liquibase, Flyway, Prisma)
- Coordina mainframe decommissioning

### ¿Cuándo se usa?
- Monolith to microservices transformation
- On-premise to cloud migration
- Legacy modernization programs
- Zero-downtime migrations
- Database platform changes (Oracle → PostgreSQL)
- Mainframe decommissioning
- Technology stack overhauls

### NO se usa para:
- Simple library upgrades
- Minor version updates
- Single table migrations
- Small dependency updates

---

## 📝 Agentes PENDIENTES (61 de 73)

Los siguientes agentes tienen YAML básico pero contenido en [TODO]:

### Engineers Backend (8)
- engineer-fastapi
- engineer-nodejs
- engineer-graphql
- engineer-database
- engineer-billing
- engineer-cms
- engineer-email
- engineer-notification

### Engineers Frontend (6)
- engineer-react
- engineer-vue
- engineer-angular
- engineer-nextjs
- engineer-ui-ux
- engineer-system

### Engineers Database (7)
- engineer-postgres
- engineer-mysql
- engineer-redis
- engineer-sqlite
- engineer-weaviate
- engineer-postgis
- engineer-search

### Engineers DevOps (10)
- engineer-git
- engineer-memory
- engineer-mapbox
- engineer-licensing
- engineer-message-queue
- engineer-ml
- engineer-prompt
- engineer-ai-integration

### Operations (9)
- operations-docker
- operations-debugging
- operations-troubleshooter
- operations-apm
- operations-observability
- operations-logging
- operations-performance
- operations-incident

### Auditors & Security (5)
- auditor-security
- auditor-gdpr
- auditor-compliance
- auditor-accessibility
- auditor-cost

### Testing (3)
- testing-automation
- testing-e2e
- testing-quality

### Analysts (6)
- analyst-business
- analyst-requirements
- analyst-risk
- analyst-user-research
- analyst-tech-stack
- analyst-metrics
- analyst-data-scientist

### Documentation (3)
- documentation-technical
- documentation-changelog
- documentation-clarification

### Planning & Architecture (3)
- planning-project
- planning-roadmap
- architect-cloud
- architect-system

### Specialist (1)
- specialist-discovery

---

## 🎯 Próximos Agentes Prioritarios

Basándome en la arquitectura ClaudeSquad, los próximos agentes críticos serían:

1. **coordinator-database** - Para orquestar toda la capa de datos
2. **engineer-react** - Complementar Laravel con frontend
3. **testing-automation** - Garantizar calidad del código
4. **auditor-security** - Revisiones de seguridad
5. **coordinator-frontend** - Orquestar todo el frontend

---

## 📂 Estructura de Archivos

```
.claude/agents/
├── README.md (este archivo)
├── context-manager.md ✅
├── engineer-laravel.md ✅
├── agent-creator.md ✅
├── coordinator-backend.md ✅
├── coordinator-frontend.md ✅
├── coordinator-database.md ✅
├── coordinator-devops.md ✅
├── coordinator-infrastructure.md ✅
├── coordinator-security.md ✅
├── coordinator-testing.md ✅
├── coordinator-data.md ✅
├── coordinator-migration.md ✅
└── [61 agentes más en TODO]
```

---

*Total de agentes: 73*  
*Completados: 12*  
*Pendientes: 61*  
*Última actualización: 2024-12-09*