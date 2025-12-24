---
name: sage-list
description: List installed Sage prompts and skills
allowed-tools: Bash(sage list:*), Bash(which sage:*)
---

List all installed prompts and skills from the workspace.

```bash
which sage || echo "Error: Sage CLI not installed. Run: npm install -g @sage-protocol/cli"
sage list --json
```
