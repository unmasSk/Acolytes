# ClaudeSquad Agents Catalog & Routing Rules

## Agent Statistics

**Total Agents:** 57  
**0 tick (🔳):** 12 (21.1%)  
**1 tick (✅):** 12 (21.1%)  
**2 tick (✅✅):** 33 (57.9%)  
**3 tick (✅✅✅):** 0 (0%)

**Progress Tracking:**

- ✅ **Created** - Agent exists with basic content
- ✅✅ **Audited perfect** - FLAGS, order and info correct (setup/coordinator don't need FLAGS)
- ✅✅✅ **fix.md errors corrected** - All issues from fix.md checklist resolved

## 🚀 Setup and Configuration

✅✅ **setup.agent-creator** (362 lines) - Module research specialist that reads all module files, understands code purpose and creates the perfect dynamic agent for the assigned module.
✅✅ **setup.codebase** (283 lines) - Analyzes code structure, modules, quality, tests and technical patterns  
✅✅ **setup.context** (213 lines) - Analyzes project architecture and tech stack during initial configuration  
✅✅ **setup.environment** (270 lines) - Detects development environment configuration and tools  
✅✅ **setup.infrastructure** (312 lines) - Analyzes deployment infrastructure and DevOps configuration

## 🎮 Control and Orchestration

✅✅ **coordinator.backend** (786 lines)  
**Role:** Strategic backend architecture orchestrator  
**Tech:** Microservices, API design, service mesh, distributed systems, load balancing, monolith migration, modular architecture, dependency analysis, coupling optimization, bounded context definition, cross-module coordination, performance orchestration, security architecture, technical debt management, CI/CD coordination, Infrastructure as Code, zero-downtime deployment, monitoring architecture, disaster recovery  
**When:** IF designing backend architecture OR choosing between multiple backend technologies OR scaling strategy OR microservices migration OR architectural decision making OR cross-module coordination OR performance optimization strategy OR security architecture design OR technical debt assessment OR system-wide changes  
**Keywords:** architecture, microservices, monolith, migration, API design, service mesh, distributed, load balancing, scaling, coordination, cross-module, dependency, bounded context, performance, orchestration, technical debt, strategic, system-wide  
**Integrates:** @backend.nodejs [optional], @backend.python [optional], @backend.laravel [optional], @backend.go [optional], @backend.java [optional], @backend.rust [optional], @backend.api [optional,seq:2], @database.postgres [optional,seq:3]

✅✅ **coordinator.database** (2032 lines)  
**Role:** Strategic data architecture orchestrator  
**Tech:** SQL/NoSQL/Vector databases, data modeling, replication, sharding, analytics, PostgreSQL, MongoDB, Redis, MySQL, MariaDB, Cassandra, DynamoDB, ClickHouse, Elasticsearch, polyglot persistence, cross-database migration, zero-downtime migration, schema transformation, performance optimization, query optimization, indexing strategies, resource utilization  
**When:** IF choosing database technology OR designing data architecture OR planning data flow across systems OR polyglot persistence strategy OR cross-database migration OR database performance optimization OR schema design OR data modeling decisions OR analytics architecture OR database selection  
**Keywords:** database, SQL, NoSQL, vector, data modeling, replication, sharding, analytics, migration, PostgreSQL, MongoDB, Redis, polyglot, persistence, schema, performance, optimization, indexing, transformation, selection, architecture  
**Integrates:** @database.postgres [optional], @database.mongodb [optional], @database.redis [optional], @database.vectorial [optional], @database.mariadb [optional], @database.sqlite [optional], @database.pgvector [optional], @database.postgis [optional]

✅✅ **coordinator.devops** (702 lines)  
**Role:** Strategic DevOps and automation orchestrator  
**Tech:** CI/CD strategy, GitOps, release management patterns, automation workflows, Jenkins, GitLab CI, GitHub Actions, ArgoCD, Terraform, Ansible, Docker, Kubernetes, monitoring architecture, deployment automation, pipeline optimization, release orchestration, environment management, infrastructure automation  
**When:** DevOps strategy, pipeline architecture, deployment patterns, release planning, CI/CD design, GitOps implementation, automation strategy, infrastructure planning, monitoring strategy, deployment orchestration  
**Keywords:** DevOps, CI/CD, GitOps, pipeline, deployment, automation, Jenkins, GitLab, GitHub Actions, ArgoCD, Terraform, Ansible, Docker, Kubernetes, release, strategy, orchestration, infrastructure  
**Integrates:** @ops.git [optional], @ops.cicd [optional], @ops.iac [optional], @ops.containers [optional], @ops.monitoring [optional], @coordinator.infrastructure [optional,seq:2]

✅✅ **coordinator.frontend** (299 lines)  
**Role:** Strategic frontend architecture orchestrator  
**Tech:** React, Vue, Angular, state management, micro-frontends, design systems, component architecture, UI framework selection, TypeScript, JavaScript, webpack, Vite, SSR, SSG, PWA, responsive design, accessibility, performance optimization, build tools, routing strategies  
**When:** Frontend architecture decisions, UI framework selection, component strategy, micro-frontends design, design system creation, state management strategy, build tool selection, performance optimization strategy, accessibility planning  
**Keywords:** frontend, architecture, React, Vue, Angular, component, micro-frontend, design system, state management, TypeScript, SSR, SSG, PWA, responsive, accessibility, performance, strategy, UI framework  
**Integrates:** @frontend.react [optional], @frontend.vue [optional], @frontend.angular [optional], @frontend.mobile [optional], @backend.api [optional,seq:2]

✅✅ **coordinator.infrastructure** (640 lines)  
**Role:** Strategic infrastructure architect  
**Tech:** Multi-cloud (AWS, Azure, GCP), load balancers, CDN, auto scaling, capacity planning, cloud architecture, hybrid cloud, edge computing, containerization, service mesh, network architecture, security architecture, cost optimization, monitoring infrastructure, backup strategies, disaster recovery  
**When:** Multi-cloud architecture, infrastructure strategy, workload placement, disaster recovery planning, cloud migration strategy, capacity planning, cost optimization, network design, security planning, monitoring architecture  
**Keywords:** infrastructure, cloud, AWS, Azure, GCP, multi-cloud, load balancer, CDN, scaling, capacity, architecture, hybrid, edge, containers, service mesh, network, disaster recovery, cost optimization  
**Integrates:** @ops.containers [optional], @ops.webserver [optional], @ops.iac [optional], @ops.monitoring [optional], @coordinator.security [optional,seq:2]

✅✅ **coordinator.migration** (634 lines)  
**Role:** Strategic migration and transformation orchestrator  
**Tech:** Legacy modernization, cloud migration, data migration, re-architecture patterns, zero-downtime migration, database migration, application modernization, microservices extraction, API transformation, infrastructure migration, dependency mapping, risk assessment, rollback planning  
**When:** Migration strategy planning, legacy transformation, technology stack migrations, cloud migration planning, database migration strategy, application modernization, microservices migration, zero-downtime deployment planning  
**Keywords:** migration, legacy, modernization, cloud migration, transformation, zero-downtime, database migration, microservices, re-architecture, rollback, strategy, planning, extraction, dependency mapping  
**Integrates:** @coordinator.backend [optional], @coordinator.database [optional], @coordinator.infrastructure [optional], @ops.iac [optional,seq:2], @database.postgres [optional,seq:3]

✅✅ **coordinator.security** (634 lines)  
**Role:** Strategic security architecture orchestrator  
**Tech:** IAM/RBAC, compliance frameworks (SOC2, PCI, HIPAA), security scanning, incident response, threat modeling, vulnerability assessment, security monitoring, encryption strategies, authentication architecture, authorization patterns, security policies, audit logging, penetration testing coordination  
**When:** Security architecture design, compliance strategy, security policy orchestration, threat modeling, vulnerability management, incident response planning, security monitoring strategy, authentication/authorization design, compliance planning  
**Keywords:** security, IAM, RBAC, compliance, SOC2, PCI, HIPAA, threat modeling, vulnerability, incident response, authentication, authorization, encryption, audit, penetration testing, monitoring, policies  
**Integrates:** @service.auth [optional], @audit.security [optional], @ops.monitoring [optional,seq:2], @coordinator.infrastructure [optional,seq:3]

✅✅ **coordinator.testing** (634 lines)  
**Role:** Strategic testing and quality orchestrator  
**Tech:** Test automation frameworks, quality gates, performance testing, test data management, CI/CD integration, test strategy, unit testing, integration testing, end-to-end testing, load testing, security testing, accessibility testing, test coverage analysis, test environment management  
**When:** Testing strategy design, quality assurance architecture, test automation planning, test framework selection, quality gates design, performance testing strategy, test environment planning, coverage strategy, CI/CD test integration  
**Keywords:** testing, quality, automation, test strategy, unit testing, integration testing, e2e testing, performance testing, load testing, security testing, accessibility, coverage, quality gates, CI/CD integration  
**Integrates:** @test.quality [optional], @ops.cicd [optional], @coordinator.devops [optional,seq:2], @ops.performance [optional,seq:3]

## 💾 Data Management

✅✅ **database.mariadb** (1755 lines)  
**Role:** MariaDB specialist and MySQL evolution expert  
**Tech:** MariaDB 11+, Galera clustering, MaxScale load balancing, ColumnStore analytics, Spider sharding, MySQL compatibility, high-availability architecture, zero-downtime migrations, performance optimization, replication, backup strategies, enterprise deployment  
**When:** MySQL modernization, high-availability clustering, zero-downtime migrations, analytical workloads, MySQL to MariaDB migration, Galera cluster setup, performance optimization, enterprise MySQL replacement  
**Keywords:** MariaDB, MySQL, Galera, clustering, MaxScale, ColumnStore, Spider, sharding, high-availability, migration, replication, performance, analytics, enterprise  
**Integrates:** @database.postgres [optional], @ops.monitoring [optional,seq:2], @coordinator.database [optional,seq:3]

✅✅ **database.mongodb** (2411 lines)  
**Role:** MongoDB and NoSQL document database expert  
**Tech:** MongoDB 7+, aggregation pipelines, sharding, change streams, Atlas, Compass, document modeling, replica sets, GridFS, transactions, indexing strategies, performance optimization, horizontal scaling, enterprise deployment  
**When:** Flexible document schemas, real-time data streaming, content management, rapid prototyping, NoSQL architecture, document-based applications, horizontal scaling, real-time analytics, content management systems  
**Keywords:** MongoDB, NoSQL, document, aggregation, sharding, replica sets, Atlas, Compass, change streams, GridFS, transactions, horizontal scaling, flexible schema  
**Integrates:** @backend.nodejs [optional], @backend.python [optional], @service.data [optional,seq:2], @ops.monitoring [optional,seq:3]

✅✅ **database.pgvector** (2739 lines)  
**Role:** PostgreSQL vector database and AI search expert  
**Tech:** PostgreSQL + pgvector, HNSW/IVFFlat indexing, pgvectorscale, embedding models, hybrid search, DiskANN algorithms, billion-scale vectors, similarity search, semantic search, OpenAI embeddings, Hugging Face transformers, RAG architectures  
**When:** RAG applications, semantic search, similarity matching, AI-powered recommendations, multi-modal search, vector similarity, embedding storage, AI search applications, chatbot knowledge bases  
**Keywords:** pgvector, vector, embeddings, similarity, semantic search, RAG, AI search, HNSW, IVFFlat, OpenAI, Hugging Face, chatbot, knowledge base, multi-modal  
**Integrates:** @service.ai [required], @database.postgres [required,seq:2], @backend.python [optional,seq:3], @backend.nodejs [optional,seq:4]

✅✅ **database.postgres** (1974 lines)  
**Role:** PostgreSQL advanced features and performance expert  
**Tech:** PostgreSQL 15+, advanced indexing (GiST, GIN, BRIN), TimescaleDB, PgBouncer, Citus, PostGIS, query optimization, performance tuning, replication, high availability, VACUUM optimization, connection pooling, partitioning, enterprise deployment  
**When:** Complex relational data, time-series analytics, geospatial applications, enterprise OLTP systems, query optimization, performance tuning, high-availability setup, connection pooling, database scaling  
**Keywords:** PostgreSQL, Postgres, indexing, GiST, GIN, BRIN, TimescaleDB, PgBouncer, Citus, PostGIS, query optimization, performance, replication, OLTP, partitioning, vacuum  
**Integrates:** @database.postgis [optional], @database.pgvector [optional], @ops.monitoring [optional,seq:2], @coordinator.database [optional,seq:3]

✅✅ **database.redis** (1270 lines)  
**Role:** Redis in-memory data structures and caching expert  
**Tech:** Redis 7+, Redis Stack (JSON, Search, Graph), Streams, pub/sub, clustering, Lua scripting, Redis Sentinel, Redis Cluster, persistence strategies, memory optimization, high availability, performance tuning  
**When:** Sub-millisecond caching, session storage, real-time leaderboards, pub/sub messaging, rate limiting, in-memory analytics, real-time data processing, high-performance caching  
**Keywords:** Redis, caching, in-memory, JSON, Search, Graph, Streams, pub/sub, clustering, Lua, Sentinel, rate limiting, session, leaderboard, real-time  
**Integrates:** @backend.nodejs [optional], @backend.python [optional], @service.data [optional,seq:2], @ops.monitoring [optional,seq:3]

✅✅ **database.sqlite** (1407 lines)  
**Role:** SQLite embedded database and edge computing expert  
**Tech:** SQLite 3.44+, WAL mode, FTS5, JSON operations, Core ML optimization, Litestream replication, WASM, edge deployment, mobile optimization, local-first sync, backup strategies, performance optimization  
**When:** Embedded applications, edge computing, mobile apps, serverless databases, local-first architectures, offline-first applications, mobile development, edge deployment, lightweight databases  
**Keywords:** SQLite, embedded, edge computing, mobile, WAL, FTS5, JSON, Core ML, Litestream, WASM, local-first, offline, serverless, lightweight  
**Integrates:** @frontend.mobile [optional], @backend.serverless [optional], @ops.monitoring [optional,seq:2]

✅✅ **database.vectorial** (6498 lines)  
**Role:** Strategic vector database consultant across multiple platforms  
**Tech:** Weaviate v4+, Pinecone Serverless, Qdrant v1.15+, Chroma v1.0+, Milvus v2.6+, Supabase pgvector, MongoDB Atlas Vector Search, vector indexing algorithms, HNSW, IVF, similarity metrics, embedding models, hybrid search, performance optimization  
**When:** Vector database selection, RAG applications, semantic search, AI-powered search, embedding storage, hybrid architectures, vector database architecture, similarity matching, AI search systems, knowledge retrieval  
**Keywords:** vector database, Weaviate, Pinecone, Qdrant, Chroma, Milvus, vector search, embeddings, similarity, HNSW, IVF, RAG, semantic search, AI search, knowledge retrieval  
**Integrates:** @service.ai [required], @database.pgvector [optional], @backend.python [optional,seq:2], @coordinator.database [optional,seq:3]

✅✅ **database.postgis** (1362 lines)  
**Role:** PostGIS geospatial database and GIS expert  
**Tech:** PostGIS, spatial indexing, geographic queries, coordinate systems, spatial analysis, GIS algorithms, geometric operations, raster data, topology, spatial relationships, GPS data processing, mapping applications  
**When:** Location-based applications, mapping systems, geographic data analysis, spatial queries, GIS applications, GPS tracking, geofencing, spatial analytics, mapping services, location intelligence  
**Keywords:** PostGIS, spatial, GIS, geographic, coordinate systems, spatial analysis, mapping, GPS, geofencing, location, geometric, raster, topology  
**Integrates:** @database.postgres [required], @service.mapbox [optional,seq:2], @backend.python [optional,seq:3]

## 💻 Software Development

### Frontend

✅✅ **frontend.angular** (1404 lines)  
**Role:** Angular framework and enterprise TypeScript expert  
**Tech:** Angular 17+, TypeScript 5+, RxJS, Angular Material, PrimeNG, NgRx, standalone components, Signals API, dependency injection, reactive forms, Angular CLI, Angular DevKit, testing framework (Jasmine/Karma), performance optimization  
**When:** Enterprise applications, complex forms, reactive programming, TypeScript-heavy projects, large-scale applications, enterprise UI frameworks, reactive data flows, complex state management  
**Keywords:** Angular, TypeScript, RxJS, NgRx, standalone components, Signals API, reactive forms, enterprise, Angular Material, PrimeNG, dependency injection, reactive programming  
**Integrates:** @backend.api [optional], @service.auth [optional,seq:2], @docs-specialist [optional,seq:3]

✅✅ **frontend.react** (1889 lines)  
**Role:** React ecosystem and modern JavaScript expert  
**Tech:** React 18+, Next.js, TypeScript, Material-UI, Chakra UI, shadcn/ui, Zustand, React Query, React Router, Redux Toolkit, Styled Components, Emotion, Vite, Webpack, ESLint, Prettier, Testing Library, Jest, Storybook  
**When:** Single-page applications, server-side rendering, component libraries, modern web apps, React applications, component architecture, state management, performance optimization, modern build tools  
**Keywords:** React, Next.js, TypeScript, hooks, JSX, components, state management, Zustand, React Query, Material-UI, Chakra UI, shadcn/ui, SSR, SPA, modern JavaScript  
**Integrates:** @backend.api [optional], @service.auth [optional,seq:2], @docs-specialist [optional,seq:3]

✅✅ **frontend.vue** (1885 lines)  
**Role:** Vue.js ecosystem and progressive framework expert  
**Tech:** Vue 3+, Nuxt.js, TypeScript, Composition API, Vuetify, Pinia, Vue Router, Vite, Options API, Vuex (legacy), Vue Test Utils, Vitest, Single File Components (SFC), reactive data, computed properties, watchers  
**When:** Progressive web apps, rapid prototyping, developer-friendly projects, gradual adoption, Vue applications, reactive applications, component-based architecture, modern build tools  
**Keywords:** Vue, Nuxt.js, Composition API, Pinia, Vuetify, Vue Router, Vite, reactive, SFC, progressive, TypeScript, rapid prototyping, developer-friendly  
**Integrates:** @backend.api [optional], @service.auth [optional,seq:2], @docs-specialist [optional,seq:3]

✅✅ **frontend.mobile** (693 lines)  
**Role:** Cross-platform mobile development expert  
**Tech:** React Native (New Architecture), Flutter 3.24+, Expo SDK 52+, Capacitor 7+, native modules, iOS/Android integration, app store deployment, mobile CI/CD, EAS workflows, Fastlane automation, React Navigation, native module bridging, performance optimization, offline storage, push notifications, deep linking  
**When:** Mobile app development, cross-platform solutions, native feature integration, app store publishing, React Native/Flutter development, mobile performance optimization, iOS/Android deployment, mobile architecture  
**Keywords:** React Native, Flutter, mobile, cross-platform, iOS, Android, Expo, Capacitor, native modules, app store, EAS, mobile CI/CD, push notifications, deep linking, mobile performance  
**Integrates:** @backend.api [optional], @service.auth [optional], @service.communication [optional,seq:2], @ops.cicd [optional,seq:3]

### Backend

✅✅ **backend.laravel** (1634 lines)  
**Role:** Laravel framework and PHP ecosystem expert  
**Tech:** Laravel 11+, PHP 8.3+, Eloquent ORM, Livewire, Inertia.js, Horizon, Telescope, Artisan CLI, queue systems, broadcasting, caching, middleware, service providers, Blade templating, Laravel Sanctum, Passport, Nova  
**When:** Rapid web development, MVC architecture, PHP-based applications, admin panels, Laravel applications, Eloquent ORM usage, queue processing, real-time features, enterprise PHP development  
**Keywords:** Laravel, PHP, Eloquent, ORM, Livewire, Inertia.js, Horizon, Telescope, Artisan, queue, broadcasting, middleware, Blade, Sanctum, Passport, MVC  
**Integrates:** @database.postgres [optional], @database.redis [optional], @frontend.vue [optional,seq:2], @service.auth [optional,seq:3]

✅✅ **backend.nodejs** (3975 lines)  
**Role:** Node.js runtime and JavaScript backend expert  
**Tech:** Node.js 20+, Express, NestJS, TypeScript, Fastify, Prisma, Socket.io, microservices, GraphQL, REST APIs, WebSocket, async/await, event-driven architecture, middleware, authentication, caching, performance optimization  
**When:** IF implementing Node.js backend OR real-time features OR JavaScript-based microservices OR REST/GraphQL APIs OR WebSocket applications OR event-driven systems OR TypeScript backend development  
**Keywords:** Node.js, Express, NestJS, TypeScript, Fastify, Prisma, Socket.io, microservices, REST API, GraphQL, WebSocket, real-time, async, event-driven, JavaScript backend  
**Integrates:** @database.postgres [optional], @database.mongodb [optional], @database.redis [optional], @frontend.react [optional,seq:2], @service.auth [optional,seq:3]

✅✅ **backend.python** (3274 lines)  
**Role:** Python ecosystem and versatile backend expert  
**Tech:** Python 3.11+, Django, FastAPI, Flask, SQLAlchemy, Celery, asyncio, data processing, Pydantic, Django REST Framework, Alembic, Redis, PostgreSQL adapters, machine learning integration, scientific computing, async programming  
**When:** Data-heavy applications, ML integration, rapid development, scientific computing, REST APIs, async applications, data processing, machine learning backends, Django/Flask applications  
**Keywords:** Python, Django, FastAPI, Flask, SQLAlchemy, Celery, asyncio, data processing, ML integration, Pydantic, REST API, async, scientific computing  
**Integrates:** @database.postgres [optional], @database.redis [optional], @service.ai [optional], @database.pgvector [optional,seq:2], @service.data [optional,seq:3]

✅✅ **backend.go** (1967 lines)  
**Role:** Go language and high-performance systems expert  
**Tech:** Go 1.21+, Gin, Echo, Fiber, gRPC, concurrency patterns, goroutines, channels, context package, error handling, HTTP/2, WebSocket, protocol buffers, performance optimization, memory management, testing  
**When:** High-performance APIs, microservices, system programming, concurrent processing, gRPC services, high-throughput systems, concurrent applications, Go backend development  
**Keywords:** Go, Golang, Gin, Echo, Fiber, gRPC, goroutines, channels, concurrency, high-performance, microservices, protocol buffers, system programming  
**Integrates:** @database.postgres [optional], @database.redis [optional], @backend.api [optional,seq:2], @ops.monitoring [optional,seq:3]

✅✅ **backend.java** (1518 lines)  
**Role:** Java enterprise and Spring ecosystem expert  
**Tech:** Java 17+, Spring Boot, Spring Cloud, Hibernate, Maven, Gradle, enterprise patterns, Spring Security, Spring Data, JPA, microservices architecture, Docker, Kubernetes integration, enterprise deployment  
**When:** Enterprise applications, large-scale systems, legacy modernization, corporate environments, Spring Boot applications, enterprise Java, microservices with Spring Cloud, JPA/Hibernate usage  
**Keywords:** Java, Spring Boot, Spring Cloud, Hibernate, JPA, Maven, Gradle, enterprise, Spring Security, Spring Data, microservices, corporate, legacy modernization  
**Integrates:** @database.postgres [optional], @ops.containers [optional], @coordinator.migration [optional,seq:2], @ops.monitoring [optional,seq:3]

✅✅ **backend.rust** (1754 lines)  
**Role:** Rust systems programming and performance expert  
**Tech:** Rust, Actix-web, Rocket, Axum, Tokio, WebAssembly, async programming, memory safety, Serde, Diesel ORM, performance optimization, zero-cost abstractions, cargo, testing, error handling  
**When:** System-level programming, performance-critical applications, WebAssembly, safe concurrency, high-performance backends, memory-safe systems, Rust web services, async applications  
**Keywords:** Rust, Actix-web, Rocket, Axum, Tokio, WebAssembly, WASM, async, memory safety, performance, zero-cost abstractions, safe concurrency, systems programming  
**Integrates:** @database.postgres [optional], @ops.monitoring [optional,seq:2], @ops.performance [optional,seq:3]

✅✅ **backend.api** (1188 lines)  
**Role:** API design and integration architecture expert  
**Tech:** REST, GraphQL, WebSocket, gRPC, OpenAPI/Swagger, API gateways, rate limiting, versioning, authentication, authorization, caching, monitoring, error handling, API documentation, testing, security  
**When:** API-first development, GraphQL schemas, API governance, documentation standards, REST API design, GraphQL implementation, API security, versioning strategies, integration architecture  
**Keywords:** API, REST, GraphQL, WebSocket, gRPC, OpenAPI, Swagger, API gateway, rate limiting, versioning, authentication, integration, API design, API security  
**Integrates:** @backend.nodejs [optional], @backend.python [optional], @backend.go [optional], @service.auth [optional,seq:2], @docs-specialist [optional,seq:3]

✅✅ **backend.serverless** (1173 lines)  
**Role:** Serverless functions and edge computing expert  
**Tech:** AWS Lambda, Vercel Functions, Netlify Functions, CloudFlare Workers, edge runtime, FaaS patterns, serverless frameworks, cold start optimization, event-driven architecture, API Gateway, serverless deployment  
**When:** Serverless architectures, edge computing, event-driven functions, cost-optimized backends, FaaS development, edge functions, serverless APIs, event-driven processing  
**Keywords:** serverless, AWS Lambda, Vercel Functions, Netlify Functions, CloudFlare Workers, FaaS, edge computing, event-driven, cold start, API Gateway, cost-optimized  
**Integrates:** @database.sqlite [optional], @coordinator.infrastructure [optional], @ops.monitoring [optional,seq:2]

## 🧩 Services

✅✅ **service.ai** (4566 lines)  
**Role:** AI/ML integration and model management expert  
**Tech:** LangGraph, CrewAI, AutoGen, advanced RAG (Agentic RAG, HyDE), vector databases (Qdrant, Milvus, pgvector), modern fine-tuning (PEFT/LoRA/QLoRA), latest models (DeepSeek-V3, Llama 3.3, Mistral Large 2, Qwen 2.5), production deployment (vLLM, TGI, Ollama), LangSmith observability, OpenAI API, Hugging Face transformers, embedding models, prompt engineering  
**When:** AI feature integration, chatbots, content generation, ML model deployment, prompt optimization, advanced RAG systems, vector search, agent orchestration, AI-powered applications, machine learning pipelines, model fine-tuning, AI system architecture  
**Keywords:** AI, ML, LangGraph, CrewAI, AutoGen, RAG, vector databases, fine-tuning, OpenAI, Hugging Face, embeddings, chatbot, content generation, model deployment, prompt engineering, agent orchestration  
**Integrates:** @database.vectorial [required], @database.pgvector [optional], @backend.python [required,seq:2], @service.data [optional,seq:3]

✅✅ **service.auth** (2587 lines)  
**Role:** Authentication and authorization security expert  
**Tech:** OAuth2/2.1, JWT, SSO (SAML, OIDC), Auth0, Firebase Auth, Passport.js, multi-factor authentication, RBAC, WebAuthn, passwordless authentication, session management, token validation, identity providers, secure coding practices  
**When:** IF implementing user authentication OR OAuth flows OR SSO integration OR JWT token management OR RBAC implementation OR MFA setup OR identity provider integration OR authentication architecture  
**Keywords:** authentication, authorization, OAuth2, JWT, SSO, SAML, OIDC, Auth0, Firebase Auth, RBAC, MFA, WebAuthn, identity, session, token, security, login  
**Integrates:** @database.postgres [optional], @backend.nodejs [optional], @backend.python [optional], @coordinator.security [optional,seq:2]

✅✅ **service.communication** (2042 lines)  
**Role:** Multi-channel communication and messaging expert  
**Tech:** Twilio Messaging Services with A2P compliance, SendGrid v3 API with dynamic templates, Firebase Cloud Messaging (FCM) v1 API, WebSocket architecture with Socket.IO, webhook validation, circuit breaker patterns, message queuing with retry mechanisms, PII detection, GDPR compliance, real-time monitoring, email templates, SMS automation, push notification orchestration  
**When:** Transactional emails, SMS notifications, push notifications, real-time messaging, webhook processing, multi-channel communication, messaging automation, notification systems, real-time chat, communication workflows  
**Keywords:** communication, messaging, Twilio, SendGrid, FCM, push notifications, SMS, email, WebSocket, Socket.IO, real-time, notifications, templates, automation  
**Integrates:** @backend.nodejs [optional], @database.redis [optional], @service.integrations [optional,seq:2], @frontend.mobile [optional,seq:3]

✅✅ **service.data** (2169 lines)  
**Role:** Data processing and infrastructure services expert  
**Tech:** Elasticsearch/OpenSearch 8+ with advanced indexing and cluster management, Apache Kafka 3.8+ with Kafka Streams and event-driven architectures, Apache Airflow 2.10+ with TaskFlow API and enterprise deployment, RabbitMQ 4+ with advanced clustering and HA, modern ETL/ELT pipelines, enterprise data mesh architecture, real-time streaming, comprehensive monitoring & observability  
**When:** Search functionality, data streaming, message queuing, data pipelines, real-time data processing, ETL/ELT workflows, event-driven architecture, data mesh implementation, search infrastructure, streaming analytics  
**Keywords:** data processing, Elasticsearch, OpenSearch, Kafka, Airflow, RabbitMQ, ETL, ELT, data pipelines, streaming, event-driven, search, data mesh, analytics  
**Integrates:** @database.postgres [optional], @database.mongodb [optional], @backend.python [optional,seq:2], @ops.monitoring [optional,seq:3]

✅✅ **service.integrations** (2905 lines)  
**Role:** Third-party API integration and external services expert  
**Tech:** REST APIs, SDK integrations, rate limiting, web scraping (Playwright, Selenium), data synchronization, webhook processing, API orchestration, OAuth integrations, GraphQL clients, service mesh integration, circuit breakers, retry mechanisms  
**When:** External API consumption, third-party SDKs, service orchestration, automation workflows, API integration, webhook handling, data synchronization, external service coordination, integration architecture  
**Keywords:** integration, API integration, third-party, SDK, REST API, webhook, data synchronization, external services, orchestration, automation, rate limiting, API consumption  
**Integrates:** @service.auth [optional], @backend.nodejs [optional], @backend.python [optional], @service.communication [optional,seq:2]

✅✅ **service.mapbox** (1020 lines)  
**Role:** Mapbox and geospatial services expert  
**Tech:** Mapbox GL JS, Navigation API, geocoding, routing, spatial analysis, custom map styles, location services, vector tiles, real-time traffic, EV routing, geofencing, directions API, static maps, SDK integration  
**When:** Interactive maps, location-based features, route optimization, geofencing, spatial data visualization, mapping applications, GPS tracking, location intelligence, navigation systems, geospatial analytics  
**Keywords:** Mapbox, maps, geospatial, geocoding, routing, navigation, location services, GPS, geofencing, spatial analysis, vector tiles, mapping, location intelligence  
**Integrates:** @database.postgis [optional], @frontend.react [optional], @frontend.vue [optional], @frontend.mobile [optional,seq:2]

## 💼 Business Systems

✅✅ **business.billing** (2121 lines)  
**Role:** Billing systems and revenue management expert  
**Tech:** Stripe Billing, invoice generation, tax calculation, revenue recognition, dunning management, Chargebee, Recurly, Zuora, QuickBooks API, Xero API, Avalara, TaxJar, multi-currency, ASC 606 compliance, SOC 2 Type II  
**When:** SaaS billing, subscription management, complex pricing models, tax compliance, revenue reporting, recurring charges, proration, multi-currency billing, accounting integration, SOX audit trails  
**Keywords:** invoice, billing, tax, revenue, dunning, proration, ASC 606, recurring, charges, QuickBooks, Xero, Avalara, TaxJar, SOC 2, audit, accounting, multi-currency  
**Integrates:** @business.payment [required], @business.subscription [required,seq:2], @database.postgres [optional], @service.integrations [optional,seq:3]

✅✅ **business.payment** (2762 lines)  
**Role:** Payment processing and financial transactions expert  
**Tech:** Stripe, PayPal, Square, PCI compliance, tokenization, fraud prevention, 3D Secure, webhooks, Braintree, Apple Pay, Google Pay, Strong Customer Authentication (SCA), PSD2, GDPR compliance, machine learning fraud detection  
**When:** E-commerce payments, transaction processing, financial integrations, payment security, fraud detection, PCI DSS compliance, gateway integration, webhook processing, payment analytics, risk assessment  
**Keywords:** payment, Stripe, PayPal, PCI, tokenization, fraud, 3D Secure, webhooks, gateway, transaction, security, compliance, card, processing, merchant, SCA, PSD2  
**Integrates:** @service.auth [optional], @database.postgres [required], @ops.monitoring [optional,seq:2], @audit.security [optional,seq:3]

✅✅ **business.subscription** (2370 lines)  
**Role:** SaaS subscription and recurring revenue expert  
**Tech:** Subscription models, usage-based billing, metered pricing, customer lifecycle, churn prevention, MRR/ARR analytics, revenue recognition, dunning management  
**When:** SaaS platforms, recurring revenue models, subscription analytics, customer retention strategies, usage metering, churn prediction, B2B subscription commerce, freemium models  
**Keywords:** MRR, ARR, churn, LTV, subscription, billing, recurring, usage-based, metering, retention, cohort, proration, dunning  
**Integrates:** @business.payment [required], @backend.api [required,seq:2], @database.analytics [optional], @frontend.dashboard [optional,seq:3]

## 📝 Documentation

✅✅ **docs-specialist** (539 lines)  
**Role:** Comprehensive documentation architecture and technical writing expert  
**Tech:** Semantic versioning, changelog generation, technical writing, API documentation, markdown mastery, GitHub repository files (README.md, CONTRIBUTING.md, LICENSE, CODE_OF_CONDUCT.md), OpenAPI/Swagger, Mermaid diagrams, .github templates, community health files, shields.io badges, accessibility compliance, documentation automation, quality metrics, multi-platform publishing, Keep a Changelog format, GitHub Flavored Markdown (GFM), WCAG compliance, conventional commits  
**When:** Documentation creation/updates, changelog management, version management, API documentation, README optimization, GitHub repository setup, community health files, issue/PR templates, CONTRIBUTING guidelines, LICENSE files, technical guides, documentation quality audits, release notes, migration guides, architecture documentation, cross-reference management  
**Keywords:** documentation, changelog, versioning, semantic, markdown, README, API docs, OpenAPI, Swagger, GitHub, templates, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, badges, shields, Mermaid, diagrams, technical writing, migration guides, release notes, community, accessibility, WCAG  
**Integrates:** @backend.api [optional], @frontend.react [optional], @frontend.vue [optional], @frontend.angular [optional], @ops.git [optional,seq:2], @service.integrations [optional,seq:3]

## 📊 Analysis and Strategy

✅✅ **analyst.strategic** (1171 lines)  
**Role:** Business and technical strategy analysis expert  
**Tech:** Requirements analysis, roadmap planning, stakeholder analysis, competitive analysis, market research tools, OKR framework, SWOT analysis, Porter's Five Forces, Evidence BI platform, modern 2025 strategic frameworks, business model canvas, technology assessment, ROI analysis, feasibility studies  
**When:** Strategic planning, business requirements, technology selection, project roadmaps, feasibility studies, competitive intelligence, ROI analysis, stakeholder management, business strategy, technology strategy, market analysis, strategic decision making  
**Keywords:** strategy, strategic planning, OKR, SWOT, Porter's Five Forces, business requirements, roadmap, feasibility, competitive analysis, ROI, stakeholder, business model, technology assessment  
**Integrates:** @coordinator.backend [optional], @coordinator.database [optional], @coordinator.infrastructure [optional], @business.billing [optional,seq:2]

✅✅ **analyst.data**
**Role:** Data science and analytics expert
**Tech:** Python (pandas, numpy, scipy, matplotlib, seaborn), R (ggplot2, dplyr, tidyverse), Jupyter Notebooks, statistical analysis, hypothesis testing, A/B testing, predictive modeling, Tableau, Power BI, data visualization, KPI frameworks, user research methodologies
**When:** Statistical analysis, KPIs definition, user research, predictive analytics, business intelligence dashboards, risk assessment, hypothesis testing, A/B testing design, data visualization, exploratory data analysis, statistical modeling
**Keywords:** statistics, statistical analysis, hypothesis testing, A/B testing, KPIs, data visualization, user research, predictive modeling, business intelligence, exploratory analysis, statistical modeling
**Integrates:** @database.postgres [optional], @database.mariadb [optional], @database.mongodb [optional], @analyst.strategic [optional,seq:2], @service.data [optional,seq:3]

## 🔍 Audit and Compliance

✅✅ **audit.compliance** (1430 lines)  
**Role:** Regulatory compliance and accessibility expert specializing in GDPR data protection, WCAG accessibility standards, cost optimization analysis, and privacy compliance frameworks  
**Tech:** GDPR compliance tools, OneTrust Privacy Management, WCAG 2.2 AA testing automation, axe-core, Pa11y, WAVE accessibility evaluator, Lighthouse audits, SOC 2 compliance frameworks, privacy impact assessment tools, cost optimization analysis, regulatory change monitoring, automated compliance scanning  
**When:** GDPR privacy compliance, WCAG accessibility audits, privacy impact assessments, regulatory compliance analysis, cost-benefit compliance analysis, accessibility barrier identification, compliance monitoring automation, regulatory framework mapping  
**Keywords:** GDPR, WCAG, accessibility, compliance, privacy, audit, regulation, PIA, DPIA, SOC 2, cost optimization, monitoring, automation, barriers, remediation  
**Integrates:** @audit.security [optional], @service.auth [optional], @coordinator.security [optional,seq:2], @frontend.react [optional,seq:3]

✅✅ **audit.security** (1200 lines)  
**Role:** Expert security vulnerability assessment specialist with deep expertise in penetration testing, OWASP methodologies, and comprehensive security audits  
**Tech:** OWASP Top 10, OWASP ZAP, OWASP Nettacker, Burp Suite Professional, Nessus, OpenVAS, Qualys VMDR, penetration testing frameworks, vulnerability scanners, CVSS 3.1 scoring, security compliance validation, threat modeling, automated security testing  
**When:** Penetration testing, vulnerability assessments, security audits, OWASP compliance validation, threat modeling, security risk assessment, vulnerability scanning automation, security compliance verification  
**Keywords:** OWASP, penetration testing, vulnerability, security audit, Burp Suite, Nessus, OpenVAS, CVSS, threat modeling, security scanning, risk assessment, compliance  
**Integrates:** @audit.compliance [optional], @coordinator.security [optional], @service.auth [optional,seq:2], @ops.monitoring [optional,seq:3]

## ⚙️ Operations and DevOps

✅✅ **ops.git** (1317 lines)  
**Role:** Git workflow and version control expert  
**Tech:** Git, GitHub Actions, branching strategies, conventional commits, git hooks, submodules, LFS, merge strategies, conflict resolution, rebase workflows, cherry-picking, bisect debugging, release management, semantic versioning, pull request workflows  
**When:** Repository management, branching strategies, commit conventions, code review workflows, version control optimization, Git workflow setup, merge conflict resolution, release management, repository organization  
**Keywords:** Git, GitHub, branching, commits, conventional commits, hooks, merge, rebase, conflict resolution, pull request, release management, version control, repository  
**Integrates:** @docs-specialist [optional], @coordinator.devops [optional,seq:2], @ops.cicd [optional,seq:3]

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

## 🧪 Testing and Quality

🔳 **test.quality** (0 lines)  
 **Role:** Comprehensive testing and quality assurance expert  
 **Tech:** Jest, Cypress, Playwright, JUnit, pytest, test automation frameworks, coverage tools (Istanbul, c8)  
 **When:** Test strategy implementation, automated testing pipelines, quality gates, coverage analysis, testing best practices

## 📅 Planning

🔳 **plan.strategy** (0 lines)  
 **Role:** Project management and strategic planning expert  
 **Tech:** Project management tools (Jira, Asana), agile methodologies, resource planning, timeline management, Gantt charts  
 **When:** Project planning, resource allocation, sprint planning, roadmap creation, timeline management

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

| Domain          | IF                                                                                                           | THEN                                       | Priority                       |
| --------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------ | ------------------------------ |
| Angular         | Angular 17+, NgRx, Angular Material/PrimeNG, complex forms                                                   | frontend.angular                           | Solo                           |
| React           | React 18+/Next.js, UI libs (MUI/Chakra/shadcn), React Query/Zustand                                          | frontend.react                             | Solo                           |
| Vue             | Vue 3/Nuxt, Composition API, Pinia, Vuetify                                                                  | frontend.vue                               | Solo                           |
| Mobile          | React Native (New Architecture)/Flutter 3.24+/Expo SDK 52+/Capacitor 7+; app store publishing; EAS workflows | frontend.mobile                            | Solo                           |
| FE Architecture | Deciding framework/micro-frontends/design system/global state                                                | coordinator.frontend → {angular/react/vue} | Sequential (coordinator first) |

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

| Domain                      | IF                                                                                             | THEN                                  | Priority                         |
| --------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------- | -------------------------------- |
| Postgres (OLTP/TS/Geo)      | GiST/GIN/BRIN indices; Timescale; Citus; OLTP; geospatial                                      | database.postgres                     | Solo                             |
| pgvector (AI Search)        | RAG with PostgreSQL; embeddings in Postgres; similarity search with SQL                        | database.pgvector                     | Solo                             |
| Postgres + Vector           | OLTP + semantic search in same database                                                        | database.postgres ∥ database.pgvector | Parallel (or Sequential by task) |
| MongoDB                     | Documents; aggregations; sharding; change streams                                              | database.mongodb                      | Solo                             |
| MariaDB                     | Galera/MaxScale; MySQL migration; ColumnStore analytics                                        | database.mariadb                      | Solo                             |
| Redis                       | Cache/JSON/Streams; rate-limiting; session store; pub/sub                                      | database.redis                        | Solo                             |
| SQLite (edge)               | Local-first; serverless; FTS5; WAL; Litestream                                                 | database.sqlite                       | Solo                             |
| Vector Databases (Multiple) | Vector database platforms: Weaviate, Pinecone, Qdrant, Chroma, Milvus, pgvector, MongoDB Atlas | database.vectorial                    | Solo                             |
| PostGIS                     | GIS queries; routing; spatial analysis                                                         | database.postgis                      | Solo                             |
| Data Architecture           | DB selection; models; flows; analytical vs transactional                                       | coordinator.database → {db.\*}        | Sequential (coordinator first)   |

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
| ------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------- |
| Payments (transaction)    | Stripe/PayPal/Square; 3DS; PCI; tokenization; fraud prevention | business.payment                                            | Solo                                        |
| Billing (invoices/taxes)  | Invoices; taxes; dunning; revenue recognition                  | business.billing                                            | Solo                                        |
| Subscriptions             | Plans/usage-based; metering; churn; SaaS KPIs                  | business.subscription                                       | Solo                                        |
| **Complete Subscription** | "Stripe subscription with invoicing and billing"               | business.payment ∥ business.billing ∥ business.subscription | Parallel/Sequential (coordinated by Claude) |

### ⚙️ Operations & DevOps Routing

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
   - IF vector database (any platform) → **database.vectorial**
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
7. **Container Orchestration:** Docker/K8s → **ops.containers** ONLY; backend agents handle language-specific code, not infrastructure.
8. **Frontend vs Backend Confusion:**

   - IF **"React component", "Vue component", "UI element", "styling", "responsive design"** → **frontend.{framework}**
   - IF **"API endpoint", "database query", "business logic", "authentication middleware"** → **backend.{stack}**
   - IF **"full-stack feature"** → **backend.{stack}** → **frontend.{framework}** (sequential, backend first)

9. **Database Schema vs Query Optimization:**

   - IF **"design database", "create tables", "relationships", "migration"** → **database.{type}**
   - IF **"slow queries", "performance tuning", "indexes", "query optimization"** → **database.{type}** (same agent, different task)
   - IF **"choose database technology"** → **coordinator.database** → **database.{selected}**

10. **DevOps Strategy vs Tactical Implementation:**

    - IF **"CI/CD strategy", "deployment patterns", "release management"** → **coordinator.devops**
    - IF **"GitHub Actions workflow", "Docker compose", "Kubernetes manifest"** → **ops.{tool}**
    - IF **"implement monitoring"** → **ops.monitoring** directly

11. **API Design vs Integration:**

    - IF **"design REST API", "GraphQL schema", "API architecture"** → **backend.api**
    - IF **"consume external API", "third-party SDK", "webhook handling"** → **service.integrations**
    - IF **"API gateway configuration"** → **ops.webserver** or **coordinator.infrastructure**

12. **Testing Strategy vs Implementation:**

    - IF **"testing strategy", "quality gates", "test automation architecture"** → **coordinator.testing**
    - IF **"write unit tests", "configure Jest", "Cypress setup"** → **{specialist-agent}** (not test agent)
    - IF **"testing framework selection"** → **coordinator.testing** → **{specialist}**

13. **Security Architecture vs Implementation:**

    - IF **"security model", "compliance framework", "threat modeling"** → **coordinator.security**
    - IF **"implement 2FA", "OAuth setup", "JWT validation"** → **service.auth**
    - IF **"penetration testing", "vulnerability scan"** → **audit.security**

14. **Data Processing vs Storage:**

    - IF **"ETL pipeline", "data streaming", "message queues"** → **service.data**
    - IF **"database design", "data modeling", "storage optimization"** → **database.{type}**
    - IF **"analytics dashboard", "data visualization"** → **frontend.{framework}** + **service.data**

15. **Mobile vs Web Development:**

    - IF **"React Native", "Flutter", "iOS/Android", "app store"** → **frontend.mobile**
    - IF **"responsive web", "PWA", "browser compatibility"** → **frontend.{web-framework}**
    - IF **"mobile API", "push notifications"** → **backend.{stack}** + **service.communication**

16. **Infrastructure vs Application:**

    - IF **"server provisioning", "cloud architecture", "load balancing"** → **coordinator.infrastructure**
    - IF **"application deployment", "container orchestration"** → **ops.containers**
    - IF **"code optimization", "application performance"** → **{language-specialist}**

17. **Multi-Agent Workflows:**
    - **"Create user roles system"** → **coordinator.security** → **service.auth** → **database.{selected}** (sequential)
    - **"Deploy web app in container"** → **ops.containers** ∥ **ops.webserver** (parallel)
    - **"GraphQL schema design"** → **backend.api** ONLY (no database involvement)
    - **"Optimize PostgreSQL performance"** → **database.postgres** ONLY (tactical optimization)
    - **"Build e-commerce checkout"** → **business.payment** ∥ **business.billing** ∥ **frontend.{framework}** (parallel)
    - **"Implement search feature"** → **database.vectorial** → **backend.{stack}** → **frontend.{framework}** (sequential)
