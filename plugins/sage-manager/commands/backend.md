---
name: sage-backend
description: Show CLI backend status and configure preferences (scroll vs sage)
allowed-tools: Bash(which:*), Bash(scroll:*), Bash(sage:*), Bash(claude:*), Bash(cat:*), Bash(mkdir:*), Bash(echo:*), Bash(grep:*), Bash(sed:*), Bash(date:*)
argument-hint: [show|prefer <scroll|sage|auto>]
---

Show backend status and configure CLI preferences for the sage-manager plugin.

**Commands:**
- `/sage-backend` or `/sage-backend show` - Display current CLI status
- `/sage-backend prefer scroll` - Prefer scroll for speed/MCP
- `/sage-backend prefer sage` - Prefer sage for full features
- `/sage-backend prefer auto` - Auto-select based on operation

```bash
set -euo pipefail

ACTION="${ARGUMENTS:-show}"
PREF_FILE="$HOME/.config/sage-manager/preferences.json"
STATUS_FILE="$HOME/.config/sage-manager/cli-status.json"

# ============================================================================
# Helper Functions
# ============================================================================

show_status() {
  echo "┌─ Sage Protocol Backend Status ─────────────────────────────────────────┐"
  echo "│                                                                        │"

  # Check sage
  if command -v sage >/dev/null 2>&1; then
    SAGE_VER=$(sage --version 2>/dev/null | head -1 || echo "installed")
    echo "│  sage:   [OK] $SAGE_VER"
  else
    echo "│  sage:   [--] Not installed"
  fi

  # Check scroll
  if command -v scroll >/dev/null 2>&1; then
    SCROLL_VER=$(scroll --version 2>/dev/null | head -1 || echo "installed")
    echo "│  scroll: [OK] $SCROLL_VER"

    # Check daemon
    if scroll daemon status 2>/dev/null | grep -q "running"; then
      echo "│  daemon: [OK] Running"
    else
      echo "│  daemon: [--] Not running"
    fi
  else
    echo "│  scroll: [--] Not installed (optional)"
  fi

  echo "│                                                                        │"

  # Check MCP registration
  if command -v claude >/dev/null 2>&1; then
    if claude mcp list 2>/dev/null | grep -q "scroll"; then
      echo "│  MCP:    [OK] scroll registered as MCP server"
    else
      echo "│  MCP:    [--] scroll not registered"
    fi
  fi

  echo "│                                                                        │"

  # Show current preference
  if [ -f "$PREF_FILE" ]; then
    PREF=$(cat "$PREF_FILE" | grep -o '"preferred_backend"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/.*"\([^"]*\)"$/\1/')
    echo "│  Preference: $PREF"
  else
    echo "│  Preference: auto (default)"
  fi

  echo "│                                                                        │"
  echo "│  Commands:                                                             │"
  echo "│    /sage-backend prefer scroll  - Use scroll for speed                 │"
  echo "│    /sage-backend prefer sage    - Use sage for full features           │"
  echo "│    /sage-backend prefer auto    - Auto-select per operation            │"
  echo "│                                                                        │"
  echo "└────────────────────────────────────────────────────────────────────────┘"
}

set_preference() {
  local pref="$1"

  case "$pref" in
    scroll|sage|auto)
      mkdir -p "$HOME/.config/sage-manager"
      cat > "$PREF_FILE" << EOF
{
  "preferred_backend": "$pref",
  "fallback_enabled": true,
  "updated_at": "$(date -Iseconds 2>/dev/null || date)"
}
EOF
      echo "Preference set to: $pref"
      echo ""
      echo "Backend routing:"
      case "$pref" in
        scroll)
          echo "  - Read operations: scroll MCP / CLI first"
          echo "  - Write operations: sage CLI (required for signing)"
          ;;
        sage)
          echo "  - All operations: sage CLI"
          ;;
        auto)
          echo "  - Read operations: MCP if available, else fastest CLI"
          echo "  - Write operations: sage CLI (required for signing)"
          ;;
      esac
      ;;
    *)
      echo "Invalid preference: $pref"
      echo "Valid options: scroll, sage, auto"
      exit 1
      ;;
  esac
}

# ============================================================================
# Main
# ============================================================================

case "$ACTION" in
  show|"")
    show_status
    ;;
  prefer\ scroll|prefer\ sage|prefer\ auto)
    PREF=$(echo "$ACTION" | sed 's/prefer //')
    set_preference "$PREF"
    ;;
  prefer)
    echo "Usage: /sage-backend prefer <scroll|sage|auto>"
    exit 1
    ;;
  *)
    echo "Unknown action: $ACTION"
    echo ""
    echo "Usage:"
    echo "  /sage-backend              - Show status"
    echo "  /sage-backend show         - Show status"
    echo "  /sage-backend prefer <x>   - Set preference (scroll|sage|auto)"
    exit 1
    ;;
esac
```
