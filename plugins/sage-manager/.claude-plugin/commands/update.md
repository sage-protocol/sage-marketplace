---
name: sage-update
description: Update installed Sage prompts and skills
allowed-tools: Bash(sage update:*), Bash(which sage:*)
argument-hint: [key] [--all]
---

Update installed dependencies to their latest versions.

```bash
if ! which sage >/dev/null 2>&1; then
  echo "Error: Sage CLI not installed. Run: /sage-setup"
  exit 1
fi

sage update $ARGUMENTS --json
```

Use `--all` to update all dependencies, or specify a key to update one.
