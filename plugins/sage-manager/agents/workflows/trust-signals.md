<objective>
Look up trust signals (badges + contribution history) for any address. Trust signals are composable indicators of on-chain activity - they are NOT a canonical reputation score.
</objective>

<important_disclaimer>
**Trust signals are NOT a reputation score.**

Trust signals show verifiable on-chain activity:
- **Badges**: Contributor SBTs minted when work is accepted (bounties, governance)
- **Contributions**: Count of accepted proposals, bounty completions, etc.

These are raw signals that consumers can interpret as they see fit. There is no single "reputation number" - different use cases may weight signals differently.

**Caveat: Executor addresses may be contracts.** When looking up the "contributor" for a manifest update, the address may be a Safe multisig or Timelock contract, not an individual. The CLI labels these appropriately.
</important_disclaimer>

<command_reference>
```
# Check trust signals for any address
sage reputation check <address>
sage reputation check <address> --subdao 0x...          # Filter to specific DAO
sage reputation check <address> --json                  # Machine-readable output

# Gating flags (optional - exit code 1 if gates fail)
sage reputation check <address> --min-badges 1
sage reputation check <address> --min-contributions 5
sage reputation check <address> --require-badge 1 --require-badge 2

# Pull prompt with contributor trust signals
sage prompts pull <key> --with-reputation
sage prompts pull <key> --with-reputation --subdao 0x...

# Verify contributor meets gates when pulling
sage prompts pull <key> --verify-reputation --min-badges 1
sage prompts pull <key> --verify-reputation --min-contributions 3

# Subgraph configuration
sage reputation check <address> --subgraph <url>
# Or set env: SUBGRAPH_URL or SAGE_SUBGRAPH_URL
```
</command_reference>

<exit_codes>
**`sage reputation check` exit codes:**

| Code | Meaning | When |
|------|---------|------|
| 0 | OK | No gates specified, or all gates passed |
| 1 | Gates failed | Address does not meet specified requirements |
| 2 | Invalid args | Bad address format, invalid options |
| 3 | Fetch error | Subgraph unreachable, network issues |

**Usage in scripts:**
```bash
# Check if contributor has at least 1 badge
if sage reputation check 0x1234... --min-badges 1; then
  echo "Contributor has badges"
else
  echo "Contributor does not meet badge requirement"
fi

# Get exit code explicitly
sage reputation check 0x1234... --min-badges 5
EXIT_CODE=$?
```
</exit_codes>

<json_output>
**JSON output schema (`--json`):**

```json
{
  "address": "0x1234567890abcdef...",
  "subdao": "0xABCD..." | null,
  "signals": {
    "badgeCount": 3,
    "totalContributions": 12,
    "governanceOriginated": 8,
    "bountyOriginated": 4,
    "lastContributionAt": 1702345678
  },
  "badges": [
    {
      "id": "badge-0x...",
      "contract": "0x...",
      "badgeId": "1",
      "recipient": "0x...",
      "evidenceURI": "ipfs://...",
      "blockNumber": 12345678,
      "blockTimestamp": 1702345678,
      "transactionHash": "0x..."
    }
  ],
  "contributionAggregates": {
    "totalContributions": 12,
    "uniqueContributors": 1,
    "bountyOriginated": 4,
    "governanceOriginated": 8,
    "totalForVotes": "50000000000000000000",
    "totalAgainstVotes": "0",
    "averageVoterCount": 3,
    "badgeCount": 3
  },
  "gates": {
    "minBadges": 1,
    "minContributions": 5
  } | null,
  "evaluation": {
    "ok": true,
    "reasons": []
  } | null
}
```

**When gates fail:**
```json
{
  "evaluation": {
    "ok": false,
    "reasons": [
      "minBadges:0<1",
      "minContributions:2<5"
    ]
  }
}
```
</json_output>

<prompts_pull_integration>
**Show contributor trust signals when pulling prompts:**

```bash
# Basic pull with trust signals
sage prompts pull code-review --with-reputation

# Output includes:
#   Contributor: 0x1234...
#   Last updated: 2024-01-15T10:30:00.000Z
#   Trust signals: 3 badges, 12 contributions
```

**Verify contributor meets requirements:**

```bash
# Pull only if contributor has badges
sage prompts pull code-review --verify-reputation --min-badges 1

# Pull only if contributor has significant history
sage prompts pull code-review --verify-reputation --min-contributions 10

# Multiple gates
sage prompts pull code-review --verify-reputation \
  --min-badges 1 \
  --min-contributions 5 \
  --require-badge 42
```

**Caveat: Executor vs contributor addresses**

When a manifest is updated through governance, the on-chain executor may be:
- A Timelock contract (for token-governed DAOs)
- A Safe multisig (for council DAOs)
- An EOA (for operator DAOs)

The CLI looks up the `PromptContribution.contributor` from the subgraph to find the actual human/agent who proposed the change, not just the executor address. However, if no contribution record exists (e.g., legacy data), the executor address is shown with a warning.

**Subgraph configuration:**

```bash
# Set via environment (recommended)
export SUBGRAPH_URL=https://api.studio.thegraph.com/query/...

# Or per-command
sage prompts pull code-review --with-reputation --subgraph https://...

# If not configured, shows warning and continues without reputation data
```
</prompts_pull_integration>

<agent_patterns>
**Agent workflow: Verify prompt source before using**

```bash
# 1. Check who contributed the prompt
sage prompts pull my-prompt --with-reputation --json | jq '.reputation'

# 2. If contributor has history, proceed
sage prompts pull my-prompt --verify-reputation --min-contributions 1

# 3. Use in automation
if sage prompts pull my-prompt --verify-reputation --min-badges 1 2>/dev/null; then
  # Contributor is verified, safe to use
  cat prompts/my-prompt.md
else
  echo "Prompt contributor does not meet trust requirements"
fi
```

**Agent workflow: Check address before interacting**

```bash
# Before accepting a bounty submission from unknown address
sage reputation check 0xSubmitter... --min-contributions 1 --json

# Before delegating tokens to an address
sage reputation check 0xDelegate... --min-badges 2
```
</agent_patterns>

<troubleshooting>
| Issue | Cause | Fix |
|-------|-------|-----|
| "Subgraph URL not configured" | No SUBGRAPH_URL env | Set `export SUBGRAPH_URL=https://...` |
| "SDK reputation module not available" | Old SDK version | Update `@sage-protocol/sdk` |
| "No contribution history found" | Prompt has no on-chain contributions | Contributor info not available |
| Gates fail unexpectedly | Address has no on-chain history | Check address is correct |
| Exit code 3 | Subgraph unreachable | Check network, try again |
</troubleshooting>
