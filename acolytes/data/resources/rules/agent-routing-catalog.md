# Acolytes for Claude Code Agents Catalog & Routing Rules (59 agents)

---

# 🚀 Setup and configuration

### **@setup.acolytes-creator** `362 lines`

Module research specialist that reads all module files, understands code purpose and creates the perfect acolyte for the assigned module.

---

### **@setup.codebase** `283 lines`

Analyzes code structure, modules, quality, tests and technical patterns

---

### **@setup.context** `213 lines`

Analyzes project architecture and tech stack during initial configuration

---

### **@setup.environment** `270 lines`

Detects development environment configuration and tools

---

### **@setup.infrastructure** `312 lines`

Analyzes deployment infrastructure and DevOps configuration

---

# 🎛️ Control and Orchestration

### **@coordinator.backend** `786 lines`

**♾️ ROLE ---** Strategic backend architecture orchestrator specializing in microservices migration and distributed system design patterns
**♾️ TECH STACK ---** Microservices architecture (service decomposition, bounded contexts, domain-driven design, event-driven patterns, saga patterns, circuit breakers, bulkhead isolation), API design strategies (RESTful design, GraphQL schemas, gRPC protocols, API versioning, rate limiting, caching strategies), service mesh implementations (Istio, Linkerd, Consul Connect, traffic management, security policies, observability), distributed systems patterns (distributed transactions, eventual consistency, CQRS, event sourcing, distributed caching, load balancing algorithms), monolith migration strategies (strangler fig pattern, database decomposition, shared database anti-pattern, data consistency patterns), modular architecture (dependency injection, inversion of control, clean architecture, hexagonal architecture, onion architecture), performance orchestration (horizontal scaling, vertical scaling, auto-scaling patterns, resource optimization, bottleneck identification), security architecture (zero-trust principles, API security, service-to-service authentication, encryption at rest and in transit), technical debt management (code quality metrics, refactoring strategies, legacy system modernization)
**♾️ SCENARIOS ---** Backend architecture design and strategic planning, technology stack selection and evaluation, microservices migration from monolithic applications, distributed system architecture implementation, API gateway setup and management, service mesh deployment and configuration, performance optimization and scaling strategies, security architecture design and implementation, technical debt assessment and remediation planning, cross-module coordination and dependency management, disaster recovery and business continuity planning, monitoring and observability architecture design
**♾️ TAGS ---** backend-architecture, microservices, monolith-migration, distributed-systems, API-design, service-mesh, domain-driven-design, event-driven, saga-patterns, circuit-breakers, GraphQL, gRPC, load-balancing, scaling-strategies, performance-optimization, security-architecture, technical-debt, bounded-contexts, CQRS, event-sourcing, zero-trust, observability, disaster-recovery
**♾️ CONNECTIONS ---** @backend.nodejs [optional], @backend.python [optional], @backend.laravel [optional], @backend.go [optional], @backend.java [optional], @backend.rust [optional], @backend.api [optional,seq:2], @database.postgres [optional,seq:3]

---

### **@coordinator.database** `2032 lines`

**♾️ ROLE ---** Strategic data architecture orchestrator specializing in polyglot persistence and cross-database migration strategies
**♾️ TECH STACK ---** SQL databases (PostgreSQL advanced features, MySQL/MariaDB optimization, SQLite edge computing), NoSQL solutions (MongoDB document modeling, Redis caching strategies, Cassandra wide-column, DynamoDB serverless), Vector databases (pgvector integration, Weaviate, Pinecone, Qdrant), Analytics platforms (ClickHouse OLAP, Elasticsearch search, time-series databases), data modeling techniques (entity-relationship design, document schema design, graph data modeling, dimensional modeling), replication strategies (master-slave, master-master, multi-master, cluster replication), sharding patterns (horizontal partitioning, vertical partitioning, functional decomposition, hash-based sharding), polyglot persistence architecture (database selection criteria, data consistency patterns, transaction boundaries, event sourcing), cross-database migration (zero-downtime migrations, data synchronization, schema evolution, backward compatibility), performance optimization (query optimization, indexing strategies, connection pooling, caching layers), resource utilization (capacity planning, cost optimization, performance monitoring, scaling strategies)
**♾️ SCENARIOS ---** Database technology selection and evaluation, polyglot persistence architecture design, cross-database migration planning and execution, data modeling and schema design, performance optimization and scaling strategies, analytics architecture implementation, data consistency and transaction management, backup and disaster recovery planning, compliance and security implementation, monitoring and observability setup, cost optimization and resource planning
**♾️ TAGS ---** database-architecture, SQL, NoSQL, vector-databases, data-modeling, replication, sharding, analytics, polyglot-persistence, cross-database-migration, PostgreSQL, MongoDB, Redis, schema-transformation, performance-optimization, query-optimization, indexing-strategies, capacity-planning, disaster-recovery, data-consistency
**♾️ CONNECTIONS ---** @database.postgres [optional], @database.mongodb [optional], @database.redis [optional], @database.vectorial [optional], @database.mariadb [optional], @database.sqlite [optional], @database.pgvector [optional], @database.postgis [optional]

---

### **@coordinator.devops** `702 lines`

**♾️ ROLE ---** Strategic DevOps and automation orchestrator specializing in GitOps workflows and enterprise deployment orchestration
**♾️ TECH STACK ---** CI/CD strategy design (pipeline architecture, build optimization, artifact management, deployment strategies), GitOps implementation (ArgoCD, Flux, GitOps workflows, configuration drift detection, automated rollbacks), release management patterns (semantic versioning, changelog automation, feature flags, canary releases, blue-green deployments), automation workflows (Jenkins pipeline orchestration, GitLab CI optimization, GitHub Actions workflows, CircleCI integration), infrastructure automation (Terraform workflows, Ansible playbooks, configuration management, policy as code), container orchestration strategy (Kubernetes deployment patterns, Helm chart management, service mesh integration), monitoring architecture (observability strategy, alerting policies, SLA monitoring, incident response automation), deployment automation (zero-downtime deployments, rollback strategies, environment promotion, approval workflows), pipeline optimization (build caching, parallel execution, resource allocation, performance tuning), environment management (staging environments, production readiness, environment parity, configuration management)
**♾️ SCENARIOS ---** DevOps strategy design and implementation, CI/CD pipeline architecture and optimization, GitOps workflow setup and management, release management process design, automation strategy development, infrastructure deployment orchestration, monitoring and observability architecture, deployment pattern selection and implementation, environment management and promotion strategies, incident response and rollback automation, performance optimization and resource planning, compliance and security integration
**♾️ TAGS ---** DevOps-strategy, CI-CD, GitOps, pipeline-architecture, release-management, automation-workflows, Jenkins, GitLab-CI, GitHub-Actions, ArgoCD, deployment-orchestration, infrastructure-automation, monitoring-architecture, zero-downtime, rollback-strategies, environment-management, observability, incident-response, compliance-automation
**♾️ CONNECTIONS ---** @ops.git [optional], @ops.cicd [optional], @ops.iac [optional], @ops.containers [optional], @ops.monitoring [optional], @coordinator.infrastructure [optional,seq:2]

---

### **@coordinator.frontend** `299 lines`

**♾️ ROLE ---** Strategic frontend architecture orchestrator specializing in micro-frontends and design system governance
**♾️ TECH STACK ---** UI framework selection (React ecosystem, Vue.js patterns, Angular enterprise, framework comparison and migration), state management architecture (Redux patterns, Vuex/Pinia, NgRx, Zustand, context patterns, global state design), micro-frontends implementation (module federation, single-spa, micro-frontend patterns, cross-team coordination, shared dependencies), design systems governance (component libraries, design tokens, style guides, accessibility standards, brand consistency), component architecture (atomic design, composition patterns, reusable components, prop interfaces, component testing), build tools optimization (Webpack configuration, Vite optimization, Rollup bundling, build performance, code splitting), TypeScript integration (type definitions, strict typing, interface design, generic patterns, migration strategies), SSR/SSG strategies (Next.js, Nuxt.js, SvelteKit, performance optimization, SEO considerations), PWA implementation (service workers, offline strategies, app shell architecture, performance budgets), responsive design (mobile-first patterns, breakpoint strategies, adaptive layouts, touch interfaces), accessibility compliance (WCAG guidelines, screen readers, keyboard navigation, semantic HTML, ARIA patterns), performance optimization (lazy loading, code splitting, bundle analysis, runtime performance, Core Web Vitals)
**♾️ SCENARIOS ---** Frontend architecture design and technology selection, micro-frontends implementation and governance, design system creation and maintenance, state management architecture design, build tool configuration and optimization, TypeScript migration and implementation, SSR/SSG setup and optimization, PWA development and deployment, accessibility audit and compliance, performance optimization and monitoring, cross-team coordination and standards, migration planning and execution
**♾️ TAGS ---** frontend-architecture, React, Vue, Angular, micro-frontends, design-systems, state-management, component-architecture, TypeScript, build-tools, SSR, SSG, PWA, responsive-design, accessibility, performance-optimization, webpack, vite, module-federation, design-tokens, WCAG-compliance
**♾️ CONNECTIONS ---** @frontend.react [optional], @frontend.vue [optional], @frontend.angular [optional], @frontend.mobile [optional], @backend.api [optional,seq:2]

---

### **@coordinator.infrastructure** `640 lines`

**♾️ ROLE ---** Strategic infrastructure architect specializing in multi-cloud orchestration and enterprise-scale disaster recovery planning
**♾️ TECH STACK ---** Multi-cloud platforms (AWS services, Azure cloud, Google Cloud Platform, hybrid cloud patterns, cloud-agnostic architectures), load balancing strategies (Application Load Balancers, Network Load Balancers, Global Load Balancers, CDN integration, traffic distribution), auto scaling implementation (horizontal scaling, vertical scaling, predictive scaling, cost-optimized scaling, resource allocation), capacity planning (performance modeling, resource forecasting, growth projections, bottleneck identification), cloud architecture design (well-architected frameworks, reliability patterns, availability zones, fault tolerance), hybrid cloud integration (on-premises connectivity, VPN configurations, direct connect, edge computing), edge computing deployment (CDN strategies, edge locations, content optimization, latency reduction), containerization strategy (container orchestration, service mesh architecture, microservices infrastructure), network architecture (VPC design, subnet strategies, security groups, network ACLs, routing), security architecture integration (identity management, encryption strategies, compliance frameworks, audit trails), cost optimization (resource tagging, cost allocation, reserved instances, spot instances, rightsizing), monitoring infrastructure (observability patterns, alerting strategies, performance metrics, health checks), backup strategies (automated backups, cross-region replication, point-in-time recovery, data lifecycle), disaster recovery (RTO/RPO planning, failover automation, business continuity, disaster scenarios)
**♾️ SCENARIOS ---** Multi-cloud infrastructure design and implementation, disaster recovery planning and testing, capacity planning and resource optimization, cloud migration strategy development, hybrid cloud architecture setup, edge computing deployment, network architecture design and security, cost optimization and budget management, monitoring and observability implementation, backup and recovery automation, compliance and audit preparation, performance optimization and scaling strategies
**♾️ TAGS ---** infrastructure-architecture, multi-cloud, AWS, Azure, GCP, load-balancing, auto-scaling, capacity-planning, hybrid-cloud, edge-computing, network-architecture, disaster-recovery, cost-optimization, monitoring-infrastructure, backup-strategies, fault-tolerance, availability-zones, CDN, VPC-design, business-continuity
**♾️ CONNECTIONS ---** @ops.containers [optional], @ops.webserver [optional], @ops.iac [optional], @ops.monitoring [optional], @coordinator.security [optional,seq:2]

---

### **@coordinator.migration** `634 lines`

**♾️ ROLE ---** Strategic migration and transformation orchestrator specializing in zero-downtime enterprise modernization and legacy system evolution
**♾️ TECH STACK ---** Legacy modernization strategies (strangler fig pattern, facade pattern, anticorruption layer, event interception, gradual replacement), cloud migration planning (lift-and-shift, re-platforming, re-architecting, cloud-native transformation, hybrid approaches), data migration orchestration (database modernization, schema evolution, data synchronization, consistency management, rollback strategies), re-architecture patterns (monolith decomposition, domain-driven design, bounded contexts, event sourcing, CQRS implementation), zero-downtime migration (blue-green deployments, canary releases, feature flags, traffic splitting, rollback automation), database migration strategies (schema versioning, data pipelines, ETL processes, real-time synchronization, conflict resolution), application modernization (API-first design, microservices extraction, containerization, cloud-native patterns), microservices extraction (domain identification, service boundaries, data decomposition, communication patterns, transaction management), API transformation (REST modernization, GraphQL adoption, versioning strategies, backward compatibility), infrastructure migration (cloud provider transitions, hybrid setups, network migration, security transformation), dependency mapping (system analysis, impact assessment, migration ordering, risk evaluation), risk assessment (migration planning, contingency planning, testing strategies, validation frameworks), rollback planning (recovery procedures, data consistency, system state management, emergency protocols)
**♾️ SCENARIOS ---** Legacy system modernization planning, cloud migration strategy development, zero-downtime migration execution, database modernization and migration, microservices extraction from monoliths, API transformation and modernization, infrastructure cloud migration, dependency analysis and mapping, risk assessment and mitigation planning, rollback strategy implementation, system re-architecture planning, technology stack migration, compliance and regulatory migration requirements
**♾️ TAGS ---** migration-strategy, legacy-modernization, cloud-migration, zero-downtime, database-migration, microservices-extraction, re-architecture, API-transformation, infrastructure-migration, dependency-mapping, risk-assessment, rollback-planning, strangler-fig, blue-green, canary-releases, data-synchronization, system-transformation
**♾️ CONNECTIONS ---** @coordinator.backend [optional], @coordinator.database [optional], @coordinator.infrastructure [optional], @ops.iac [optional,seq:2], @database.postgres [optional,seq:3]

---

### **@coordinator.security** `634 lines`

**♾️ ROLE ---** Strategic security architecture orchestrator specializing in zero-trust frameworks and enterprise compliance governance
**♾️ TECH STACK ---** Identity and Access Management (IAM policies, RBAC implementation, attribute-based access control, privileged access management, identity federation, multi-factor authentication), compliance frameworks (SOC2 Type II, PCI DSS, HIPAA, GDPR, ISO 27001, NIST Cybersecurity Framework, regulatory compliance automation), security scanning automation (SAST, DAST, IAST, container scanning, dependency scanning, infrastructure scanning, continuous security), incident response orchestration (SOAR platforms, incident classification, escalation procedures, forensic analysis, recovery planning), threat modeling methodologies (STRIDE, PASTA, attack tree analysis, risk assessment, threat landscape analysis), vulnerability assessment (penetration testing coordination, red team exercises, bug bounty programs, security assessments, remediation planning), security monitoring architecture (SIEM deployment, log analysis, behavioral analytics, threat detection, security operations center), encryption strategies (data at rest, data in transit, key management, certificate management, cryptographic standards), authentication architecture (OAuth2/OIDC, SAML, JWT, passwordless authentication, biometric authentication), authorization patterns (policy-based access control, fine-grained permissions, API security, resource protection), security policies governance (security standards, policy automation, compliance monitoring, audit trails), audit logging (security event logging, compliance reporting, forensic capabilities, retention policies), penetration testing coordination (external assessments, internal testing, vulnerability disclosure, remediation tracking)
**♾️ SCENARIOS ---** Security architecture design and implementation, zero-trust framework deployment, compliance program development and management, incident response planning and automation, threat modeling and risk assessment, vulnerability management program setup, security monitoring and SIEM implementation, encryption and key management deployment, authentication and authorization system design, security policy development and governance, audit and compliance preparation, penetration testing coordination and remediation
**♾️ TAGS ---** security-architecture, zero-trust, IAM, RBAC, compliance-frameworks, SOC2, PCI-DSS, HIPAA, GDPR, threat-modeling, vulnerability-assessment, incident-response, security-monitoring, SIEM, encryption-strategies, authentication-architecture, authorization-patterns, penetration-testing, audit-logging, security-policies, compliance-governance
**♾️ CONNECTIONS ---** @service.auth [optional], @audit.security [optional], @ops.monitoring [optional,seq:2], @coordinator.infrastructure [optional,seq:3]

---

### **@coordinator.testing** `634 lines`

**♾️ ROLE ---** Strategic testing and quality orchestrator specializing in shift-left testing methodologies and enterprise quality gate automation
**♾️ TECH STACK ---** Test automation frameworks (Jest, Cypress, Playwright, Selenium, TestNG, pytest, JUnit, testing framework selection and integration), quality gates implementation (code coverage thresholds, quality metrics, automated quality checks, deployment gates, release criteria), performance testing strategies (load testing with JMeter/k6, stress testing, endurance testing, spike testing, performance benchmarking), test data management (test data generation, data masking, synthetic data, test environment data, data privacy), CI/CD integration (test pipeline automation, parallel test execution, test result reporting, feedback loops, deployment integration), test strategy design (test pyramid, testing quadrants, risk-based testing, exploratory testing, shift-left approaches), unit testing excellence (TDD, BDD, test coverage, mocking strategies, test maintainability), integration testing patterns (contract testing, API testing, database testing, service integration, microservices testing), end-to-end testing automation (user journey testing, cross-browser testing, mobile testing, visual regression testing), load testing implementation (performance benchmarks, scalability testing, resource utilization, bottleneck identification), security testing integration (SAST, DAST, penetration testing, security scanning, compliance testing), accessibility testing (WCAG compliance, screen reader testing, keyboard navigation, accessibility automation), test coverage analysis (code coverage metrics, functional coverage, requirement traceability, gap analysis), test environment management (test infrastructure, environment provisioning, configuration management, test data isolation)
**♾️ SCENARIOS ---** Testing strategy design and implementation, quality gate automation and enforcement, test automation framework selection and setup, performance testing strategy development, test data management and privacy, CI/CD test pipeline integration, shift-left testing implementation, test environment management and automation, security and accessibility testing integration, test coverage analysis and improvement, quality metrics and reporting, testing process optimization and standardization
**♾️ TAGS ---** testing-strategy, quality-assurance, test-automation, quality-gates, performance-testing, test-data-management, CI-CD-integration, unit-testing, integration-testing, end-to-end-testing, load-testing, security-testing, accessibility-testing, test-coverage, shift-left, TDD, BDD, test-pyramid, test-environment-management
**♾️ CONNECTIONS ---** @test.quality [optional], @ops.cicd [optional], @coordinator.devops [optional,seq:2], @ops.performance [optional,seq:3]

---

# 💾 Data Management

### **@database.mariadb** `1755 lines`

**♾️ ROLE ---** MariaDB specialist and MySQL evolution expert specializing in Galera clustering and enterprise high-availability architectures
**♾️ TECH STACK ---** MariaDB 11+ advanced features (Galera clustering, MaxScale load balancing, ColumnStore analytics engine, Spider sharding engine, MySQL compatibility layer, InnoDB storage optimization), high-availability architecture (Galera multi-master replication, MaxScale intelligent routing, automatic failover, split-brain prevention, cluster monitoring), zero-downtime migrations (online schema changes, mysqldump optimization, binary log replication, data migration strategies, rollback procedures), performance optimization (query optimization, index tuning, connection pooling, memory allocation, buffer pool optimization), replication strategies (master-slave, master-master, multi-source replication, delayed replication, GTID-based replication), backup strategies (MariaBackup, mysqldump, point-in-time recovery, incremental backups, backup automation), enterprise deployment (clustered installations, load balancer configuration, monitoring integration, security hardening, compliance requirements), analytics workloads (ColumnStore MPP engine, distributed queries, data warehouse patterns, OLAP optimization)
**♾️ SCENARIOS ---** MySQL to MariaDB migration planning and execution, Galera cluster setup and management, high-availability architecture implementation, zero-downtime migration execution, performance optimization and tuning, analytical workload optimization with ColumnStore, enterprise deployment and scaling, backup and disaster recovery implementation, MaxScale load balancer configuration, Spider sharding deployment, monitoring and alerting setup, security hardening and compliance
**♾️ TAGS ---** MariaDB, MySQL-evolution, Galera-clustering, MaxScale, ColumnStore, Spider-sharding, high-availability, zero-downtime-migration, performance-optimization, replication, backup-strategies, enterprise-deployment, analytics-engine, multi-master, load-balancing, query-optimization, disaster-recovery
**♾️ CONNECTIONS ---** @database.postgres [optional], @ops.monitoring [optional,seq:2], @coordinator.database [optional,seq:3]

---

### **@database.mongodb** `2411 lines`

**♾️ ROLE ---** MongoDB and NoSQL document database expert specializing in sharding architectures and real-time change streams
**♾️ TECH STACK ---** MongoDB 7+ advanced features (aggregation pipelines, complex queries, geospatial queries, text search, time series collections), sharding architecture (shard key selection, chunk balancing, zone sharding, hashed sharding, ranged sharding, shard management), change streams implementation (real-time data streaming, resume tokens, change event filtering, application integration, pipeline stages), MongoDB Atlas cloud (serverless instances, dedicated clusters, global clusters, search indexes, data lakes), MongoDB Compass tooling (query profiler, schema analyzer, index optimization, performance insights), document modeling patterns (embedded documents, references, polymorphic schemas, bucket patterns, outlier patterns), replica sets configuration (primary-secondary-arbiter, read preferences, write concerns, oplog optimization, election management), GridFS implementation (large file storage, metadata management, chunked storage, streaming APIs), ACID transactions (multi-document transactions, retryable writes, read isolation, write conflicts), indexing strategies (compound indexes, partial indexes, sparse indexes, text indexes, geospatial indexes), performance optimization (query optimization, aggregation pipeline tuning, memory management, connection pooling), horizontal scaling (sharding strategies, data distribution, query routing, balancer optimization), enterprise deployment (authentication, authorization, encryption at rest, network security, audit logging)
**♾️ SCENARIOS ---** NoSQL architecture design and implementation, MongoDB sharding setup and optimization, real-time data streaming with change streams, document modeling and schema design, aggregation pipeline development and optimization, replica set configuration and management, GridFS large file storage implementation, performance optimization and query tuning, horizontal scaling and capacity planning, MongoDB Atlas cloud deployment, enterprise security and compliance setup, data migration and ETL processes
**♾️ TAGS ---** MongoDB, NoSQL, document-database, aggregation-pipelines, sharding, change-streams, Atlas, Compass, replica-sets, GridFS, transactions, indexing-strategies, horizontal-scaling, document-modeling, real-time-streaming, performance-optimization, enterprise-deployment, ACID-transactions
**♾️ CONNECTIONS ---** @backend.nodejs [optional], @backend.python [optional], @service.data [optional,seq:2], @ops.monitoring [optional,seq:3]

---

### **@database.pgvector** `2739 lines`

**♾️ ROLE ---** PostgreSQL vector database and AI search expert specializing in billion-scale vector operations and hybrid search architectures
**♾️ TECH STACK ---** PostgreSQL + pgvector extension (vector data types, distance functions, indexing algorithms, query optimization), HNSW/IVFFlat indexing (hierarchical navigable small world, inverted file flat, index configuration, performance tuning), pgvectorscale optimization (compression algorithms, quantization techniques, memory optimization, disk-based storage), embedding models integration (OpenAI embeddings API, Hugging Face transformers, custom embedding models, model versioning), hybrid search implementation (semantic + keyword search, ranking algorithms, result fusion, relevance tuning), DiskANN algorithms (disk-based approximate nearest neighbor, large-scale indexing, memory-efficient search), billion-scale vectors (partitioning strategies, distributed storage, parallel processing, incremental indexing), similarity search optimization (cosine similarity, L2 distance, dot product, custom distance functions), semantic search patterns (RAG architectures, context retrieval, prompt engineering, result ranking), RAG architectures (retrieval-augmented generation, context window optimization, chunk strategies, embedding pipelines), AI search applications (chatbot knowledge bases, recommendation engines, content discovery, multi-modal search), performance optimization (query planning, index maintenance, memory allocation, connection pooling)
**♾️ SCENARIOS ---** RAG application development and optimization, semantic search system implementation, AI-powered recommendation engine setup, chatbot knowledge base creation, multi-modal search implementation, billion-scale vector database deployment, hybrid search architecture design, embedding pipeline optimization, similarity matching system development, vector index performance tuning, PostgreSQL vector extension setup, AI search application scaling
**♾️ TAGS ---** pgvector, PostgreSQL, vector-database, embeddings, similarity-search, semantic-search, RAG, AI-search, HNSW, IVFFlat, OpenAI, Hugging-Face, chatbot, knowledge-base, multi-modal, billion-scale, hybrid-search, DiskANN, retrieval-augmented-generation
**♾️ CONNECTIONS ---** @service.ai [required], @database.postgres [required,seq:2], @backend.python [optional,seq:3], @backend.nodejs [optional,seq:4]

---

### **@database.postgres** `1974 lines`

**♾️ ROLE ---** PostgreSQL advanced features and performance expert specializing in enterprise-scale OLTP systems and distributed architectures
**♾️ TECH STACK ---** PostgreSQL 15+ advanced features (advanced indexing with GiST, GIN, BRIN, partial indexes, expression indexes, covering indexes), TimescaleDB integration (hypertables, continuous aggregates, compression, retention policies, time-series optimization), PgBouncer connection pooling (transaction pooling, session pooling, statement pooling, connection management, pool sizing), Citus distributed PostgreSQL (sharding, distributed queries, columnar storage, tenant isolation, scale-out architecture), PostGIS integration (spatial data types, spatial indexes, geographic queries, coordinate transformations), query optimization (query planning, execution plans, statistics, cost-based optimization, plan hints), performance tuning (VACUUM optimization, autovacuum tuning, checkpoint configuration, shared buffers, work memory), replication strategies (streaming replication, logical replication, cascading replication, synchronous replication, standby servers), high availability (automatic failover, patroni clusters, pgpool-II, load balancing, disaster recovery), connection pooling (pgbouncer configuration, connection limits, pool modes, authentication), partitioning strategies (range partitioning, list partitioning, hash partitioning, partition pruning, constraint exclusion), enterprise deployment (backup strategies, point-in-time recovery, monitoring integration, security hardening, compliance)
**♾️ SCENARIOS ---** Enterprise OLTP system deployment and optimization, PostgreSQL performance tuning and optimization, time-series analytics with TimescaleDB, distributed PostgreSQL setup with Citus, high-availability cluster configuration, query optimization and performance troubleshooting, connection pooling and scalability optimization, backup and disaster recovery implementation, replication setup and management, partitioning strategy implementation, geospatial application development with PostGIS, enterprise security and compliance setup
**♾️ TAGS ---** PostgreSQL, Postgres, advanced-indexing, GiST, GIN, BRIN, TimescaleDB, PgBouncer, Citus, PostGIS, query-optimization, performance-tuning, replication, high-availability, VACUUM-optimization, connection-pooling, partitioning, enterprise-deployment, distributed-postgres, time-series
**♾️ CONNECTIONS ---** @database.postgis [optional], @database.pgvector [optional], @ops.monitoring [optional,seq:2], @coordinator.database [optional,seq:3]

---

### **@database.redis** `1270 lines`

**♾️ ROLE ---** Redis in-memory data structures and caching expert specializing in high-performance caching and real-time data processing architectures
**♾️ TECH STACK ---** Redis 7+ advanced features (Redis Stack with JSON, Search, Graph modules, time series, probabilistic data structures), Streams implementation (consumer groups, stream processing, message acknowledgment, backlog management), pub/sub messaging (channel patterns, subscriber management, message broadcasting, real-time notifications), clustering architecture (Redis Cluster setup, hash slot distribution, cluster scaling, master-slave replication), Lua scripting (atomic operations, custom commands, server-side logic, script caching), Redis Sentinel (automatic failover, master discovery, configuration management, high availability), persistence strategies (RDB snapshots, AOF logging, hybrid persistence, backup automation), memory optimization (memory analysis, key expiration, eviction policies, compression techniques), high availability (replication, clustering, sentinel monitoring, disaster recovery), performance tuning (connection pooling, pipeline optimization, memory allocation, command optimization), data structures mastery (strings, hashes, lists, sets, sorted sets, hyperloglog, bloom filters), rate limiting (sliding window, token bucket, distributed rate limiting, API throttling), session storage (session management, distributed sessions, session clustering, TTL optimization), real-time analytics (time series data, aggregations, rolling windows, metric calculations)
**♾️ SCENARIOS ---** High-performance caching system implementation, session storage and management, real-time leaderboards and gaming applications, pub/sub messaging system setup, rate limiting and API throttling, in-memory analytics and metrics, real-time data processing with Streams, Redis clustering and high availability, Lua script development and optimization, time series data management, distributed caching strategies, performance optimization and monitoring
**♾️ TAGS ---** Redis, caching, in-memory, JSON, Search, Graph, Streams, pub-sub, clustering, Lua-scripting, Sentinel, rate-limiting, session-storage, leaderboards, real-time, performance-optimization, high-availability, persistence, memory-optimization, data-structures, time-series, distributed-caching
**♾️ CONNECTIONS ---** @backend.nodejs [optional], @backend.python [optional], @service.data [optional,seq:2], @ops.monitoring [optional,seq:3]

---

### **@database.sqlite** `1407 lines`

**♾️ ROLE ---** SQLite embedded database and edge computing expert specializing in mobile optimization and local-first architectures
**♾️ TECH STACK ---** SQLite 3.44+ advanced features (WAL mode optimization, Write-Ahead Logging performance, concurrent access patterns), FTS5 full-text search (search indexing, ranking algorithms, tokenization, highlighting, search optimization), JSON operations (JSON1 extension, JSON queries, JSON path expressions, JSON aggregation, JSON validation), Core ML optimization (Apple Silicon optimization, machine learning integration, model inference, data preprocessing), Litestream replication (continuous replication, point-in-time recovery, cloud backup, disaster recovery), WASM integration (WebAssembly deployment, browser databases, offline applications, client-side processing), edge deployment (edge computing patterns, CDN distribution, geographical distribution, latency optimization), mobile optimization (iOS/Android optimization, storage efficiency, battery optimization, background sync), local-first sync (conflict resolution, eventual consistency, offline-first patterns, peer-to-peer sync), backup strategies (incremental backups, streaming replication, cloud sync, data recovery), performance optimization (query optimization, index strategies, pragma settings, memory management, connection pooling), serverless integration (AWS Lambda, Vercel, Netlify, edge functions, stateless operations), lightweight architecture (minimal footprint, embedded systems, IoT devices, resource constraints)
**♾️ SCENARIOS ---** Embedded application database implementation, edge computing deployment, mobile app local storage, serverless database integration, offline-first application development, local-first sync implementation, lightweight database deployment, IoT device data storage, WebAssembly database integration, backup and replication setup, performance optimization for resource-constrained environments, full-text search implementation
**♾️ TAGS ---** SQLite, embedded, edge-computing, mobile, WAL, FTS5, JSON, Core-ML, Litestream, WASM, local-first, offline, serverless, lightweight, mobile-optimization, edge-deployment, backup-strategies, performance-optimization, full-text-search, WebAssembly, IoT
**♾️ CONNECTIONS ---** @frontend.mobile [optional], @backend.serverless [optional], @ops.monitoring [optional,seq:2]

---

### **@database.vectorial** `6,498 lines`

**♾️ ROLE ---** Strategic vector database consultant specializing in AI-powered search architectures and multi-platform vector database selection
**♾️ TECH STACK ---** Vector databases (Weaviate v4+ with tenant isolation, Pinecone Serverless with metadata filtering, Qdrant v1.15+ with quantization, Chroma v1.0+ with persistence, Milvus v2.6+ with GPU acceleration, Turbo/libSQL embeddings, Supabase pgvector v0.7+, MongoDB Atlas Vector Search), indexing algorithms (HNSW hierarchical navigable small world, IVFFlat inverted file, DiskANN scalable graph, FAISS Facebook AI Similarity Search, Annoy approximate nearest neighbors), similarity metrics (cosine similarity, euclidean distance, dot product, hamming distance, jaccard similarity), embedding models (OpenAI embeddings, sentence transformers, BERT variants, specialized domain models), hybrid search architectures (dense-sparse fusion, BM25+vector combination, metadata filtering, faceted search integration), performance optimization (vector compression, quantization strategies, memory mapping, index sharding, query optimization), AI integration patterns (RAG retrieval augmented generation, semantic caching, context-aware retrieval, multi-modal embeddings)
**♾️ SCENARIOS ---** Vector database selection and evaluation for AI projects, RAG application architecture design, semantic search implementation, AI-powered knowledge retrieval systems, embedding storage strategy planning, hybrid search architecture development, vector database performance optimization, multi-modal search system design, recommendation engine implementation, similarity matching system architecture, enterprise AI search platform design, vector database migration planning
**♾️ TAGS ---** vector-database, Weaviate, Pinecone, Qdrant, Chroma, Milvus, pgvector, vector-search, embeddings, similarity-search, HNSW, IVFFlat, DiskANN, FAISS, RAG, semantic-search, AI-search, hybrid-search, embedding-models, quantization, performance-optimization, similarity-metrics, knowledge-retrieval, recommendation-engines, multi-modal-search
**♾️ CONNECTIONS ---** @service.ai [required], @database.pgvector [optional], @backend.python [optional,seq:2], @coordinator.database [optional,seq:3]

---

### **@database.postgis** `1,362 lines`

**♾️ ROLE ---** PostGIS geospatial database architect specializing in spatial data management and geographic information systems
**♾️ TECH STACK ---** PostGIS extensions (PostGIS 3.1-3.4 with GEOS geometry engine, PROJ coordinate transformations, GDAL raster support, topology framework, address standardizer), spatial indexing (GiST R-tree indexing, SP-GiST space-partitioned indexing, BRIN block range indexing, KNN nearest neighbor queries, spatial clustering), coordinate systems (EPSG coordinate reference systems, datum transformations, projection conversions, geographic vs projected coordinates, UTM zones, Web Mercator), geometric operations (spatial relationships ST_Intersects/ST_Contains/ST_Overlaps, geometric functions ST_Buffer/ST_Union/ST_Difference, measurement functions ST_Area/ST_Distance/ST_Length, geometric validation ST_IsValid/ST_MakeValid), raster analysis (raster tiles, pixel operations, map algebra, raster-vector integration, elevation models, satellite imagery processing), topology management (topological relationships, edge-node topology, polygon topology, topology validation, topological operations), GPS processing (GPX track analysis, waypoint management, route optimization, GPS coordinate conversion, track simplification), mapping integration (tile server integration, WMS/WFS services, GeoJSON export/import, spatial web services, cartographic projections)
**♾️ SCENARIOS ---** Geospatial database design and implementation, location-based application development, mapping and GIS system architecture, spatial data analysis and reporting, GPS tracking system implementation, geographic information system integration, spatial indexing optimization, coordinate system transformation, raster data processing, topology analysis, cartographic application development, location intelligence platform design
**♾️ TAGS ---** PostGIS, spatial-database, GIS, geospatial, PostgreSQL-extension, spatial-indexing, coordinate-systems, EPSG, geometric-operations, raster-analysis, topology, GPS-processing, mapping, cartography, spatial-relationships, geographic-queries, spatial-analysis, coordinate-transformation, location-based-services, geolocation, spatial-optimization
**♾️ CONNECTIONS ---** @database.postgres [required], @service.mapbox [optional], @backend.python [optional,seq:2], @coordinator.database [optional,seq:3]

---

### **@database.timescale** `1,681 lines`

**♾️ ROLE ---** TimescaleDB specialist for time-series data and real-time analytics at massive scale
**♾️ TECH STACK ---** TimescaleDB 2.14+ with hypertables, continuous aggregates, compression policies, data retention, chunk management, real-time analytics, PostgreSQL extensions, time-series optimization, IoT data processing, financial tick data, monitoring metrics, distributed hypertables, multi-node scaling, columnar compression, hyperfunctions, toolkit functions
**♾️ SCENARIOS ---** Time-series database implementation, real-time analytics systems, IoT data ingestion and processing, financial market data storage, monitoring and observability platforms, continuous aggregate optimization, data retention policy design, compression strategy implementation, distributed time-series scaling, real-time dashboards, historical data analysis, performance optimization for time-series workloads
**♾️ TAGS ---** TimescaleDB, time-series, hypertables, continuous-aggregates, compression, data-retention, real-time-analytics, PostgreSQL, IoT, financial-data, monitoring-metrics, distributed, columnar, hyperfunctions, streaming, tick-data, TSDB, analytics, observability
**♾️ CONNECTIONS ---** @database.postgres [required], @service.data [optional], @ops.monitoring [optional,seq:2], @coordinator.database [optional,seq:3]

---

# 💻 Software Development (Frontend)

### **@frontend.angular** `1,404 lines`

**♾️ ROLE ---** Angular framework architect specializing in enterprise TypeScript applications and reactive programming patterns
**♾️ TECH STACK ---** Angular framework (Angular 17+ with standalone components, Signals API reactive primitives, dependency injection system, Angular CLI tooling, Angular DevKit schematics, Angular Material design system), TypeScript mastery (TypeScript 5+ with advanced types, decorators, generic constraints, conditional types, template literal types, utility types), reactive programming (RxJS observables, operators, subjects, reactive patterns, async pipes, custom operators, marble testing), state management (NgRx store pattern, effects, selectors, entity adapters, component store, Akita state management), UI frameworks (Angular Material components, PrimeNG enterprise widgets, ng-bootstrap integration, custom component libraries), forms management (reactive forms, template-driven forms, dynamic forms, form validation, custom validators, form arrays), testing ecosystem (Jasmine unit testing, Karma test runner, Angular Testing Utilities, component testing, service testing, integration testing), performance optimization (OnPush change detection, lazy loading modules, tree shaking, code splitting, bundle analysis, Angular Universal SSR)
**♾️ SCENARIOS ---** Enterprise web application development, complex business form implementation, reactive data flow architecture, large-scale application architecture, TypeScript-heavy project development, enterprise UI component library creation, real-time application development, progressive web application implementation, Angular migration strategies, performance optimization and tuning, Angular Universal server-side rendering, micro-frontend architecture with Angular Elements
**♾️ TAGS ---** Angular, TypeScript, RxJS, NgRx, reactive-programming, enterprise-applications, standalone-components, Signals-API, dependency-injection, reactive-forms, Angular-Material, PrimeNG, Angular-CLI, performance-optimization, testing, Jasmine, Karma, lazy-loading, change-detection, Angular-Universal, micro-frontends, progressive-web-apps
**♾️ CONNECTIONS ---** @backend.api [optional], @service.auth [optional,seq:2], @docs.specialist [optional,seq:3]

---

### **@frontend.react** `1,889 lines`

**♾️ ROLE ---** React ecosystem architect specializing in modern JavaScript applications and component-based architectures
**♾️ TECH STACK ---** React framework (React 18+ with concurrent features, Suspense, Server Components, hooks system, custom hooks development), Next.js full-stack (App Router, Server Actions, middleware, API routes, static generation, incremental static regeneration, edge runtime), TypeScript integration (strict typing, component props, generic components, utility types, React TypeScript patterns), state management (Zustand lightweight state, Redux Toolkit modern Redux, React Query/TanStack Query server state, Context API patterns, React Hook Form), UI libraries (Material-UI/MUI components, Chakra UI modular design, shadcn/ui headless components, Mantine hooks and components, React Spring animations), styling solutions (Styled Components CSS-in-JS, Emotion styled system, Tailwind CSS utility-first, CSS Modules scoped styling), build optimization (Vite fast bundler, Webpack configuration, SWC compilation, tree shaking, code splitting, bundle analysis), testing ecosystem (React Testing Library, Jest unit testing, Storybook component documentation, Playwright e2e testing, MSW API mocking), performance optimization (React.memo, useMemo, useCallback, lazy loading, React DevTools profiler)
**♾️ SCENARIOS ---** Single-page application development, Next.js full-stack web applications, component library creation and maintenance, modern web application architecture, server-side rendering implementation, progressive web application development, React migration strategies, performance optimization and profiling, responsive design system implementation, real-time application development, micro-frontend architecture, e-commerce platform development
**♾️ TAGS ---** React, Next.js, TypeScript, hooks, JSX, components, state-management, Zustand, React-Query, Material-UI, Chakra-UI, shadcn-ui, SSR, SPA, modern-JavaScript, performance-optimization, Server-Components, concurrent-features, build-tools, Vite, Webpack, testing, Storybook, progressive-web-apps
**♾️ CONNECTIONS ---** @backend.api [optional], @service.auth [optional,seq:2], @docs.specialist [optional,seq:3]

---

### **@frontend.vue** `1,885 lines`

**♾️ ROLE ---** Vue.js ecosystem architect specializing in progressive framework development and reactive web applications
**♾️ TECH STACK ---** Vue framework (Vue 3+ with Composition API, Options API patterns, reactive system, computed properties, watchers, lifecycle hooks, template syntax, directives), Nuxt.js full-stack (Nuxt 3 with auto-imports, server-side rendering, static site generation, middleware, plugins, modules, universal rendering), TypeScript integration (Vue 3 TypeScript support, component props typing, composables typing, reactive refs typing), state management (Pinia stores with composition API, Vuex legacy support, global state patterns, store modules, state persistence), UI frameworks (Vuetify Material Design, Quasar components, PrimeVue enterprise widgets, Naive UI lightweight components, Vue transitions and animations), routing system (Vue Router 4, nested routes, route guards, dynamic routing, programmatic navigation, route transitions), build tooling (Vite HMR development, Vue CLI project scaffolding, build optimization, bundle analysis, tree shaking), testing ecosystem (Vue Test Utils, Vitest unit testing, Cypress component testing, Jest integration, testing composables), Single File Components (SFC structure, scoped styling, CSS modules, preprocessors, custom blocks)
**♾️ SCENARIOS ---** Progressive web application development, rapid prototyping and MVP development, developer-friendly project implementation, Vue.js application architecture, gradual framework adoption, reactive application development, component-based architecture design, modern build tool integration, Vue 2 to Vue 3 migration, enterprise Vue application development, server-side rendering with Nuxt.js, SPA to universal application conversion
**♾️ TAGS ---** Vue, Nuxt.js, Composition-API, Pinia, Vuetify, Vue-Router, Vite, reactive, SFC, progressive, TypeScript, rapid-prototyping, developer-friendly, universal-rendering, server-side-rendering, component-based, build-optimization, Vue-Test-Utils, Vitest, modern-JavaScript, state-management, routing
**♾️ CONNECTIONS ---** @backend.api [optional], @service.auth [optional,seq:2], @docs.specialist [optional,seq:3]

---

### **@frontend.mobile** `693 lines`

**♾️ ROLE ---** Cross-platform mobile development architect specializing in React Native and Flutter applications with enterprise deployment
**♾️ TECH STACK ---** React Native ecosystem (React Native New Architecture with Fabric renderer, TurboModules native bridging, Hermes JavaScript engine, Metro bundler, React Navigation routing), Flutter development (Flutter 3.24+ with null safety, Dart language, Flutter widgets, state management with Bloc/Provider/Riverpod, custom animations, platform channels), Expo platform (Expo SDK 52+ with EAS Build, EAS Submit, EAS Update over-the-air, Expo Application Services, custom development builds, bare workflow), Capacitor integration (Capacitor 7+ with native plugin system, web-to-native bridging, iOS/Android native features, Progressive Web App compatibility), app store deployment (iOS App Store Connect, Google Play Console, app signing, metadata management, release management, TestFlight beta testing), mobile CI/CD (Fastlane automation, EAS Build cloud builds, GitHub Actions mobile workflows, automated testing, code signing, deployment pipelines), performance optimization (bundle size optimization, memory management, battery optimization, native performance profiling, crash reporting with Sentry/Bugsnag)
**♾️ SCENARIOS ---** Cross-platform mobile application development, React Native enterprise app creation, Flutter application architecture, hybrid mobile app development with Capacitor, app store publishing and deployment, mobile CI/CD pipeline setup, native module integration and bridging, mobile performance optimization, offline-first mobile application development, push notification implementation, deep linking and navigation, mobile authentication integration
**♾️ TAGS ---** React-Native, Flutter, mobile, cross-platform, iOS, Android, Expo, Capacitor, native-modules, app-store, EAS, mobile-CI-CD, push-notifications, deep-linking, mobile-performance, Fastlane, Hermes, TurboModules, Fabric-renderer, native-bridging, deployment-automation, app-store-publishing, mobile-architecture
**♾️ CONNECTIONS ---** @backend.api [optional], @service.auth [optional], @service.communication [optional,seq:2], @ops.cicd [optional,seq:3]

---

# 💻 Software Development (Backend)

### **@backend.laravel** `1,634 lines`

**♾️ ROLE ---** Laravel framework architect specializing in PHP ecosystem development and rapid web application deployment
**♾️ TECH STACK ---** Laravel framework (Laravel 11+ with Artisan CLI, Eloquent ORM advanced relationships, Laravel Sanctum authentication, Laravel Passport OAuth2, Laravel Nova admin panel), PHP ecosystem (PHP 8.3+ with type declarations, enums, readonly properties, match expressions, fibers, JIT compilation), real-time features (Laravel Livewire reactive components, Inertia.js SPA adapter, Laravel Echo WebSocket broadcasting, Pusher integration, Redis pub/sub), background processing (Laravel Horizon queue management, job batching, queue workers, failed job handling, job chaining, scheduled tasks), caching strategies (Redis caching, file caching, database caching, cache tagging, cache locks), middleware system (custom middleware, rate limiting, CORS handling, authentication middleware), service architecture (service providers, dependency injection, facades, contracts, repository patterns), testing ecosystem (PHPUnit testing, Laravel Dusk browser testing, database factories, model factories, feature testing)
**♾️ SCENARIOS ---** Rapid web application development, MVC architecture implementation, PHP-based enterprise applications, admin panel and dashboard creation, Laravel application architecture, Eloquent ORM complex query optimization, queue processing and background job management, real-time feature implementation with Livewire, enterprise PHP development patterns, Laravel API development, e-commerce platform development
**♾️ TAGS ---** Laravel, PHP, Eloquent, ORM, Livewire, Inertia.js, Horizon, Telescope, Artisan, queue, broadcasting, middleware, Blade, Sanctum, Passport, MVC, real-time, background-processing, service-providers, dependency-injection, caching, testing, PHPUnit, enterprise-PHP, rapid-development
**♾️ CONNECTIONS ---** @database.postgres [optional], @database.redis [optional], @frontend.vue [optional,seq:2], @service.auth [optional,seq:3]

---

### **@backend.nodejs** `3,975 lines`

**♾️ ROLE ---** Node.js runtime architect specializing in JavaScript backend systems and event-driven architectures
**♾️ TECH STACK ---** Node.js runtime (Node.js 20+ with V8 engine, ES modules, worker threads, cluster mode, async hooks, performance hooks), framework ecosystem (Express.js lightweight framework, NestJS enterprise architecture, Fastify high-performance server, Koa.js async middleware), TypeScript integration (strict typing, decorators, generic constraints, module resolution, build optimization with swc/esbuild), database integration (Prisma modern ORM, TypeORM enterprise patterns, Mongoose ODM, native database drivers), real-time features (Socket.io WebSocket server, WebRTC implementations, Server-Sent Events, real-time pub/sub patterns), microservices architecture (service discovery, circuit breakers, distributed tracing, event sourcing, CQRS patterns, message queues), API development (REST API design, GraphQL with Apollo Server, gRPC services, API versioning, rate limiting, OpenAPI documentation), performance optimization (memory profiling, CPU optimization, clustering, load balancing, caching strategies, connection pooling), testing ecosystem (Jest unit testing, Supertest API testing, test-driven development, mocking strategies, integration testing)
**♾️ SCENARIOS ---** Node.js backend application development, real-time application implementation, JavaScript-based microservices architecture, REST and GraphQL API development, WebSocket application creation, event-driven system design, TypeScript backend development, high-performance server implementation, enterprise Node.js application architecture, streaming and real-time data processing, serverless function development
**♾️ TAGS ---** Node.js, Express, NestJS, TypeScript, Fastify, Prisma, Socket.io, microservices, REST-API, GraphQL, WebSocket, real-time, async, event-driven, JavaScript-backend, performance-optimization, clustering, testing, Jest, enterprise-architecture, streaming, serverless
**♾️ CONNECTIONS ---** @database.postgres [optional], @database.mongodb [optional], @database.redis [optional], @frontend.react [optional,seq:2], @service.auth [optional,seq:3]

---

### **@backend.python** `3,274 lines`

**♾️ ROLE ---** Python ecosystem architect specializing in data-heavy applications and machine learning backend integration
**♾️ TECH STACK ---** Python runtime (Python 3.11+ with type hints, async/await, context managers, dataclasses, pattern matching, performance optimizations), web frameworks (Django full-stack with Django REST Framework, FastAPI high-performance async, Flask microframework, Starlette ASGI foundation), ORM and database (SQLAlchemy advanced ORM, Django ORM, Alembic migrations, asyncpg PostgreSQL driver, aiomysql MySQL driver, motor MongoDB async), async programming (asyncio event loop, aiohttp async HTTP, async database drivers, concurrent programming, async context managers), background processing (Celery distributed task queue, RQ Redis queue, APScheduler job scheduling, asyncio task management), data processing (pandas data analysis, NumPy numerical computing, scikit-learn machine learning, TensorFlow/PyTorch integration), API development (Pydantic data validation, OpenAPI documentation, FastAPI automatic docs, serialization patterns, middleware architecture), testing ecosystem (pytest testing framework, asyncio testing, mocking with unittest.mock, test-driven development, coverage analysis)
**♾️ SCENARIOS ---** Data-heavy application development, machine learning backend integration, rapid web application development, scientific computing applications, async REST API development, data processing pipeline creation, machine learning model serving, Django enterprise application development, FastAPI microservice architecture, data analysis and visualization backends, ETL pipeline implementation
**♾️ TAGS ---** Python, Django, FastAPI, Flask, SQLAlchemy, Celery, asyncio, data-processing, ML-integration, Pydantic, REST-API, async, scientific-computing, pandas, NumPy, pytest, background-processing, data-analysis, machine-learning, enterprise-Python, microservices, ASGI, performance-optimization
**♾️ CONNECTIONS ---** @database.postgres [optional], @database.redis [optional], @service.ai [optional], @database.pgvector [optional,seq:2], @service.data [optional,seq:3]

---

### **@backend.go** `1,967 lines`

**♾️ ROLE ---** Go language architect specializing in high-performance systems and concurrent programming patterns
**♾️ TECH STACK ---** Go runtime (Go 1.25+ with generics, fuzzing, workspaces, embedded files, performance optimizations), web frameworks (Gin HTTP framework, Echo high-performance web framework, Fiber Express-inspired framework, Gorilla toolkit), concurrency systems (goroutines lightweight threads, channels communication primitives, context package for cancellation, select statements, mutex synchronization, atomic operations), gRPC services (Protocol Buffers serialization, gRPC-Go implementation, streaming RPC, service discovery, load balancing, interceptors), networking (HTTP/2 support, WebSocket implementations, TCP/UDP programming, custom protocols), performance optimization (memory management, garbage collector tuning, profiling with pprof, benchmarking, CPU optimization), database integration (GORM ORM, raw SQL drivers, connection pooling, prepared statements, database/sql interface), testing ecosystem (built-in testing package, table-driven tests, benchmarking, race detection, fuzzing, mocking)
**♾️ SCENARIOS ---** High-performance API development, microservices architecture implementation, system programming and tooling, concurrent processing applications, gRPC service development, high-throughput system design, concurrent application architecture, Go backend service development, network programming, real-time system implementation, CLI tool development, performance-critical backend systems
**♾️ TAGS ---** Go, Golang, Gin, Echo, Fiber, gRPC, goroutines, channels, concurrency, high-performance, microservices, protocol-buffers, system-programming, performance-optimization, networking, HTTP-2, WebSocket, testing, benchmarking, memory-management, concurrent-processing, real-time-systems
**♾️ CONNECTIONS ---** @database.postgres [optional], @database.redis [optional], @backend.api [optional,seq:2], @ops.monitoring [optional,seq:3]

---

### **@backend.java** `1,518 lines`

**♾️ ROLE ---** Java enterprise architect specializing in Spring ecosystem and large-scale system modernization
**♾️ TECH STACK ---** Java platform (Java 21 LTS with virtual threads, pattern matching, records, sealed classes, text blocks, performance improvements), Spring ecosystem (Spring Boot 3.x auto-configuration, Spring Cloud microservices, Spring Security OAuth2/JWT, Spring Data repositories, Spring WebFlux reactive programming), persistence layer (Hibernate ORM advanced mappings, JPA entity relationships, Spring Data JPA repositories, database migrations with Flyway/Liquibase), build systems (Maven multi-module projects, Gradle build automation, dependency management, plugin ecosystems), microservices architecture (Spring Cloud Gateway, service discovery with Eureka/Consul, circuit breakers with Hystrix/Resilience4j, distributed configuration), containerization (Docker containerization, Kubernetes deployment, Helm charts, Spring Boot actuator health checks), enterprise integration (Spring Integration messaging, Apache Camel routing, JMS message queues, REST template/WebClient), testing ecosystem (JUnit 5, Mockito mocking, Testcontainers integration testing, Spring Boot Test slices)
**♾️ SCENARIOS ---** Enterprise application development, large-scale system architecture, legacy system modernization, corporate environment deployment, Spring Boot application development, enterprise Java development, microservices architecture with Spring Cloud, JPA and Hibernate data layer implementation, Spring Security authentication and authorization, enterprise integration patterns
**♾️ TAGS ---** Java, Spring-Boot, Spring-Cloud, Hibernate, JPA, Maven, Gradle, enterprise, Spring-Security, Spring-Data, microservices, corporate, legacy-modernization, virtual-threads, reactive-programming, containerization, Kubernetes, enterprise-integration, testing, JUnit, Spring-Boot-Test, performance-optimization
**♾️ CONNECTIONS ---** @database.postgres [optional], @ops.containers [optional], @coordinator.migration [optional,seq:2], @ops.monitoring [optional,seq:3]

---

### **@backend.rust** `1,754 lines`

**♾️ ROLE ---** Rust systems programming architect specializing in memory-safe performance-critical applications
**♾️ TECH STACK ---** Rust language (Rust 1.89+ with ownership system, borrowing, lifetimes, pattern matching, trait system, macro system, zero-cost abstractions), web frameworks (Axum modern async framework, Actix-web actor-based framework, Rocket type-safe framework, Warp functional framework), async runtime (Tokio async runtime, async/await syntax, futures, streams, async traits, parallel processing), WebAssembly (WASM compilation targets, wasm-bindgen JavaScript bindings, web-sys DOM bindings, wasm-pack build tool), serialization (Serde serialization framework, JSON/YAML/TOML support, custom derive macros), database integration (Diesel ORM type-safe queries, SQLx async database driver, database connection pooling, migrations), memory management (ownership rules, smart pointers, reference counting, memory safety guarantees), performance optimization (zero-cost abstractions, LLVM optimizations, profiling tools, benchmark frameworks), error handling (Result type, Option type, custom error types, error propagation with ? operator), testing ecosystem (built-in unit testing, integration tests, property-based testing with proptest, mocking frameworks)
**♾️ SCENARIOS ---** System-level programming and tooling, performance-critical application development, WebAssembly module creation, safe concurrent system design, high-performance backend service development, memory-safe system programming, Rust web service architecture, async application development, CLI tool and utility development, embedded systems programming, blockchain and cryptocurrency applications
**♾️ TAGS ---** Rust, Actix-web, Rocket, Axum, Tokio, WebAssembly, WASM, async, memory-safety, performance, zero-cost-abstractions, safe-concurrency, systems-programming, ownership, borrowing, lifetimes, Serde, Diesel, SQLx, error-handling, testing, benchmarking, CLI-tools, embedded-systems
**♾️ CONNECTIONS ---** @database.postgres [optional], @ops.monitoring [optional,seq:2], @ops.performance [optional,seq:3]

---

### **@backend.api** `1,188 lines`

**♾️ ROLE ---** API design and integration architect specializing in comprehensive API lifecycle management and governance
**♾️ TECH STACK ---** API protocols (REST architectural principles, GraphQL schema design and federation, WebSocket real-time communication, gRPC high-performance RPC, OpenAPI/Swagger 3.0 specifications), API gateways (Kong API management, AWS API Gateway, Azure API Management, Google Cloud Endpoints, Zuul proxy, Ambassador edge stack), authentication systems (OAuth 2.0/2.1, JWT token management, API key authentication, mTLS mutual authentication, SAML integration), rate limiting (token bucket algorithms, sliding window, distributed rate limiting, quota management, throttling strategies), API versioning (semantic versioning, backward compatibility, deprecation strategies, migration planning, header-based versioning, URI versioning), monitoring and analytics (API metrics, latency tracking, error rate monitoring, usage analytics, performance monitoring, distributed tracing), security patterns (API security best practices, CORS handling, input validation, output sanitization, SQL injection prevention, XSS protection), testing frameworks (API testing automation, contract testing with Pact, load testing with JMeter/K6, integration testing, mock services)
**♾️ SCENARIOS ---** API-first development strategy implementation, GraphQL schema design and federation, API governance and standards establishment, REST API design and documentation, API security implementation, versioning strategy development, integration architecture planning, API gateway configuration and management, microservices API orchestration, third-party API integration, API testing automation, API performance optimization
**♾️ TAGS ---** API, REST, GraphQL, WebSocket, gRPC, OpenAPI, Swagger, API-gateway, rate-limiting, versioning, authentication, integration, API-design, API-security, OAuth, JWT, API-testing, contract-testing, API-governance, microservices-integration, performance-monitoring, distributed-tracing
**♾️ CONNECTIONS ---** @backend.nodejs [optional], @backend.python [optional], @backend.go [optional], @service.auth [optional,seq:2], @docs.specialist [optional,seq:3]

---

### **@backend.serverless** `1,173 lines`

**♾️ ROLE ---** Serverless architecture specialist focusing on Function-as-a-Service and edge computing implementations
**♾️ TECH STACK ---** Cloud functions (AWS Lambda with custom runtimes, Vercel Functions edge runtime, Netlify Functions JAMstack integration, CloudFlare Workers V8 isolates), edge computing (CloudFlare Workers KV storage, Vercel Edge Functions, AWS Lambda@Edge, Fastly Compute@Edge), serverless frameworks (Serverless Framework infrastructure, AWS SAM serverless applications, Terraform serverless modules, Pulumi cloud programming), FaaS patterns (function composition, event-driven architecture, choreography patterns, saga patterns, function orchestration), cold start optimization (provisioned concurrency, connection pooling, shared resources, initialization optimization, runtime selection), event-driven systems (AWS EventBridge, Google Cloud Pub/Sub, Azure Service Bus, SQS/SNS integration, event sourcing patterns), API integration (API Gateway configuration, HTTP API optimization, custom authorizers, request/response transformations), monitoring solutions (AWS X-Ray tracing, CloudWatch monitoring, application insights, distributed tracing, function metrics), deployment strategies (blue-green deployments, canary releases, infrastructure as code, CI/CD pipelines, environment management)
**♾️ SCENARIOS ---** Serverless architecture design and implementation, edge computing solution development, event-driven function orchestration, cost-optimized backend development, Function-as-a-Service development, edge function implementation, serverless API development, event-driven processing systems, microservices with serverless functions, JAMstack backend implementation, serverless data processing pipelines
**♾️ TAGS ---** serverless, AWS-Lambda, Vercel-Functions, Netlify-Functions, CloudFlare-Workers, FaaS, edge-computing, event-driven, cold-start, API-Gateway, cost-optimized, serverless-framework, edge-runtime, function-orchestration, JAMstack, microservices, event-sourcing, distributed-tracing, infrastructure-as-code
**♾️ CONNECTIONS ---** @database.sqlite [optional], @coordinator.infrastructure [optional], @ops.monitoring [optional,seq:2]

---

# 🧩 Service Integration Specialists

### **@service.ai** `4,565 lines`

**♾️ ROLE ---** AI/ML integration architect specializing in advanced model deployment and agent orchestration systems
**♾️ TECH STACK ---** Agent frameworks (LangGraph state machine orchestration, CrewAI multi-agent coordination, AutoGen conversational agents, LangChain workflow automation), advanced RAG systems (Agentic RAG with tool calling, HyDE hypothetical document embeddings, multi-query RAG, contextual compression, parent document retrieval), vector databases (Qdrant high-performance search, Milvus distributed vector database, pgvector PostgreSQL extension, FAISS similarity search, Weaviate knowledge graphs), model fine-tuning (PEFT parameter-efficient fine-tuning, LoRA low-rank adaptation, QLoRA quantized LoRA, DPO direct preference optimization, RLHF reinforcement learning), cutting-edge models (DeepSeek-V3 reasoning, Llama 3.3 instruction following, Mistral Large 2 multilingual, Qwen 2.5 coding, Claude-3.5 Sonnet reasoning), production deployment (vLLM high-throughput serving, TGI text generation inference, Ollama local deployment, Ray Serve distributed serving, TensorRT optimization), observability (LangSmith tracing, Weights & Biases experiment tracking, MLflow model registry, Prometheus metrics, distributed tracing), API integration (OpenAI GPT API, Anthropic Claude API, Hugging Face Inference API, Azure OpenAI, Google Vertex AI)
**♾️ SCENARIOS ---** AI feature integration and architecture, chatbot and conversational AI development, content generation system implementation, ML model deployment and serving, prompt optimization and engineering, advanced RAG system architecture, vector search implementation, multi-agent system orchestration, AI-powered application development, machine learning pipeline creation, model fine-tuning and customization, AI system observability and monitoring
**♾️ TAGS ---** AI, ML, LangGraph, CrewAI, AutoGen, RAG, vector-databases, fine-tuning, OpenAI, Hugging-Face, embeddings, chatbot, content-generation, model-deployment, prompt-engineering, agent-orchestration, multi-agent-systems, PEFT, LoRA, QLoRA, vLLM, TGI, Ollama, LangSmith, observability, production-AI
**♾️ CONNECTIONS ---** @database.vectorial [required], @database.pgvector [optional], @backend.python [required,seq:2], @service.data [optional,seq:3]

---

### **@service.auth** `2,587 lines`

**♾️ ROLE ---** Authentication and authorization architect specializing in enterprise identity management and secure access control
**♾️ TECH STACK ---** OAuth protocols (OAuth 2.0/2.1 with PKCE, authorization code flow, client credentials flow, device code flow, refresh token rotation), JWT management (JWT token creation and validation, JWE encryption, JWS signing, token refresh strategies, blacklisting mechanisms), SSO implementations (SAML 2.0 identity federation, OIDC OpenID Connect flows, Auth0 universal login, Okta identity management, Azure AD B2C, Google Identity Platform), multi-factor authentication (TOTP time-based codes, SMS verification, push notifications, WebAuthn biometric authentication, FIDO2 security keys, backup codes), RBAC systems (role-based access control, permission hierarchies, dynamic permissions, resource-based access control, attribute-based access control), identity providers (Firebase Authentication, AWS Cognito, Auth0 platform, Passport.js strategies, custom identity solutions), session management (secure session storage, session invalidation, concurrent session handling, session timeout policies), security patterns (password hashing with bcrypt/Argon2, rate limiting, brute force protection, CSRF protection, secure cookie handling, password policy enforcement)
**♾️ SCENARIOS ---** User authentication system implementation, OAuth flow development, SSO integration with enterprise systems, JWT token management architecture, RBAC implementation and optimization, multi-factor authentication setup, identity provider integration, passwordless authentication development, session management optimization, authentication architecture design, secure login flow implementation, enterprise identity federation
**♾️ TAGS ---** authentication, authorization, OAuth2, JWT, SSO, SAML, OIDC, Auth0, Firebase-Auth, RBAC, MFA, WebAuthn, identity, session, token, security, login, PKCE, TOTP, FIDO2, password-hashing, rate-limiting, enterprise-identity, identity-federation, passwordless-auth
**♾️ CONNECTIONS ---** @database.postgres [optional], @backend.nodejs [optional], @backend.python [optional], @coordinator.security [optional,seq:2]

---

### **@service.communication** `2,042 lines`

**♾️ ROLE ---** Multi-channel communication architect specializing in enterprise messaging and notification orchestration
**♾️ TECH STACK ---** SMS services (Twilio Messaging Services with A2P 10DLC compliance, Programmable SMS API, WhatsApp Business API, bulk messaging, delivery tracking), email platforms (SendGrid v3 API with dynamic templates, transactional email automation, email validation API, bounce/spam handling, reputation management), push notifications (Firebase Cloud Messaging FCM v1 API, APNs Apple Push Notification service, topic-based messaging, device group messaging, notification analytics), real-time messaging (WebSocket architecture with Socket.IO, real-time chat implementation, presence detection, message acknowledgments, scalable message routing), webhook systems (webhook validation and security, retry mechanisms with exponential backoff, webhook signature verification, payload transformation), circuit breaker patterns (fault tolerance, service degradation, automatic recovery, health checks), message queuing (Redis pub/sub, RabbitMQ message routing, message persistence, delivery guarantees), compliance systems (PII detection and masking, GDPR compliance automation, data retention policies, audit logging, consent management), monitoring solutions (delivery tracking, engagement metrics, failure analysis, real-time alerting, communication analytics)
**♾️ SCENARIOS ---** Transactional email system implementation, SMS notification automation, push notification orchestration, real-time messaging system development, webhook processing and validation, multi-channel communication automation, notification system architecture, real-time chat application development, communication workflow automation, messaging compliance implementation, engagement analytics setup
**♾️ TAGS ---** communication, messaging, Twilio, SendGrid, FCM, push-notifications, SMS, email, WebSocket, Socket.IO, real-time, notifications, templates, automation, A2P-compliance, webhook-validation, circuit-breaker, message-queuing, PII-detection, GDPR-compliance, delivery-tracking, engagement-analytics
**♾️ CONNECTIONS ---** @backend.nodejs [optional], @database.redis [optional], @service.integrations [optional,seq:2], @frontend.mobile [optional,seq:3]

---

### **@service.data** `2,169 lines`

**♾️ ROLE ---** Data processing and infrastructure architect specializing in enterprise data mesh and real-time streaming systems
**♾️ TECH STACK ---** Search platforms (Elasticsearch/OpenSearch 8+ with advanced indexing, cluster management, search relevancy tuning, aggregations, percolator queries, cross-cluster search), streaming platforms (Apache Kafka 3.8+ with Kafka Streams, Kafka Connect, schema registry, exactly-once semantics, partition strategies, consumer groups), workflow orchestration (Apache Airflow 2.10+ with TaskFlow API, dynamic DAGs, enterprise deployment, XComs, task dependencies, retry strategies), message queuing (RabbitMQ 4+ with advanced clustering, high availability, federation, shovel plugins, message routing patterns), ETL/ELT pipelines (modern data pipeline architecture, change data capture CDC, real-time data synchronization, data quality validation, schema evolution), data mesh architecture (domain-oriented data ownership, data as a product, federated computational governance, self-serve data infrastructure), real-time streaming (stream processing, event sourcing, CQRS patterns, windowing operations, stateful stream processing), monitoring systems (comprehensive data observability, data lineage tracking, pipeline monitoring, data quality metrics, alerting systems)
**♾️ SCENARIOS ---** Search functionality implementation, data streaming architecture, message queuing systems, data pipeline orchestration, real-time data processing, ETL/ELT workflow development, event-driven architecture implementation, data mesh strategy execution, search infrastructure deployment, streaming analytics platform development, data quality monitoring, pipeline observability setup
**♾️ TAGS ---** data-processing, Elasticsearch, OpenSearch, Kafka, Airflow, RabbitMQ, ETL, ELT, data-pipelines, streaming, event-driven, search, data-mesh, analytics, stream-processing, data-quality, data-observability, CDC, schema-evolution, real-time-processing, workflow-orchestration
**♾️ CONNECTIONS ---** @database.postgres [optional], @database.mongodb [optional], @backend.python [optional,seq:2], @ops.monitoring [optional,seq:3]

---

### **@service.integrations** `2,905 lines`

**♾️ ROLE ---** Third-party API integration architect specializing in external service orchestration and automation workflows
**♾️ TECH STACK ---** API integration (REST API consumption, GraphQL client implementations, gRPC service communication, OpenAPI client generation, SDK integrations), rate limiting (token bucket algorithms, sliding window patterns, distributed rate limiting, quota management, backoff strategies), web automation (Playwright browser automation, Selenium WebDriver, headless browser orchestration, page scraping, form automation), data synchronization (real-time sync patterns, batch processing, change detection, conflict resolution, eventual consistency), webhook processing (webhook validation, signature verification, retry mechanisms, dead letter queues, payload transformation), service orchestration (API composition patterns, saga patterns, choreography vs orchestration, service mesh integration, distributed transactions), circuit breakers (fault tolerance patterns, health checks, automatic recovery, bulkhead isolation, timeout management), authentication flows (OAuth 2.0 client implementations, API key management, token refresh patterns, multi-provider authentication), monitoring solutions (integration health monitoring, API analytics, error tracking, performance metrics, SLA monitoring)
**♾️ SCENARIOS ---** External API consumption and integration, third-party SDK implementation, service orchestration and coordination, automation workflow development, API integration architecture, webhook handling and processing, data synchronization between systems, external service coordination, integration testing and monitoring, multi-service authentication, API gateway integration
**♾️ TAGS ---** integration, API-integration, third-party, SDK, REST-API, webhook, data-synchronization, external-services, orchestration, automation, rate-limiting, API-consumption, circuit-breaker, service-mesh, web-scraping, Playwright, Selenium, OAuth-client, service-orchestration, fault-tolerance
**♾️ CONNECTIONS ---** @service.auth [optional], @backend.nodejs [optional], @backend.python [optional], @service.communication [optional,seq:2]

---

### **@service.crypto** `1,253 lines`

**♾️ ROLE ---** Cryptocurrency and blockchain expert specializing in trading, DeFi protocols, NFT ecosystems, and Web3 security
**♾️ TECH STACK ---** Solidity ecosystem (OpenZeppelin contracts, Hardhat development, Foundry testing, Remix IDE, upgradeable proxy patterns), Rust blockchain development (Anchor Framework for Solana, Substrate for Polkadot, Near Protocol SDK, CosmWasm for Cosmos), JavaScript/TypeScript Web3 (Ethers.js v6, Web3.js, Wagmi v2, RainbowKit wallet integration, Viem type-safe client), Python crypto development (Web3.py Ethereum Python, Brownie contract testing, CCXT exchange APIs, Pandas/NumPy data analysis), DeFi platforms (Uniswap V4, Aave V3, Compound III, MakerDAO, Curve Finance, Balancer V3), Layer 2 scaling (Arbitrum, Polygon zkEVM, Optimism, zkSync Era, Starknet, Linea), on-chain analytics (Glassnode Studio, CryptoQuant, Dune Analytics, The Graph, DeFiLlama), security tools (Slither static analysis, MythX scanning, Certora formal verification, Forta monitoring), wallet integration (MetaMask SDK, WalletConnect V2, Safe SDK, Account Abstraction), cross-chain infrastructure (LayerZero, Wormhole, Axelar, Chainlink CCIP, IBC Protocol)
**♾️ SCENARIOS ---** Cryptocurrency trading with technical analysis, DeFi protocol development and deployment, smart contract security auditing, NFT marketplace development, Web3 infrastructure design, tokenomics and DAO governance, cross-chain bridge development, on-chain analytics and market intelligence, crypto wallet integration, blockchain project due diligence, MEV protection implementation, yield farming optimization
**♾️ TAGS ---** crypto, blockchain, Web3, DeFi, NFT, smart-contracts, Solidity, Ethereum, Bitcoin, Layer2, tokenomics, DAO, yield-farming, liquidity-pools, AMM, MEV, cross-chain, bridges, wallet-integration, on-chain-analytics, security-audit, formal-verification, crypto-trading, staking
**♾️ CONNECTIONS ---** @database.pgvector [optional], @service.auth [optional], @backend.nodejs [optional,seq:2], @frontend.react [optional,seq:3]

---

### **@service.mapbox** `1,020 lines`

**♾️ ROLE ---** Mapbox platform integration specialist focusing on interactive mapping and navigation services
**♾️ TECH STACK ---** Mapbox platform (Mapbox GL JS v3.0+ interactive mapping, Navigation API v2.0+ turn-by-turn directions, Mapbox Maps SDK mobile integration, Mapbox Studio custom styling), geocoding services (Search API address search, Geocoding API coordinate conversion, reverse geocoding, batch geocoding, place suggestions), routing optimization (Directions API multi-modal routing, Matrix API distance calculations, Isochrone API reachability analysis, Map Matching API GPS trace alignment, real-time traffic integration), vector tiles (Mapbox Vector Tile specification, custom tileset generation, data-driven styling, collision detection, label placement), location services (geofencing API, GPS tracking, location analytics, proximity detection, real-time position updates), custom visualizations (data visualization overlays, heatmaps, choropleth maps, 3D extrusions, custom markers and popups), enterprise features (EV routing with charging stations, real-time traffic optimization, fleet management integration, enterprise authentication, usage analytics)
**♾️ SCENARIOS ---** Interactive map implementation, location-based application development, route optimization and navigation, geofencing and proximity alerts, spatial data visualization, mapping application development, GPS tracking system integration, location intelligence analytics, navigation system development, geospatial data analysis, real-time location services, fleet management solutions
**♾️ TAGS ---** Mapbox, maps, geospatial, geocoding, routing, navigation, location-services, GPS, geofencing, spatial-analysis, vector-tiles, mapping, location-intelligence, interactive-maps, turn-by-turn-navigation, real-time-traffic, EV-routing, fleet-management, data-visualization, proximity-detection
**♾️ CONNECTIONS ---** @database.postgis [optional], @frontend.react [optional], @frontend.vue [optional], @frontend.mobile [optional,seq:2]

---

# 💼 Business Systems

### **@business.billing** `2129 lines`

**♾️ ROLE ---** Billing systems and revenue management expert specializing in enterprise-scale automated billing orchestration and revenue recognition compliance
**♾️ TECH STACK ---** Stripe Billing advanced (Billing Portal, Customer Portal, Invoice API, Tax rates, Promotion codes, billing intervals, proration calculations, usage-based billing, metered billing), Chargebee enterprise (Plans API, Addons, Coupons, billing automation, dunning management, payment retry logic, multi-gateway support, taxation engine), Zuora revenue (CPQ integration, billing automation, revenue recognition ASC 606, subscription analytics, usage aggregation, invoice customization, payment orchestration), enterprise billing platforms (Recurly subscription management, FastSpring global billing, Paddle merchant of record, 2Checkout payment processing, BlueSnap global payments), tax automation (Avalara AvaTax, TaxJar sales tax, Thomson Reuters ONESOURCE, Vertex tax technology, EU VAT compliance, GST automation), accounting integration (QuickBooks Enterprise API, Xero accounting API, NetSuite ERP integration, Sage Intacct revenue management, SAP finance integration, Oracle Financials Cloud), revenue recognition (ASC 606 automation, IFRS 15 compliance, deferred revenue management, contract modifications, performance obligations, revenue allocation, audit trail automation), dunning optimization (intelligent retry logic, payment recovery workflows, customer communication automation, grace period management, payment method updating, churn prevention)
**♾️ SCENARIOS ---** Enterprise billing system implementation and migration, automated usage-based billing with real-time metering, complex pricing model implementation with tiered and volume discounts, global tax compliance automation across multiple jurisdictions, revenue recognition compliance for ASC 606 and IFRS 15, dunning management optimization to reduce involuntary churn, multi-currency billing with automated currency conversion, accounting system integration with automated journal entries, invoice customization and branding automation, billing analytics and revenue reporting dashboards, subscription plan migration without revenue loss, payment recovery workflow optimization, contract modification revenue impact analysis
**♾️ TAGS ---** billing-automation, Stripe-Billing, Chargebee, Zuora, revenue-recognition, ASC-606, IFRS-15, usage-based-billing, metered-billing, tax-automation, Avalara, TaxJar, multi-currency, dunning-management, payment-recovery, invoice-customization, proration-calculations, accounting-integration, QuickBooks, NetSuite, billing-analytics, revenue-reporting, subscription-billing, enterprise-billing, compliance-automation, deferred-revenue, performance-obligations, billing-orchestration
**♾️ CONNECTIONS ---** @business.payment [required], @business.subscription [required,seq:2], @database.postgres [optional], @service.integrations [optional,seq:3]

---

### **@business.payment** `2761 lines`

**♾️ ROLE ---** Payment processing and financial transactions expert specializing in enterprise payment orchestration and multi-gateway fraud prevention systems
**♾️ TECH STACK ---** Stripe advanced (Payment Intents API, Setup Intents, Payment Methods, Multi-party payments, Connect platform, radar fraud detection, webhooks v2, Terminal SDK, identity verification, tax calculation), PayPal commerce (Checkout SDK, Payments API, Subscriptions API, PayPal Commerce Platform, Braintree vault, risk management, PayPal Credit, Express Checkout), enterprise gateways (Adyen unified commerce, Worldpay payment processing, Chase Payment Solutions, First Data Omni API, Authorize.Net CIM), digital wallets (Apple Pay Web, Google Pay API, Samsung Pay, PayPal wallet, Amazon Pay, Shop Pay), fraud prevention (Stripe Radar, Kount fraud protection, Sift fraud detection, Riskified guarantee, Signifyd commerce protection, machine learning risk models), compliance frameworks (PCI DSS Level 1, PCI 3DS server, Strong Customer Authentication SCA, PSD2 compliance, GDPR payment data protection, SOX financial controls), payment orchestration (routing optimization, failover strategies, transaction retry logic, gateway load balancing, cost optimization algorithms), tokenization security (network tokenization, gateway tokenization, vault management, PCI-compliant storage, token lifecycle management, provisioning automation)
**♾️ SCENARIOS ---** E-commerce payment gateway integration and optimization, multi-gateway payment orchestration with automatic failover, fraud detection and prevention system implementation, PCI DSS compliance audit and certification, digital wallet integration across web and mobile platforms, payment analytics and transaction reporting dashboards, cross-border payment processing with currency conversion, subscription payment automation with retry logic, marketplace payment splitting and escrow management, payment security hardening and penetration testing, regulatory compliance implementation for global markets, payment performance optimization and cost reduction strategies
**♾️ TAGS ---** payment-processing, Stripe, PayPal, Adyen, PCI-DSS, fraud-prevention, payment-orchestration, digital-wallets, Apple-Pay, Google-Pay, tokenization, SCA, PSD2, gateway-integration, payment-security, transaction-monitoring, payment-analytics, multi-gateway, failover-strategies, compliance-automation, cross-border-payments, marketplace-payments, payment-optimization, risk-management, webhook-processing, payment-routing, cost-optimization
**♾️ CONNECTIONS ---** @service.auth [optional], @database.postgres [required], @ops.monitoring [optional,seq:2], @audit.security [optional,seq:3]

---

### **@business.subscription** `1450 lines`

**♾️ ROLE ---** SaaS subscription and recurring revenue engineer specializing in predictive churn prevention and enterprise billing orchestration
**♾️ TECH STACK ---** Stripe advanced (subscriptions API, webhooks, usage-based billing, proration calculations, dunning management, payment method updates, billing cycles, metadata management, trial conversions, invoice customization), Kill Bill expertise (multi-tenant billing, complex billing cycles, invoice templates, payment orchestration, enterprise pricing models, revenue recognition ASC 606, audit trails, subscription lifecycle management), subscription analytics mastery (MRR/ARR tracking, cohort analysis, retention curves, LTV calculations, churn prediction ML models, customer health scoring, expansion revenue tracking, revenue forecasting), customer success automation (lifecycle triggers, intervention workflows, onboarding automation, feature adoption tracking, usage monitoring, at-risk customer identification), enterprise compliance (revenue recognition ASC 606, tax compliance automation, GDPR privacy controls, SOC 2 audit trails, financial reporting, multi-currency support), predictive modeling (churn prediction algorithms, LTV optimization, pricing elasticity analysis, cohort retention modeling, revenue forecasting, customer segmentation)
**♾️ SCENARIOS ---** SaaS subscription system implementation, usage-based billing with real-time metering, churn prediction and prevention automation, enterprise subscription onboarding workflows, multi-platform billing integration (Stripe + Kill Bill), revenue recognition compliance implementation, customer lifecycle automation, subscription analytics dashboards, predictive revenue modeling, pricing optimization experiments, dunning management workflows, expansion revenue tracking systems, compliance automation (ASC 606, tax, GDPR), enterprise customer success automation
**♾️ TAGS ---** subscription, recurring-revenue, MRR, ARR, churn-prediction, LTV, customer-lifecycle, usage-based-billing, metered-pricing, retention, cohort-analysis, revenue-recognition, dunning-management, Stripe, Kill-Bill, billing-orchestration, customer-success, onboarding-automation, predictive-analytics, revenue-forecasting, pricing-optimization, expansion-revenue, compliance-automation, ASC-606, enterprise-billing, multi-tenant, subscription-analytics, health-scoring, lifecycle-triggers, intervention-workflows
**♾️ CONNECTIONS ---** @business.payment [required], @business.billing [required,seq:2], @database.postgres [required], @service.integrations [optional], @frontend.react [optional,seq:3]

---

# 📝 Documentation

### **@docs.specialist** `539 lines`

**♾️ ROLE ---** Comprehensive documentation architecture and technical writing expert
**♾️ TECH STACK ---** Semantic versioning, changelog generation, technical writing, API documentation, markdown mastery, GitHub repository files (README.md, CONTRIBUTING.md, LICENSE, CODE_OF_CONDUCT.md), OpenAPI/Swagger, Mermaid diagrams, .github templates, community health files, shields.io badges, accessibility compliance, documentation automation, quality metrics, multi-platform publishing, Keep a Changelog format, GitHub Flavored Markdown (GFM), WCAG compliance, conventional commits
**♾️ SCENARIOS ---** Documentation creation/updates, changelog management, version management, API documentation, README optimization, GitHub repository setup, community health files, issue/PR templates, CONTRIBUTING guidelines, LICENSE files, technical guides, documentation quality audits, release notes, migration guides, architecture documentation, cross-reference management
**♾️ TAGS ---** documentation, changelog, versioning, semantic, markdown, README, API-docs, OpenAPI, Swagger, GitHub, templates, LICENSE, CONTRIBUTING, CODE-OF-CONDUCT, badges, shields, Mermaid, diagrams, technical-writing, migration-guides, release-notes, community, accessibility, WCAG
**♾️ CONNECTIONS ---** @backend.api [optional], @frontend.react [optional], @frontend.vue [optional], @frontend.angular [optional], @ops.git [optional,seq:2], @service.integrations [optional,seq:3]

---

# 📊 Analysis and Strategy

### **@analyst.strategic** `1171 lines`

**♾️ ROLE ---** Business and technical strategy analysis expert
**♾️ TECH STACK ---** Requirements analysis, roadmap planning, stakeholder analysis, competitive analysis, market research tools, OKR framework, SWOT analysis, Porter's Five Forces, Evidence BI platform, modern 2025 strategic frameworks, business model canvas, technology assessment, ROI analysis, feasibility studies
**♾️ SCENARIOS ---** Strategic planning, business requirements, technology selection, project roadmaps, feasibility studies, competitive intelligence, ROI analysis, stakeholder management, business strategy, technology strategy, market analysis, strategic decision making
**♾️ TAGS ---** strategy, strategic-planning, OKR, SWOT, Porters-Five-Forces, business-requirements, roadmap, feasibility, competitive-analysis, ROI, stakeholder, business-model, technology-assessment
**♾️ CONNECTIONS ---** @coordinator.backend [optional], @coordinator.database [optional], @coordinator.infrastructure [optional], @business.billing [optional,seq:2]

---

### **@analyst.data** `502 lines`

**♾️ ROLE ---** Data science and analytics expert
**♾️ TECH STACK ---** Python (pandas, numpy, scipy, matplotlib, seaborn), R (ggplot2, dplyr, tidyverse), Jupyter Notebooks, statistical analysis, hypothesis testing, A/B testing, predictive modeling, Tableau, Power BI, data visualization, KPI frameworks, user research methodologies
**♾️ SCENARIOS ---** Statistical analysis, KPIs definition, user research, predictive analytics, business intelligence dashboards, risk assessment, hypothesis testing, A/B testing design, data visualization, exploratory data analysis, statistical modeling
**♾️ TAGS ---** statistics, statistical-analysis, hypothesis-testing, A-B-testing, KPIs, data-visualization, user-research, predictive-modeling, business-intelligence, exploratory-analysis, statistical-modeling
**♾️ CONNECTIONS ---** @database.postgres [optional], @database.mariadb [optional], @database.mongodb [optional], @analyst.strategic [optional,seq:2], @service.data [optional,seq:3]

---

# 🔍 Audit and Compliance

### **@audit.compliance** `1429 lines`

**♾️ ROLE ---** Regulatory compliance and accessibility expert specializing in GDPR data protection, WCAG accessibility standards, cost optimization analysis, and privacy compliance frameworks
**♾️ TECH STACK ---** GDPR compliance tools, OneTrust Privacy Management, WCAG 2.2 AA testing automation, axe-core, Pa11y, WAVE accessibility evaluator, Lighthouse audits, SOC 2 compliance frameworks, privacy impact assessment tools, cost optimization analysis, regulatory change monitoring, automated compliance scanning
**♾️ SCENARIOS ---** GDPR privacy compliance, WCAG accessibility audits, privacy impact assessments, regulatory compliance analysis, cost-benefit compliance analysis, accessibility barrier identification, compliance monitoring automation, regulatory framework mapping
**♾️ TAGS ---** GDPR, WCAG, accessibility, compliance, privacy, audit, regulation, PIA, DPIA, SOC-2, cost-optimization, monitoring, automation, barriers, remediation
**♾️ CONNECTIONS ---** @audit.security [optional], @service.auth [optional], @coordinator.security [optional,seq:2], @frontend.react [optional,seq:3]

---

### **@audit.security** `1200 lines`

**♾️ ROLE ---** Expert security vulnerability assessment specialist with deep expertise in penetration testing, OWASP methodologies, and comprehensive security audits
**♾️ TECH STACK ---** OWASP Top 10, OWASP ZAP, OWASP Nettacker, Burp Suite Professional, Nessus, OpenVAS, Qualys VMDR, penetration testing frameworks, vulnerability scanners, CVSS 3.1 scoring, security compliance validation, threat modeling, automated security testing
**♾️ SCENARIOS ---** Penetration testing, vulnerability assessments, security audits, OWASP compliance validation, threat modeling, security risk assessment, vulnerability scanning automation, security compliance verification
**♾️ TAGS ---** OWASP, penetration-testing, vulnerability, security-audit, Burp-Suite, Nessus, OpenVAS, CVSS, threat-modeling, security-scanning, risk-assessment, compliance
**♾️ CONNECTIONS ---** @audit.compliance [optional], @coordinator.security [optional], @service.auth [optional,seq:2], @ops.monitoring [optional,seq:3]

---

# ⚙️ Operations and DevOps

### **@ops.git** `1317 lines`

**♾️ ROLE ---** Git workflow and version control expert specializing in professional branching strategies and conventional commit mastery
**♾️ TECH STACK ---** Git advanced (branching strategies, conventional commits, semantic versioning, git hooks, submodules, LFS, merge strategies, conflict resolution, rebase workflows, cherry-picking, bisect debugging), GitHub Actions (CI/CD workflows, automated testing, release automation, pull request automation), repository management (code review workflows, branch protection rules, CODEOWNERS files, issue templates, pull request templates), release management (semantic versioning, changelog generation, tag management, GitHub releases, automated versioning), workflow optimization (commit message standards, merge vs rebase strategies, feature branch patterns, hotfix workflows)
**♾️ SCENARIOS ---** Repository setup and organization, branching strategy implementation, conventional commit workflow establishment, automated versioning and changelog generation, code review process optimization, release management automation, conflict resolution training, Git workflow consulting, repository migration planning, team collaboration enhancement
**♾️ TAGS ---** Git, version-control, branching-strategies, conventional-commits, semantic-versioning, GitHub-Actions, merge-strategies, conflict-resolution, rebase, cherry-pick, bisect, release-management, code-review, pull-request, repository-management, workflow-automation, team-collaboration, changelog-generation, tag-management, CI-CD-integration
**♾️ CONNECTIONS ---** @docs.specialist [optional], @coordinator.devops [optional,seq:2], @ops.cicd [optional,seq:3]

---

### **@ops.monitoring** `3,294 lines`

**♾️ ROLE ---** Production-grade monitoring and observability expert specializing in enterprise Prometheus clusters, Grafana dashboard architecture, ELK stack optimization, and APM tool mastery
**♾️ TECH STACK ---** Enterprise Prometheus federations (high-availability clusters, sharding, recording rules, alerting rules, service discovery, cardinality management), Grafana dashboard architecture (advanced visualizations, template variables, alert notifications, data source management, plugin ecosystem), ELK stack optimization (Elasticsearch cluster tuning, Logstash pipeline optimization, Kibana advanced queries, index lifecycle management, TB-scale log processing), APM tools mastery (DataDog infrastructure monitoring, New Relic application performance monitoring, Dynatrace AI-powered observability), OpenTelemetry distributed tracing (spans, traces, metrics, baggage propagation, instrumentation), Thanos/Cortex long-term storage (multi-cluster federation, compaction, downsampling, deduplication), intelligent alerting systems (PagerDuty integration, escalation policies, alert fatigue reduction, SLA monitoring), business metrics integration (KPI dashboards, revenue tracking, user behavior analytics), custom instrumentation (StatsD, Telegraf, custom metrics, application-specific monitoring)
**♾️ SCENARIOS ---** Production monitoring infrastructure setup, enterprise observability architecture design, Prometheus federation deployment, Grafana dashboard creation and optimization, ELK cluster deployment and tuning, APM tool configuration and integration, distributed tracing implementation, alerting strategy development, metrics collection and analysis, log aggregation and analysis, performance monitoring optimization, monitoring automation, incident response integration, capacity planning, SLA monitoring implementation
**♾️ TAGS ---** Prometheus, Grafana, ELK, Elasticsearch, Logstash, Kibana, DataDog, New-Relic, Dynatrace, OpenTelemetry, monitoring, observability, alerting, metrics, logs, tracing, APM, Thanos, Cortex, federation, instrumentation, dashboards, performance-monitoring, incident-response, capacity-planning, SLA-monitoring, cardinality-management, alert-fatigue, business-metrics
**♾️ CONNECTIONS ---** @ops.containers [optional], @coordinator.infrastructure [optional], @database.postgres [optional,seq:2], @ops.performance [optional,seq:3]

---

### **@ops.containers** `1193 lines`

**♾️ ROLE ---** Container orchestration and tactical deployment expert specializing in production Kubernetes clusters and enterprise container security
**♾️ TECH STACK ---** Docker containers (multi-stage builds, security scanning, image optimization, multi-arch builds, BuildKit, container registries management), Kubernetes clusters (cluster administration, workload management, resource quotas, RBAC, networking, storage orchestration), Helm charts (templating, dependency management, lifecycle hooks, chart testing, repository management), Istio service mesh (traffic management, security policies, observability, gateway configuration, virtual services, destination rules), ingress controllers (NGINX, Traefik, HAProxy, SSL termination, path-based routing, host-based routing), Pod Security Standards (restricted, baseline, privileged policies, security contexts, admission controllers), network policies (NetworkPolicy resources, Calico, Cilium, traffic segmentation), container performance optimization (resource limits, requests, quality of service, horizontal pod autoscaling, vertical pod autoscaling), health checks (liveness probes, readiness probes, startup probes), container debugging (kubectl debugging, log analysis, resource troubleshooting, networking issues)
**♾️ SCENARIOS ---** Production Kubernetes cluster deployment, container security hardening, service mesh implementation, ingress controller setup and optimization, container registry management, Helm chart development and deployment, microservices orchestration, container performance tuning, pod autoscaling configuration, network policy implementation, container debugging and troubleshooting, multi-environment deployment strategies, blue-green deployments, canary releases, disaster recovery planning
**♾️ TAGS ---** Docker, Kubernetes, containers, pods, Helm, Istio, service-mesh, ingress, kubectl, deployment, orchestration, K8s, containerization, microservices, scaling, security-policies, networking, registry, images, RBAC, network-policies, autoscaling, health-checks, multi-arch, container-security, pod-security-standards, service-mesh-traffic-management
**♾️ CONNECTIONS ---** @coordinator.infrastructure [optional], @ops.monitoring [optional], @ops.webserver [optional,seq:2], @audit.security [optional,seq:3]

---

### **@ops.webserver** `3,058 lines`

**♾️ ROLE ---** Elite web server and reverse proxy expert specializing in enterprise-grade configurations and HTTP/3+QUIC implementations
**♾️ TECH STACK ---** Nginx advanced (HTTP/3+QUIC support, reverse proxy optimization, upstream health checks, dynamic configuration reloading, stream processing, embedded Lua scripting, rate limiting, SSL/TLS termination), Apache HTTP Server mastery (HTTP/2 with mod_http2, virtual host optimization, mod_rewrite expertise, MPM tuning, mod_ssl configuration, security modules), Caddy automation (automatic HTTPS with ACME, on-demand TLS, encrypted client hello, post-quantum cryptography, JSON configuration), HAProxy expertise (TCP/HTTP load balancing, QUIC support, advanced ACLs, stick tables, HTTP/3 termination, health checks), SSL/TLS optimization (TLS 1.3, ECDSA certificates, session resumption, OCSP stapling, perfect forward secrecy, cipher suite optimization), security architecture (CSP headers, HTTP security headers, rate limiting, DDoS mitigation, WAF integration, geo-blocking), performance tuning (connection pooling, compression algorithms, caching strategies, buffer optimization, keep-alive optimization)
**♾️ SCENARIOS ---** Enterprise web server deployment and optimization, high-availability reverse proxy configuration, HTTP/3+QUIC protocol implementation, SSL/TLS termination setup and optimization, load balancer architecture design, security hardening and compliance implementation, performance optimization and tuning, zero-downtime deployment strategies, A/B testing infrastructure setup, blue-green deployment pattern implementation, monitoring integration and health checks, CDN integration and optimization, web application firewall configuration
**♾️ TAGS ---** Nginx, Apache, Caddy, HAProxy, HTTP-3, QUIC, TLS, SSL, reverse-proxy, load-balancing, web-server, proxy, SSL-termination, performance-tuning, security-headers, rate-limiting, DDoS-protection, ACME, certificates, upstream, virtual-hosts, mod-rewrite, compression, caching, connection-pooling, zero-downtime, high-availability, enterprise-configuration, health-checks, WAF
**♾️ CONNECTIONS ---** @ops.containers [optional], @coordinator.infrastructure [optional], @ops.iac [optional], @ops.monitoring [optional], @coordinator.security [optional,seq:2]

---

### **@ops.cicd** `3391 lines`

**♾️ ROLE ---** CI/CD pipeline implementation and automation expert specializing in enterprise GitOps workflows and deployment orchestration
**♾️ TECH STACK ---** Jenkins advanced (pipeline as code, Blue Ocean, distributed builds, plugin ecosystem, pipeline optimization), GitLab CI expertise (YAML pipelines, runners, container registry, security scanning, deployment strategies), GitHub Actions mastery (workflow automation, custom actions, matrix builds, reusable workflows, secrets management), CircleCI optimization (parallelism, caching strategies, orbs, workflow orchestration), ArgoCD GitOps (application deployment, sync policies, rollback strategies, multi-cluster management), deployment automation (blue-green deployments, canary releases, rolling updates, feature flags), pipeline optimization (build caching, artifact management, parallel execution, dependency optimization), security integration (SAST, DAST, dependency scanning, container security, secrets scanning), monitoring integration (build metrics, deployment tracking, failure alerting, performance monitoring)
**♾️ SCENARIOS ---** Enterprise CI/CD pipeline design and implementation, GitOps workflow setup with ArgoCD, multi-environment deployment orchestration, security-first pipeline development, automated testing integration, container-based build systems, deployment strategy optimization, pipeline performance tuning, build artifact management, secrets and security scanning integration, monitoring and alerting setup, disaster recovery planning, rollback automation, compliance automation
**♾️ TAGS ---** Jenkins, GitLab-CI, GitHub-Actions, CircleCI, ArgoCD, CI-CD, pipeline, deployment-automation, GitOps, blue-green, canary, rolling-updates, build-optimization, security-scanning, SAST, DAST, container-builds, artifact-management, secrets-management, monitoring-integration, automation, orchestration, rollback, compliance
**♾️ CONNECTIONS ---** @ops.git [required], @ops.containers [optional], @coordinator.devops [optional,seq:2], @audit.security [optional,seq:3]

---

### **@ops.iac** `1285 lines`

**♾️ ROLE ---** Infrastructure as Code architect specializing in enterprise multi-cloud IaC governance with operational excellence
**♾️ TECH STACK ---** Terraform advanced (state management, remote backends S3+DynamoDB, workspace isolation, module architecture, dynamic blocks, for_each loops, lifecycle management, Terratest testing), Pulumi expertise (Automation API, component resources, stack management, cross-stack dependencies, policy-as-code with CrossGuard, multi-language SDKs), Ansible mastery (configuration management, playbook architecture, role-based organization, Jinja2 templating, Molecule testing, AWX/Tower integration), CloudFormation templates (nested stacks, custom resources, drift detection), Bicep deployments (ARM templates, resource loops, conditions), policy-as-code (Open Policy Agent, HashiCorp Sentinel, AWS Config Rules), multi-cloud abstraction patterns, cost optimization strategies, GitOps workflows, infrastructure drift detection, disaster recovery procedures, secret management (HashiCorp Vault, AWS Secrets Manager), security scanning (Checkov, tfsec, Bridgecrew), compliance automation (SOC2, HIPAA, PCI-DSS, CIS benchmarks)
**♾️ SCENARIOS ---** Infrastructure provisioning and automation, Terraform state management and module development, Pulumi automation API implementation, Ansible configuration management at scale, policy-as-code enforcement, compliance automation, cost optimization initiatives, GitOps workflow design, infrastructure drift remediation, disaster recovery planning, multi-cloud governance, IaC security scanning, secret management integration, operational excellence implementation
**♾️ TAGS ---** Terraform, Pulumi, Ansible, Infrastructure-as-Code, IaC, state-management, automation-API, configuration-management, policy-as-code, multi-cloud, compliance-automation, cost-optimization, GitOps, infrastructure-drift, disaster-recovery, secret-management, security-scanning, operational-excellence, CloudFormation, Bicep, Terratest, Molecule, Vault, Checkov, tfsec, remote-state, workspace-isolation, module-architecture, stack-management, playbook-architecture, role-organization, compliance-frameworks
**♾️ CONNECTIONS ---** @coordinator.infrastructure [optional], @backend.serverless [optional], @ops.containers [optional], @ops.monitoring [optional,seq:2], @coordinator.security [optional,seq:2]

---

### **@ops.troubleshooting** `893 lines`

**♾️ ROLE ---** System debugging and incident resolution expert specializing in production environment troubleshooting, systematic root cause analysis, performance profiling, and emergency response procedures for enterprise systems
**♾️ TECH STACK ---** Debugging methodologies (systematic root cause analysis, incident response protocols, diagnostic workflows, emergency response procedures), performance profiling (application profiling, system monitoring, bottleneck identification, resource analysis), troubleshooting tools (log analysis, error tracking systems, monitoring dashboards, diagnostic utilities), incident management (incident classification, escalation procedures, post-incident analysis, prevention strategies)
**♾️ SCENARIOS ---** Production system failures and debugging, performance bottleneck investigation and resolution, incident response and emergency troubleshooting, systematic root cause analysis for complex issues, post-incident analysis and prevention strategy development, enterprise troubleshooting workflow implementation
**♾️ TAGS ---** troubleshooting, debugging, incident-response, root-cause-analysis, performance-profiling, system-monitoring, emergency-response, production-issues, diagnostic-analysis, incident-management
**♾️ CONNECTIONS ---** @ops.monitoring [required for system metrics], @ops.performance [optional for performance analysis], @coordinator.infrastructure [optional for system architecture], @ops.containers [optional for containerized environments]

---

### **@ops.performance** `368 lines`

**♾️ ROLE ---** Strategic performance consultant specializing in capacity planning, performance architecture guidance, and optimization roadmaps for enterprise-scale systems
**♾️ TECH STACK ---** Capacity planning (traffic growth modeling, resource requirement modeling, scaling strategy design, cost-performance analysis), performance architecture strategy (application performance patterns, caching architecture design, database performance strategy, network performance optimization, monitoring strategy), load testing strategy (testing methodology design, tool selection guidance, performance budget definition, CI/CD integration strategy), performance consulting framework (assessment and analysis, optimization strategy development, priority matrix, implementation planning)
**♾️ SCENARIOS ---** Performance bottleneck identification and resolution, scalability analysis and optimization, load testing strategy implementation, capacity planning and forecasting, caching architecture design, database performance optimization, application profiling and tuning, performance monitoring setup, performance CI/CD integration, emergency performance incident response
**♾️ TAGS ---** performance-optimization, load-testing, JMeter, k6, caching-strategies, database-tuning, code-optimization, profiling, scalability, capacity-planning, performance-monitoring, bottleneck-analysis, query-optimization, memory-optimization, response-time-optimization
**♾️ CONNECTIONS ---** @ops.containers [optional], @coordinator.infrastructure [optional], @database.postgres [optional,seq:2], @ops.monitoring [optional,seq:3]

---

### **@ops.bash** `3161 lines`

**♾️ ROLE ---** Expert Bash shell scripting and automation specialist with 15+ years mastering enterprise-grade scripts, error handling, performance optimization, and bulletproof automation pipelines. Advanced debugging, security hardening, and cross-platform compatibility expert
**♾️ TECH STACK ---** Bash scripting mastery (advanced parameter expansion, process substitution, co-processes, arrays, associative arrays, parameter manipulation, string operations, arithmetic expansion), error handling frameworks (trap mechanisms, signal handling, exit codes, recovery procedures, fail-safe patterns), security architecture (credential management, input validation, sanitization, privilege escalation prevention, audit logging), performance profiling (benchmarking, memory tracking, optimization techniques, resource monitoring, bottleneck identification), cross-platform automation (Linux, macOS, Unix variants, portable scripting, environment detection), enterprise testing (mocking, assertions, test frameworks, CI/CD integration, automated testing), modular architecture (library systems, configuration management, reusable functions, plugin architectures), automation patterns (system administration, deployment scripts, monitoring automation, backup procedures, maintenance scripts)
**♾️ SCENARIOS ---** Enterprise shell script development and optimization, automation pipeline creation, system administration script development, deployment automation, monitoring script implementation, backup and maintenance automation, cross-platform script compatibility, security hardening of shell scripts, performance optimization of automation workflows, enterprise scripting standards implementation, debugging complex shell environments, legacy script modernization
**♾️ TAGS ---** bash, shell-scripting, automation, system-administration, error-handling, security-hardening, performance-optimization, cross-platform, enterprise-scripting, deployment-automation, monitoring-scripts, backup-automation, script-debugging, trap-mechanisms, signal-handling, process-management, file-operations, string-manipulation, array-handling, modular-scripting, testing-frameworks
**♾️ CONNECTIONS ---** @ops.cicd [optional for deployment automation], @ops.monitoring [optional for monitoring scripts], @coordinator.infrastructure [optional for system automation], @ops.containers [optional for containerized environments]

---

# 🧪 Testing and Quality

### **@test.quality** `3365 lines`

**♾️ ROLE ---** Comprehensive testing and quality assurance expert specializing in test automation frameworks, quality gates, performance testing, and end-to-end testing strategies. Master of Jest, Cypress, Playwright, code coverage analysis, and enterprise testing methodologies
**♾️ TECH STACK ---** Test automation frameworks (Jest unit testing, Cypress integration testing, Playwright end-to-end testing, JUnit Java testing, pytest Python testing), code coverage analysis (Istanbul JavaScript coverage, c8 V8 coverage, JaCoCo Java coverage, pytest-cov Python coverage), quality gates implementation (SonarQube integration, quality thresholds, automated quality checks), performance testing (JMeter load testing, k6 performance testing, Lighthouse web vitals), testing strategies (test pyramid implementation, TDD methodologies, BDD frameworks, mutation testing)
**♾️ SCENARIOS ---** Test automation strategy development and implementation, comprehensive quality gate setup with coverage thresholds, end-to-end testing pipeline creation, performance and load testing implementation, code coverage analysis and optimization, enterprise testing methodology design and deployment
**♾️ TAGS ---** testing-automation, quality-assurance, test-frameworks, code-coverage, Jest, Cypress, Playwright, JUnit, pytest, quality-gates, performance-testing, end-to-end-testing, TDD, BDD, test-strategy, mutation-testing
**♾️ CONNECTIONS ---** @coordinator.testing [optional for strategy coordination], @ops.cicd [optional for pipeline integration], @coordinator.devops [optional for DevOps integration], @ops.performance [optional for performance testing]

---

# 📅 Planning

### **@plan.strategy** `406 lines`

**♾️ ROLE ---** Strategic project organizer that transforms expert recommendations into structured execution plans with phased timelines, job creation, and dependency management for optimal project delivery
**♾️ TECH STACK ---** Project organization engine (phase organization strategy, job creation engine, dependency management), timeline organization (smart timeline distribution, realistic hour calculation, buffer strategy), execution best practices (dependency management, parallel execution optimization, timeline buffer strategy), output formatting (concise project plans, expansion plans, Claude presentation templates)
**♾️ SCENARIOS ---** Organizing expert recommendations into executable phases, transforming technology decisions into structured jobs, creating realistic timelines with dependency management, managing project execution phases and milestones, organizing expansion plans for existing projects, optimizing parallel development opportunities
**♾️ TAGS ---** project-organization, execution-planning, job-creation, timeline-management, dependency-management, phase-organization, execution-optimization, project-coordination, development-sequencing, milestone-planning
**♾️ CONNECTIONS ---** Receives expert recommendations from @analyst.strategic, @coordinator.backend, @coordinator.database, @coordinator.infrastructure, @security.audit, creates JOBS in SQLite database, formats output for Claude presentation
