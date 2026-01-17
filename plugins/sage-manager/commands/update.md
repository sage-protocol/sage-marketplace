---
name: sage-update
description: Update installed Sage prompts and skills
allowed-tools: Bash(which:*), Bash(sage:*)
argument-hint: [key] [--all]
---

Update installed dependencies to their latest versions.

```bash
set -euo pipefail

if ! which sage >/dev/null 2>&1; then
  echo "Error: Sage CLI not installed. Run: /sage-setup"
  exit 1
fi

ARGS="${ARGUMENTS:-}"

if [ -z "$ARGS" ]; then
  echo "Usage:"
  echo "  /sage-update --all"
  echo "  /sage-update <dependency-key>"
  echo ""
  echo "Tip: run /sage-list to see keys."
  exit 1
fi

sage update $ARGS --json
```

Use `--all` to update all dependencies, or specify a key to update one.
