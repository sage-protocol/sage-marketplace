---
name: sage-update
description: Update installed Sage prompts and skills
allowed-tools: Bash(curl:*), Bash(python3:*), Bash(mkdir:*), Bash(cat:*), Bash(printf:*), Bash(test:*)
argument-hint: [key] [--all]
---

Update installed prompts to their latest versions using REST (no CLI).

```bash
set -euo pipefail

ARGS="${ARGUMENTS:-}"
WORKER_BASE="${SAGE_WORKER_BASE:-https://api.sageprotocol.io}"
CACHE_DIR="${HOME}/.sage/cache"
PROJECT_DIR="$(pwd)"
PROJECT_PROMPTS_DIR="${PROJECT_DIR}/prompts"
PROJECT_SAGE_DIR="${PROJECT_DIR}/.sage"
INSTALLED_MANIFEST="${PROJECT_SAGE_DIR}/installed.json"

mkdir -p "$CACHE_DIR" "$PROJECT_PROMPTS_DIR" "$PROJECT_SAGE_DIR"

if [ ! -f "$INSTALLED_MANIFEST" ]; then
  echo "{\"ok\":false,\"error\":\"No installed manifest found\"}"
  exit 1
fi

TARGET_KEY=""
UPDATE_ALL="0"
if echo "$ARGS" | grep -q -- "--all"; then
  UPDATE_ALL="1"
else
  TARGET_KEY="$(printf "%s" "$ARGS" | awk '{print $1}')"
fi

download_prompt() {
  local cid="$1"
  local key="$2"

  local cache_path="${CACHE_DIR}/${cid}"
  local cache_file="${cache_path}/prompt.md"
  mkdir -p "$cache_path"

  local url="${WORKER_BASE}/prompt/${cid}"
  local tmp_file
  tmp_file="$(mktemp)"

  if ! curl -fsSL "$url" -o "$tmp_file"; then
    local err
    err="$(curl -sS "$url" || true)"
    if echo "$err" | python3 - <<'PY'
import json, sys
try:
  data = json.loads(sys.stdin.read() or "{}")
  print("unknown_prompt" if data.get("error") == "unknown_prompt" else "")
except Exception:
  print("")
PY
    then
      echo "Error: Prompt CID is not allowlisted (unknown_prompt)."
    else
      echo "Error: Failed to download prompt content."
    fi
    rm -f "$tmp_file"
    return 1
  fi

  mv "$tmp_file" "$cache_file"
  local dest_file="${PROJECT_PROMPTS_DIR}/${key}.md"
  cp "$cache_file" "$dest_file"

python3 - <<'PY' "$INSTALLED_MANIFEST" "$key" "$cid" "$dest_file"
import json, os, sys, time
manifest_path, key, cid, dest = sys.argv[1:5]
data = {"items": []}
if os.path.exists(manifest_path):
  try:
    with open(manifest_path, "r") as f:
      data = json.load(f) or {"items": []}
  except Exception:
    data = {"items": []}
items = data.get("items") or []
for item in items:
  if item.get("key") == key:
    item["cid"] = cid
    item["path"] = dest
    item["updatedAt"] = int(time.time())
with open(manifest_path, "w") as f:
  json.dump(data, f, indent=2)
PY

  echo "✅ Updated prompt: ${key}"
  echo "   CID: ${cid}"
  return 0
}

items_json="$(cat "$INSTALLED_MANIFEST")"
python3 - <<'PY' "$items_json" "$TARGET_KEY" "$UPDATE_ALL" > /tmp/sage_update_items.json
import json, sys
data = json.loads(sys.argv[1]) if sys.argv[1] else {}
target = sys.argv[2]
all_flag = sys.argv[3] == "1"
items = data.get("items") or []
if all_flag:
  out = items
else:
  out = [i for i in items if i.get("key") == target]
print(json.dumps(out))
PY

UPDATED=0
python3 - <<'PY' /tmp/sage_update_items.json "$WORKER_BASE"
import json, sys
items = json.loads(open(sys.argv[1]).read() or "[]")
base = sys.argv[2]
for item in items:
  source = item.get("source") or ""
  key = item.get("key") or ""
  if "#" in source or ":" in source:
    sep = "#" if "#" in source else ":"
    dao, prompt_key = source.split(sep, 1)
    print(f"{dao} {prompt_key} {key}")
PY | while read -r DAO PROMPT_KEY KEY; do
  [ -z "$DAO" ] && continue
  MARKETPLACE_URL="${WORKER_BASE}/marketplace/library/${DAO}?all=true"
  MARKETPLACE_JSON="$(curl -fsSL "$MARKETPLACE_URL")"
  CID="$(python3 - <<'PY' "$MARKETPLACE_JSON" "$PROMPT_KEY"
import json, sys
data = json.loads(sys.argv[1])
key = sys.argv[2]
plugins = data.get("plugins", [])
for p in plugins:
  if p.get("name") == key:
    url = (p.get("source") or {}).get("url") or ""
    parts = url.split("/")
    if "ipfs" in parts and "content" in parts:
      idx = parts.index("content")
      if idx + 1 < len(parts):
        print(parts[idx+1]); sys.exit(0)
    if "prompt" in parts:
      idx = parts.index("prompt")
      if idx + 1 < len(parts):
        print(parts[idx+1]); sys.exit(0)
print("")
PY
)"
  if [ -z "$CID" ]; then
    echo "⚠️  Prompt ${KEY} not found in DAO marketplace"
    continue
  fi
  if download_prompt "$CID" "$KEY"; then
    UPDATED=$((UPDATED+1))
  fi
done

if [ "$UPDATE_ALL" = "0" ] && [ -z "$TARGET_KEY" ]; then
  echo "Usage: /sage-update <key> or /sage-update --all"
  exit 1
fi
```

Use `--all` to update all DAO-sourced dependencies, or specify a key to update one.
