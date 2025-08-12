# Dynamic Agent Upgrade Template

## Upgrade Metadata
- **Agent**: {{agent_name}}
- **Current Version**: {{current_version}}
- **New Version**: {{new_version}}
- **Upgrade Date**: {{upgrade_date}}
- **Reason**: {{upgrade_reason}}

## What Changed in the Module

### Structural Changes
{{#if structural_changes}}
#### New Directories
{{#each new_directories}}
- {{this.path}}: {{this.purpose}}
{{/each}}

#### Removed Directories
{{#each removed_directories}}
- {{this.path}}: {{this.reason}}
{{/each}}

#### Moved Components
{{#each moved_components}}
- {{this.from}} → {{this.to}}: {{this.reason}}
{{/each}}
{{/if}}

### New Components Added
{{#each new_components}}
#### {{this.name}}
- **Type**: {{this.type}}
- **Location**: {{this.location}}
- **Purpose**: {{this.purpose}}
- **Impact**: {{this.impact}}
- **Dependencies**: {{this.dependencies}}
{{/each}}

### Pattern Changes
{{#if pattern_changes}}
#### New Patterns Adopted
{{#each new_patterns}}
- **Pattern**: {{this.name}}
- **Reason**: {{this.reason}}
- **Implementation**: {{this.implementation}}
- **Files Affected**: {{this.affected_files}}
{{/each}}

#### Deprecated Patterns
{{#each deprecated_patterns}}
- **Pattern**: {{this.name}}
- **Replaced By**: {{this.replacement}}
- **Migration**: {{this.migration_guide}}
{{/each}}
{{/if}}

### Technology Updates
{{#if tech_updates}}
{{#each framework_updates}}
- **{{this.framework}}**: {{this.old_version}} → {{this.new_version}}
  - Breaking Changes: {{this.breaking_changes}}
  - Migration Done: {{this.migration_status}}
{{/each}}

{{#each new_dependencies}}
- **Added**: {{this.package}} ({{this.version}})
  - Purpose: {{this.purpose}}
  - Impact: {{this.impact}}
{{/each}}

{{#each removed_dependencies}}
- **Removed**: {{this.package}}
  - Reason: {{this.reason}}
  - Replaced By: {{this.replacement}}
{{/each}}
{{/if}}

### Performance Improvements
{{#if performance_improvements}}
{{#each optimizations}}
#### {{this.area}}
- **Before**: {{this.before_metrics}}
- **After**: {{this.after_metrics}}
- **Improvement**: {{this.improvement_percentage}}%
- **How**: {{this.technique}}
{{/each}}
{{/if}}

### New Business Rules
{{#each new_business_rules}}
- **Rule**: {{this.rule}}
- **Implementation**: {{this.implementation}}
- **Validation**: {{this.validation}}
- **Tests**: {{this.test_coverage}}
{{/each}}

### Security Enhancements
{{#if security_updates}}
{{#each security_fixes}}
- **Vulnerability**: {{this.type}}
- **Severity**: {{this.severity}}
- **Fix**: {{this.fix_description}}
- **Validation**: {{this.validation_method}}
{{/each}}
{{/if}}

## Updated Knowledge Base

### New Anti-patterns Discovered
{{#each new_antipatterns}}
- **Don't**: {{this.bad_practice}}
- **Why**: {{this.reason}}
- **Instead**: {{this.good_practice}}
- **Example**: {{this.example}}
{{/each}}

### Lessons Learned
{{#each lessons}}
- **Issue**: {{this.issue}}
- **Root Cause**: {{this.cause}}
- **Solution**: {{this.solution}}
- **Prevention**: {{this.prevention}}
{{/each}}

### Updated Best Practices
{{#each updated_practices}}
- **Practice**: {{this.practice}}
- **Old Way**: {{this.old_way}}
- **New Way**: {{this.new_way}}
- **Benefits**: {{this.benefits}}
{{/each}}

## Regression Risks

### Areas to Watch
{{#each risk_areas}}
- **Area**: {{this.area}}
- **Risk Level**: {{this.level}}
- **Potential Issues**: {{this.issues}}
- **Monitoring**: {{this.monitoring_strategy}}
{{/each}}

### Backward Compatibility
{{#if breaking_changes}}
⚠️ **Breaking Changes**:
{{#each breaking_changes}}
- {{this.change}}
  - Impact: {{this.impact}}
  - Migration: {{this.migration}}
{{/each}}
{{else}}
✅ **Fully backward compatible**
{{/if}}

## Updated Metrics

### Before Upgrade
```json
{{old_metrics}}
```

### After Upgrade
```json
{{new_metrics}}
```

### Delta Analysis
- **File Count**: {{file_count_delta}}
- **Line Count**: {{line_count_delta}}
- **Complexity**: {{complexity_delta}}
- **Test Coverage**: {{coverage_delta}}
- **Performance**: {{performance_delta}}

## Migration Checklist

### For Existing Code
{{#each migration_tasks}}
- [ ] {{this.task}}
  - Files: {{this.files}}
  - Effort: {{this.effort}}
  - Priority: {{this.priority}}
{{/each}}

### For Team Members
{{#each team_updates}}
- [ ] {{this.action}}
  - Who: {{this.responsible}}
  - When: {{this.timeline}}
{{/each}}

## Testing Requirements

### New Test Scenarios
{{#each new_test_scenarios}}
- **Scenario**: {{this.scenario}}
- **Type**: {{this.type}}
- **Priority**: {{this.priority}}
- **Coverage**: {{this.coverage}}
{{/each}}

### Regression Tests
{{#each regression_tests}}
- {{this.area}}: {{this.test_count}} tests
{{/each}}

## Communication Updates

### Updated Context Format
```json
{
  "version": "{{new_version}}",
  "new_capabilities": {{new_capabilities}},
  "deprecated_features": {{deprecated_features}},
  "migration_status": "{{migration_status}}"
}
```

### Review Criteria Updates
{{#each updated_review_criteria}}
- **New Criterion**: {{this.criterion}}
- **Applies To**: {{this.scope}}
- **Validation**: {{this.how_to_validate}}
{{/each}}

## Rollback Plan

### If Issues Arise
1. **Detection**: {{rollback_triggers}}
2. **Decision**: {{decision_criteria}}
3. **Execution**: {{rollback_steps}}
4. **Validation**: {{rollback_validation}}

### Preserved State
- **Backup Location**: {{backup_location}}
- **Backup Version**: {{backup_version}}
- **Recovery Time**: {{recovery_estimate}}

---

## Upgrade Summary

**From Version {{current_version}} to {{new_version}}**

### Key Improvements
{{#each key_improvements}}
- {{this}}
{{/each}}

### Action Required
{{#each required_actions}}
- {{this.who}}: {{this.action}} by {{this.when}}
{{/each}}

### Next Review Date
**{{next_review_date}}** - Check for further optimizations and updates

---

*This upgrade enhances my understanding of the {{module_name}} module, incorporating {{days_of_learning}} days of learning and {{change_count}} changes.*