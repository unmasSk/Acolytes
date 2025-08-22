# Smart Git Commit

I'll analyze your changes and create a meaningful commit message.

**Pre-Commit Quality Checks:**
Before committing, I'll verify:

- Build passes (if build command exists)
- Tests pass (if test command exists)
- Linter passes (if lint command exists)
- No obvious errors in changed files

First, let me check if this is a git repository and what's changed:

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

1. What files were modified
2. The nature of changes (feature, fix, refactor, etc.)
3. The scope/component affected

If the analysis or commit encounters errors:

- I'll explain what went wrong
- Suggest how to resolve it
- Ensure no partial commits occur

```bash
# If nothing is staged, I'll stage all changes (including untracked)
if git diff --cached --quiet; then
    echo "No files staged. Staging all changes..."
    git add -A
fi

# Show what will be committed
git diff --cached --name-status
```

Based on the analysis, I'll create a conventional commit message:

- **Type**: feat|fix|docs|style|refactor|test|chore
- **Scope**: component or area affected (optional)
- **Subject**: clear description in present tense
- **Body**: why the change was made (if needed)
- **Session ID**: automatically included from current session context

```bash
# First I'll get the current session ID from the system
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

# I'll create the commit with session ID in footer
# Example: git commit -m "fix(auth): resolve login timeout issue

# session_abc123def456"
```

The commit message will be concise, meaningful, follow your project's conventions, and include session traceability for better project tracking.

**Important**: I will NEVER:

- Add "Co-authored-by" or any Claude signatures
- Include "Generated with Claude Code" or similar messages
- Modify git config or user credentials
- Add any AI/assistant attribution to the commit
- Use emojis in commits, PRs, or git-related content

The commit will use only your existing git user configuration, maintaining full ownership and authenticity of your commits.
