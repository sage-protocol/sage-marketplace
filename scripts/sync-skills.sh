#!/bin/bash
set -e

WORKER_URL="${WORKER_URL:-https://api.sageprotocol.io}"
PLUGINS_DIR="plugins"
MARKETPLACE_FILE=".claude-plugin/marketplace.json"

echo "Fetching skills from $WORKER_URL/marketplace/skills..."
skills=$(curl -s "$WORKER_URL/marketplace/skills" | jq -c '.skills // []')

if [ "$skills" = "[]" ] || [ -z "$skills" ]; then
  echo "No skills found or failed to fetch"
  exit 0
fi

echo "Found $(echo "$skills" | jq 'length') skills"

# Track which plugins we've synced
synced_plugins=()

# Process each skill
echo "$skills" | jq -c '.[]' | while read -r skill; do
  key=$(echo "$skill" | jq -r '.key // .name // empty')
  cid=$(echo "$skill" | jq -r '.cid // empty')

  if [ -z "$key" ] || [ -z "$cid" ]; then
    echo "Skipping skill with missing key or cid"
    continue
  fi

  # Normalize key to be filesystem-safe
  safe_key=$(echo "$key" | tr '/' '-' | tr -cd '[:alnum:]-_')
  plugin_dir="$PLUGINS_DIR/$safe_key"

  echo "Processing skill: $key (CID: ${cid:0:12}...)"

  # Check if we already have this exact CID synced
  if [ -f "$plugin_dir/.synced_cid" ]; then
    existing_cid=$(cat "$plugin_dir/.synced_cid")
    if [ "$existing_cid" = "$cid" ]; then
      echo "  Already synced, skipping"
      synced_plugins+=("$safe_key")
      continue
    fi
  fi

  # Fetch skill content from IPFS
  echo "  Fetching content from IPFS..."
  content=$(curl -s "$WORKER_URL/ipfs/content/$cid" 2>/dev/null || echo "")

  if [ -z "$content" ]; then
    echo "  Failed to fetch content, trying gateway..."
    content=$(curl -s "https://cloudflare-ipfs.com/ipfs/$cid" 2>/dev/null || echo "")
  fi

  if [ -z "$content" ]; then
    echo "  Failed to fetch content, skipping"
    continue
  fi

  # Parse the content - it's a skill bundle with files map
  # Try multiple unwrap levels: direct, .content, .content.content
  files=$(echo "$content" | jq -c '.files // {}' 2>/dev/null || echo "{}")

  if [ "$files" = "{}" ]; then
    # Try one level of .content unwrap
    inner=$(echo "$content" | jq -r '.content // empty' 2>/dev/null || echo "")
    if [ -n "$inner" ]; then
      files=$(echo "$inner" | jq -c '.files // {}' 2>/dev/null || echo "{}")

      # Try another level if still no files (double-wrapped envelope)
      if [ "$files" = "{}" ]; then
        inner2=$(echo "$inner" | jq -r '.content // empty' 2>/dev/null || echo "")
        if [ -n "$inner2" ]; then
          files=$(echo "$inner2" | jq -c '.files // {}' 2>/dev/null || echo "{}")
        fi
      fi
    fi
  fi

  if [ "$files" = "{}" ]; then
    echo "  No files found in skill bundle, skipping"
    continue
  fi

  # Create plugin directory
  mkdir -p "$plugin_dir"

  # Extract files
  echo "  Extracting files..."
  echo "$files" | jq -r 'to_entries[] | @base64' | while read -r entry; do
    filepath=$(echo "$entry" | base64 -d | jq -r '.key')
    filecontent=$(echo "$entry" | base64 -d | jq -r '.value')

    # Skip if filepath is empty or contains ..
    if [ -z "$filepath" ] || [[ "$filepath" == *".."* ]]; then
      continue
    fi

    # Create directory if needed
    filedir=$(dirname "$plugin_dir/$filepath")
    mkdir -p "$filedir"

    # Write file
    echo "$filecontent" > "$plugin_dir/$filepath"
  done

  # Record the synced CID
  echo "$cid" > "$plugin_dir/.synced_cid"

  synced_plugins+=("$safe_key")
  echo "  Synced successfully"
done

# Update marketplace.json
echo "Updating marketplace.json..."

# Read existing marketplace
if [ -f "$MARKETPLACE_FILE" ]; then
  marketplace=$(cat "$MARKETPLACE_FILE")
else
  marketplace='{
    "name": "sage-marketplace",
    "owner": {
      "name": "Sage Protocol",
      "url": "https://github.com/sage-protocol"
    },
    "metadata": {
      "description": "Sage Protocol plugin marketplace for Claude Code",
      "version": "1.0.0"
    },
    "plugins": []
  }'
fi

# Build new plugins array from synced skills
new_plugins="[]"
for plugin_dir in "$PLUGINS_DIR"/*/; do
  if [ ! -d "$plugin_dir" ]; then
    continue
  fi

  plugin_name=$(basename "$plugin_dir")
  plugin_json="$plugin_dir/plugin.json"

  if [ ! -f "$plugin_json" ]; then
    continue
  fi

  # Read plugin.json
  pjson=$(cat "$plugin_json")
  name=$(echo "$pjson" | jq -r '.name // empty')
  description=$(echo "$pjson" | jq -r '.description // "A Sage Protocol skill"')
  version=$(echo "$pjson" | jq -r '.version // "1.0.0"')
  author=$(echo "$pjson" | jq -c '.author // {"name": "Sage Protocol"}')
  tags=$(echo "$pjson" | jq -c '.keywords // .tags // []')

  # Use directory name if no name in plugin.json
  if [ -z "$name" ]; then
    name="$plugin_name"
  fi

  # Create plugin entry
  entry=$(jq -n \
    --arg name "$name" \
    --arg desc "$description" \
    --arg ver "$version" \
    --argjson author "$author" \
    --argjson tags "$tags" \
    --arg source "./plugins/$plugin_name" \
    '{
      name: $name,
      description: $desc,
      version: $ver,
      author: $author,
      homepage: "https://sageprotocol.io",
      tags: $tags,
      source: $source
    }')

  new_plugins=$(echo "$new_plugins" | jq --argjson entry "$entry" '. + [$entry]')
done

# Update marketplace with new plugins
updated=$(echo "$marketplace" | jq --argjson plugins "$new_plugins" '.plugins = $plugins')
echo "$updated" | jq '.' > "$MARKETPLACE_FILE"

echo "Sync complete!"
