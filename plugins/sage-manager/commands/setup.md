---
name: sage-setup
description: Install and configure Sage Protocol CLIs (sage + scroll)
allowed-tools: Bash(which:*), Bash(npm:*), Bash(cargo:*), Bash(uname:*), Bash(tr:*), Bash(head:*), Bash(grep:*), Bash(date:*), Bash(scroll:*), Bash(sage:*), Bash(claude:*), Bash(mkdir:*), Bash(cat:*)
---

Detect and install Sage Protocol CLIs. This sets up:
- **sage** (Node.js) - Full governance, bounties, NFTs, treasury
- **scroll** (Rust) - MCP hub, fast library sync, daemon

```bash
set -euo pipefail

echo "┌─ Sage Protocol CLI Setup ─────────────────────────────────────────────┐"
echo "│                                                                        │"

# ============================================================================
# Platform Detection
# ============================================================================

OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

case "$OS" in
  darwin) OS_DISPLAY="macOS" ;;
  linux)  OS_DISPLAY="Linux" ;;
  mingw*|msys*|cygwin*) OS_DISPLAY="Windows"; OS="windows" ;;
  *) OS_DISPLAY="$OS" ;;
esac

case "$ARCH" in
  x86_64|amd64) ARCH_DISPLAY="x86_64" ;;
  aarch64|arm64) ARCH_DISPLAY="ARM64" ;;
  *) ARCH_DISPLAY="$ARCH" ;;
esac

echo "│  Platform: $OS_DISPLAY ($ARCH_DISPLAY)"
echo "│                                                                        │"

# ============================================================================
# Check Current State
# ============================================================================

SAGE_STATUS="missing"
SCROLL_STATUS="missing"

if command -v sage >/dev/null 2>&1; then
  SAGE_VER=$(sage --version 2>/dev/null | head -1 || echo "installed")
  echo "│  sage:   [OK] $SAGE_VER"
  SAGE_STATUS="installed"
else
  echo "│  sage:   [--] Not installed"
fi

if command -v scroll >/dev/null 2>&1; then
  SCROLL_VER=$(scroll --version 2>/dev/null | head -1 || echo "installed")
  echo "│  scroll: [OK] $SCROLL_VER"
  SCROLL_STATUS="installed"
else
  echo "│  scroll: [--] Not installed (optional - MCP hub)"
fi

echo "│                                                                        │"
echo "└────────────────────────────────────────────────────────────────────────┘"
echo ""

# Exit early if both installed
if [ "$SAGE_STATUS" = "installed" ] && [ "$SCROLL_STATUS" = "installed" ]; then
  echo "All CLIs installed. Checking MCP registration..."

  # Check if scroll MCP is registered
  if command -v claude >/dev/null 2>&1; then
    if claude mcp list 2>/dev/null | grep -q "scroll"; then
      echo "[OK] scroll MCP already registered"
    else
      echo "Registering scroll as MCP server..."
      claude mcp add scroll -- scroll serve && echo "[OK] scroll MCP registered"
    fi
  fi

  echo ""
  echo "Setup complete. Run 'sage doctor' to verify configuration."
  exit 0
fi

# ============================================================================
# Install sage CLI (Node.js)
# ============================================================================

if [ "$SAGE_STATUS" = "missing" ]; then
  echo "Installing sage CLI..."

  if command -v npm >/dev/null 2>&1; then
    npm install -g @sage-protocol/cli
    if command -v sage >/dev/null 2>&1; then
      SAGE_VER=$(sage --version 2>/dev/null | head -1)
      echo "[OK] sage installed: $SAGE_VER"
      SAGE_STATUS="installed"
    else
      echo "[!!] sage installation failed"
    fi
  else
    echo "[!!] npm not found"
    echo "     Install Node.js from https://nodejs.org"
    echo "     Then run: npm install -g @sage-protocol/cli"
  fi
  echo ""
fi

# ============================================================================
# Install/Detect scroll CLI (Rust - optional)
# ============================================================================

if [ "$SCROLL_STATUS" = "missing" ]; then
  echo "Checking scroll CLI (optional - enables MCP hub)..."

  if command -v cargo >/dev/null 2>&1; then
    echo "Attempting to install scroll via cargo..."
    echo "(This requires access to the sage-protocol/scroll repo)"

    # Try cargo install - will fail if no repo access (that's OK)
    if cargo install --git https://github.com/sage-protocol/scroll.git 2>/dev/null; then
      if command -v scroll >/dev/null 2>&1; then
        SCROLL_VER=$(scroll --version 2>/dev/null | head -1)
        echo "[OK] scroll installed: $SCROLL_VER"
        SCROLL_STATUS="installed"
      fi
    else
      echo "[--] scroll not installed (repo access required)"
      echo "     The plugin works without scroll, using sage CLI only."
      echo "     scroll adds: MCP hub, daemon, faster library sync"
    fi
  else
    echo "[--] cargo not found (Rust toolchain not installed)"
    echo "     The plugin works without scroll, using sage CLI only."
    echo "     To install scroll later: cargo install --git https://github.com/sage-protocol/scroll.git"
  fi
  echo ""
fi

# ============================================================================
# Register scroll MCP (if installed)
# ============================================================================

if [ "$SCROLL_STATUS" = "installed" ]; then
  if command -v claude >/dev/null 2>&1; then
    echo "Registering scroll as MCP server..."
    if claude mcp list 2>/dev/null | grep -q "scroll"; then
      echo "[OK] scroll MCP already registered"
    else
      claude mcp add scroll -- scroll serve && echo "[OK] scroll MCP registered"
    fi
    echo ""
  fi
fi

# ============================================================================
# Save CLI Status
# ============================================================================

mkdir -p ~/.config/sage-manager
cat > ~/.config/sage-manager/cli-status.json << EOF
{
  "sage": {
    "available": $([ "$SAGE_STATUS" = "installed" ] && echo true || echo false),
    "version": "$(sage --version 2>/dev/null | head -1 || echo null)"
  },
  "scroll": {
    "available": $([ "$SCROLL_STATUS" = "installed" ] && echo true || echo false),
    "version": "$(scroll --version 2>/dev/null | head -1 || echo null)"
  },
  "detected_at": "$(date -Iseconds 2>/dev/null || date)"
}
EOF

# ============================================================================
# Final Status
# ============================================================================

echo "┌─ Setup Complete ───────────────────────────────────────────────────────┐"
echo "│                                                                        │"

if [ "$SAGE_STATUS" = "installed" ]; then
  echo "│  sage:   [OK] Ready for governance, bounties, NFTs                   │"
else
  echo "│  sage:   [!!] Not installed - some features unavailable              │"
fi

if [ "$SCROLL_STATUS" = "installed" ]; then
  echo "│  scroll: [OK] MCP hub available                                      │"
else
  echo "│  scroll: [--] Not installed (optional)                               │"
fi

echo "│                                                                        │"
echo "│  Next steps:                                                           │"
echo "│    - Connect wallet: sage wallet connect-privy                         │"
if [ "$SCROLL_STATUS" = "installed" ]; then
  echo "│    - Start daemon:   scroll daemon start                               │"
fi
echo "│    - Run diagnostics: sage doctor                                      │"
echo "│                                                                        │"
echo "└────────────────────────────────────────────────────────────────────────┘"
```
