---
description: Comprehensive project setup with environment verification, security, CI/CD, and complete configuration
---

# Advanced Project Setup & Complete Configuration

I will perform a comprehensive analysis and setup of your development environment, covering everything from basic stack to security, deployment, and monitoring.

## Phase 0: Environment Verification

First, let me verify your development environment...

```yaml
Checking prerequisites:
- Git version and configuration
- Node.js/npm/yarn versions
- PHP/Composer (if applicable)
- Python/pip (if applicable)
- Docker/Docker Compose
- IDE/Editor configuration
- Shell environment (bash/zsh/powershell)
- Operating system details
- File permissions
- Network connectivity

Missing tools detected:
- [List of missing prerequisites]
- Installation commands provided
- Alternative solutions suggested
```

## Detection Phase

Analyzing project type (new vs existing)...

*[Checking for package.json, composer.json, requirements.txt, Gemfile, go.mod, .env, docker-compose.yml, and CI/CD configs]*

---

## FOR NEW/EMPTY PROJECTS

### Comprehensive Project Interview

I see this is a new project. I'll gather complete requirements through a conversational approach. **Start by describing your project in your own words, in any language you prefer.**

Based on your description, I'll explore these areas:

### 1. BUSINESS & DOMAIN
```yaml
Core Questions:
- What problem are you solving?
- Who are the users/stakeholders?
- What's the business model?
- Competition/alternatives?
- Success metrics/KPIs?
- Timeline and milestones?
- Budget constraints?
- Scalability expectations?
```

### 2. TECHNICAL ARCHITECTURE
```yaml
Stack Decisions:
- Why this language/framework?
- Monolith vs microservices?
- API design (REST/GraphQL/gRPC)?
- Real-time requirements (WebSockets/SSE)?
- Background jobs/queues?
- Caching strategy?
- Search functionality?
- File storage (S3/local/CDN)?
```

### 3. DATABASE & DATA
```yaml
Data Architecture:
- Database choice rationale?
- ACID vs eventual consistency?
- Data volume expectations?
- Backup/recovery strategy?
- Data retention policies?
- GDPR/privacy requirements?
- Analytics/reporting needs?
- Data migration from existing?
```

### 4. SECURITY & COMPLIANCE
```yaml
Security Requirements:
- Authentication method (JWT/OAuth/SAML)?
- Authorization model (RBAC/ABAC)?
- Encryption requirements (at rest/in transit)?
- OWASP compliance level?
- PCI-DSS/HIPAA/SOC2 needed?
- Secrets management strategy?
- API rate limiting?
- DDoS protection?
- Audit logging requirements?
- Penetration testing schedule?
```

### 5. INFRASTRUCTURE & DEPLOYMENT
```yaml
Infrastructure Planning:
- Cloud provider (AWS/GCP/Azure/Self-hosted)?
- Container orchestration (K8s/ECS/Swarm)?
- Serverless components?
- CDN strategy (CloudFlare/CloudFront)?
- Multi-region requirements?
- Load balancing approach?
- Auto-scaling triggers?
- Disaster recovery plan?
- Infrastructure as Code (Terraform/CloudFormation)?
```

### 6. CI/CD & DEVOPS
```yaml
Pipeline Configuration:
- Version control (GitHub/GitLab/Bitbucket)?
- Branching strategy (GitFlow/GitHub Flow)?
- CI/CD platform (Actions/Jenkins/CircleCI)?
- Deployment strategy (Blue-green/Canary/Rolling)?
- Environments (dev/staging/prod/more)?
- Automated testing gates?
- Code quality gates?
- Security scanning in pipeline?
- Dependency vulnerability scanning?
- Container registry?
```

### 7. MONITORING & OBSERVABILITY
```yaml
Observability Stack:
- APM tool (DataDog/New Relic/AppDynamics)?
- Error tracking (Sentry/Rollbar/Bugsnag)?
- Log aggregation (ELK/Splunk/CloudWatch)?
- Custom metrics/KPIs?
- Alerting rules and channels?
- SLA/SLO definitions?
- Uptime monitoring (Pingdom/UptimeRobot)?
- Distributed tracing?
- Performance budgets?
- Cost monitoring?
```

### 8. TESTING STRATEGY
```yaml
Quality Assurance:
- Test coverage target (70%/80%/90%)?
- Unit/Integration/E2E ratio?
- TDD/BDD approach?
- Performance testing tools?
- Load testing thresholds?
- Security testing (SAST/DAST)?
- Accessibility testing?
- Cross-browser testing?
- Mobile testing strategy?
- Chaos engineering?
```

### 9. DOCUMENTATION & KNOWLEDGE
```yaml
Documentation Plans:
- API documentation (OpenAPI/GraphQL schema)?
- Code documentation standards?
- Architecture diagrams (C4/UML)?
- Database ERD generation?
- Runbook creation?
- Onboarding documentation?
- Video tutorials needed?
- Knowledge base platform?
- Changelog automation?
- Public vs internal docs?
```

### 10. ACCESSIBILITY & I18N
```yaml
Accessibility Requirements:
- WCAG compliance level (A/AA/AAA)?
- Screen reader support?
- Keyboard navigation complete?
- Color contrast requirements?
- Languages to support?
- RTL language support?
- Date/time localization?
- Currency/number formats?
- Translation workflow?
- Content moderation per locale?
```

### 11. TEAM & COLLABORATION
```yaml
Team Structure:
- Team size and roles?
- Remote/hybrid/onsite?
- Time zones involved?
- Communication tools (Slack/Teams)?
- Project management (Jira/Linear/Asana)?
- Code review process?
- Pair programming practices?
- Knowledge sharing sessions?
- On-call rotation?
- External contractors/vendors?
```

### 12. DEVELOPMENT ENVIRONMENT
```yaml
Developer Experience:
- Local development setup?
- Docker development environment?
- Hot reload requirements?
- Seed data management?
- Development tools/extensions?
- Linting/formatting standards?
- Pre-commit hooks?
- IDE configurations shared?
- Development documentation?
- Onboarding time target?
```

### 13. LANGUAGE & COMMUNICATION
```yaml
Language Configuration:
- User interface language(s)?
- Documentation language?
- Code comments language?
- Variable/function naming convention?
- Git commit message language?
- Error messages language?
- Log messages language?
- Support communication language?
- Legal documents language?
- Marketing content language?
```

### 14. USER EXPERIENCE LEVEL
```yaml
Your Experience Profile:
- Years in programming?
- Experience with chosen stack?
- Familiarity with cloud services?
- DevOps experience level?
- Preference for explanations (detailed/concise)?
- Learning style (examples/theory/hands-on)?
- Biggest knowledge gaps?
- Previous similar projects?
- Preferred resources/documentation?
- Mentorship needs?
```

---

## FOR EXISTING PROJECTS

### Phase 1: Comprehensive Analysis

Delegating to specialized analysts and additional inspectors:

```yaml
Core Analysts:
- discovery-engineer → Structure, stack, dependencies
- quality-engineer → Tests, security, documentation
- architecture-engineer → Patterns, organization, debt

Additional Inspections:
- Security audit (OWASP compliance check)
- Performance baseline (current metrics)
- Dependency audit (outdated/vulnerable)
- License compliance scan
- Accessibility audit (WCAG check)
- Docker/container analysis
- CI/CD pipeline review
- Database schema analysis
- API endpoint inventory
- Environment configs audit
```

### Phase 2: Intelligent Clarification

If ambiguities are detected:

```yaml
Stack Clarification:
- "Multiple Node versions in .nvmrc and package.json"
- "Both REST and GraphQL endpoints found"
- "Docker configs present but not used in CI"

Security Clarification:
- "Auth middleware found but not consistently applied"
- "Secrets in .env but also hardcoded values found"
- "CORS configuration seems incomplete"

Testing Clarification:
- "Test files exist but CI doesn't run them"
- "Coverage reports outdated by 6 months"
- "E2E tests configured but broken"
```

### Phase 3: Module Detection & Dynamic Agent Generation

Analyzing project structure to generate specialized agents...

```bash
# Step 1: Detect modules in the project
echo "🔍 Scanning project structure..."

# Find main directories with substantial code
find . -type d -name "node_modules" -prune -o \
       -type d -name ".git" -prune -o \
       -type d -mindepth 1 -maxdepth 3 \
       -exec sh -c 'echo "$(find "$1" -type f \( -name "*.js" -o -name "*.ts" -o -name "*.php" -o -name "*.py" \) | wc -l) $1"' _ {} \; \
       | sort -rn | head -20

# Step 2: Analyze each module
for module_path in backend/api backend/payments backend/auth frontend/components services/email; do
    if [ -d "$module_path" ]; then
        echo "📊 Analyzing module: $module_path"
        
        # Count files and lines
        file_count=$(find "$module_path" -type f -name "*.js" -o -name "*.ts" -o -name "*.php" | wc -l)
        line_count=$(find "$module_path" -type f -name "*.js" -o -name "*.ts" -o -name "*.php" -exec wc -l {} + | tail -1 | awk '{print $1}')
        
        # Detect main technology
        if [ -f "$module_path/composer.json" ]; then
            tech="PHP/Laravel"
        elif [ -f "$module_path/package.json" ]; then
            tech="JavaScript/Node"
        elif [ -f "$module_path/requirements.txt" ]; then
            tech="Python"
        else
            tech="Mixed"
        fi
        
        echo "  Files: $file_count | Lines: $line_count | Tech: $tech"
    fi
done

# Step 3: Generate dynamic agent for each module
echo "🤖 Generating dynamic agents..."
```

```python
# Dynamic agent generation using external template
def generate_dynamic_agent(module_name, module_path, analysis):
    """Generate a dynamic agent file for a specific module using template"""
    
    # Load the template
    template_path = ".claude/resources/templates/dynamic-agent-initial.md"
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Prepare data for template
    template_data = {
        "module_name": module_name,
        "module_name_title": module_name.title(),
        "module_path": module_path,
        "version": "1.0.0",
        "created_date": datetime.now().isoformat(),
        "last_updated": datetime.now().isoformat(),
        "technology_stack": analysis['technology'],
        "file_count": analysis['file_count'],
        "line_count": analysis['line_count'],
        "test_coverage": analysis.get('coverage', 0),
        "complexity_score": analysis.get('complexity', 5),
        "primary_purpose": analysis['purpose'],
        "tree_structure": analysis['tree_structure'],
        "key_files": analysis['key_files'],
        "components": analysis.get('components', []),
        "internal_dependencies": analysis.get('internal_deps', []),
        "external_dependencies": analysis.get('external_deps', []),
        "patterns": analysis.get('patterns', []),
        "conventions": analysis.get('conventions', []),
        "antipatterns": analysis.get('antipatterns', []),
        # ... more fields as needed
    }
    
    # Render template (using simple replacement for now)
    agent_content = template
    for key, value in template_data.items():
        agent_content = agent_content.replace(f"{{{{{key}}}}}", str(value))
    
    # Save to .claude/agents/
    agent_file = f".claude/agents/{module_name}-agent.md"
    save_to_file(agent_file, agent_content)
    
    print(f"✅ Generated {agent_file}")
    return agent_file

def upgrade_dynamic_agent(agent_name, changes_detected):
    """Upgrade an existing dynamic agent when module changes"""
    
    # Load upgrade template
    upgrade_template_path = ".claude/resources/templates/dynamic-agent-upgrade.md"
    current_agent_path = f".claude/agents/{agent_name}.md"
    
    # Analyze what changed
    upgrade_data = analyze_changes(current_agent_path, changes_detected)
    
    # Apply upgrade template
    upgraded_content = render_upgrade(upgrade_template_path, upgrade_data)
    
    # Backup old version
    backup_path = f".claude/agents/backup/{agent_name}-v{upgrade_data['old_version']}.md"
    
    # Save upgraded version
    save_to_file(current_agent_path, upgraded_content)
    
    print(f"⬆️ Upgraded {agent_name} from v{upgrade_data['old_version']} to v{upgrade_data['new_version']}")
```

#### 🤖 Dynamic Agent Generation

Creating specialized agents for your project modules:

```yaml
Generated Agents:
1. api-agent.md
   - Module: /backend/api
   - Expertise: REST endpoints, middleware, validation
   - Lines of Code: 12,450
   - Key Files: 47 controllers, 23 middleware, 89 routes
   
2. payments-agent.md
   - Module: /backend/payments
   - Expertise: Stripe integration, invoicing, webhooks
   - Lines of Code: 3,200
   - Key Files: PaymentService, StripeGateway, InvoiceGenerator
   
3. auth-agent.md
   - Module: /backend/auth
   - Expertise: JWT, OAuth2, 2FA, permissions
   - Lines of Code: 2,100
   - Key Files: AuthController, JWTService, PermissionMiddleware
```

#### 📁 Memory System Initialization

Creating project memory structure:

```
.claude/memory/
├── context/
│   ├── architecture.md      # Your project's architecture
│   ├── decisions.md         # Technical decisions log
│   ├── conventions.md       # Coding standards
│   └── stack.md            # Technology stack details
├── modules/
│   ├── api/                # API module knowledge
│   ├── payments/           # Payments module knowledge
│   └── auth/               # Auth module knowledge
├── sessions/
│   └── current.json        # Current session context
└── consolidated/
    └── patterns.json       # Learned patterns
```

### Phase 4: Comprehensive Configuration Review

```markdown
📊 COMPLETE PROJECT CONFIGURATION:

**CORE STACK:**
- Backend: [framework, version, architecture]
- Frontend: [framework, version, build tool]
- Database: [type, version, ORM/ODM]
- Cache: [Redis/Memcached, configuration]
- Queue: [system, configuration]
- Search: [Elasticsearch/Algolia, setup]

**INFRASTRUCTURE:**
- Deployment: [platform, method]
- Containers: [Docker/K8s setup]
- CI/CD: [platform, pipeline stages]
- Environments: [list, promotion flow]
- Monitoring: [APM, logs, metrics]

**QUALITY & SECURITY:**
- Test Coverage: [current %, framework]
- Security: [auth method, vulnerabilities]
- Code Quality: [linting, formatting]
- Documentation: [coverage, format]
- Accessibility: [WCAG level, issues]

**DEVELOPMENT PRACTICES:**
- Git Flow: [branching strategy]
- Code Review: [process, tools]
- Dependencies: [outdated count, vulnerabilities]
- Tech Debt: [critical issues]
- Performance: [current metrics]

**LANGUAGE SETTINGS:**
- User Communication: [detected]
- Documentation: [detected]
- Code/Comments: [detected]
- Commits: [detected]

**TEAM CONFIGURATION:**
- Contributors: [active count]
- Last Activity: [date]
- Issue/PR Velocity: [metrics]

✅ Confirm this analysis?
🔧 Critical issues to address?
📝 Additional context needed?
🎯 Priority improvements?
```

### Phase 5: Enhanced CLAUDE.md Generation with Dynamic Agents

Generate comprehensive orchestrator configuration with dynamic agent mapping:

```markdown
# Project Orchestrator Configuration v3.0 - ClaudeSquad Edition

## Project Identity
- Name: [Project Name]
- Type: [Application Type]
- Stage: [Development/Production]
- Version: [Current Version]

## 🤖 Dynamic Agents Generated for YOUR Project

### Module-Specific Agents (Created by /setup)
These agents have deep knowledge of your specific modules:

1. **api-agent** 
   - Module: /backend/api
   - Expertise: Your REST endpoints, middleware, validation rules
   - Key Knowledge: 47 controllers, 23 middleware, 89 routes
   - Reviews: All API-related implementations
   
2. **payments-agent**
   - Module: /backend/payments  
   - Expertise: Your Stripe integration, invoicing, webhooks
   - Key Knowledge: PaymentService, StripeGateway, InvoiceGenerator
   - Reviews: All payment-related code
   
3. **auth-agent**
   - Module: /backend/auth
   - Expertise: Your JWT setup, OAuth2, 2FA, permissions
   - Key Knowledge: AuthController, JWTService, PermissionMiddleware  
   - Reviews: All authentication code

### Global Specialist Engineers (From ClaudeSquad)
These engineers implement based on dynamic agent guidance:

- **engineer-laravel**: Laravel implementation expert
- **engineer-react**: React development specialist
- **coordinator-database**: Database operations coordinator
- **testing-automation**: Test implementation specialist
- **auditor-security**: Security review specialist

## 🔄 Orchestration Workflow

When you request: "Implement OAuth in the API"

1. I consult **api-agent** for module context
2. api-agent provides conventions, patterns, existing auth
3. I instruct **engineer-laravel** with this context
4. engineer-laravel implements following api-agent's guidance
5. **api-agent reviews** the implementation
6. If issues found, engineer-laravel fixes them
7. Knowledge saved to project memory

## Complete Technology Stack
[Detailed stack with all versions and configurations]

## Available Engineers & Specialists
- Dynamic Agents: [List of generated agents]
- Global Engineers: [List of ClaudeSquad engineers]

## Language Configuration Matrix
- User Interface: [languages]
- API Responses: [language]
- Documentation: [public/internal languages]
- Code Comments: [language/style]
- Variable Naming: [convention]
- Database Fields: [convention]
- Git Commits: [language/format]
- Error Messages: [user/system languages]

## User Experience Profile
- Programming Level: [detailed level]
- Stack Expertise: [per technology]
- Preferred Learning: [style]
- Known Concepts: [list]
- Learning Goals: [areas]

## Architecture & Patterns
[Complete architectural documentation]

## Security Configuration
- Authentication: [method, provider]
- Authorization: [model, implementation]
- Encryption: [at rest, in transit]
- Compliance: [requirements]
- Audit: [logging strategy]

## Infrastructure Blueprint
- Cloud Platform: [provider, services]
- Deployment: [strategy, automation]
- Scaling: [rules, limits]
- Disaster Recovery: [RTO, RPO]

## CI/CD Pipeline
[Complete pipeline configuration with stages]

## Monitoring & Alerting
- APM: [tool, key metrics]
- Logs: [aggregation, retention]
- Alerts: [rules, channels]
- SLOs: [definitions]

## Testing Strategy
- Coverage Target: [percentage]
- Test Types: [ratios]
- Performance: [benchmarks]
- Security: [scan schedule]

## Development Workflow
[Detailed workflows for common tasks]

## Delegation Patterns
[Specific patterns for each engineer]

## Memory System Structure
[Complete memory organization]

## Critical Issues & Tech Debt
[Prioritized list with remediation plans]

## Performance Targets & Metrics
[Specific, measurable targets]

## Team Conventions & Standards
[Coding standards, review process, etc.]

## Integration Points
[External services, APIs, webhooks]

## Documentation Standards
[Requirements and templates]

## Emergency Procedures
[Incident response, rollback procedures]
```

### Phase 5: Template Generation

Generate essential configuration files:

```yaml
Creating project templates:
- .env.example (with all required variables)
- .gitignore (comprehensive, stack-specific)
- docker-compose.yml (development environment)
- docker-compose.prod.yml (production setup)
- .github/workflows/ci.yml (complete CI pipeline)
- .github/workflows/deploy.yml (deployment pipeline)
- .github/PULL_REQUEST_TEMPLATE.md
- .github/ISSUE_TEMPLATE/bug_report.md
- .github/ISSUE_TEMPLATE/feature_request.md
- .eslintrc.json / .phpcs.xml (linting)
- .prettierrc (formatting)
- .editorconfig (editor settings)
- .husky/pre-commit (git hooks)
- .husky/commit-msg (conventional commits)
- sonar-project.properties (code quality)
- jest.config.js / phpunit.xml (testing)
- .vscode/settings.json (IDE config)
- .vscode/extensions.json (recommended extensions)
- CONTRIBUTING.md (contribution guide)
- SECURITY.md (security policy)
- CODE_OF_CONDUCT.md (community standards)
- CHANGELOG.md (with keepachangelog format)
- README.md (comprehensive template)
- docs/ARCHITECTURE.md (C4 diagrams)
- docs/API.md (endpoint documentation)
- docs/DEPLOYMENT.md (deployment guide)
- docs/DEVELOPMENT.md (local setup)
- terraform/main.tf (if using IaC)
- k8s/deployment.yaml (if using Kubernetes)
- monitoring/alerts.yml (alert rules)
- scripts/setup.sh (one-click setup)
- scripts/backup.sh (backup automation)
```

### Phase 6: Agent Installation

Interactive installation with validation:

```yaml
📦 Installing Required Engineers:

Core Engineers ([X] required):
[List of essential engineers]

Optional Specialists (recommended):
[List of helpful but optional engineers]

Copy command for your OS:
- Windows: Copy-Item "source\*.md" "dest\" -Force
- Mac/Linux: cp source/*.md dest/

Or install one by one with confirmation:
1. [agent-name] - [why needed]
   Install? [y/n]

Validation:
- Checking file permissions
- Verifying agent compatibility
- Ensuring no conflicts
```

### Phase 7: Final Verification & Launch

```markdown
✅ SETUP COMPLETE - VERIFICATION CHECKLIST:

**Environment:**
☑ All required tools installed
☑ Proper versions confirmed
☑ Permissions verified

**Configuration:**
☑ [X] engineers installed
☑ CLAUDE.md generated
☑ Memory structure created
☑ Templates generated
☑ Git hooks configured

**Security:**
☑ Secrets properly managed
☑ Security scanning configured
☑ Compliance requirements noted

**Quality:**
☑ Linting/formatting ready
☑ Testing framework configured
☑ CI/CD pipeline ready

**Documentation:**
☑ README template created
☑ API docs structure ready
☑ Contributing guide present

**Monitoring:**
☑ Error tracking configured
☑ Metrics collection ready
☑ Alerts defined

**QUICK STARTS:**
- Run tests: npm test / composer test
- Start dev: npm run dev / php artisan serve
- Build: npm run build / composer build
- Deploy: npm run deploy / ./deploy.sh

**NEXT STEPS:**
1. Review generated templates
2. Customize configurations
3. Set up environment variables
4. Initialize git repository
5. Create first commit
6. Set up remote repository
7. Configure CI/CD secrets
8. Deploy to staging

Ready to build amazing things! 🚀

Need help? Ask: "How do I [task]?"
```

## Intelligent Defaults & Smart Suggestions

Based on domain and initial answers, I'll suggest:

```yaml
Domain-Specific Defaults:
- E-commerce → Payment integration, inventory, shipping
- SaaS → Subscription, multi-tenant, billing
- Healthcare → HIPAA, audit trails, encryption
- Finance → PCI-DSS, transaction logs, compliance
- Education → LMS features, progress tracking
- Government → Accessibility, security, audit

Stack-Specific Setup:
- Laravel → Sanctum, Horizon, Telescope, Nova
- React → Redux/Zustand, Router, Testing Library
- Node.js → Express/Fastify, PM2, clustering
- Python → FastAPI/Django, Celery, pytest

Common Integrations:
- Stripe/PayPal for payments
- SendGrid/SES for emails
- S3/Cloudinary for files
- Algolia/Elasticsearch for search
- Redis for cache/queues
- Sentry for error tracking
```

## Error Recovery & Troubleshooting

If setup fails at any point:

```yaml
Error Handling:
- Automatic rollback points
- Clear error messages
- Suggested fixes
- Manual override options
- Skip problematic steps
- Partial setup recovery
- Support contact info
```

## Ready to Begin

This comprehensive setup will take 5-10 minutes but will save hours of configuration and prevent common pitfalls.

**Start setup? [yes/no]**

*Note: You can save progress and resume anytime by using `/setup --resume`*