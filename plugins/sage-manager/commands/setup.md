---
name: sage-setup
description: Install the Sage Protocol CLI
allowed-tools: Bash(npm install:*), Bash(which:*)
---

Install the Sage Protocol CLI globally.

```bash
# Check if already installed
if which sage > /dev/null 2>&1; then
  echo "✅ Sage CLI already installed: $(sage --version)"
  exit 0
fi

# Install globally
npm install -g @sage-protocol/cli

# Verify installation
if which sage > /dev/null 2>&1; then
  echo "✅ Sage CLI installed successfully: $(sage --version)"
else
  echo "❌ Installation failed. Try running manually: npm install -g @sage-protocol/cli"
  exit 1
fi
```
