---
name: sage-install
description: Install prompts or skills via the Sage CLI (skills auto-activate in Claude Code)
allowed-tools: Bash(which sage:*), Bash(sage install:*), Bash(mkdir:*), Bash(cp:*), Bash(mv:*), Bash(ls:*)
argument-hint: <source>
---

Install prompts or skills using the Sage CLI.

**Sources:**
- `bafkrei...` - CID (IPFS content address)
- `0x...` - DAO address (installs DAO's library)
- `github:org/repo` - GitHub repository
- `skill-name` - Bundled skill from CLI

**Skill Auto-Discovery:**
Skills containing SKILL.md are installed to `.claude/skills/` for automatic activation.
Prompts go to the workspace's `.sage/prompts/` directory.

```bash
set -euo pipefail

SOURCE="${ARGUMENTS:-}"
if [ -z "$SOURCE" ]; then
  echo "Usage: /sage-install <cid | 0xDAO | github:org/repo | skill-name>"
  echo ""
  echo "Examples:"
  echo "  /sage-install bafkreiab...          # Install from IPFS CID"
  echo "  /sage-install 0x61835...            # Install from DAO library"
  echo "  /sage-install github:sage/prompts   # Install from GitHub"
  echo "  /sage-install my-custom-skill       # Install bundled skill"
  exit 1
fi

# Ensure CLI is installed
if ! which sage >/dev/null 2>&1; then
  echo "Installing Sage CLI..."
  npm install -g @sage-protocol/cli
fi

# Install to temp location first to inspect
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "Fetching: $SOURCE"
sage install "$SOURCE" --to "$TEMP_DIR" --yes --json 2>/dev/null || sage install "$SOURCE" --to "$TEMP_DIR" --yes

# Check if it's a skill (has SKILL.md)
if [ -f "$TEMP_DIR/SKILL.md" ]; then
  # It's a skill - install to .claude/skills/
  SKILL_NAME=$(basename "$SOURCE" | sed 's/^0x.*/dao-skill/' | sed 's/^bafk.*/ipfs-skill/' | sed 's/github://' | tr '/' '-')
  SKILL_DIR=".claude/skills/$SKILL_NAME"

  mkdir -p "$SKILL_DIR"
  cp -r "$TEMP_DIR"/* "$SKILL_DIR/"

  echo ""
  echo "Skill installed to: $SKILL_DIR"
  echo "Restart Claude Code or start new conversation to activate."
elif [ -d "$TEMP_DIR" ] && [ "$(ls -A $TEMP_DIR)" ]; then
  # It's prompts - install to .sage/prompts/
  mkdir -p ".sage/prompts"
  cp -r "$TEMP_DIR"/* ".sage/prompts/"

  echo ""
  echo "Prompts installed to: .sage/prompts/"
  echo "Use 'sage list' to see installed prompts."
else
  echo "Error: Nothing was installed"
  exit 1
fi
```
