---
name: sage-list
description: List installed Sage prompts and skills
allowed-tools: Bash(which:*), Bash(sage:*)
---

List all installed prompts and skills from the workspace.

```bash
set -euo pipefail

if ! which sage >/dev/null 2>&1; then
  echo "Error: Sage CLI not installed. Run: /sage-setup"
  exit 1
fi

sage list --json
```
