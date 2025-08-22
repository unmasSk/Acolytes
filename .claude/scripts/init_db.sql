-- ClaudeSquad SQLite Schema
-- Timestamp format: 'YYYY-MM-DD HH:MM'

-- 1. DYNAMIC AGENTS (Project-specific agents with memories)
CREATE TABLE IF NOT EXISTS agents_dynamic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    module TEXT NOT NULL,           -- Main module (e.g., "rag", "auth", "payments")
    sub_module TEXT,                -- Sub-module for complex modules (e.g., "embeddings", "retrieval")
    created_at TEXT NOT NULL,
    updated_at TEXT
);

-- 2. AGENTS CATALOG (Directory of all available agents)
CREATE TABLE IF NOT EXISTS agents_catalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,      -- '@specialist.laravel', '@rag-embeddings-agent'
    type TEXT NOT NULL,             -- 'dynamic', 'specialist', 'coordinator', 'service'
    module TEXT NOT NULL,           -- Primary domain/module
    sub_module TEXT,                -- Sub-domain for complex modules
    description TEXT NOT NULL,       -- Brief description of agent capabilities
    capabilities JSON,              -- Specific capabilities/skills
    routing_keywords JSON,          -- Keywords for intelligent routing
    status TEXT DEFAULT 'active',   -- 'active', 'deprecated', 'maintenance'
    created_at TEXT NOT NULL
);

-- 3. AGENT MEMORY
-- memory_type must be one of these 9 types:
-- 'knowledge': Core understanding - purpose, features, architecture, TODOs
-- 'structure': Code organization - files, classes, functions, APIs, endpoints
-- 'patterns': Best practices - conventions, anti-patterns, design patterns
-- 'dependencies': Connections - internal deps, external libs, services, integrations
-- 'quality': Code health - tests, coverage, performance metrics, security analysis
-- 'operations': DevOps - config, deployment, monitoring, migrations, CI/CD
-- 'context': Business logic - decisions, history, roadmap, stakeholders
-- 'domain': Specialized - ML models, GraphQL schemas, i18n, specific to domain
-- 'interactions': Recent interactions - last consultations, implementations, delegations
CREATE TABLE IF NOT EXISTS agent_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id INTEGER NOT NULL,
    memory_type TEXT CHECK(memory_type IN ('knowledge', 'structure', 'patterns', 'dependencies', 'quality', 'operations', 'context', 'domain', 'interactions')) NOT NULL,
    content JSON NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (agent_id) REFERENCES agents_dynamic(id) ON DELETE CASCADE
);

-- 3. JOBS
CREATE TABLE IF NOT EXISTS jobs (
    id TEXT PRIMARY KEY,  -- "job_a1b2c3d4e5f6", "job_9f8e7d6c5b4a", etc.
    title TEXT,
    status TEXT DEFAULT 'active' CHECK(status IN ('active', 'paused', 'completed')) NOT NULL,
    created_at TEXT NOT NULL,
    paused_at TEXT,
    resumed_at TEXT,
    completed_at TEXT,
    pause_reason TEXT  -- Why was it paused? What interrupted it?
);

-- 4. SESSIONS
CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY,  -- "session_a1b2c3d4e5f6", "session_9f8e7d6c5b4a", etc.
    job_id TEXT NOT NULL,
    claude_session_id TEXT,  -- Real Claude session UUID from .jsonl files
    accomplishments JSON,
    decisions JSON,
    bugs_fixed JSON,
    errors_encountered JSON,
    breakthrough_moment TEXT,
    next_session_priority TEXT,
    quality_score INTEGER,
    created_at TEXT NOT NULL,
    ended_at TEXT,
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);

-- 5. MESSAGES
-- Complete chronological conversation flow (backup, not auto-loaded)
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    conversation_flow TEXT NOT NULL,  -- Full narrative: what happened from start to end
    total_exchanges INTEGER,          -- Number of user-assistant exchanges
    duration_minutes INTEGER,         -- Session duration
    created_at TEXT NOT NULL,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
);

-- 6. FLAGS
-- Inter-module communication system for changes that affect other modules
CREATE TABLE IF NOT EXISTS flags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chain_origin_id INTEGER,              -- Links to original FLAG in chain (NULL for origin flags)
    session_id TEXT,                      -- Session where flag was created
    flag_type TEXT NOT NULL,              -- change/new_feature/refactor/deprecation/breaking_change/enhancement
    source_agent TEXT NOT NULL,           -- Agent that created the flag
    target_agent TEXT,                    -- Specific agent target (@agent-name)
    change_description TEXT NOT NULL,     -- What changed (e.g., "Created global TIME utility")
    action_required TEXT NOT NULL,        -- What other modules need to do
    impact_level TEXT DEFAULT 'medium',   -- low/medium/high/critical (impact, not error severity)
    status TEXT DEFAULT 'pending',        -- pending/acknowledged/in_progress/completed/skipped
    locked BOOLEAN DEFAULT FALSE,         -- NEW: TRUE if waiting for response, FALSE if actionable
    related_files TEXT,                   -- Files involved (comma-separated)
    code_location TEXT,                   -- file:line_number format if specific location
    example_usage TEXT,                   -- Example of how to use the new change
    context JSON,                          -- Additional structured data
    created_at TEXT NOT NULL,
    acknowledged_at TEXT,                 -- When affected modules acknowledged
    completed_at TEXT,                     -- When all affected modules adapted
    completed_by TEXT,                     -- Agents that completed the adaptation
    notes TEXT,                            -- Resolution notes or comments
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE SET NULL,
    FOREIGN KEY (chain_origin_id) REFERENCES flags(id) ON DELETE SET NULL
);

-- 7. AGENT HEALTH
-- Monitors agent drift and memory size to maintain system health
CREATE TABLE IF NOT EXISTS agent_health (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id INTEGER NOT NULL,
    session_id TEXT,                      -- Session where check happened
    drift_score INTEGER NOT NULL,         -- 0-100 drift from reality
    confidence_score INTEGER,              -- 0-100 confidence in agent knowledge
    status TEXT NOT NULL,                  -- healthy/degraded/critical/oversized
    file_count_current INTEGER,            -- Current files in module
    file_count_baseline INTEGER,           -- Files when agent was created/updated
    memory_size_kb INTEGER,                -- Total size of all 9 memories
    memory_size_warning TEXT,              -- null/large/critical
    largest_memory_type TEXT,              -- Which memory is largest
    needs_compaction BOOLEAN DEFAULT 0,   -- If memories need cleaning
    patterns_changed TEXT,                 -- New patterns detected
    dependencies_changed TEXT,             -- Changed dependencies
    issues JSON,                           -- Structured issues found
    recommendations TEXT,                  -- Clear action recommendation
    auto_upgrade_eligible BOOLEAN DEFAULT 0, -- Can be auto-upgraded
    checked_at TEXT NOT NULL,
    last_upgrade_at TEXT,                  -- When agent was last upgraded
    upgraded_by TEXT,                      -- Who upgraded (auto/manual/agent)
    FOREIGN KEY (agent_id) REFERENCES agents_dynamic(id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE SET NULL
);

-- 8. TOOL LOGS
-- Tracks all tool usage for analysis and auditing
CREATE TABLE IF NOT EXISTS tool_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,                      -- Session where tool was used
    agent_name TEXT,                      -- Which agent/subagent used it
    tool_name TEXT NOT NULL,              -- Read/Write/Bash/Edit/Grep/etc
    tool_category TEXT,                   -- file/search/execution/ai/web
    parameters JSON,                      -- Full tool parameters
    file_affected TEXT,                   -- File path if applicable
    lines_changed INTEGER,                -- Lines added/removed/modified
    bytes_processed INTEGER,               -- Size of data processed
    result_summary TEXT,                   -- Brief result description
    success BOOLEAN DEFAULT 1,            -- Whether tool succeeded
    error_message TEXT,                   -- Error if failed
    blocked_by_hook BOOLEAN DEFAULT 0,    -- If pre_tool_use blocked it
    hook_message TEXT,                     -- Hook block reason
    duration_ms INTEGER,                  -- Execution time
    timestamp TEXT NOT NULL,               -- When tool was called
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE SET NULL
);

-- 9. TODOS
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT DEFAULT 'pending',         -- pending/in_progress/completed/blocked/cancelled
    created_at TEXT NOT NULL,
    completed_at TEXT,
    
    -- Integration with agents and sessions
    agent_id INTEGER,                      -- Agent that created or is assigned
    session_id TEXT,                       -- Session when created
    assigned_to TEXT,                      -- Agent or module assigned to
    
    -- Better time management
    estimated_hours REAL,                  -- Estimated time to complete
    actual_hours REAL,                     -- Actual time spent
    start_date TEXT,                       -- When work started
    reminder_at TEXT,                      -- When to remind
    due_date TEXT,
    
    -- Categorization and context
    module TEXT,                           -- Module affected
    tags JSON,                             -- Tags for search and filtering
    dependencies JSON,                     -- Array of TODO IDs that block this
    
    -- Traceability
    created_by TEXT DEFAULT 'user',       -- user/agent/system
    updated_at TEXT,                       -- Last modification
    updated_by TEXT,                       -- Who modified it
    completed_by TEXT,                     -- Who completed it
    
    -- Links and context
    related_files JSON,                    -- Array of related file paths
    
    -- Metrics
    subtasks_total INTEGER DEFAULT 0,     -- Total subtasks
    subtasks_completed INTEGER DEFAULT 0, -- Completed subtasks
    blocked_reason TEXT,                   -- Why it's blocked
    
    -- AI and automation
    auto_created BOOLEAN DEFAULT 0,       -- If created automatically
    ai_suggested BOOLEAN DEFAULT 0,       -- If suggested by AI
    context JSON,                          -- Additional context
    
    FOREIGN KEY (agent_id) REFERENCES agents_dynamic(id) ON DELETE SET NULL,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE SET NULL
);

-- INDEXES
CREATE INDEX IF NOT EXISTS idx_jobs_active ON jobs(completed_at) WHERE completed_at IS NULL;
CREATE INDEX IF NOT EXISTS idx_sessions_job ON sessions(job_id);
CREATE INDEX IF NOT EXISTS idx_messages_session ON messages(session_id);
CREATE INDEX IF NOT EXISTS idx_flags_pending ON flags(status) WHERE status = 'pending';
CREATE INDEX IF NOT EXISTS idx_flags_source ON flags(source_agent);
CREATE INDEX IF NOT EXISTS idx_flags_session ON flags(session_id);
CREATE INDEX IF NOT EXISTS idx_flags_workable ON flags(target_agent, locked, status) WHERE locked = FALSE AND status = 'pending';
CREATE INDEX IF NOT EXISTS idx_flags_target ON flags(target_agent, status);
CREATE INDEX IF NOT EXISTS idx_flags_chain ON flags(chain_origin_id);
CREATE INDEX IF NOT EXISTS idx_agent_memory ON agent_memory(agent_id, memory_type);
CREATE INDEX IF NOT EXISTS idx_tool_logs_session ON tool_logs(session_id, timestamp);
CREATE INDEX IF NOT EXISTS idx_sessions_time ON sessions(datetime(created_at) DESC);

-- UNIQUE CONSTRAINTS
-- Ensure only one job can be active at a time
CREATE UNIQUE INDEX IF NOT EXISTS idx_only_one_active_job ON jobs (status) WHERE status = 'active';

-- VIEWS
CREATE VIEW IF NOT EXISTS latest_session AS
SELECT * FROM sessions 
ORDER BY datetime(created_at) DESC 
LIMIT 1;

CREATE VIEW IF NOT EXISTS pending_flags AS
SELECT * FROM flags 
WHERE status = 'pending' 
ORDER BY 
    CASE impact_level 
        WHEN 'critical' THEN 1 
        WHEN 'high' THEN 2 
        WHEN 'medium' THEN 3 
        WHEN 'low' THEN 4 
    END,
    created_at ASC;

-- PRE-POPULATE AGENTS CATALOG with professional agents (only implementation agents for FLAGS routing)
INSERT OR IGNORE INTO agents_catalog (name, type, module, description, capabilities, routing_keywords) VALUES

-- Database Agents
('@database.mariadb', 'database', 'mariadb', 'MariaDB specialist and MySQL evolution expert', '["MariaDB 11+", "Galera clustering", "MaxScale load balancing", "ColumnStore analytics", "Spider sharding"]', '["MySQL modernization", "high-availability clustering", "zero-downtime migrations", "analytical workloads"]'),
('@database.mongodb', 'database', 'mongodb', 'MongoDB and NoSQL document database expert', '["MongoDB 7+", "aggregation pipelines", "sharding", "change streams", "Atlas", "Compass", "document modeling"]', '["Flexible document schemas", "real-time data streaming", "content management", "rapid prototyping"]'),
('@database.pgvector', 'database', 'pgvector', 'PostgreSQL vector database and AI search expert', '["PostgreSQL + pgvector", "HNSW/IVFFlat indexing", "pgvectorscale", "embedding models", "hybrid search"]', '["RAG applications", "semantic search", "similarity matching", "AI-powered recommendations", "multi-modal search"]'),
('@database.postgres', 'database', 'postgres', 'PostgreSQL advanced features and performance expert', '["PostgreSQL 15+", "advanced indexing (GiST, GIN, BRIN)", "TimescaleDB", "PgBouncer", "Citus", "PostGIS"]', '["Complex relational data", "time-series analytics", "geospatial applications", "enterprise OLTP systems"]'),
('@database.redis', 'database', 'redis', 'Redis in-memory data structures and caching expert', '["Redis 7+", "Redis Stack (JSON, Search, Graph)", "Streams", "pub/sub", "clustering", "Lua scripting"]', '["Sub-millisecond caching", "session storage", "real-time leaderboards", "pub/sub messaging", "rate limiting"]'),
('@database.sqlite', 'database', 'sqlite', 'SQLite embedded database and edge computing expert', '["SQLite 3.44+", "WAL mode", "FTS5", "JSON operations", "Core ML optimization", "Litestream replication"]', '["Embedded applications", "edge computing", "mobile apps", "serverless databases", "local-first architectures"]'),
('@database.weaviate', 'database', 'weaviate', 'Vector database and semantic search expert', '["Weaviate v4+", "HNSW indexing", "REST API", "vectorization modules", "hybrid search", "multi-tenancy"]', '["RAG applications", "semantic search", "question-answering systems", "multi-modal AI search", "knowledge graphs"]'),

-- Frontend Agents
('@frontend.angular', 'frontend', 'angular', 'Angular framework and enterprise TypeScript expert', '["Angular 17+", "TypeScript", "RxJS", "Angular Material", "PrimeNG", "NgRx", "standalone components"]', '["Enterprise applications", "complex forms", "reactive programming", "TypeScript-heavy projects"]'),
('@frontend.react', 'frontend', 'react', 'React ecosystem and modern JavaScript expert', '["React 18+", "Next.js", "TypeScript", "Material-UI", "Chakra UI", "shadcn/ui", "Zustand", "React Query"]', '["Single-page applications", "server-side rendering", "component libraries", "modern web apps"]'),
('@frontend.vue', 'frontend', 'vue', 'Vue.js ecosystem and progressive framework expert', '["Vue 3+", "Nuxt.js", "TypeScript", "Composition API", "Vuetify", "Pinia", "Vue Router", "Vite"]', '["Progressive web apps", "rapid prototyping", "developer-friendly projects", "gradual adoption"]'),

-- Backend Agents
('@backend.laravel', 'backend', 'laravel', 'Laravel framework and PHP ecosystem expert', '["Laravel 11+", "PHP 8.3+", "Eloquent ORM", "Livewire", "Inertia.js", "Horizon", "Telescope"]', '["Rapid web development", "MVC architecture", "PHP-based applications", "admin panels"]'),
('@backend.nodejs', 'backend', 'nodejs', 'Node.js runtime and JavaScript backend expert', '["Node.js 20+", "Express", "NestJS", "TypeScript", "Fastify", "Prisma", "Socket.io", "microservices"]', '["implementing Node.js backend", "real-time features", "JavaScript-based microservices"]'),
('@backend.python', 'backend', 'python', 'Python ecosystem and versatile backend expert', '["Python 3.11+", "Django", "FastAPI", "Flask", "SQLAlchemy", "Celery", "asyncio", "data processing"]', '["Data-heavy applications", "ML integration", "rapid development", "scientific computing"]'),
('@backend.go', 'backend', 'go', 'Go language and high-performance systems expert', '["Go 1.21+", "Gin", "Echo", "Fiber", "gRPC", "concurrency patterns", "goroutines", "channels"]', '["High-performance APIs", "microservices", "system programming", "concurrent processing"]'),
('@backend.java', 'backend', 'java', 'Java enterprise and Spring ecosystem expert', '["Java 17+", "Spring Boot", "Spring Cloud", "Hibernate", "Maven", "Gradle", "enterprise patterns"]', '["Enterprise applications", "large-scale systems", "legacy modernization", "corporate environments"]'),
('@backend.rust', 'backend', 'rust', 'Rust systems programming and performance expert', '["Rust", "Actix-web", "Rocket", "Axum", "Tokio", "WebAssembly", "async programming", "memory safety"]', '["System-level programming", "performance-critical applications", "WebAssembly", "safe concurrency"]'),
('@backend.api', 'backend', 'api', 'API design and integration architecture expert', '["REST", "GraphQL", "WebSocket", "gRPC", "OpenAPI/Swagger", "API gateways", "rate limiting", "versioning"]', '["API-first development", "GraphQL schemas", "API governance", "documentation standards"]'),
('@backend.serverless', 'backend', 'serverless', 'Serverless functions and edge computing expert', '["AWS Lambda", "Vercel Functions", "Netlify Functions", "CloudFlare Workers", "edge runtime", "FaaS patterns"]', '["Serverless architectures", "edge computing", "event-driven functions", "cost-optimized backends"]'),

-- Service Agents
('@service.ai', 'service', 'ai', 'AI/ML integration and model management expert', '["LangGraph", "CrewAI", "AutoGen", "advanced RAG (Agentic RAG, HyDE)", "vector databases (Qdrant, Milvus, pgvector)", "modern fine-tuning (PEFT/LoRA/QLoRA)", "latest models (DeepSeek-V3, Llama 3.3, Mistral Large 2, Qwen 2.5)", "production deployment (vLLM, TGI, Ollama)", "LangSmith observability"]', '["AI feature integration", "chatbots", "content generation", "ML model deployment", "prompt optimization", "advanced RAG systems", "vector search", "agent orchestration"]'),
('@service.auth', 'service', 'auth', 'Authentication and authorization security expert', '["OAuth2", "JWT", "SSO (SAML, OIDC)", "Auth0", "Firebase Auth", "Passport.js", "multi-factor authentication", "RBAC"]', '["implementing user authentication", "OAuth flows", "SSO integration", "JWT token management"]'),
('@service.communication', 'service', 'communication', 'Multi-channel communication and messaging expert', '["Twilio Messaging Services with A2P compliance", "SendGrid v3 API with dynamic templates", "Firebase Cloud Messaging (FCM) v1 API", "WebSocket architecture with Socket.IO", "webhook validation", "circuit breaker patterns", "message queuing with retry mechanisms", "PII detection", "GDPR compliance", "real-time monitoring"]', '["Transactional emails", "SMS notifications", "push notifications", "real-time messaging", "webhook processing"]'),
('@service.data', 'service', 'data', 'Data processing and infrastructure services expert', '["Elasticsearch/OpenSearch 8+ with advanced indexing and cluster management", "Apache Kafka 3.8+ with Kafka Streams and event-driven architectures", "Apache Airflow 2.10+ with TaskFlow API and enterprise deployment", "RabbitMQ 4+ with advanced clustering and HA", "modern ETL/ELT pipelines", "enterprise data mesh architecture", "real-time streaming", "comprehensive monitoring & observability"]', '["Search functionality", "data streaming", "message queuing", "data pipelines", "real-time data processing"]'),
('@service.integrations', 'service', 'integrations', 'Third-party API integration and external services expert', '["REST APIs", "SDK integrations", "rate limiting", "web scraping (Playwright, Selenium)", "data synchronization"]', '["External API consumption", "third-party SDKs", "service orchestration", "automation workflows"]'),
('@service.mapbox', 'service', 'mapbox', 'Mapbox and geospatial services expert', '["Mapbox GL JS", "Navigation API", "geocoding", "routing", "spatial analysis", "custom map styles", "location services"]', '["Interactive maps", "location-based features", "route optimization", "geofencing", "spatial data visualization"]'),

-- Business Agents
('@business.billing', 'business', 'billing', 'Billing systems and revenue management expert', '["Stripe Billing", "invoice generation", "tax calculation", "revenue recognition", "dunning management"]', '["SaaS billing", "subscription management", "complex pricing models", "tax compliance", "revenue reporting"]'),
('@business.payment', 'business', 'payment', 'Payment processing and financial transactions expert', '["Stripe", "PayPal", "Square", "PCI compliance", "tokenization", "fraud prevention", "3D Secure", "webhooks"]', '["E-commerce payments", "transaction processing", "financial integrations", "payment security", "fraud detection"]'),

-- Documentation Agents  
('@docs-specialist', 'docs', 'specialist', 'Professional documentation specialist managing all project documentation', '["semantic versioning", "changelog generation", "technical writing", "API documentation", "markdown mastery", "GitHub repository files", "README.md optimization", "CONTRIBUTING.md", "LICENSE files", "CODE_OF_CONDUCT", "community health files", "issue templates", "PR templates", "version management", "OpenAPI/Swagger", "Mermaid diagrams", "shields.io badges", "accessibility compliance", "documentation automation", ".github templates"]', '["changelog creation", "version management", "release documentation", "API documentation", "technical guides", "README optimization", "GitHub repository setup", "community health files", "CONTRIBUTING guidelines", "LICENSE management", "issue/PR templates", "documentation quality metrics", "cross-reference management", "repository documentation"]'),

-- Mobile Agents
('@frontend.mobile', 'frontend', 'mobile', 'Cross-platform mobile development expert', '["React Native", "Flutter", "Expo", "Capacitor", "native modules", "app store deployment", "mobile CI/CD"]', '["Mobile app development", "cross-platform solutions", "native feature integration", "app store publishing"]'),

-- Additional Database Agents  
('@database.postgis', 'database', 'postgis', 'PostGIS geospatial database and GIS expert', '["PostGIS", "spatial indexing", "geographic queries", "coordinate systems", "spatial analysis"]', '["Location-based applications", "mapping systems", "geographic data analysis", "spatial queries"]'),

-- Business Service Agents
('@business.subscription', 'business', 'subscription', 'SaaS subscription and recurring revenue expert', '["Subscription models", "usage-based billing", "metered pricing", "customer lifecycle", "churn prevention"]', '["SaaS platforms", "recurring revenue models", "subscription analytics", "customer retention strategies"]'),


-- Analysis and Strategy Agents
('@analyst.strategic', 'analyst', 'strategic', 'Business and technical strategy analysis expert', '["Requirements analysis", "roadmap planning", "stakeholder analysis", "competitive analysis", "market research tools"]', '["Strategic planning", "business requirements", "technology selection", "project roadmaps", "feasibility studies"]'),
('@analyst.data', 'analyst', 'data', 'Data science and analytics expert', '["Python (pandas, numpy)", "R", "Jupyter", "Tableau", "Power BI", "statistical analysis", "machine learning", "predictive modeling"]', '["Data analysis", "KPIs definition", "user research", "predictive analytics", "business intelligence", "risk assessment"]'),

-- Audit and Compliance Agents
('@audit.compliance', 'audit', 'compliance', 'Regulatory compliance and accessibility expert', '["GDPR compliance tools", "WCAG guidelines", "accessibility testing", "cost optimization tools", "compliance frameworks"]', '["Regulatory compliance", "accessibility audits", "cost analysis", "privacy compliance", "legal requirements"]'),
('@audit.security', 'audit', 'security', 'Security vulnerability assessment expert', '["OWASP tools", "penetration testing", "vulnerability scanners", "security frameworks", "threat modeling"]', '["Security audits", "vulnerability assessments", "penetration testing", "security compliance", "threat analysis"]'),

-- Operations Agents
('@ops.git', 'ops', 'git', 'Git workflow and version control expert', '["Git", "GitHub Actions", "branching strategies", "conventional commits", "git hooks", "submodules", "LFS"]', '["Repository management", "branching strategies", "commit conventions", "code review workflows", "version control optimization"]'),
('@ops.monitoring', 'ops', 'monitoring', 'Application monitoring and observability expert', '["Prometheus", "Grafana", "ELK stack", "APM tools (DataDog, New Relic)", "OpenTelemetry", "custom dashboards", "alerting"]', '["System monitoring", "log aggregation", "alerting systems", "observability implementation", "metrics collection"]'),
('@ops.containers', 'ops', 'containers', 'Container orchestration and tactical deployment expert', '["Docker", "Kubernetes deployments", "Helm charts", "Istio service mesh", "container registries", "ingress controllers"]', '["Container deployments", "Kubernetes manifests", "service mesh configuration", "container security", "pod orchestration"]'),
('@ops.webserver', 'ops', 'webserver', 'Web server configuration and reverse proxy expert', '["Nginx", "Apache", "Caddy", "HAProxy", "SSL/TLS certificates", "reverse proxy", "load balancing", "HTTP/3"]', '["Web server setup", "reverse proxy configuration", "SSL certificate management", "traffic routing"]'),
('@ops.cicd', 'ops', 'cicd', 'CI/CD pipeline implementation and automation expert', '["Jenkins", "GitLab CI", "CircleCI", "GitHub Actions", "ArgoCD", "deployment automation", "pipeline optimization"]', '["CI/CD pipeline creation", "build automation", "deployment pipelines", "continuous integration setup"]'),
('@ops.iac', 'ops', 'iac', 'Infrastructure as Code implementation expert', '["Terraform", "Pulumi", "Ansible", "CloudFormation", "configuration management", "infrastructure automation"]', '["Infrastructure provisioning", "configuration management", "infrastructure automation", "IaC implementation"]'),
('@ops.troubleshooting', 'ops', 'troubleshooting', 'System debugging and incident resolution expert', '["Debugging tools", "profiling tools", "root cause analysis", "incident response", "diagnostic techniques", "error tracking"]', '["Production issues", "system failures", "incident management", "problem diagnosis", "emergency response"]'),
('@ops.performance', 'ops', 'performance', 'Application and system performance optimization expert', '["Performance profiling", "load testing (JMeter, k6)", "caching strategies", "database tuning", "code optimization"]', '["Performance bottlenecks", "scalability issues", "optimization strategies", "load testing", "capacity planning"]'),

-- Testing and Quality Agents
('@test.quality', 'test', 'quality', 'Comprehensive testing and quality assurance expert', '["Jest", "Cypress", "Playwright", "JUnit", "pytest", "test automation frameworks", "coverage tools (Istanbul, c8)"]', '["Test strategy implementation", "automated testing pipelines", "quality gates", "coverage analysis", "testing best practices"]'),

-- Planning Agents
('@plan.strategy', 'plan', 'strategy', 'Project management and strategic planning expert', '["Project management tools (Jira, Asana)", "agile methodologies", "resource planning", "timeline management", "Gantt charts"]', '["Project planning", "resource allocation", "sprint planning", "roadmap creation", "timeline management"]');

-- TRIGGERS FOR FLAGS QUALITY CONTROL
CREATE TRIGGER validate_flag_quality
BEFORE INSERT ON flags
BEGIN
  SELECT CASE
    WHEN LENGTH(NEW.action_required) < 100 
    THEN RAISE(ABORT, 'action_required must be at least 100 characters for quality control. Be specific: include file paths, line numbers, exact changes needed.')
    WHEN LENGTH(NEW.change_description) < 50 
    THEN RAISE(ABORT, 'change_description must be at least 50 characters. Describe what changed and why.')
    WHEN NEW.target_agent IS NULL AND NEW.impact_level IN ('high', 'critical')
    THEN RAISE(ABORT, 'High/critical impact flags must have specific target_agent specified.')
  END;
END;

CREATE TRIGGER validate_flag_quality_update
BEFORE UPDATE ON flags
BEGIN
  SELECT CASE
    WHEN LENGTH(NEW.action_required) < 100 
    THEN RAISE(ABORT, 'action_required must be at least 100 characters for quality control. Be specific: include file paths, line numbers, exact changes needed.')
    WHEN LENGTH(NEW.change_description) < 50 
    THEN RAISE(ABORT, 'change_description must be at least 50 characters. Describe what changed and why.')
    WHEN NEW.target_agent IS NULL AND NEW.impact_level IN ('high', 'critical')
    THEN RAISE(ABORT, 'High/critical impact flags must have specific target_agent specified.')
  END;
END;