# 📦 VERSION UPDATE GUIDE

## 📋 FILES TO UPDATE WHEN CHANGING VERSION

### 1️⃣ **CORE PACKAGE FILES** (Required)
| File | Location | Update |
|------|----------|--------|
| `pyproject.toml` | `acolytes/pyproject.toml` | `version = "X.Y.Z"` |
| `setup.py` | `acolytes/setup.py` | `version="X.Y.Z"` |
| `__init__.py` | `acolytes/acolytes/__init__.py` | `__version__ = "X.Y.Z"` |
| `init_command.py` | `acolytes/acolytes/commands/init_command.py` | `"version": "X.Y.Z"` in settings dict |

### 2️⃣ **DOCUMENTATION** (Required)
| File | Location | Update |
|------|----------|--------|
| `CHANGELOG.md` | Root directory | Add new version entry with date |

### 3️⃣ **README FILES** (Recommended)
| File | Location | Update |
|------|----------|--------|
| `README.md` | Root directory | Version badge or mention |
| `README.md` | `acolytes/README.md` | PyPI package version |

### 4️⃣ **ADDITIONAL DOCUMENTATION** (If exists)
| File | Location | Update |
|------|----------|--------|
| `PIP_INSTALLATION_FLOW.md` | Root directory | Version references |
| `settings.json` | `.claude/settings.json` | `"version": "X.Y.Z"` |

---

## 🤖 HOW PROFESSIONALS MANAGE VERSION UPDATES

### **1. Manual Update (Small Projects)**
```bash
# Update each file manually
# Error-prone, tedious for many files
```

### **2. bump2version / bumpversion (Python Standard)**
```bash
# Install
pip install bump2version

# Configuration file: .bumpversion.cfg
[bumpversion]
current_version = 1.0.0
commit = True
tag = True

[bumpversion:file:setup.py]
[bumpversion:file:acolytes/__init__.py]
[bumpversion:file:pyproject.toml]

# Usage
bump2version patch  # 1.0.0 -> 1.0.1
bump2version minor  # 1.0.0 -> 1.1.0
bump2version major  # 1.0.0 -> 2.0.0
```

### **3. poetry (Modern Python)**
```bash
# If using poetry for package management
poetry version patch  # 1.0.0 -> 1.0.1
poetry version minor  # 1.0.0 -> 1.1.0
poetry version major  # 1.0.0 -> 2.0.0
```

### **4. setuptools-scm (Git-based)**
```python
# setup.py
setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
# Version from git tags automatically
```

### **5. Custom Script (Full Control)**
```python
#!/usr/bin/env python
# update_version.py
import re
import sys
from pathlib import Path

def update_version(new_version):
    """Update version in all required files."""
    
    files_to_update = [
        ('acolytes/pyproject.toml', r'version = "[^"]*"', f'version = "{new_version}"'),
        ('acolytes/setup.py', r'version="[^"]*"', f'version="{new_version}"'),
        ('acolytes/acolytes/__init__.py', r'__version__ = "[^"]*"', f'__version__ = "{new_version}"'),
        ('acolytes/acolytes/commands/init_command.py', r'"version": "[^"]*"', f'"version": "{new_version}"'),
    ]
    
    for filepath, pattern, replacement in files_to_update:
        path = Path(filepath)
        if path.exists():
            content = path.read_text()
            updated = re.sub(pattern, replacement, content)
            path.write_text(updated)
            print(f"✅ Updated {filepath}")
        else:
            print(f"⚠️ File not found: {filepath}")
    
    # Update CHANGELOG
    print("📝 Don't forget to update CHANGELOG.md manually!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_version.py X.Y.Z")
        sys.exit(1)
    
    new_version = sys.argv[1]
    update_version(new_version)
```

### **6. npm-style (package.json)**
```bash
# If it were a Node.js project
npm version patch  # Updates package.json and creates git tag
npm version minor
npm version major
```

### **7. Makefile Approach**
```makefile
# Makefile
VERSION := $(shell python -c "import acolytes; print(acolytes.__version__)")

bump-patch:
	python update_version.py $(shell python -c "v='$(VERSION)'.split('.'); print(f'{v[0]}.{v[1]}.{int(v[2])+1}')")

bump-minor:
	python update_version.py $(shell python -c "v='$(VERSION)'.split('.'); print(f'{v[0]}.{int(v[1])+1}.0')")

bump-major:
	python update_version.py $(shell python -c "v='$(VERSION)'.split('.'); print(f'{int(v[0])+1}.0.0')")
```

### **8. GitHub Actions (CI/CD)**
```yaml
# .github/workflows/version-bump.yml
name: Bump version
on:
  push:
    branches: [main]
jobs:
  bump:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Bump version and push tag
        uses: anothrNick/github-tag-action@1.26.0
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          WITH_V: true
```

---

## 🎯 RECOMMENDED APPROACH FOR ACOLYTES

### **Option 1: bump2version (Easiest)**

Create `.bumpversion.cfg`:
```ini
[bumpversion]
current_version = 1.0.0
commit = True
tag = True
message = 🔖 Bump version: {current_version} → {new_version}

[bumpversion:file:acolytes/pyproject.toml]
[bumpversion:file:acolytes/setup.py]
[bumpversion:file:acolytes/acolytes/__init__.py]
[bumpversion:file:acolytes/acolytes/commands/init_command.py]
search = "version": "{current_version}"
replace = "version": "{new_version}"
```

Usage:
```bash
bump2version patch  # For bug fixes: 1.0.0 -> 1.0.1
bump2version minor  # For new features: 1.0.0 -> 1.1.0  
bump2version major  # For breaking changes: 1.0.0 -> 2.0.0
```

### **Option 2: Custom Python Script (More Control)**

Save the script above as `update_version.py` and use:
```bash
python update_version.py 1.0.1
```

---

## 📝 SEMANTIC VERSIONING RULES

```
MAJOR.MINOR.PATCH

MAJOR: Breaking changes (incompatible API changes)
MINOR: New features (backwards compatible)
PATCH: Bug fixes (backwards compatible)

Examples:
1.0.0 -> 1.0.1  # Fixed a bug
1.0.1 -> 1.1.0  # Added new agents
1.1.0 -> 2.0.0  # Changed how FLAGS work (breaking)
```

---

## ✅ CHECKLIST FOR VERSION RELEASE

- [ ] Update version in all files
- [ ] Update CHANGELOG.md with changes
- [ ] Commit with message: `🔖 Bump version: X.Y.Z`
- [ ] Create git tag: `git tag -a vX.Y.Z -m "Version X.Y.Z"`
- [ ] Push changes: `git push && git push --tags`
- [ ] Build package: `python -m build`
- [ ] Upload to PyPI: `twine upload dist/*`
- [ ] Create GitHub release from tag

---

## 🚀 QUICK COMMANDS

```bash
# See current version
python -c "import acolytes; print(acolytes.__version__)"

# Update all files manually (one-liner)
find . -name "*.py" -o -name "*.toml" | xargs sed -i 's/1.0.0/1.0.1/g'

# Create git tag
git tag -a v1.0.1 -m "Release version 1.0.1"

# Push to PyPI
python -m build
twine upload dist/*
```