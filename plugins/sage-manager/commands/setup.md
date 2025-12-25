---
name: sage-setup
description: Install the Sage CLI for plugin commands
allowed-tools: Bash(npm install:*), Bash(which sage:*)
---

Install the Sage CLI (required for /sage-install, /sage-list, /sage-update).

```bash
which sage || npm install -g @sage-protocol/cli
```
