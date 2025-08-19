# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-08-15

### Added
- **Git Workflow Commands**: Complete professional Git integration
  - `/commit` command with multi-agent analysis and linting
  - `/pr` command for automated pull request creation
  - `/issue` command for structured bug reporting
  - `/docs` command for documentation management
- **specialist-git Agent**: Professional Git workflow specialist
  - Conventional commits with 20 standardized types 
  - Advanced branching strategies (Git Flow, GitHub Flow)
  - Intelligent commit message generation
  - History cleanup and conflict resolution
- **Enhanced FLAGS System**: Improved cross-domain coordination
  - Streamlined agent-to-agent communication
  - Automated issue detection and routing
- **Agent Template Improvements**: Professional formatting standards
  - Enhanced dynamic agent creation templates
  - Simplified agent structure (model + color)
  - Professional documentation standards

### Changed
- **documentation-changelog Agent**: Enhanced with comprehensive versioning expertise
  - Complete semantic versioning rules
  - Automated changelog generation
  - Version bump analysis and recommendations
- **engineer-laravel Agent**: Simplified and streamlined structure
- **Setup System**: Updated phases for new Git workflow integration
- **Professional Standards**: Unified commit message format without emojis

### Removed
- **Environment Detection System**: Deprecated unused shell detection
  - Removed `.claude/memory/environment.json`
  - Removed `.claude/commands/detect-env.md` 
  - Removed `.claude/docs/environment-detection-flow.md`
- **Legacy MCP Configurations**: Cleaned up unused server definitions
- **Obsolete Documentation**: Removed outdated workflow files

### Security
- Added commit analysis for secrets detection
- Implemented pre-commit security validation
- Enhanced code review automation

---

**Migration Notes**: No breaking changes. New Git commands are optional additions to existing workflow.

## [2.0.0] - 2025-08-14

### Added
- Initial release of ClaudeSquad system
- 77 specialized agents architecture
- Dynamic agent creation system
- Dual memory systems (JSON local + MCP Server)
- FLAGS coordination protocol
- MCP server integrations

[2.1.0]: https://github.com/user/ClaudeSquad/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/user/ClaudeSquad/releases/tag/v2.0.0