# Claude Code Agents Catalog

## Overview
This directory contains all global agents available for Claude Code. Agents are automatically loaded and can be delegated to based on project needs. The `/setup` command will detect your tech stack and install only the relevant agents to your project.

## Agent Hierarchy

### 🎯 Level 1: Coordinators
Domain-level orchestrators that manage entire areas of development and delegate to specialized engineers.

#### backend-coordinator.md
Orchestrates all backend development tasks including API design, business logic, database interactions, and server-side architecture. Delegates to framework-specific engineers (Laravel, FastAPI, Node.js) and coordinates with database-coordinator for schema design and infrastructure-coordinator for deployment strategies. Primary point of contact for any server-side implementation.

#### frontend-coordinator.md
Manages all client-side development including UI components, state management, routing, and user interactions. Delegates to framework engineers (React, Vue, Angular) and collaborates with ui-ux-engineer for design implementation and backend-coordinator for API integration. Ensures consistent frontend architecture across the application.

#### database-coordinator.md
Oversees all database operations including schema design, query optimization, migrations, and data integrity. Delegates to specific database engineers (PostgreSQL, MySQL, Redis) and works closely with backend-coordinator for ORM configuration and migration-coordinator for database versioning strategies.

#### devops-coordinator.md
Manages CI/CD pipelines, deployment strategies, containerization, and infrastructure automation. Delegates to docker-engineer and cloud architects while coordinating with security-coordinator for compliance and testing-coordinator for automated test integration.

#### infrastructure-coordinator.md
Handles cloud architecture, server provisioning, networking, and system scalability. Works with cloud-architect for platform decisions, docker-engineer for containerization, and security-coordinator for infrastructure security. Ensures system reliability and performance at scale.

#### security-coordinator.md
Oversees application security, vulnerability assessments, compliance requirements, and security best practices. Delegates to security-auditor, gdpr-compliance-engineer, and coordinates with all other coordinators to implement security measures across the stack.

#### testing-coordinator.md
Manages testing strategy including unit tests, integration tests, E2E tests, and performance testing. Delegates to test-automation-engineer, e2e-engineer, performance-tester and ensures test coverage across all components.

#### data-coordinator.md
Orchestrates data pipelines, ETL processes, analytics, and machine learning workflows. Delegates to data-scientist, ml-engineer, and coordinates with database-coordinator for data warehouse design and backend-coordinator for data API development.

#### migration-coordinator.md
Specializes in system migrations, legacy code refactoring, database migrations, and platform transitions. Works with all coordinators to ensure smooth transitions while maintaining system stability and data integrity.

---

### 🔧 Level 2: Engineers
Technical specialists with deep expertise in specific technologies, frameworks, or domains.

## Backend Engineers

#### laravel-engineer.md
Expert in Laravel PHP framework, handles Eloquent ORM, Artisan commands, middleware, service providers, queues, and Laravel ecosystem packages. Implements RESTful APIs, authentication with Sanctum/Passport, and follows Laravel best practices. Works closely with postgres-engineer for database optimization and redis-engineer for caching strategies.

#### fastapi-engineer.md
Expert in FastAPI for high-performance Python APIs, handles async/await patterns, Pydantic models, dependency injection, and OpenAPI documentation. Implements WebSocket connections, background tasks with Celery, and integrates with SQLAlchemy. Works with postgres-engineer for async database operations.

#### nodejs-engineer.md
Specializes in Node.js ecosystem including Express, Koa, NestJS, and microservices architecture. Handles npm packages, async programming, streams, and clustering. Implements real-time features with Socket.io and manages Node.js performance optimization.

#### graphql-engineer.md
Specializes in GraphQL API design, schema definition, resolvers, and subscriptions. Handles Apollo Server, GraphQL federation, and performance optimization with DataLoader. Works with any backend framework to implement GraphQL endpoints.

## Frontend Engineers

#### react-engineer.md
Expert in React ecosystem including hooks, Context API, Redux/Zustand, React Router, and Next.js. Implements component patterns, handles SSR/SSG, optimizes bundle size, and manages React performance. Collaborates with ui-ux-engineer for design systems and backend-coordinator for API integration.

#### vue-engineer.md
Specializes in Vue.js including Composition API, Vuex/Pinia, Vue Router, and Nuxt.js. Handles reactive data, component communication, and Vue ecosystem tools. Implements SSR/SSG strategies and works with ui-ux-engineer for component libraries.

#### angular-engineer.md
Expert in Angular framework including RxJS, Angular Material, dependency injection, and Angular Universal. Manages modules, services, directives, and pipes. Handles complex form validation and implements micro-frontend architectures.

#### nextjs-engineer.md
Expert in Next.js for React applications, handles SSR/SSG/ISR strategies, API routes, middleware, and Edge Runtime. Manages image optimization, font optimization, and implements advanced routing patterns. Works closely with react-engineer for component development.

#### ui-ux-engineer.md
Specializes in user interface design implementation, design systems, accessibility standards (WCAG), and responsive design. Handles CSS architectures, animation libraries, and component libraries. Bridges design and development teams, ensuring pixel-perfect implementation.

## Database Engineers

#### postgres-engineer.md
Expert in PostgreSQL including advanced queries, indexing strategies, partitioning, and performance tuning. Handles PL/pgSQL functions, triggers, and PostgreSQL extensions. Manages replication, backup strategies, and works with postgis-engineer for spatial data.

#### mysql-engineer.md
Specializes in MySQL/MariaDB optimization, replication, clustering with Galera, and performance tuning. Handles stored procedures, triggers, and MySQL-specific features. Manages backup strategies and works on high-availability configurations.

#### redis-engineer.md
Specializes in Redis for caching, session management, pub/sub messaging, and data structures. Handles Redis Cluster, Redis Streams, and Lua scripting. Implements caching strategies and real-time features with Redis.

#### sqlite-engineer.md
Expert in SQLite for embedded databases, mobile applications, and local storage. Handles SQLite-specific optimizations, full-text search, and JSON support. Manages database encryption and implements offline-first architectures.

#### weaviate-engineer.md
Expert in Weaviate vector database for AI applications, semantic search, and recommendation systems. Handles vectorization, schema design, and GraphQL queries. Integrates with ML models for embedding generation.

#### postgis-engineer.md
Specializes in PostGIS for spatial databases, handles geometric operations, spatial indexing, and geographic queries. Implements location-based features, mapping applications, and works with mapbox-engineer for visualization.

## Infrastructure Engineers

#### docker-engineer.md
Expert in Docker containerization, Dockerfile optimization, multi-stage builds, and Docker Compose orchestration. Handles container security, image optimization, and registry management. Works with infrastructure-coordinator for deployment strategies.

#### cloud-architect.md
Expert in cloud platforms (AWS, GCP, Azure), designs scalable architectures, handles IaC with Terraform/CloudFormation, and manages cloud costs. Implements serverless architectures, CDN strategies, and multi-region deployments.

#### message-queue-engineer.md
Specializes in message queue systems (RabbitMQ, Kafka, AWS SQS), handles event-driven architectures, and implements pub/sub patterns. Manages message reliability, ordering, and dead letter queues. Works on microservices communication.

## DevOps & Operations Engineers

#### git-engineer.md
Expert in Git version control, branching strategies (GitFlow, GitHub Flow), and Git hooks. Handles merge conflict resolution, repository management, and Git automation. Implements CI/CD triggers and manages monorepo strategies.

#### devops-troubleshooter.md
Specializes in debugging production issues, analyzing logs, and performance bottlenecks. Handles incident response, root cause analysis, and implements monitoring solutions. Works across all systems to identify and resolve problems.

#### logging-engineer.md
Expert in logging architectures, structured logging, and log aggregation systems. Handles ELK stack, Fluentd, and cloud logging services. Implements log retention policies, search optimization, and alerting based on log patterns.

#### observability-engineer.md
Specializes in observability platforms (Datadog, New Relic, Prometheus), implements distributed tracing, and creates dashboards. Handles metrics collection, APM integration, and SLO/SLI definition. Ensures system visibility and reliability.

#### apm-engineer.md
Expert in Application Performance Monitoring, handles performance profiling, memory leak detection, and bottleneck analysis. Implements custom metrics, traces transactions, and optimizes application performance across the stack.

## Security & Compliance Engineers

#### security-auditor.md
Performs security audits, vulnerability assessments, and penetration testing. Handles OWASP compliance, security scanning tools, and threat modeling. Creates security reports and remediation plans across all application layers.

#### gdpr-compliance-engineer.md
Specializes in GDPR compliance, data privacy regulations, and consent management. Implements data retention policies, right to erasure, and data portability features. Ensures application compliance with privacy laws.

#### licensing-engineer.md
Expert in software licensing, open source compliance, and dependency license scanning. Manages license compatibility, attribution requirements, and implements license compliance automation in CI/CD pipelines.

#### compliance-auditor.md
Handles regulatory compliance (SOC2, HIPAA, PCI-DSS), implements compliance controls, and manages audit trails. Creates compliance documentation and ensures adherence to industry standards.

## Testing Engineers

#### test-automation-engineer.md
Expert in test automation frameworks (Selenium, Cypress, Playwright), implements test strategies, and manages test data. Creates reusable test components, handles parallel test execution, and integrates tests with CI/CD pipelines.

#### e2e-engineer.md
Specializes in end-to-end testing, user journey validation, and cross-browser testing. Implements visual regression testing, handles test environment management, and ensures critical path coverage.

#### performance-tester.md
Expert in performance testing tools (JMeter, K6, Gatling), conducts load testing, stress testing, and capacity planning. Analyzes performance metrics, identifies bottlenecks, and provides optimization recommendations.

## Specialized Domain Engineers

#### ai-integration-engineer.md
Specializes in integrating AI models (OpenAI, Anthropic, Hugging Face) into applications. Handles prompt engineering, model fine-tuning, and implements RAG systems. Manages token optimization and AI service costs.

#### ml-engineer.md
Expert in machine learning pipelines, model training, and deployment with MLOps practices. Handles feature engineering, model versioning, and implements A/B testing for ML models. Works with TensorFlow, PyTorch, and scikit-learn.

#### data-scientist.md
Specializes in data analysis, statistical modeling, and predictive analytics. Handles exploratory data analysis, feature selection, and model evaluation. Creates data visualizations and provides business insights from data.

#### mapbox-engineer.md
Expert in Mapbox integration for mapping applications, handles map styling, geocoding, and routing. Implements custom map layers, clustering, and real-time location tracking. Works with postgis-engineer for spatial data.

#### billing-engineer.md
Specializes in payment processing (Stripe, PayPal), subscription management, and invoice generation. Handles PCI compliance, payment webhooks, and implements usage-based billing. Manages payment failure recovery and dunning processes.

#### email-engineer.md
Expert in email systems, transactional emails (SendGrid, AWS SES), and email template management. Handles email deliverability, bounce management, and implements email tracking. Manages email queues and bulk sending.

#### notification-engineer.md
Specializes in notification systems including push notifications, in-app notifications, and SMS. Handles notification preferences, delivery optimization, and implements notification centers. Manages cross-platform notification delivery.

#### search-engineer.md
Expert in search implementation, handles full-text search, faceted search, and search relevance tuning. Implements autocomplete, spell correction, and search analytics. Integrates various search solutions for optimal performance.

#### cms-engineer.md
Specializes in content management systems (headless CMS, Strapi, Contentful), handles content modeling, and API integration. Implements content versioning, publishing workflows, and multi-language support.

#### changelog-engineer.md
Expert in changelog generation, semantic versioning, and release note automation. Handles commit message conventions, changelog formatting, and integrates with CI/CD for automatic changelog updates.

#### docs-engineer.md
Specializes in documentation systems (Docusaurus, MkDocs), API documentation (OpenAPI, Swagger), and technical writing. Implements documentation automation, versioning, and search functionality.

## Utility Engineers

#### debugging-engineer.md
Expert in debugging techniques, profiling tools, and error analysis across all languages and frameworks. Handles memory leaks, race conditions, and complex bug investigations. Implements debugging instrumentation and logging strategies.

#### memory-engineer.md
Manages project memory base, documentation structure, and information architecture. Handles memory capture from team interactions, maintains technical wikis, and ensures memory persistence across the project.

#### clarification-engineer.md
Specializes in requirement clarification, ambiguity resolution, and specification refinement. Asks targeted questions to uncover hidden requirements, identifies edge cases, and ensures clear understanding before implementation.

#### prompt-engineer.md
Expert in crafting effective prompts for AI systems, optimizes Claude and other LLM interactions. Handles prompt templates, few-shot examples, and chain-of-thought reasoning. Improves AI agent effectiveness across the system.

#### system-engineer.md
Oversees system architecture, handles system design patterns, and ensures architectural consistency. Creates architectural decision records (ADRs), manages technical debt, and plans system evolution.

#### project-engineer.md
Manages project structure, codebase organization, and development workflows. Handles monorepo setup, build systems, and developer tooling. Ensures consistent project standards and conventions.

## Business & Planning Specialists

#### business-analyst.md
Analyzes business requirements, creates user stories, and defines acceptance criteria. Handles stakeholder communication, requirement prioritization, and creates business process documentation.

#### project-planner.md
Creates project timelines, sprint planning, and resource allocation. Handles task dependencies, risk assessment, and milestone tracking. Coordinates with all engineers to ensure realistic planning.

#### requirements-analyst.md
Specializes in requirement gathering, analysis, and documentation. Creates requirement specifications, use cases, and ensures requirement traceability throughout the project lifecycle.

#### risk-analyst.md
Identifies project risks, creates mitigation strategies, and maintains risk registers. Handles technical debt assessment, security risk analysis, and provides risk-based decision support.

#### user-researcher.md
Conducts user research, usability testing, and creates user personas. Handles user journey mapping, A/B testing analysis, and provides UX insights to guide development decisions.

#### tech-stack-selector.md
Evaluates and recommends technology choices based on project requirements. Analyzes framework trade-offs, considers team expertise, and ensures technology alignment with business goals.

#### metrics-analyst.md
Defines and tracks KPIs, creates analytics dashboards, and provides data-driven insights. Handles funnel analysis, cohort analysis, and implements analytics tracking across the application.

#### cost-optimizer.md
Analyzes and optimizes infrastructure costs, identifies cost-saving opportunities, and implements resource optimization. Handles cloud cost management, performance-per-dollar analysis, and budget tracking.

#### incident-responder.md
Manages incident response procedures, coordinates emergency fixes, and handles post-mortems. Creates runbooks, implements alerting strategies, and ensures rapid incident resolution.

## Project Analysis Specialists

#### discovery-engineer.md
Analyzes project structure, stack, dependencies, and configuration for comprehensive discovery. Performs deep analysis of project basics including purpose identification, complete directory tree mapping, technology stack detection with versions, dependencies audit, database schema analysis, and API endpoints mapping. Generates concise 2-3 page summaries for setup process.

#### quality-engineer.md
Analyzes code quality, testing, security, performance, and documentation coverage. Conducts comprehensive quality assessment including test coverage analysis, security vulnerability scanning, performance metrics collection, documentation coverage assessment, error patterns analysis, Git history insights, and CI/CD setup evaluation. Essential for understanding project health.

#### architecture-engineer.md
Analyzes design patterns, code organization, integrations, and technical debt. Reviews architecture and patterns including design pattern identification, code organization analysis, integration points mapping, technical debt assessment, configuration management review, deployment strategy analysis, and improvement opportunities. Provides strategic insights for project setup.

---

## Usage

Agents are invoked automatically based on task requirements or can be explicitly called:

```
# Automatic delegation
"Build a user authentication system"
# Claude detects need for backend-coordinator → laravel-engineer → postgres-engineer

# Explicit invocation
"Have the react-engineer optimize our component performance"
```

## memory Persistence

Each agent maintains memory in `.claude/memory/[domain]/[agent].md` files, enabling persistent learning across sessions through the hook system defined in `hooks.json`.

## Cross-Domain Communication

Agents communicate through:
- Direct delegation patterns
- memory files with flags (DATABASE_INVESTIGATION, SECURITY_BREACH, etc.)
- Module-specific documentation in `.claude/memory/modules/`

---

*Total agents: 71*
*Last updated: [Auto-generated]*

