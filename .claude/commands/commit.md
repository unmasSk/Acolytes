# Smart Git Commit with Emoji System

I'll analyze your changes and create a meaningful commit message with appropriate emoji based on awesome-claude-code's 110+ emoji classification system.

**Pre-Commit Quality Checks:**
Before committing, I'll verify:

- Build passes (if build command exists)
- Tests pass (if test command exists)
- Linter passes (if lint command exists)
- No obvious errors in changed files

## Emoji Classification System

I'll automatically select the most appropriate emoji based on file changes and commit type:

### Core Types
- ✨ `feat`: New feature
- 🐛 `fix`: Bug fix
- 📝 `docs`: Documentation
- 💄 `style`: Formatting/style
- ♻️ `refactor`: Code refactoring
- ⚡️ `perf`: Performance improvements
- ✅ `test`: Tests
- 🔧 `chore`: Tooling, configuration

### Extended Classification
- 🚀 `ci`: CI/CD improvements
- 🗑️ `revert`: Reverting changes
- 🧪 `test`: Add a failing test
- 🚨 `fix`: Fix compiler/linter warnings
- 🔒️ `fix`: Fix security issues
- 👥 `chore`: Add or update contributors
- 🚚 `refactor`: Move or rename resources
- 🏗️ `refactor`: Make architectural changes
- 🔀 `chore`: Merge branches
- 📦️ `chore`: Add or update compiled files or packages
- ➕ `chore`: Add a dependency
- ➖ `chore`: Remove a dependency
- 🌱 `chore`: Add or update seed files
- 🧑‍💻 `chore`: Improve developer experience
- 🧵 `feat`: Add or update code related to multithreading or concurrency
- 🔍️ `feat`: Improve SEO
- 🏷️ `feat`: Add or update types
- 💬 `feat`: Add or update text and literals
- 🌐 `feat`: Internationalization and localization
- 👔 `feat`: Add or update business logic
- 📱 `feat`: Work on responsive design
- 🚸 `feat`: Improve user experience / usability
- 🩹 `fix`: Simple fix for a non-critical issue
- 🥅 `fix`: Catch errors
- 👽️ `fix`: Update code due to external API changes
- 🔥 `fix`: Remove code or files
- 🎨 `style`: Improve structure/format of the code
- 🚑️ `fix`: Critical hotfix
- 🎉 `chore`: Begin a project
- 🔖 `chore`: Release/Version tags
- 🚧 `wip`: Work in progress
- 💚 `fix`: Fix CI build
- 📌 `chore`: Pin dependencies to specific versions
- 👷 `ci`: Add or update CI build system
- 📈 `feat`: Add or update analytics or tracking code
- ✏️ `fix`: Fix typos
- ⏪️ `revert`: Revert changes
- 📄 `chore`: Add or update license
- 💥 `feat`: Introduce breaking changes
- 🍱 `assets`: Add or update assets
- ♿️ `feat`: Improve accessibility
- 💡 `docs`: Add or update comments in source code
- 🗃️ `db`: Perform database related changes
- 🔊 `feat`: Add or update logs
- 🔇 `fix`: Remove logs
- 🤡 `test`: Mock things
- 🥚 `feat`: Add or update an easter egg
- 🙈 `chore`: Add or update .gitignore file
- 📸 `test`: Add or update snapshots
- ⚗️ `experiment`: Perform experiments
- 🚩 `feat`: Add, update, or remove feature flags
- 💫 `ui`: Add or update animations and transitions
- ⚰️ `refactor`: Remove dead code
- 🦺 `feat`: Add or update code related to validation
- ✈️ `feat`: Improve offline support

First, let me check the repository status and analyze changes:

```bash
# Verify we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not a git repository"
    echo "This command requires git version control"
    exit 1
fi

# Check if we have changes to commit
if ! git diff --cached --quiet || ! git diff --quiet; then
    echo "Changes detected:"
    git status --short
else
    echo "No changes to commit"
    exit 0
fi

# Show detailed changes
git diff --cached --stat
git diff --stat
```

Now I'll analyze the changes to determine:

1. **File types**: Configuration, source code, documentation, assets
2. **Change patterns**: New files, deletions, modifications, renames
3. **Content analysis**: Feature additions, bug fixes, refactoring, etc.
4. **Scope detection**: Components or areas affected

## Smart Emoji Selection Logic

Based on file analysis, I'll select the most appropriate emoji:

- **package.json/requirements.txt changes**: ➕ (add dependency) or ➖ (remove dependency)
- **.gitignore changes**: 🙈 (update .gitignore)
- **CI/CD files**: 🚀 (CI improvements) or 👷 (CI build system)
- **Documentation files**: 📝 (docs) or 💡 (code comments)
- **Test files**: ✅ (tests), 🧪 (failing test), 📸 (snapshots), 🤡 (mocks)
- **Security fixes**: 🔒️ (security issues)
- **Performance**: ⚡️ (performance improvements)
- **UI/UX**: 💄 (style), 📱 (responsive), 🚸 (UX), 💫 (animations)
- **Database**: 🗃️ (database changes)
- **Breaking changes**: 💥 (breaking changes)
- **Critical fixes**: 🚑️ (critical hotfix)
- **Code structure**: 🎨 (structure), ♻️ (refactor), ⚰️ (dead code)
- **Assets**: 🍱 (assets)
- **Accessibility**: ♿️ (accessibility)
- **Logs**: 🔊 (add logs), 🔇 (remove logs)
- **Feature flags**: 🚩 (feature flags)
- **Validation**: 🦺 (validation)
- **Offline support**: ✈️ (offline support)

```bash
# If nothing is staged, I'll stage all changes (including untracked)
if git diff --cached --quiet; then
    echo "No files staged. Staging all changes..."
    git add -A
fi

# Show what will be committed
git diff --cached --name-status
```

I'll create a conventional commit message with emoji:

**Format**: `emoji type(scope): description`
- **Emoji**: Automatically selected from 110+ classification
- **Type**: Conventional commit type (feat, fix, docs, etc.)
- **Scope**: Component or area affected (optional)
- **Description**: Clear description in present tense
- **Session ID**: Included in footer for traceability

```bash
# Get current session ID from SQLite database
SESSION_ID=$(cd .claude && python -c "
import sqlite3
import os
db_path = os.path.join('memory', 'project.db')
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('SELECT session_id FROM sessions ORDER BY created_at DESC LIMIT 1')
    result = cursor.fetchone()
    print(result[0] if result else 'unknown')
    conn.close()
except Exception as e:
    print('unknown')
")

# Create commit with emoji, conventional format, and session tracking
# Example: "✨ feat(auth): add OAuth2 integration with GitHub

# session_abc123def456"
```

The commit will be:
- **Visually clear**: Emoji makes commit type immediately recognizable
- **Conventional**: Follows standard commit message format
- **Contextual**: Emoji selection based on actual changes
- **Traceable**: Includes session ID for project tracking
- **Professional**: Maintains git authorship integrity

**Commit Message Examples:**

- `✨ feat(auth): add OAuth2 integration with GitHub`
- `🐛 fix(api): resolve timeout issue in user endpoints`
- `📝 docs(readme): update installation instructions`
- `⚡️ perf(database): optimize query performance for user lookup`
- `🔒️ fix(security): patch XSS vulnerability in form validation`
- `🧪 test(auth): add failing test for login edge cases`
- `♻️ refactor(components): extract reusable validation logic`
- `➕ chore(deps): add lodash for utility functions`
- `🎨 style(components): improve code structure and formatting`
- `🚑️ fix(critical): patch memory leak in session handler`

**Important**: This system maintains full git authorship integrity while providing enhanced visual context for commit history browsing.

**I will NEVER:**

- Add "Co-authored-by" or any Claude signatures
- Include "Generated with Claude Code" or similar messages
- Modify git config or user credentials
- Add any AI/assistant attribution to the commit

The commit will use only your existing git user configuration, maintaining full ownership and authenticity of your commits.
