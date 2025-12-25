---
name: sage-list
description: List installed Sage prompts and skills
allowed-tools: Bash(python3:*), Bash(test:*)
---

List all installed prompts and skills from the workspace.

```bash
set -euo pipefail

MANIFEST_FILE="$(pwd)/.sage/installed.json"
if [ ! -f "$MANIFEST_FILE" ]; then
  echo "{\"ok\":true,\"items\":[]}"
  exit 0
fi

python3 - <<'PY' "$MANIFEST_FILE"
import json, sys
path = sys.argv[1]
try:
  with open(path, "r") as f:
    data = json.load(f) or {}
except Exception:
  data = {}
items = data.get("items") or []
print(json.dumps({"ok": True, "items": items}, indent=2))
PY
```
