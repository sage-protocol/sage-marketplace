---
name: sage-install
description: Install prompts or skills from Sage Protocol
allowed-tools: Bash(curl:*), Bash(python3:*), Bash(mkdir:*), Bash(cat:*), Bash(printf:*), Bash(test:*)
argument-hint: <source>
---

Install a prompt from Sage Protocol without requiring the CLI.

Sources:
- Prompt CID
- DAO + prompt key (format: `0xDAO#promptKey` or `0xDAO:promptKey`)

```bash
set -euo pipefail

SOURCE="${ARGUMENTS:-}"
if [ -z "$SOURCE" ]; then
  echo "Usage: /sage-install <cid | 0xDAO#promptKey>"
  exit 1
fi

WORKER_BASE="${SAGE_WORKER_BASE:-https://api.sageprotocol.io}"
CACHE_DIR="${HOME}/.sage/cache"
PROJECT_DIR="$(pwd)"
PROJECT_PROMPTS_DIR="${PROJECT_DIR}/prompts"
PROJECT_SAGE_DIR="${PROJECT_DIR}/.sage"
INSTALLED_MANIFEST="${PROJECT_SAGE_DIR}/installed.json"

mkdir -p "$CACHE_DIR" "$PROJECT_PROMPTS_DIR" "$PROJECT_SAGE_DIR"

is_cid() {
  printf "%s" "$1" | python3 - <<'PY'
import re, sys
cid = sys.stdin.read().strip()
v0 = re.match(r"^Qm[1-9A-HJ-NP-Za-km-z]{44}$", cid)
v1 = re.match(r"^b[a-z2-7]{50,}$", cid)
print("1" if (v0 or v1) else "0")
PY
}

is_dao() {
  printf "%s" "$1" | python3 - <<'PY'
import re, sys
dao = sys.stdin.read().strip()
print("1" if re.match(r"^0x[a-fA-F0-9]{40}$", dao) else "0")
PY
}

parse_dao_key() {
  python3 - <<'PY' "$SOURCE"
import sys
src = sys.argv[1]
sep = "#" if "#" in src else (":" if ":" in src else None)
if not sep:
  print("")
  sys.exit(0)
dao, key = src.split(sep, 1)
print(f"{dao} {key}")
PY
}

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
    # Fetch error body if available
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
      echo "If this prompt is from a public DAO/library, wait for sync or ensure it was published."
    else
      echo "Error: Failed to download prompt content."
    fi
    rm -f "$tmp_file"
    exit 1
  fi

  mv "$tmp_file" "$cache_file"

  local dest_file="${PROJECT_PROMPTS_DIR}/${key}.md"
  cp "$cache_file" "$dest_file"

  python3 - <<'PY' "$INSTALLED_MANIFEST" "$key" "$cid" "$SOURCE" "$dest_file"
import json, os, sys, time
manifest_path, key, cid, source, dest = sys.argv[1:6]
entry = {
  "key": key,
  "cid": cid,
  "source": source,
  "path": dest,
  "installedAt": int(time.time()),
}
data = {"items": []}
if os.path.exists(manifest_path):
  try:
    with open(manifest_path, "r") as f:
      data = json.load(f) or {"items": []}
  except Exception:
    data = {"items": []}
items = data.get("items") or []
items = [i for i in items if i.get("key") != key]
items.append(entry)
data["items"] = items
with open(manifest_path, "w") as f:
  json.dump(data, f, indent=2)
PY

  echo "✅ Installed prompt: ${key}"
  echo "   CID: ${cid}"
  echo "   Cached: ${cache_file}"
  echo "   Project: ${dest_file}"
}

if [ "$(is_cid "$SOURCE")" = "1" ]; then
  KEY="${SOURCE}"
  download_prompt "$SOURCE" "$KEY"
  exit 0
fi

DAO_KEY="$(parse_dao_key)"
if [ -n "$DAO_KEY" ]; then
  DAO="$(echo "$DAO_KEY" | awk '{print $1}')"
  KEY="$(echo "$DAO_KEY" | awk '{print $2}')"
  if [ "$(is_dao "$DAO")" != "1" ] || [ -z "$KEY" ]; then
    echo "Error: Invalid DAO or prompt key. Use 0xDAO#promptKey"
    exit 1
  fi

  MARKETPLACE_URL="${WORKER_BASE}/marketplace/library/${DAO}?all=true"
  MARKETPLACE_JSON="$(curl -fsSL "$MARKETPLACE_URL")"
  CID="$(python3 - <<'PY' "$MARKETPLACE_JSON" "$KEY"
import json, sys
data = json.loads(sys.argv[1])
key = sys.argv[2]
plugins = data.get("plugins", [])
for p in plugins:
  if p.get("name") == key:
    url = (p.get("source") or {}).get("url") or ""
    # Expect /ipfs/content/<cid> or /prompt/<cid>
    parts = url.split("/")
    if "ipfs" in parts and "content" in parts:
      idx = parts.index("content")
      if idx + 1 < len(parts):
        print(parts[idx+1])
        sys.exit(0)
    if "prompt" in parts:
      idx = parts.index("prompt")
      if idx + 1 < len(parts):
        print(parts[idx+1])
        sys.exit(0)
print("")
PY
)"

  if [ -z "$CID" ]; then
    echo "Error: Prompt key not found in DAO marketplace."
    exit 1
  fi

  SOURCE="${DAO}#${KEY}"
  download_prompt "$CID" "$KEY"
  exit 0
fi

echo "Error: Unsupported source. Use a prompt CID or 0xDAO#promptKey."
exit 1

```
