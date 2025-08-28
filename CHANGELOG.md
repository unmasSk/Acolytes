# Changelog

All notable changes to the Acolytes for Claude Code project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.6] - 2025-01-28

### Added
- **NEW COMMAND**: Created `/acolytes` command to replace `/flags` with improved branding and user experience
- Enhanced dependency detection system in infrastructure_check.py for better setup validation
- Improved setup flow with automatic dependency checking and installation before Phase 3

### Changed
- **DATABASE REFACTORING**: Eliminated redundant `acolytes` table, consolidated all agents in `agents_catalog` for simplified architecture
- Modified `agents_memory` table to use `agent_name` (TEXT) instead of `agent_id` (INTEGER) for direct agent access without joins
- Enhanced system architecture with streamlined database design and improved data access patterns

### Fixed
- Fixed agent_db.py to detect project database in current directory first for improved database path resolution
- Added validation checks before agent insertion to prevent UNIQUE constraint errors in database operations
- Improved Windows path handling in setup agents and scripts for better cross-platform compatibility
- Enhanced pre_tool_use hook with better error messages and validation feedback
- Simplified setup_mcp.py removing redundant logic and improving code maintainability
- Updated templates with Git Bash path resolution notes for better user guidance
- Fixed SQL schema formatting and organization for improved readability

### Removed
- Removed obsolete install_verify.py script that was no longer needed

## 1.0.5 - 2025-08-27

### Critical Windows Path Fixes

#### Fixed
- **CRITICAL**: Fixed path handling across all Python scripts for Windows compatibility
- Corrected backslash vs forward slash inconsistencies in file operations
- Fixed path joining issues that caused failures on Windows systems
- Added proper path quoting for directories with spaces
- Updated all scripts to use os.path.join() and pathlib for cross-platform compatibility

#### Changed
- README badge now uses dynamic PyPI version from shields.io
- CHANGELOG examples updated with shell-specific command formats
- Removed hardcoded version from README badge

## 1.0.4 - 2025-08-27

### Improved - Single Source of Truth for Version

#### Changed
- Made pyproject.toml the single source of truth for version
- Updated setup.py to dynamically obtain version at runtime
- Modified __init__.py to derive version from importlib.metadata
- Removed version duplication across files

#### Fixed
- Replaced deprecated pkg_resources with importlib.resources
- Eliminated UserWarning about pkg_resources deprecation
- Cleaned up bumpversion configuration

## 1.0.3 - 2025-08-27

### Patch - Corrected Package Build

#### Fixed
- Synchronized all version numbers across files (setup.py was outdated)
- Fixed bump2version configuration with correct file paths
- Added Version badge to README for clear version tracking
- Ensured proper build process for PyPI distribution

## 1.0.2 - 2025-08-27

### Critical Fix - Hook Command Format

#### Fixed
- **CRITICAL**: Fixed broken hook command format that prevented hooks from executing
- Added missing 'python' after 'uv run' in all hook commands
- Corrected path handling for Windows (absolute paths) vs Unix (~/ expansion)

#### Removed
- Removed accidentally committed settings.json from repository

#### Technical Details
- Previous broken format: `uv run /path/to/hook.py`
- Correct format: `uv run python /path/to/hook.py`

Shell-specific examples with proper quoting:
- **PowerShell**: `uv run python "$env:USERPROFILE/.claude/hooks/session_start.py"`
- **CMD**: `uv run python "%USERPROFILE%\.claude\hooks\session_start.py"`
- **Unix/Mac/Git Bash**: `uv run python "$HOME/.claude/hooks/session_start.py"`

Note: Always quote paths to handle spaces in usernames or directories. The 'python' token after 'uv run' is required for proper execution.

## 1.0.1 - 2025-08-27

### Hotfix - Settings.json Generation

#### Fixed
- Corrected settings.json format to match Claude Code requirements
- Fixed hook structure from simplified to proper Claude Code format
- Updated next steps instructions in init command output

## 1.0.0 - 2025-08-27

### Major Release - Complete PyPI Package

#### Added
- **PyPI Package**: Complete Python package for easy installation via `pip install acolytes`
- **CLI Tool**: Global `acolytes` command with init, update, doctor, repair, list, backup, and clean commands
- **Automated Installation**: One-command setup with `acolytes --init` that configures everything
- **52 Public Agents**: All specialized agents for backend, frontend, database, ops, and more
- **7 Internal Agents**: System agents (setup.*, flags.*, plan.*) for internal operations
- **Complete Hook System**: 8 hooks for Claude Code integration
- **Templates & Resources**: Internal templates for project initialization

#### Changed
- Consolidated all agents into single directory structure
- Improved agent filtering to show only public agents in list command
- Enhanced installation flow with automatic uv installation
- Standardized all documentation and code to English

## 0.14.1 - 2025-08-27

### Changed
- Added sequential-thinking tool to 40+ reasoning agents (coordinators, auditors, analysts) for enhanced decision-making capabilities
- Configured specialized MCPs: 21st-dev_magic for frontend agents (React/Vue/Angular), chrome-devtools/playwright/puppeteer for testing agents
- Restricted Edit/MultiEdit tools from 15 orchestration-only coordinator agents to prevent direct code manipulation
- Standardized tool configuration patterns across 57 global agents and dynamic module acolytes

### Enhanced
- Improved agent workflow standardization with consistent tool access patterns by role type
- Added voice-mode MCP integration to operations and testing agents for advanced interaction capabilities

## 0.14.0 - 2025-08-27

### Added
- **BREAKTHROUGH**: Integrated code-index MCP server with advanced search capabilities using ripgrep/ugrep/ag backends
- Fast file pattern matching with glob support (*.py, **/*.js patterns) for 50x faster project analysis
- Real-time file watcher system with debounced updates and automatic index synchronization
- Advanced search features: regex patterns, case sensitivity, context lines, fuzzy matching with ugrep
- File summary generation with function/class detection and complexity metrics for supported languages

### Changed
- Project scanning performance improved from 30+ seconds to sub-second response times
- Agent workflow efficiency dramatically enhanced through lightning-fast code location and pattern matching
- Search functionality now supports multiple command-line tools with automatic fallback selection

### Technical
- Implemented search_code_advanced with safety validation to prevent ReDoS attacks
- Added find_files with in-memory file index using standard glob patterns
- Configured refresh_index for manual index rebuilds after large-scale file operations

## 0.13.2 - 2025-08-26

### Added
- Merged 15+ remote documentation files (.claude/project/vision.md, architecture.md, technical-decisions.md) while preserving local agent updates
- Enhanced documentation coverage with complete project context files for all 57 global agents
- Added comprehensive team preferences and coding standards documentation

### Fixed
- Resolved Git merge conflicts between local agent modifications and remote documentation updates
- Maintained consistency across documentation sources using three-way merge strategy
- Preserved custom agent configurations during documentation synchronization

## 0.13.1 - 2025-08-26

### Added
- Mandatory project context reading step added to all 57 global agent workflows and dynamic module acolytes
- Agent initialization now reads .claude/project/ documents: vision.md, architecture.md, technical-decisions.md, team-preferences.md, project-context.md
- Complete project understanding integration before agent task execution

### Changed
- Enhanced agent startup process with comprehensive context loading from SQLite database and project files
- Standardized context reading protocol across all coordinator, specialist, auditor, analyst, and operations agents
- Improved agent decision-making through complete project awareness before task execution

## 0.13.0 - 2025-08-26

### Added
- **NEW SYSTEM**: Unified job management system with `--job` command supporting activate/list/switch operations
- SQLite-based job persistence in `jobs` table with status tracking (active/inactive/completed)
- Always exactly one active job requirement enforced at database level (system critical constraint)
- Comprehensive job rules with edge case handling: auto-creation, validation, and conflict resolution
- Job context inheritance system for seamless workflow continuity across sessions

### Changed
- Consolidated all job operations under single `--job` command interface replacing scattered activation methods
- Redesigned job workflow with atomic operations and transaction safety for concurrent access
- Enhanced Phase 6 setup documentation with complete job system rules and SQLite schema definitions
- Improved session management integration with automatic job context loading

### Removed
- Deprecated standalone `--activate` command and related job activation scripts in favor of unified system
- Removed legacy job tracking mechanisms replaced by SQLite-based persistence

## 0.12.2 - 2025-08-25

### Changed
- Enhanced setup phase definitions (Phases 1-8) with specific Claude instruction formatting and execution steps
- Improved documentation clarity for phase-based installation with detailed command sequences and validation checkpoints
- Added comprehensive user guidance for setup process with error recovery procedures and troubleshooting steps
- Refined Phase 2 (setup agents), Phase 3 (database initialization), and Phase 6 (acolyte creation) documentation

## 0.12.1 - 2025-08-25

### Fixed
- **CRITICAL**: Resolved 12+ critical bugs identified by CodeRabbit automated analysis including memory leaks and race conditions
- Fixed system stability issues in session management, database connections, and agent lifecycle management
- Improved error handling and edge case management in spawn_claude.py and FLAGS processing
- Resolved potential failure points in SQLite database operations and MCP server integration
- Fixed agent template validation and tool configuration inconsistencies across coordinator agents

## 0.12.0 - 2025-08-25

### Added
- **NEW FEATURE**: Automatic Claude session ID extraction from transcript files using regex pattern matching
- Enhanced session tracking with unique session identifiers linked to conversation transcripts
- Session analysis features including conversation flow tracking, tool usage statistics, and performance metrics
- Automated session archiving with timestamp-based organization and searchable metadata

### Changed
- Improved session lifecycle management with automatic session ID capture during conversation processing
- Enhanced transcript processing automation with real-time session data extraction and database storage
- Better debugging capabilities through comprehensive session tracking and cross-reference analysis

## 0.11.1 - 2025-08-24

### Added
- Professional vector logo design with SVG format and multiple size variants (16x16, 32x32, 64x64, 128x128, 256x256)
- Enhanced README branding with logo integration, shields.io badges, and professional formatting
- Visual identity improvements including favicon, GitHub social preview, and repository branding assets
- Marketing materials with consistent brand guidelines and color scheme

### Changed
- Enhanced project branding with consistent visual identity across all documentation and repository assets
- Improved README structure with professional layout, feature highlights, and clear installation instructions
- Added comprehensive branding assets for community recognition and professional presentation

## 0.11.0 - 2025-08-24

### Added
- **MAJOR CHANGE**: Complete rebranding from "ClaudeSquad" to "Acolytes for Claude Code" across entire codebase
- New standardized agent naming convention: `acolyte.{module}` format for dynamic module agents
- Performance validation benchmarks demonstrating 3x faster task completion and superior multi-agent coordination
- Brand consistency validation across 100+ files including agents, scripts, documentation, and configuration files

### Changed
- Updated all references across 127 files for complete rebranding including function names, variable names, and documentation
- Database schema migration: renamed table `agents_dynamic` → `acolytes` with data preservation and foreign key updates
- Enhanced agent architecture with improved naming conventions and consistent module identification patterns
- Conducted comprehensive performance testing validating system superiority over traditional single-agent approaches

### Fixed
- Removed redundant agent notes and deprecated references from 51 global agent files
- Fixed all code references in Python scripts (.claude/scripts/), command definitions, and agent templates
- Maintained full backward compatibility during transition with graceful fallback mechanisms for legacy references
- Updated SQLite database queries and MCP server integration to use new table names and schema

## 0.10.6 - 2025-08-24

### Changed
- System migration and optimization improvements with database schema updates and performance tuning
- Internal architecture enhancements including agent communication protocol refinements and memory management optimization

## 0.10.5 - 2025-08-24

### Changed
- Continued system migration with SQLite database optimization and MCP server stability improvements
- Infrastructure updates including session management enhancements and FLAGS system performance tuning

## 0.10.4 - 2025-08-24

### Fixed
- YAML configuration format corrections across 15+ agent template files and setup configuration files
- Resolved configuration file inconsistencies in agent tool definitions and MCP server configurations
- Fixed formatting issues in .claude/commands/ setup files and documentation templates

## 0.10.3 - 2025-08-23

### Added
- Enterprise-grade `@ops.bash` shell scripting specialist agent with 2,100+ lines of advanced bash expertise
- Advanced shell scripting capabilities including process management, system monitoring, and automation features
- Comprehensive bash script validation, security analysis, and performance optimization tools

### Changed
- Enhanced operations toolkit with specialized bash expertise for system administration and DevOps workflows
- Improved system administration capabilities with automated script generation and best practices enforcement
- Added bash script testing and validation frameworks for enterprise-grade shell scripting

## 0.10.2 - 2025-08-23

### Added
- Complete phases 1-2 documentation system with comprehensive setup guides and architectural documentation
- Phase 1: Environment validation and dependency checking with automated system requirements verification
- Phase 2: Setup agents activation including infrastructure.setup, environment.setup, context.setup, and codebase.setup agents

### Changed
- Enhanced documentation structure with phase-based installation workflow and detailed command sequences
- Improved user onboarding experience with step-by-step setup validation and error recovery procedures
- Added comprehensive troubleshooting guides and setup validation checkpoints

## 0.10.1 - 2025-08-23

### Changed
- System migration with SQLite database schema optimization and performance improvements
- Internal optimizations including agent template refinements and tool configuration standardization

## 0.10.0 - 2025-08-23

### Added
- **NEW FEATURE**: Complete audit compliance system
- Agent routing evolution with enhanced decision-making
- Advanced compliance monitoring and reporting capabilities

### Changed
- Enhanced agent routing with improved intelligence
- Better compliance tracking and audit trail management

## 0.9.1 - 2025-08-23

### Added
- Emoji commit system integration for better Git workflow
- Enhanced setup agents with visual commit indicators
- Improved developer experience with expressive commit messages

### Changed
- Enhanced Git workflow with emoji-based commit categorization
- Better commit message standards and visual clarity

## 0.9.0 - 2025-08-23

### Added
- **NEW FEATURE**: Automatic conversation transcript system
- Advanced hook-based conversation tracking and analysis
- Complete session recording and management capabilities

### Changed
- Enhanced session management with automated transcript generation
- Improved debugging capabilities through comprehensive logging

## 0.8.1 - 2025-08-22

### Changed
- Optimized `ops.git` agent performance and capabilities
- Reorganized database agents for better efficiency
- Enhanced Git operations handling and workflow management

## 0.8.0 - 2025-08-22

### Added
- **NEW FEATURE**: Specialized backend and database agents
- Comprehensive documentation for new agent capabilities
- Enhanced system architecture with domain-specific expertise

### Changed
- Improved agent specialization and domain separation
- Better database management and backend operation handling

## 0.7.4 - 2025-08-22

### Added
- Extensive documentation improvements and additions
- Enhanced user guides and technical documentation
- Better project documentation coverage

### Changed
- Improved documentation quality and completeness
- Enhanced user experience through better guidance

## 0.7.3 - 2025-08-22

### Changed
- Comprehensive template improvements based on CodeRabbit analysis
- Enhanced code quality and maintainability
- Better template structure and organization

### Fixed
- Resolved template inconsistencies and improvement suggestions
- Applied best practices across template system

## 0.7.2 - 2025-08-22

### Fixed
- Corrected incorrect commands in templates
- Resolved template accuracy and usability issues
- Improved command documentation and examples

## 0.7.1 - 2025-08-21

### Added
- Enhanced interaction memory system (ninth iteration)
- Improved error tracking and code review capabilities

### Changed
- Better memory management for agent interactions
- Enhanced error detection and resolution workflows

## 0.7.0 - 2025-08-20

### Added
- **NEW FEATURE**: FLAGS orchestration system implementation
- `spawn_claude.py` for managing specialized Claude instances
- `@flags-agent` for coordinating inter-agent communication
- Advanced agent coordination and task delegation capabilities
- Quality validation system for FLAGS creation
- Session management improvements with database backup mechanisms

### Changed
- Enhanced agent communication through centralized FLAGS protocol
- Improved session tracking and management capabilities
- Better agent template structure and invocation protocols

### Security
- Implemented FLAGS system for secure inter-agent communication
- Enhanced data validation and quality controls

## 0.6.4 - 2025-08-20

### Added
- Basic FLAGS system implementation
- Initial inter-agent communication capabilities

## 0.6.3 - 2025-08-20

### Changed
- Repository cleanup and temporary file management
- Improved project structure and organization

### Removed
- Cleaned up temporary and unnecessary files
- Improved repository hygiene

## 0.6.2 - 2025-08-20

### Security
- **SECURITY**: Implemented comprehensive Git operation protections
- Enhanced security measures for version control operations
- Protected against accidental repository exposure

## 0.6.1 - 2025-08-20

### Security
- **CRITICAL FIX**: Added comprehensive .gitignore protections
- Protected sensitive files from accidental commits
- Enhanced repository security and privacy

## 0.6.0 - 2025-08-19

### Added
- **FOUNDATION**: Major ClaudeSquad architecture implementation
- Complete multi-agent system foundation
- Core agent infrastructure and communication protocols
- Initial project structure and architectural decisions
- Basic agent specialization and routing capabilities

### Changed
- Established project foundation with comprehensive agent system
- Implemented core architectural patterns and conventions

---

## Version Numbering Convention

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.0.0): Incompatible API changes, major architecture shifts
- **MINOR** (X.Y.0): New functionality, features, or significant enhancements
- **PATCH** (X.Y.Z): Bug fixes, security patches, minor improvements

### Current Status: 0.14.1

The project is in active development (0.x.x versions). Version 1.0.0 will be released when:
- Complete installation and setup system is finalized
- All core agents are fully tested and documented
- Production-ready stability is achieved
- Comprehensive user documentation is complete

