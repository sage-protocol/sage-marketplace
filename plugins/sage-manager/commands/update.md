---
name: sage-update
description: Update installed Sage prompts and skills
allowed-tools: Bash(sage update:*), Bash(which sage:*)
argument-hint: [key] [--all]
---

Update installed dependencies to their latest versions.

```bash
which sage || echo "Error: Sage CLI not installed. Run: npm install -g @sage-protocol/cli"
sage update $ARGUMENTS --json
```

Use `--all` to update all dependencies, or specify a key to update one.
