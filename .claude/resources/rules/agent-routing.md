# ClaudeSquad Agents Catalog & Routing Rules

## Agent Statistics

**Total Agents:** 58  
**Completed Agents:** 35 (60.3%)  
**Pending Agents:** 23 (39.7%)

---

## 🚀 Setup and Configuration

✅ **setup.agent-creator** (358 lines) - Module research specialist that reads all module files, understands code purpose and creates the perfect dynamic agent for the assigned module.
✅ **setup.codebase** (186 lines) - Analyzes code structure, modules, quality, tests and technical patterns  
✅ **setup.context** (113 lines) - Analyzes project architecture and tech stack during initial configuration  
✅ **setup.environment** (161 lines) - Detects development environment configuration and tools  
✅ **setup.infrastructure** (197 lines) - Analyzes deployment infrastructure and DevOps configuration

## 🎮 Control and Orchestration

✅ **coordinator.backend** (620 lines)  
 **Role:** Strategic backend architecture orchestrator  
 **Tech:** Microservices, API design, service mesh, distributed systems, load balancing  
 **When:** IF designing backend architecture OR choosing between multiple backend technologies OR scaling strategy

✅ **coordinator.database** (1727 lines)  
 **Role:** Strategic data architecture orchestrator  
 **Tech:** SQL/NoSQL/Vector databases, data modeling, replication, sharding, analytics  
 **When:** IF choosing database technology OR designing data architecture OR planning data flow across systems

✅ **coordinator.devops** (527 lines)  
 **Role:** Strategic DevOps and automation orchestrator  
 **Tech:** CI/CD strategy, GitOps, release management patterns, automation workflows  
 **When:** DevOps strategy, pipeline architecture, deployment patterns, release planning

✅ **coordinator.frontend** (611 lines)  
 **Role:** Strategic frontend architecture orchestrator  
 **Tech:** React, Vue, Angular, state management, micro-frontends, design systems  
 **When:** Frontend architecture decisions, UI framework selection, component strategy

✅ **coordinator.infrastructure** (625 lines)  
 **Role:** Strategic infrastructure architect  
 **Tech:** Multi-cloud (AWS, Azure, GCP), load balancers, CDN, auto scaling, capacity planning  
 **When:** Multi-cloud architecture, infrastructure strategy, workload placement, disaster recovery planning

✅ **coordinator.migration** (549 lines)  
 **Role:** Strategic migration and transformation orchestrator  
 **Tech:** Legacy modernization, cloud migration, data migration, re-architecture patterns  
 **When:** Migration strategy planning, legacy transformation, technology stack migrations

✅ **coordinator.security** (549 lines)  
 **Role:** Strategic security architecture orchestrator  
 **Tech:** IAM/RBAC, compliance frameworks (SOC2, PCI, HIPAA), security scanning, incident response  
 **When:** Security architecture design, compliance strategy, security policy orchestration

✅ **coordinator.testing** (549 lines)  
 **Role:** Strategic testing and quality orchestrator  
 **Tech:** Test automation frameworks, quality gates, performance testing, test data management  
 **When:** Testing strategy design, quality assurance architecture, test automation planning

## 💾 Data Management

✅ **database.mariadb** (1242 lines)  
 **Role:** MariaDB specialist and MySQL evolution expert  
 **Tech:** MariaDB 11+, Galera clustering, MaxScale load balancing, ColumnStore analytics, Spider sharding  
 **When:** MySQL modernization, high-availability clustering, zero-downtime migrations, analytical workloads

✅ **database.mongodb** (1786 lines)  
 **Role:** MongoDB and NoSQL document database expert  
 **Tech:** MongoDB 7+, aggregation pipelines, sharding, change streams, Atlas, Compass, document modeling  
 **When:** Flexible document schemas, real-time data streaming, content management, rapid prototyping

✅ **database.pgvector** (2251 lines)  
 **Role:** PostgreSQL vector database and AI search expert  
 **Tech:** PostgreSQL + pgvector, HNSW/IVFFlat indexing, pgvectorscale, embedding models, hybrid search  
 **When:** RAG applications, semantic search, similarity matching, AI-powered recommendations, multi-modal search

✅ **database.postgres** (1453 lines)  
 **Role:** PostgreSQL advanced features and performance expert  
 **Tech:** PostgreSQL 15+, advanced indexing (GiST, GIN, BRIN), TimescaleDB, PgBouncer, Citus, PostGIS  
 **When:** Complex relational data, time-series analytics, geospatial applications, enterprise OLTP systems

✅ **database.redis** (763 lines)  
 **Role:** Redis in-memory data structures and caching expert  
 **Tech:** Redis 7+, Redis Stack (JSON, Search, Graph), Streams, pub/sub, clustering, Lua scripting  
 **When:** Sub-millisecond caching, session storage, real-time leaderboards, pub/sub messaging, rate limiting

✅ **database.sqlite** (1126 lines)  
 **Role:** SQLite embedded database and edge computing expert  
 **Tech:** SQLite 3.44+, WAL mode, FTS5, JSON operations, Core ML optimization, Litestream replication  
 **When:** Embedded applications, edge computing, mobile apps, serverless databases, local-first architectures

✅ **database.weaviate** (3513 lines)  
 **Role:** Vector database and semantic search expert  
 **Tech:** Weaviate v4+, HNSW indexing, REST API, vectorization modules, hybrid search, multi-tenancy  
 **When:** RAG applications, semantic search, question-answering systems, multi-modal AI search, knowledge graphs

🔳 **database.postgis** (0 lines)  
 **Role:** PostGIS geospatial database and GIS expert  
 **Tech:** PostGIS, spatial indexing, geographic queries, coordinate systems, spatial analysis  
 **When:** Location-based applications, mapping systems, geographic data analysis, spatial queries

## 💻 Software Development

### Frontend

✅ **frontend.angular** (1249 lines)  
 **Role:** Angular framework and enterprise TypeScript expert  
 **Tech:** Angular 17+, TypeScript, RxJS, Angular Material, PrimeNG, NgRx, standalone components  
 **When:** Enterprise applications, complex forms, reactive programming, TypeScript-heavy projects

✅ **frontend.react** (1685 lines)  
 **Role:** React ecosystem and modern JavaScript expert  
 **Tech:** React 18+, Next.js, TypeScript, Material-UI, Chakra UI, shadcn/ui, Zustand, React Query  
 **When:** Single-page applications, server-side rendering, component libraries, modern web apps

✅ **frontend.vue** (1564 lines)  
 **Role:** Vue.js ecosystem and progressive framework expert  
 **Tech:** Vue 3+, Nuxt.js, TypeScript, Composition API, Vuetify, Pinia, Vue Router, Vite  
 **When:** Progressive web apps, rapid prototyping, developer-friendly projects, gradual adoption

🔳 **frontend.mobile** (0 lines)  
 **Role:** Cross-platform mobile development expert  
 **Tech:** React Native, Flutter, Expo, Capacitor, native modules, app store deployment, mobile CI/CD  
 **When:** Mobile app development, cross-platform solutions, native feature integration, app store publishing

### Backend

✅ **backend.laravel** (1139 lines)  
 **Role:** Laravel framework and PHP ecosystem expert  
 **Tech:** Laravel 11+, PHP 8.3+, Eloquent ORM, Livewire, Inertia.js, Horizon, Telescope  
 **When:** Rapid web development, MVC architecture, PHP-based applications, admin panels

✅ **backend.nodejs** (2109 lines)  
 **Role:** Node.js runtime and JavaScript backend expert  
 **Tech:** Node.js 20+, Express, NestJS, TypeScript, Fastify, Prisma, Socket.io, microservices  
 **When:** IF implementing Node.js backend OR real-time features OR JavaScript-based microservices

✅ **backend.python** (2644 lines)  
 **Role:** Python ecosystem and versatile backend expert  
 **Tech:** Python 3.11+, Django, FastAPI, Flask, SQLAlchemy, Celery, asyncio, data processing  
 **When:** Data-heavy applications, ML integration, rapid development, scientific computing

🔳 **backend.go** (0 lines)  
 **Role:** Go language and high-performance systems expert  
 **Tech:** Go 1.21+, Gin, Echo, Fiber, gRPC, concurrency patterns, goroutines, channels  
 **When:** High-performance APIs, microservices, system programming, concurrent processing

🔳 **backend.java** (0 lines)  
 **Role:** Java enterprise and Spring ecosystem expert  
 **Tech:** Java 17+, Spring Boot, Spring Cloud, Hibernate, Maven, Gradle, enterprise patterns  
 **When:** Enterprise applications, large-scale systems, legacy modernization, corporate environments

🔳 **backend.rust** (0 lines)  
 **Role:** Rust systems programming and performance expert  
 **Tech:** Rust, Actix-web, Rocket, Axum, Tokio, WebAssembly, async programming, memory safety  
 **When:** System-level programming, performance-critical applications, WebAssembly, safe concurrency

🔳 **backend.api** (0 lines)  
 **Role:** API design and integration architecture expert  
 **Tech:** REST, GraphQL, WebSocket, gRPC, OpenAPI/Swagger, API gateways, rate limiting, versioning  
 **When:** API-first development, GraphQL schemas, API governance, documentation standards

🔳 **backend.serverless** (0 lines)  
 **Role:** Serverless functions and edge computing expert  
 **Tech:** AWS Lambda, Vercel Functions, Netlify Functions, CloudFlare Workers, edge runtime, FaaS patterns  
 **When:** Serverless architectures, edge computing, event-driven functions, cost-optimized backends

### Services

✅ **service.ai** (5565 lines)  
 **Role:** AI/ML integration and model management expert  
 **Tech:** LangGraph, CrewAI, AutoGen, advanced RAG (Agentic RAG, HyDE), vector databases (Qdrant, Milvus, pgvector), modern fine-tuning (PEFT/LoRA/QLoRA), latest models (DeepSeek-V3, Llama 3.3, Mistral Large 2, Qwen 2.5), production deployment (vLLM, TGI, Ollama), LangSmith observability  
 **When:** AI feature integration, chatbots, content generation, ML model deployment, prompt optimization, advanced RAG systems, vector search, agent orchestration

✅ **service.auth** (2588 lines)  
 **Role:** Authentication and authorization security expert  
 **Tech:** OAuth2, JWT, SSO (SAML, OIDC), Auth0, Firebase Auth, Passport.js, multi-factor authentication, RBAC  
 **When:** IF implementing user authentication OR OAuth flows OR SSO integration OR JWT token management

✅ **service.communication** (2042 lines)  
 **Role:** Multi-channel communication and messaging expert  
 **Tech:** Twilio Messaging Services with A2P compliance, SendGrid v3 API with dynamic templates, Firebase Cloud Messaging (FCM) v1 API, WebSocket architecture with Socket.IO, webhook validation, circuit breaker patterns, message queuing with retry mechanisms, PII detection, GDPR compliance, real-time monitoring  
 **When:** Transactional emails, SMS notifications, push notifications, real-time messaging, webhook processing

✅ **service.data** (1828 lines)  
 **Role:** Data processing and infrastructure services expert  
 **Tech:** Elasticsearch/OpenSearch 8+ with advanced indexing and cluster management, Apache Kafka 3.8+ with Kafka Streams and event-driven architectures, Apache Airflow 2.10+ with TaskFlow API and enterprise deployment, RabbitMQ 4+ with advanced clustering and HA, modern ETL/ELT pipelines, enterprise data mesh architecture, real-time streaming, comprehensive monitoring & observability  
 **When:** Search functionality, data streaming, message queuing, data pipelines, real-time data processing

✅ **service.integrations** (1675 lines)  
 **Role:** Third-party API integration and external services expert  
 **Tech:** REST APIs, SDK integrations, rate limiting, web scraping (Playwright, Selenium), data synchronization  
 **When:** External API consumption, third-party SDKs, service orchestration, automation workflows

✅ **service.mapbox** (847 lines)  
 **Role:** Mapbox and geospatial services expert  
 **Tech:** Mapbox GL JS, Navigation API, geocoding, routing, spatial analysis, custom map styles, location services  
 **When:** Interactive maps, location-based features, route optimization, geofencing, spatial data visualization

## 💼 Business Systems

✅ **business.billing** (1821 lines)  
 **Role:** Billing systems and revenue management expert  
 **Tech:** Stripe Billing, invoice generation, tax calculation, revenue recognition, dunning management  
 **When:** SaaS billing, subscription management, complex pricing models, tax compliance, revenue reporting

✅ **business.payment** (2001 lines)  
 **Role:** Payment processing and financial transactions expert  
 **Tech:** Stripe, PayPal, Square, PCI compliance, tokenization, fraud prevention, 3D Secure, webhooks  
 **When:** E-commerce payments, transaction processing, financial integrations, payment security, fraud detection

🔳 **business.subscription** (0 lines)  
 **Role:** SaaS subscription and recurring revenue expert  
 **Tech:** Subscription models, usage-based billing, metered pricing, customer lifecycle, churn prevention  
 **When:** SaaS platforms, recurring revenue models, subscription analytics, customer retention strategies

## 📝 Documentation

✅ **docs.changelog** (303 lines) - Professional changelog and semantic versioning expert

🔳 **docs.technical** (0 lines)  
 **Role:** Technical documentation and competitive GitHub README expert  
 **Tech:** Markdown mastery, Mermaid diagrams, GitHub badges, shields.io, OpenAPI/Swagger, GitBook, competitive README analysis  
 **When:** GitHub README optimization, API documentation, technical guides, visual diagrams, competitive documentation analysis

### 📊 Analysis and Strategy

🔳 **analyst.strategic** (0 lines)  
 **Role:** Business and technical strategy analysis expert  
 **Tech:** Requirements analysis, roadmap planning, stakeholder analysis, competitive analysis, market research tools  
 **When:** Strategic planning, business requirements, technology selection, project roadmaps, feasibility studies

🔳 **analyst.data** (0 lines)  
 **Role:** Data science and analytics expert  
 **Tech:** Python (pandas, numpy), R, Jupyter, Tableau, Power BI, statistical analysis, machine learning, predictive modeling  
 **When:** Data analysis, KPIs definition, user research, predictive analytics, business intelligence, risk assessment

### 🔍 Audit and Compliance

🔳 **audit.compliance** (0 lines)  
 **Role:** Regulatory compliance and accessibility expert  
 **Tech:** GDPR compliance tools, WCAG guidelines, accessibility testing, cost optimization tools, compliance frameworks  
 **When:** Regulatory compliance, accessibility audits, cost analysis, privacy compliance, legal requirements

🔳 **audit.security** (0 lines)  
 **Role:** Security vulnerability assessment expert  
 **Tech:** OWASP tools, penetration testing, vulnerability scanners, security frameworks, threat modeling  
 **When:** Security audits, vulnerability assessments, penetration testing, security compliance, threat analysis

---

### ⚙️ Operations and DevOps

✅ **ops.git** (955 lines)  
 **Role:** Git workflow and version control expert  
 **Tech:** Git, GitHub Actions, branching strategies, conventional commits, git hooks, submodules, LFS  
 **When:** Repository management, branching strategies, commit conventions, code review workflows, version control optimization

🔳 **ops.monitoring** (0 lines)  
 **Role:** Application monitoring and observability expert  
 **Tech:** Prometheus, Grafana, ELK stack, APM tools (DataDog, New Relic), OpenTelemetry, custom dashboards, alerting  
 **When:** System monitoring, log aggregation, alerting systems, observability implementation, metrics collection

🔳 **ops.containers** (0 lines)  
 **Role:** Container orchestration and tactical deployment expert  
 **Tech:** Docker, Kubernetes deployments, Helm charts, Istio service mesh, container registries, ingress controllers  
 **When:** Container deployments, Kubernetes manifests, service mesh configuration, container security, pod orchestration

🔳 **ops.webserver** (0 lines)  
 **Role:** Web server configuration and reverse proxy expert  
 **Tech:** Nginx, Apache, Caddy, HAProxy, SSL/TLS certificates, reverse proxy, load balancing, HTTP/3  
 **When:** Web server setup, reverse proxy configuration, SSL certificate management, traffic routing

🔳 **ops.cicd** (0 lines)  
 **Role:** CI/CD pipeline implementation and automation expert  
 **Tech:** Jenkins, GitLab CI, CircleCI, GitHub Actions, ArgoCD, deployment automation, pipeline optimization  
 **When:** CI/CD pipeline creation, build automation, deployment pipelines, continuous integration setup

🔳 **ops.iac** (0 lines)  
 **Role:** Infrastructure as Code implementation expert  
 **Tech:** Terraform, Pulumi, Ansible, CloudFormation, configuration management, infrastructure automation  
 **When:** Infrastructure provisioning, configuration management, infrastructure automation, IaC implementation

🔳 **ops.troubleshooting** (0 lines)  
 **Role:** System debugging and incident resolution expert  
 **Tech:** Debugging tools, profiling tools, root cause analysis, incident response, diagnostic techniques, error tracking  
 **When:** Production issues, system failures, incident management, problem diagnosis, emergency response

🔳 **ops.performance** (0 lines)  
 **Role:** Application and system performance optimization expert  
 **Tech:** Performance profiling, load testing (JMeter, k6), caching strategies, database tuning, code optimization  
 **When:** Performance bottlenecks, scalability issues, optimization strategies, load testing, capacity planning

### 🧪 Testing and Quality

🔳 **test.quality** (0 lines)  
 **Role:** Comprehensive testing and quality assurance expert  
 **Tech:** Jest, Cypress, Playwright, JUnit, pytest, test automation frameworks, coverage tools (Istanbul, c8)  
 **When:** Test strategy implementation, automated testing pipelines, quality gates, coverage analysis, testing best practices

### 📅 Planning

🔳 **plan.strategy** (0 lines)  
 **Role:** Project management and strategic planning expert  
 **Tech:** Project management tools (Jira, Asana), agile methodologies, resource planning, timeline management, Gantt charts  
 **When:** Project planning, resource allocation, sprint planning, roadmap creation, timeline management

---

## 🎯 Agent Routing Rules

**Critical:** Use these IF/THEN rules for precise agent selection. Each rule eliminates ambiguity and ensures 0% routing errors.

### 🎮 Coordinators (Strategy/Architecture)

| Domain                     | IF (technical conditions)                                                           | THEN (agent)               | Priority |
| -------------------------- | ----------------------------------------------------------------------------------- | -------------------------- | -------- |
| Backend Architecture       | Choosing microservices/monolith; service mesh; service boundaries; scaling strategy | coordinator.backend        | Solo     |
| Data Architecture          | Selecting SQL/NoSQL/Vector; data modeling; partitioning/sharding; E2E data flows    | coordinator.database       | Solo     |
| DevOps Strategy            | High-level CI/CD design; GitOps; releases; promotion policies                       | coordinator.devops         | Solo     |
| Frontend Architecture      | Micro-frontends; design system; choosing React/Vue/Angular; global state            | coordinator.frontend       | Solo     |
| Infrastructure Multi-cloud | AWS/Azure/GCP; load balancing, CDN, autoscaling; DR/BCP                             | coordinator.infrastructure | Solo     |
| Migration                  | Modernization/rehosting/re-platforming; migration plans                             | coordinator.migration      | Solo     |
| Security Strategy          | IAM/RBAC; compliance (SOC2/PCI/HIPAA); incident response                            | coordinator.security       | Solo     |
| Testing Strategy           | Automation strategy; quality gates; test data management                            | coordinator.testing        | Solo     |

**Golden Rule:** IF choosing between technologies OR cross-domain decisions → Coordinator first; Specialist after (sequential).

### 💻 Frontend Routing

| Domain          | IF                                                                      | THEN                                       | Priority                       |
| --------------- | ----------------------------------------------------------------------- | ------------------------------------------ | ------------------------------ |
| Angular         | Angular 17+, NgRx, Angular Material/PrimeNG, complex forms              | frontend.angular                           | Solo                           |
| React           | React 18+/Next.js, UI libs (MUI/Chakra/shadcn), React Query/Zustand     | frontend.react                             | Solo                           |
| Vue             | Vue 3/Nuxt, Composition API, Pinia, Vuetify                             | frontend.vue                               | Solo                           |
| Mobile          | React Native/Flutter/Expo/Capacitor; app store publishing; mobile CI/CD | frontend.mobile                            | Solo                           |
| FE Architecture | Deciding framework/micro-frontends/design system/global state           | coordinator.frontend → {angular/react/vue} | Sequential (coordinator first) |

### 🖥️ Backend Routing

| Domain           | IF                                                                    | THEN                                  | Priority                       |
| ---------------- | --------------------------------------------------------------------- | ------------------------------------- | ------------------------------ |
| Node.js          | Express/Nest/Fastify; real-time (Socket.io); Prisma; JS microservices | backend.nodejs                        | Solo                           |
| Python           | Django/FastAPI/Flask; Celery/asyncio; data/ML backend                 | backend.python                        | Solo                           |
| Laravel/PHP      | Laravel 11+, Eloquent, Livewire/Inertia, admin panels                 | backend.laravel                       | Solo                           |
| Go               | Gin/Echo/Fiber; gRPC; concurrency; performance                        | backend.go                            | Solo                           |
| Java             | Spring Boot/Cloud; enterprise/legacy; Gradle/Maven                    | backend.java                          | Solo                           |
| Rust             | Actix/Rocket/Axum; WASM; performance and memory safety                | backend.rust                          | Solo                           |
| API Architecture | REST/GraphQL/gRPC/WebSocket; versioning; gateways; governance         | backend.api                           | Solo                           |
| Serverless/Edge  | Lambda/Vercel/Netlify/Workers; FaaS; events                           | backend.serverless                    | Solo                           |
| BE Architecture  | Choose pattern (micro/mono), partition services, SLAs, mesh           | coordinator.backend → backend.{stack} | Sequential (coordinator first) |

### 💾 Database and Data Routing

| Domain                          | IF                                                                                      | THEN                                  | Priority                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------- | -------------------------------- |
| Postgres (OLTP/TS/Geo)          | GiST/GIN/BRIN indices; Timescale; Citus; OLTP; geospatial                               | database.postgres                     | Solo                             |
| pgvector (AI Search)            | RAG with PostgreSQL; embeddings in Postgres; similarity search with SQL                 | database.pgvector                     | Solo                             |
| Postgres + Vector               | OLTP + semantic search in same database                                                 | database.postgres ∥ database.pgvector | Parallel (or Sequential by task) |
| MongoDB                         | Documents; aggregations; sharding; change streams                                       | database.mongodb                      | Solo                             |
| MariaDB                         | Galera/MaxScale; MySQL migration; ColumnStore analytics                                 | database.mariadb                      | Solo                             |
| Redis                           | Cache/JSON/Streams; rate-limiting; session store; pub/sub                               | database.redis                        | Solo                             |
| SQLite (edge)                   | Local-first; serverless; FTS5; WAL; Litestream                                          | database.sqlite                       | Solo                             |
| Weaviate (Standalone Vector DB) | Standalone vector database; REST API; vectorization modules; multi-tenant vector search | database.weaviate                     | Solo                             |
| PostGIS                         | GIS queries; routing; spatial analysis                                                  | database.postgis                      | Solo                             |
| Data Architecture               | DB selection; models; flows; analytical vs transactional                                | coordinator.database → {db.\*}        | Sequential (coordinator first)   |

### 🧩 Services Routing

| Domain                | IF                                                                         | THEN                                | Priority                |
| --------------------- | -------------------------------------------------------------------------- | ----------------------------------- | ----------------------- |
| Auth                  | OAuth2/JWT/SSO/MFA/RBAC; Auth0/Firebase Auth; OIDC/SAML flows              | service.auth                        | Solo                    |
| External Integrations | SDKs/3rd party APIs; rate-limiting; scraping (Playwright/Selenium)         | service.integrations                | Solo                    |
| **Mixed Auth + SDK**  | OAuth/SSO + external API consumption                                       | service.auth → service.integrations | Sequential (Auth first) |
| AI/ML in Product      | OpenAI/HF/LangChain; model deployment; fine-tuning; AI pipelines; chatbots | service.ai                          | Solo                    |
| Communication         | Twilio/SendGrid; email/SMS/push; templates; webhooks                       | service.communication               | Solo                    |
| Data Infra (services) | Kafka/RabbitMQ; Airflow/ETL; Elasticsearch; queues/streaming               | service.data                        | Solo                    |
| Maps                  | Mapbox GL/Navigation; geocoding/routing/geofencing                         | service.mapbox                      | Solo                    |

### 💼 Business Routing

| Domain                    | IF                                                             | THEN                                                        | Priority                                    |
| ------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------- | ---------------------------------- |
| Payments (transaction)    | Stripe/PayPal/Square; 3DS; PCI; tokenization; fraud prevention | business.payment                                            | Solo                                        |
| Billing (invoices/taxes)  | Invoices; taxes; dunning; revenue recognition                  | business.billing                                            | Solo                                        |
| Subscriptions             | Plans/usage-based; metering; churn; SaaS KPIs                  | business.subscription                                       | Solo                                        |
| **Complete Subscription** | "Stripe subscription with invoicing and billing"               | business.payment ∥ business.billing ∥ business.subscription | Parallel/Sequential (coordinated by Claude) | ### ⚙️ Operations & DevOps Routing |

| Domain                   | IF                                                      | THEN                          | Priority                       |
| ------------------------ | ------------------------------------------------------- | ----------------------------- | ------------------------------ |
| Git/Workflows            | Branch strategies; hooks; LFS; PR reviews               | ops.git                       | Solo                           |
| Monitoring/Observability | Prometheus/Grafana/ELK/APM; OTel; alerts                | ops.monitoring                | Solo                           |
| Containers/K8s           | Docker/Helm/Istio; ingress/registry; pod security       | ops.containers                | Solo                           |
| Web Server/Proxy         | Nginx/Apache/Caddy/HAProxy; TLS; LB; HTTP/3             | ops.webserver                 | Solo                           |
| CI/CD (tools)            | Jenkins/GitLab CI/CircleCI/GHA; ArgoCD; pipelines       | ops.cicd                      | Solo                           |
| IaC                      | Terraform/Pulumi/Ansible/CFn; infrastructure automation | ops.iac                       | Solo                           |
| Troubleshooting          | Incidents; RCA; profiling; error tracking               | ops.troubleshooting           | Solo                           |
| Performance              | Profiling; k6/JMeter; caching; DB tuning                | ops.performance               | Solo                           |
| **DevOps Strategy**      | Define standards, policies and CI/CD topology           | coordinator.devops → {ops.\*} | Sequential (coordinator first) |

### 🔒 Anti-Ambiguity Rules (Operational Summary)

1. **Strategy vs Execution:**
   - IF task contains **"choose", "select", "compare", "decide", "architecture", "strategy"** → _Coordinator first_
   - IF task contains **"implement", "configure", "optimize", "debug", "deploy", "code"** → _Specialist directly_
   - IF task contains **both strategy + implementation** → _Coordinator → Specialist_ (sequential)
2. **RAG/Vector Search:**
   - IF RAG with PostgreSQL/existing OLTP → **database.pgvector**
   - IF standalone vector database → **database.weaviate**
   - IF AI model integration/deployment → **service.ai**
   - IF RAG system design → **coordinator.database** → specific DB agent
3. **Hybrid DB:** OLTP/Postgres + semantic search → _Postgres_ ∥ _pgvector_ in **parallel** (or sequential by dependency).
4. **Auth vs Security Strategy:**
   - IF **"implement authentication", "OAuth flows", "JWT", "login system"** → **service.auth**
   - IF **"security architecture", "compliance", "IAM strategy", "security policies"** → **coordinator.security**
   - IF **"RBAC implementation"** → **service.auth** (tactical implementation)
   - IF **"design security model"** → **coordinator.security** → **service.auth** (sequential)
5. **Auth vs Integrations:** OAuth/SSO/JWT/MFA → **service.auth**; SDK/API consumption → **service.integrations**; if both, **Auth → Integrations** (sequential).
6. **Payments Suite:** Payment **business.payment**; invoices/taxes **business.billing**; recurrence **business.subscription**; if complete SaaS, invoke all three coordinated.
7. **Auth vs Integrations:** OAuth/SSO/JWT/MFA → **service.auth**; SDK/API consumption → **service.integrations**; if both, **Auth → Integrations** (sequential).
8. **Payments Suite:** Payment **business.payment**; invoices/taxes **business.billing**; recurrence **business.subscription**; if complete SaaS, invoke all three coordinated.
9. **Container Orchestration:** Docker/K8s → **ops.containers** ONLY; backend agents handle language-specific code, not infrastructure.
10. **Multi-Agent Workflows:**
    - **"Create user roles system"** → **coordinator.security** → **service.auth** → **database.{selected}** (sequential)
    - **"Deploy web app in container"** → **ops.containers** ∥ **ops.webserver** (parallel)
    - **"GraphQL schema design"** → **backend.api** ONLY (no database involvement)
    - **"Optimize PostgreSQL performance"** → **database.postgres** ONLY (tactical optimization)

---
# 🎭 Agent Hierarchy and Orchestration Guide

## Core Philosophy

The agent system operates on a **consultative hierarchy** where specialized agents act as **strategists and advisors**, not implementers. Only dynamic agents and dedicated code writers produce actual code. **All inter-agent communication happens through the FLAGS database system**.

## 🏗️ System Architecture

### Agent Communication Flow

```
┌─────────────────────────────────────────────────────────────┐
│                         CLAUDE                              │
│                    (Master Orchestrator)                    │
└────────────┬────────────────────────────────────────────────┘
             │
    ┌────────┴────────┬──────────────┬─────────────┐
    ▼                 ▼              ▼             ▼
┌─────────┐    ┌─────────────┐ ┌──────────┐ ┌──────────┐
│ PLANNER │───▶│COORDINATORS │ │STRATEGISTS│ │EVALUATORS│
└─────────┘    └─────────────┘ └──────────┘ └──────────┘
    │                 │              │            │
    └─────────────────┴──────────────┴────────────┘
                            │
                     ┌──────▼───────┐
                     │DYNAMIC AGENTS│◄────┐
                     └──────┬───────┘     │
                            │              │
                     ┌──────▼───────┐     │
                     │   FLAGS DB   │─────┘
                     └──────────────┘
```

## 📨 FLAGS System - How Agents Communicate

### Core Concept
**Agents CANNOT talk directly**. They communicate through FLAGS in the database. Think of FLAGS as "messages" or "tasks" that agents leave for each other.

### FLAG Naming Convention

```yaml
MODULE_FLAGS:
  format: "module_name"
  example: "auth"  # Goes to auth module
  
AGENT_FLAGS:
  format: "@agent-name"
  examples:
    "@auth-agent"           # Dynamic agent
    "@specialist.laravel"   # Specialist agent
    "@coordinator.backend"  # Coordinator
    "@test.quality"        # Test strategist
    
MULTIPLE_TARGETS:
  format: "@agent1,@agent2"
  example: "@auth-agent,@api-agent"
```

## 🚨 CRITICAL RULES FOR CLAUDE AND AGENTS

### RULE 1: Check FLAGS on Every Activation

```bash
# EVERY agent activation MUST start with:
python .claude/scripts/agent_db.py get-agent-flags "@{your-agent-name}"

# Example for auth-agent:
python .claude/scripts/agent_db.py get-agent-flags "@auth-agent"

# If FLAGS exist, MUST process them BEFORE doing anything else
```

### RULE 2: Create FLAGS for External Dependencies

```bash
# When you change something that affects others:
python .claude/scripts/agent_db.py create-flag \
  --flag_type "interface_change" \
  --source_agent "@auth-agent" \
  --target_agent "@api-agent" \
  --change_description "Added 'verified' field to User type" \
  --action_required "Update User interface to include verified: boolean" \
  --impact_level "high"
```

### RULE 3: Complete FLAGS When Done

```bash
# After processing a FLAG:
python .claude/scripts/agent_db.py execute \
  "UPDATE flags SET status='completed', completed_at='$(date +%Y-%m-%d %H:%M)', completed_by='@auth-agent' WHERE id=45"
```

## 📊 Project Lifecycle with FLAGS

### Phase 1: Discovery & Planning

```yaml
NEW_PROJECT_FLOW:
  1_Discovery:
    Actor: Claude
    Action: "Gathers requirements (95% complete)"
    FLAGS: None yet
    
  2_Strategy:
    Actor: plan.strategy
    Output: "Technology decisions"
    FLAGS: None yet
    
  3_Architecture:
    Actors: All Coordinators (parallel)
    FLAGS_CREATED:
      - coordinator.backend → "@future-backend-agents"
      - coordinator.database → "@future-database-agents"
      - coordinator.frontend → "@future-frontend-agents"
    
  4_Dynamic_Agent_Creation:
    Actor: setup.agent-creator
    Creates: Dynamic agents with their names
    ACTION: Each new agent MUST check FLAGS immediately
```

### Phase 2: Development with FLAGS

```yaml
EXAMPLE_INTERACTION:
  1_auth_agent_works:
    Check: python .claude/scripts/agent_db.py get-agent-flags "@auth-agent"
    Result: "0 pending flags"
    Work: "Creates login endpoint"
    Detects: "API module needs new endpoint"
    Creates_FLAG:
      command: |
        python .claude/scripts/agent_db.py create-flag \
          --flag_type "new_feature" \
          --source_agent "@auth-agent" \
          --target_agent "@api-agent" \
          --change_description "Created /auth/login endpoint" \
          --action_required "Add route to API gateway" \
          --example_usage "POST /auth/login {email, password}"
  
  2_api_agent_activates_later:
    Check: python .claude/scripts/agent_db.py get-agent-flags "@api-agent"
    Result: "1 pending flag from @auth-agent"
    Reads: "Need to add /auth/login route"
    Work: "Adds route to gateway"
    Completes_FLAG:
      command: |
        python .claude/scripts/agent_db.py execute \
          "UPDATE flags SET status='completed' WHERE id=46"
```

## 🔄 Complex Workflows with FLAGS

### Workflow Types

```yaml
SINGLE_FLAG:
  # Simple one-to-one communication
  from: "@auth-agent"
  to: "@api-agent"
  action: "Update interface"

PARALLEL_FLAGS:
  # Multiple agents need to act
  from: "@database-agent"
  to: ["@auth-agent", "@api-agent", "@order-agent"]
  action: "All update to new schema"
  
SEQUENTIAL_WORKFLOW:
  # Step-by-step process
  step_1: "@payment-agent" → "Implement Stripe"
  step_2: "@test.quality" → "Define test strategy"  
  step_3: "@audit.security" → "Security review"
  step_4: "@ops.deployment" → "Deploy to staging"
  
CASCADE_FLAGS:
  # One FLAG triggers more FLAGS
  initial: "@database.postgres" → "Schema changed"
  triggers:
    - All backend agents → "Update queries"
    - "@test.quality" → "Update fixtures"
```

### Creating Complex Workflows

```bash
# NOT IMPLEMENTED - This is conceptual design for future workflows
# Currently, workflows are managed manually through FLAGS
# Sequential workflow example (FUTURE):
# python .claude/scripts/agent_db.py create-workflow \
#   --type "sequential" \
#   --steps '[
#     {"target": "@payment-agent", "action": "Implement Stripe integration"},
#     {"target": "@test.quality", "action": "Create payment tests"},
#     {"target": "@audit.security", "action": "Review implementation"},
#     {"target": "@ops.deployment", "action": "Deploy with feature flag"}
#   ]'
```

## 🎯 Practical Examples for Common Scenarios

### Scenario 1: Adding Authentication

```bash
# 1. Claude activates auth-agent
python .claude/scripts/agent_db.py get-agent-flags "@auth-agent"
# No flags, proceed

# 2. auth-agent needs help from specialist
python .claude/scripts/agent_db.py create-flag \
  --flag_type "consultation_needed" \
  --source_agent "@auth-agent" \
  --target_agent "@service.auth" \
  --change_description "Need JWT implementation strategy" \
  --action_required "Provide JWT best practices for Node.js including token expiration times, refresh token strategy, algorithm selection (HS256 vs RS256), and security considerations"

# 3. service.auth responds (when activated by Claude)
python .claude/scripts/agent_db.py get-agent-flags "@service.auth"
# Sees flag, provides strategy via new FLAG back

python .claude/scripts/agent_db.py create-flag \
  --flag_type "consultation_response" \
  --source_agent "@service.auth" \
  --target_agent "@auth-agent" \
  --change_description "JWT strategy provided" \
  --action_required "Use RS256 algorithm with 15 minute access tokens and 7 day refresh tokens. Store keys securely in environment variables. Implement token rotation on refresh for enhanced security" \
  --example_usage "See context field for full implementation guide" \
  --context '{"access_token_ttl": 900, "refresh_token_ttl": 604800, "algorithm": "RS256"}'
```

### Scenario 2: Database Schema Change

```bash
# 1. database.postgres makes change
python .claude/scripts/agent_db.py create-flag \
  --flag_type "breaking_change" \
  --source_agent "@database.postgres" \
  --target_agent "@auth-agent,@api-agent,@order-agent" \
  --change_description "Column 'price' renamed to 'price_cents'" \
  --action_required "Update all queries using price field" \
  --impact_level "critical"

# 2. Each agent processes when activated
# auth-agent:
python .claude/scripts/agent_db.py get-agent-flags "@auth-agent"
# Sees critical flag, updates queries first

# 3. Complete flag when done
python .claude/scripts/agent_db.py execute \
  "UPDATE flags SET status='completed', completed_by='@auth-agent' WHERE id=47"
```

### Scenario 3: Code Review Request

```bash
# payment-agent needs security review
python .claude/scripts/agent_db.py create-flag \
  --flag_type "review_request" \
  --source_agent "@payment-agent" \
  --target_agent "@audit.security" \
  --change_description "Implemented Stripe webhook handling" \
  --action_required "Security review for payment webhooks" \
  --related_files "payment/webhook.js,payment/stripe.js" \
  --code_location "payment/webhook.js:45-120"
```

## 📋 Agent Activation Protocol

### For Dynamic Agents

```python
# This goes in EVERY dynamic agent's mental model:
"""
ACTIVATION PROTOCOL:
1. CHECK FLAGS FIRST:
   flags = bash('python .claude/scripts/agent_db.py get-agent-flags "@{my-name}"')
   
2. PROCESS CRITICAL FLAGS:
   for flag in flags.where(impact='critical'):
       incorporate_requirement(flag)
   
3. DO ASSIGNED WORK:
   complete_user_request()
   
4. CREATE FLAGS IF NEEDED:
   if changes_affect_others:
       create_flag(affected_agents, changes)
   
5. COMPLETE PROCESSED FLAGS:
   for flag in processed_flags:
       mark_completed(flag.id)
"""
```

### For Specialist Agents

```python
# Specialists only respond to FLAGS:
"""
SPECIALIST ACTIVATION:
1. CHECK FLAGS:
   flags = bash('python .claude/scripts/agent_db.py get-agent-flags "@specialist.{my-specialty}"')
   
2. PROVIDE CONSULTATION:
   for flag in flags:
       strategy = analyze_request(flag)
       create_response_flag(flag.source_agent, strategy)
   
3. MARK COMPLETE:
   mark_all_flags_completed()
"""
```

## 🚫 Anti-Patterns to Avoid

### ❌ DON'T: Skip FLAG Checking
```bash
# WRONG - Starting work without checking FLAGS
# auth-agent starts working immediately

# RIGHT - Always check first
python .claude/scripts/agent_db.py get-agent-flags "@auth-agent"
# Then proceed with work
```

### ❌ DON'T: Forget to Complete FLAGS
```bash
# WRONG - Process FLAG but don't mark complete
# This leaves FLAGS pending forever

# RIGHT - Always complete after processing
python .claude/scripts/agent_db.py execute "UPDATE flags SET status='completed' WHERE id=48"
```

### ❌ DON'T: Create Circular FLAGS
```bash
# WRONG - A flags B, B flags A, A flags B...
# This creates infinite loop

# RIGHT - System prevents this automatically
# Error: "Possible flag loop detected"
```

## 📊 FLAG Status Dashboard

### Check System Health

```bash
# View all pending FLAGS
python .claude/scripts/agent_db.py query "SELECT * FROM pending_flags"

# Check FLAGS for specific agent
python .claude/scripts/agent_db.py get-agent-flags "@auth-agent"

# See workflow status (NOT IMPLEMENTED - use query instead)
# python .claude/scripts/agent_db.py workflow-status 123
# Use: python .claude/scripts/agent_db.py query "SELECT * FROM flags WHERE chain_origin_id=123"

# View communication matrix
python .claude/scripts/agent_db.py query "SELECT * FROM agent_communication_matrix"
```

## 🔧 Quick Reference Commands

```bash
# CHECK FLAGS (start of every activation)
python .claude/scripts/agent_db.py get-agent-flags "@{agent-name}"

# CREATE FLAG (when affecting others)
python .claude/scripts/agent_db.py create-flag \
  --source_agent "@{my-name}" \
  --target_agent "@{target-name}" \
  --change_description "What changed" \
  --action_required "What they need to do" \
  --impact_level "high"  # critical|high|medium|low

# COMPLETE FLAG (after processing)
python .claude/scripts/agent_db.py execute \
  "UPDATE flags SET status='completed', completed_by='@{my-name}' WHERE id={flag-id}"

# CREATE WORKFLOW (complex multi-step)
python .claude/scripts/agent_db.py create-workflow \
  --type "sequential" \
  --steps '[...]'
```

## 🎯 Success Metrics

The system is working when:

1. **Zero Missed FLAGS**: Every agent checks on activation
2. **Clear Communication**: FLAGS have actionable requirements
3. **Timely Completion**: Critical FLAGS processed immediately
4. **No Orphans**: All FLAGS have valid targets
5. **Workflow Progress**: Sequential steps advance automatically

## 💡 Key Takeaways

1. **FLAGS are the ONLY way agents communicate**
2. **ALWAYS check FLAGS before starting work**
3. **Create FLAGS when your changes affect others**
4. **Complete FLAGS when done processing**
5. **Critical FLAGS block all other work**
6. **Specialists only respond via FLAGS**
7. **Workflows automate complex processes**

---

*This system ensures reliable, traceable communication between all agents without requiring Claude to manually orchestrate every interaction.*