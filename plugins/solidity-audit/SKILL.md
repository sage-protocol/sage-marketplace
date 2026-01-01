---
name: solidity-audit
description: Use when auditing Solidity/EVM smart contracts, triaging Slither/Semgrep results, building threat models/invariants, or producing an audit report with reproducible evidence.
tags:
  - security
  - audit
  - solidity
  - hound
  - smart-contracts
---

# Solidity Audit Skill (Hound CLI)

## Quick Start

**Hound CLI** is the primary interface. Run directly in terminal:

```bash
# 1. Create project
hound.py project create my-audit /path/to/contracts

# 2. Build knowledge graphs
hound.py graph build my-audit --auto --files "src/*.sol" --iterations 3

# 3. Run sweep analysis (Phase 1)
hound.py agent audit my-audit --mode sweep

# 4. Run intuition analysis (Phase 2)
hound.py agent audit my-audit --mode intuition --time-limit 300

# 5. Finalize findings
hound.py finalize my-audit

# 6. Generate report
hound.py report my-audit --output report.html
```

---

## Prime Directive

Be evidence-driven:
- No "this looks vulnerable" without concrete call path + state assumptions
- Always cite file/function/lines (or minimal code excerpt)
- Prefer Foundry test to justify severity
- Use Hound's knowledge graphs to trace control/data flow systematically

---

## CLI Command Reference

### Project Management

```bash
# Create project
hound.py project create <name> <source_path> [--description "text"]

# List projects
hound.py project ls

# Show project info and coverage
hound.py project info <name>
hound.py project coverage <name>

# List hypotheses (findings)
hound.py project hypotheses <name> [--details]

# Set hypothesis status manually
hound.py project set-hypothesis-status <name> <hyp_id> confirmed|rejected

# Show sessions
hound.py project sessions <name> [--list]

# Delete project
hound.py project delete <name> [--force]
```

### Knowledge Graph Building

```bash
# AUTO-BUILD (Recommended) - Creates 5 default graphs
hound.py graph build <project> --auto \
  --files "src/A.sol,src/B.sol" \
  --iterations 3

# Build with specific focus
hound.py graph build <project> --auto \
  --focus "access control,value flows" \
  --files "contracts/*.sol"

# Initialize baseline only (SystemArchitecture)
hound.py graph build <project> --init \
  --files "src/*.sol" \
  --iterations 2

# Build custom graph
hound.py graph build <project> \
  --with-spec "Reentrancy call graph" \
  --files "src/*.sol"

# Refine existing graphs
hound.py graph refine <project> --all --iterations 2

# List graphs
hound.py graph ls <project>

# Export visualization
hound.py graph export <project> --output graph.html --open
```

**Key Options:**
- `--files "path1,path2"` - Whitelist files (STRONGLY RECOMMENDED)
- `--iterations N` - Refinement iterations (default: 3)
- `--auto` - Auto-generate 5 default graphs
- `--focus "topic"` - Focus graph building on specific areas

### Autonomous Audit

```bash
# SWEEP MODE - Systematic broad analysis (Phase 1)
hound.py agent audit <project> --mode sweep

# INTUITION MODE - Deep targeted exploration (Phase 2)
hound.py agent audit <project> --mode intuition --time-limit 300

# Resume existing session
hound.py agent audit <project> --session <session_id> --mode intuition

# With telemetry UI (interactive steering)
hound.py agent audit <project> --mode sweep --telemetry
# Then open http://127.0.0.1:5280

# With custom mission
hound.py agent audit <project> \
  --mode intuition \
  --mission "Find reentrancy and access control bugs"

# Custom models
hound.py agent audit <project> \
  --mode sweep \
  --platform openai \
  --model gpt-5 \
  --strategist-model claude-3-opus
```

**Audit Parameters:**
| Flag | Description |
|------|-------------|
| `--mode sweep\|intuition` | Sweep (broad) or Intuition (deep) |
| `--time-limit N` | Stop after N minutes |
| `--iterations N` | Max iterations per investigation |
| `--session <id>` | Attach to existing session |
| `--telemetry` | Enable live UI at http://127.0.0.1:5280 |
| `--mission "text"` | Overarching audit mission |
| `--debug` | Save LLM interactions to `.hound_debug/` |

### Targeted Investigation

```bash
# Single focused investigation
hound.py agent investigate \
  "Check for reentrancy in withdraw function" \
  <project> \
  --iterations 5
```

### Finalize & Report

```bash
# Finalize (QA review to confirm/reject findings)
hound.py finalize <project>
hound.py finalize <project> --threshold 0.7

# Generate report
hound.py report <project> --output report.html
hound.py report <project> --format markdown --output REPORT.md
hound.py report <project> --all  # Include rejected findings
```

---

## Workflow: Full Audit Pipeline

### 1. INGEST: Create Project & Build Graphs

```bash
# Create project pointing to contracts
hound.py project create protocol-audit ./contracts \
  --description "Protocol v2 security audit"

# Build all graphs with file whitelist
hound.py graph build protocol-audit --auto \
  --files "src/core/*.sol,src/governance/*.sol" \
  --iterations 3
```

**Graphs produced:**
- **SystemArchitecture**: Contract inheritance, modules, external calls
- **AccessControl**: Roles, modifiers, privilege escalation paths
- **ValueFlow**: Token/ETH movements, balance-affecting state changes
- **CallGraph**: Function relationships and call chains
- **DataFlow**: Variable dependencies and taint propagation

### 2. ANALYZE: Run Sweep + Intuition

```bash
# Phase 1: Systematic sweep (checks OWASP patterns)
hound.py agent audit protocol-audit --mode sweep

# Check coverage
hound.py project coverage protocol-audit

# Phase 2: Deep exploration of high-risk areas
hound.py agent audit protocol-audit \
  --mode intuition \
  --time-limit 600
```

### 3. REVIEW: Check Hypotheses

```bash
# List all findings with details
hound.py project hypotheses protocol-audit --details

# View specific hypothesis
hound.py project hypotheses protocol-audit | grep "hyp_abc123"
```

**Hypothesis statuses:**
- `proposed` - Agent identified potential issue
- `confirmed` - Validated as real vulnerability
- `rejected` - Determined to be false positive

### 4. FINALIZE: QA Review

```bash
# Run QA to validate findings (adjusts confidence, confirms/rejects)
hound.py finalize protocol-audit

# With higher threshold (more strict)
hound.py finalize protocol-audit --threshold 0.7
```

### 5. REPORT: Generate Output

```bash
# HTML report (recommended)
hound.py report protocol-audit \
  --output ./audit/report.html \
  --title "Protocol v2 Security Audit" \
  --auditors "Security Team"

# Markdown for GitHub
hound.py report protocol-audit \
  --format markdown \
  --output ./audit/REPORT.md
```

---

## Project Directory Structure

Projects stored in `~/.hound/projects/<name>/`:

```
~/.hound/projects/my-audit/
├── project.json          # Metadata
├── hypotheses.json       # Findings (editable!)
├── coverage_index.json   # Coverage tracking
├── graphs/
│   ├── graph_SystemArchitecture.json
│   ├── graph_AccessControl.json
│   └── visualization.html
├── sessions/             # Audit sessions
├── manifest/             # Source manifest + code cards
└── reports/              # Generated reports
```

**Direct Hypothesis Editing:**
```bash
# View hypotheses file
cat ~/.hound/projects/my-audit/hypotheses.json | jq '.hypotheses | keys | length'

# Add hypothesis manually (use jq to merge)
jq -s '.[0].hypotheses *= .[1] | .[0]' hypotheses.json new_hyp.json > merged.json
```

---

## Configuration (config.yaml)

```yaml
# ~/.hound/config.yaml or ./config.yaml
openai:
  api_key_env: OPENAI_API_KEY

anthropic:
  api_key_env: ANTHROPIC_API_KEY

models:
  graph:
    provider: gemini
    model: gemini-2.5-pro
  scout:
    provider: openai
    model: gpt-5-mini
  strategist:
    provider: openai
    model: gpt-5
  finalize:
    provider: openai
    model: gpt-5
```

**Environment Variables:**
```bash
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export GOOGLE_API_KEY=...
```

---

## Common Query Patterns

Run targeted investigations:

```bash
# Reentrancy
hound.py agent investigate "Check for external calls before state updates" my-audit

# Access Control
hound.py agent investigate "What functions lack access control modifiers?" my-audit

# Flash Loans
hound.py agent investigate "Can any function be exploited via flash loan?" my-audit

# Upgrades
hound.py agent investigate "Are there storage collision risks in proxy pattern?" my-audit
```

---

## Severity Classification

| Severity | Criteria |
|----------|----------|
| Critical | Direct loss of funds, complete protocol takeover |
| High | Significant fund loss with constraints, governance bypass |
| Medium | Limited fund loss, griefing, DoS with recovery |
| Low | Edge cases, gas inefficiency, code quality |
| Info | Best practices, documentation, style |

---

## Fallback: MCP Mode (Optional)

If using Claude Desktop with MCP:

```bash
# Start Hound MCP server
scroll mcp hub start hound

# Then use MCP tools in Claude:
# hound_create_project, hound_build_graph, hound_query, etc.
```

**Note**: MCP mode has the same capabilities but requires Claude Desktop integration. CLI mode is standalone and more flexible for automation.

---

## Proof-of-Concept Management

```bash
# Generate PoC prompts for confirmed vulnerabilities
hound.py poc make-prompt my-audit

# Import PoC files
hound.py poc import my-audit hyp_abc123 exploit.sol test.js \
  --description "Demonstrates reentrancy"

# List PoCs
hound.py poc list my-audit
```

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Create project | `hound.py project create NAME PATH` |
| Build graphs | `hound.py graph build NAME --auto --files "*.sol"` |
| Sweep audit | `hound.py agent audit NAME --mode sweep` |
| Deep audit | `hound.py agent audit NAME --mode intuition` |
| Check findings | `hound.py project hypotheses NAME --details` |
| Finalize | `hound.py finalize NAME` |
| Report | `hound.py report NAME --output report.html` |
| Investigate | `hound.py agent investigate "question" NAME` |

---

## Compound: Capture Learnings

After finishing:
1. Convert confirmed bugs into regression/invariant tests
2. Add checklist items for new patterns discovered
3. Update `./audit/LESSONS.md` with key takeaways
4. Consider contributing patterns back to Hound's knowledge base
