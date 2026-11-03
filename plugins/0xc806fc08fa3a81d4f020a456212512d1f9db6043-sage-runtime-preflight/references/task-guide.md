# Task guide: sage-runtime-preflight

Read only the section relevant to the current task. The entry skill owns selection and authority boundaries. Paths in this guide are relative to the skill directory.

# Sage Runtime Preflight

Use this skill when Sage may be the dependency that determines whether any later
workflow succeeds. This is the default **diagnose before mutate** layer for CLI,
daemon, wallet auth, MCP, hooks, and multi-harness setup.

## When to Use

Use this skill when you need to:

- classify why a Sage command is failing before guessing at a fix
- decide whether a project needs `sage init`
- verify daemon, wallet, MCP, or hook posture before write operations
- choose the right OpenClaw / Claude / Codex / Grok / Pi / Hermes setup path
- separate setup problems from auth problems from command-family mistakes

## Don't Use When

Do not use this skill when:

- the task is only skill discovery or install/expose guidance
- the task is only governance, social, or bounty participation
- the task is ordinary local coding with no Sage runtime dependency
- the Sage runtime is already known-good and the user only needs a narrow specialist surface

## Core idea

Before any nontrivial Sage write path, identify which layer is actually failing:

1. project/setup context
2. daemon posture
3. wallet/auth freshness
4. MCP/server lifecycle
5. hooks/integration wiring
6. command-family misunderstanding

Do not skip directly to reconnect/reinstall unless the read posture proves that is
really the blocker.

For routing checks, test the installed CLI and daemon as one pair. Confirm both
build commits, refresh the daemon-owned skill-vector cache after manifest edits,
and inspect the live suggestion score breakdown. A new CLI against an old daemon,
or an offline lexical-only check, can pass while the real hook path still serves
stale vectors or confidence metadata.

## Procedure

### 1. Run the standard runtime read set first

Treat this as the **default baseline checklist**. Use all of it when the failing layer is unclear; once the problem is localized, prune to the path that actually matters instead of running every command mechanically.

```bash
sage doctor
sage daemon status
sage wallet status --format json
sage mcp hub status
sage config paths
```

For wallet readiness, inspect `data.daemon.source` in the status JSON.
`daemon` is a daemon-derived report, not a signing transaction; `legacy` is an
older daemon's compatibility projection, not a fresh readiness check; `local`
means live readiness is unknown because a usable daemon report was unavailable.
Check CLI/daemon versions or daemon availability before recommending wallet
reconnection. For a daemon-reported blocker, follow its provider-aware recovery
only within the approved scope. `signable` is not spending approval and does not
authorize secret access. Operation-specific capabilities, worker auth, credits,
and consent remain separate checks.

If hooks or harness integration matter, also read:

```bash
sage doctor --scope hooks
```

If agent identity/setup matters:

```bash
sage agent quickstart --check
```


### 1a. MCP hub three-check readiness

For MCP-backed work, do these three checks before starting, adding, or calling external servers:

```bash
sage daemon status          # daemon owns external server lifecycle and metrics
sage mcp hub list           # registered/available servers; registered != running
sage security policy status # MCP allowlist/denylist and auto-provision posture
```

Readiness rules:

- A server shown as `registered` is configured but not live; run `sage mcp hub start <server-id>` before expecting tools.
- `hub start` and daemon auto-started tool calls are security-gated by `security.toml`; denylisted or non-allowlisted server IDs fail closed with `blocked by security policy: ...`.
- Successful starts persist callable aliases. Prefer `sage mcp call <alias>` or code-mode `domain='external', action='call'`; do not use `server_id:tool_name` for external calls.
- If aliases are missing after a start, run `sage mcp hub alias refresh <server-id>` and retry the alias.
- Token-gated servers (HTTP MCP behind a stdio adapter such as Paste `paste-mcp-stdio` or `npx mcp-remote`) need `--env KEY=VALUE` on `hub add`, or `hub env set` before `hub start`. Env set goes through the daemon; the next start sees it without a restart. There is no hub `--url` flag.

### 1b. Know the hook and execution-feedback env vars

These are not visible from `sage doctor` but determine whether auto-installed hooks actually do anything:

| Env var | Set by | Effect |
|---|---|---|
| `SAGE_SKILL_USED` | the harness/agent only when a skill **procedure actually guided work** | Required (with `SAGE_SKILL_OUTCOME`) for Claude/Codex/Grok outcome hooks. If unset, the hook is a no-op. |
| `SAGE_SKILL_OUTCOME` | the harness/agent — explicit `passed` \| `failed` \| `revised` | **Required** with `SAGE_SKILL_USED`. No default: if unset, the outcome hook is a no-op (avoids poison auto-pass). |
| `SAGE_CAPTURE_ID` | exact `capture_id` from the current `sage:evidence-context.v1` block | Optional for recording the outcome, required for exact prompt-capture attribution. Missing IDs remain `not_linked`; never reuse another turn's ID. |
| `SAGE_AUTO_SKILL_OUTCOME` | operator (Pi/Hermes adapters) | Default **off**. When `1`/`true`, adapters may auto-record outcomes; leave unset unless you accept inferred pass/fail noise. |
| `SAGE_FILTER_EXECUTION` | the user/operator | When set (any non-empty value), `sage suggest skill` re-ranks results by execution pass rate. Equivalent to passing `--filter-execution`. |
| `SAGE_SOURCE` | the harness | Tags rows in `skill_execution` with the harness identifier (`claude-code`, `codex`, `pi`, `opencode`, ...). |
| `SAGE_SESSION_ID` | the harness | Native harness session identity used to link rows from one session. It is not a suggestion correlation ID. |
| `SAGE_DISABLE_SECURE_STORAGE` | troubleshooting | Test/troubleshooting flag — makes secure storage in-memory. Not for production. |

If a skill materially guided work but its expected outcome row is missing, inspect the recorded breakdown and the hook environment:

```bash
sage suggest feedback breakdown <skill-key> --format json
```

Zero rows alone do not prove a broken hook. They are correct when no skill materially guided work or when the explicit outcome variables were deliberately unset. Diagnose a hook contract failure only when an expected, materially guided outcome is missing. Do not enable automatic pass recording to manufacture rows.

### 2. Classify the blocker before repairing it

Use this map:

| Symptom | Likely layer | First next read |
|---|---|---|
| `No project root found` | setup/project context | confirm cwd, then `sage init --help` |
| stale socket / daemon unavailable | daemon | `sage daemon status` |
| worker-backed command says auth/session invalid | wallet/auth freshness | `sage wallet status --format json`; inspect the source, then the wallet alert/recovery |
| MCP tools missing or no servers running | MCP hub/server posture | §1a three-check: `daemon status`, `mcp hub list`, `security policy status`; then `mcp hub status` |
| Host has no Sage MCP tools at all | Bridge not started / not configured | Verify harness MCP config + `sage mcp start` / `sage_status` (not only hub status) |
| `hub status` says daemon not running | Daemon posture | `sage daemon start` then recheck |
| Server start fails with security policy | Policy gate | `sage security policy status`; do not advise offline local fallback to bypass |
| hooks not firing or duplicated | hook integration | `sage doctor --scope hooks` |
| `config_schema_migrations_pending` from doctor | config schema behind the daemon's version (the migration registry ships empty; this fires only once a migration is registered) | `sage doctor --scope config`, then with repair authority `sage doctor --scope config --fix` |
| doctor flags deprecated name-based wallet-delegation entries | allowlist keyed by name instead of `node:<id>` | with repair authority and a running daemon, `sage doctor --fix` rewrites names that match exactly one paired node; zero or several matches stay for the operator (pair the node, or rename duplicates); it grants no capability |
| an expected materially guided outcome is missing after hooks fire | hook env contract or deliberate no-op | inspect `SAGE_SKILL_USED` and `SAGE_SKILL_OUTCOME`, then run `sage suggest feedback breakdown <skill-key> --format json`; zero rows alone are not a failure |
| command exists but user guessed wrong shape | command-family confusion | parent `--help` + safe read path |

### 3. Prefer diagnosis before repair

Only repair after the read posture tells you what is wrong.

Common repair paths:

```bash
# Preferred wallet path
sage wallet create sage-wallet
sage wallet connect ows -n sage-wallet
sage wallet create-agent-key --name sage-agent

# Fallback embedded-wallet path
sage wallet connect privy --device-code
sage wallet connect privy --device-code --force

sage daemon start
sage init --yes
sage init --openclaw --mode plugin --yes
sage init --openclaw --mode hooks --yes
sage init --openclaw --mode hybrid --yes
```

Important truths:

- `sage init --yes` expects a **project root**
- Re-running `sage init` is now safer for OpenCode: it preserves existing OpenCode config instead of overwriting user-managed settings.
- OpenClaw `plugin`, `hooks`, and `hybrid` are real operator choices, not aliases
- worker-backed commands may still need a fresh wallet session even when local reads work
- OWS direct wallet is the launch/default path for signing,
  daemon-backed writes, and unattended automation; local keystore is the local
  direct-wallet fallback.
- Privy is testnet/onboarding-only hosted-wallet/social-login auth with daemon/process-memory
  sessions and device-code reauthentication after daemon restart. Do not propose
  Privy for mainnet operations; for unattended or mainnet flows, use OWS direct wallet.
- SIWE/browser sessions are separate direct-wallet web auth.
- For daemon-backed writes, require a usable daemon-derived wallet readiness
  report and the operation's own capabilities, auth, and approval checks.
  Connected identity alone is not signing readiness or spending authority.

Quick setup-path chooser:

| Intent | Best command |
|---|---|
| general project bootstrap | `sage init --yes` |
| OpenClaw plugin-first setup | `sage init --openclaw --mode plugin --yes` |
| hook-driven fallback only | `sage init --openclaw --mode hooks --yes` |
| both plugin ergonomics and hooks | `sage init --openclaw --mode hybrid --yes` |

### 4. Check policy posture when relevant

If command execution policy or security gating may matter:

```bash
sage security policy status
```

Do not assume a healthy daemon means every action is allowed.

### 5. Confirm readiness before suggesting writes

A write path is only truly ready when the required reads are healthy:

- local/runtime write -> `sage doctor`, `sage daemon status`
- worker-backed write -> `sage wallet status --format json`, then the required worker auth/credits and consent checks
- MCP-backed flow -> three-check from §1a (`daemon status` + `mcp hub list` + `security policy status`), then `mcp hub status` for the running set; host bridge is separate (`sage mcp start` / `sage_status`)
- hook/integration flow -> `sage doctor --scope hooks`

### 6. Give the smallest correct repair recommendation

Handoff after diagnosis:

- wallet/auth/funding blocker -> `sage-wallet-ops`
- stale installed binary or daemon-process drift -> `sage-runtime-refresh`
- search/install/expose/status problem rather than runtime failure -> `sage-discover-adopt-skill`
- governance or collaboration action after runtime is green -> `sage-workflow` or the narrower specialist skill

Concrete narrowed examples:

- install/expose or inspect confusion with runtime already healthy -> `sage search "<intent>" --search-type skills --scope both` or `sage library inspect ...`, then switch to `sage-discover-adopt-skill`
- stale runtime after source changes -> switch to `sage-runtime-refresh`
- worker-backed auth drift -> switch to `sage-wallet-ops`

Bad guidance:

- "Reinstall Sage"

Better guidance:

- "The daemon is healthy; the blocker is wallet auth freshness"
- "The hooks are stale; runtime posture is otherwise healthy"
- "This is a project-root/setup issue, not an auth issue"
- "You're using the wrong command family; use the parent read path first"

### 7. Diagnose read-RPC availability separately

`sage doctor --scope rpc --include-details` checks the configured read endpoint,
verifies its chain ID and latest-block freshness, and reports when a fallback is
active. It does not change transaction submission.

Configure endpoint **IDs**, never credential-bearing URLs:

```bash
sage config set rpc.primary profile
sage config set rpc.fallback base-sepolia-publicnode

# Dedicated provider URLs stay in the daemon/CLI environment:
export SAGE_BASE_SEPOLIA_PRIMARY_RPC='https://provider.example/<secret>'
sage config set rpc.primary env:SAGE_BASE_SEPOLIA_PRIMARY_RPC
sage config set rpc.fallback base-sepolia-publicnode
```

Built-in IDs are `profile`, `base-sepolia-official`,
`base-sepolia-publicnode`, `base-mainnet-official`, and
`base-mainnet-publicnode`. Read failover is sequential and limited to a primary plus one fallback.
Do not infer write failover from read fallback configuration. Check the running
CLI and daemon versions, the specific command, and the signer before relying on
transaction recovery. A locally reviewed patch is not evidence that the installed
runtime supports it. Never bypass a contract rejection, wallet policy, or expired
credential by switching RPCs. After an ambiguous send, inspect its hash or sender
and nonce before any new invocation; do not rebuild or repeat a funded action.
Transaction-recovery work must preserve signer authority and immutable signed
bytes, with separate receipt and authoritative-state verification.

## Quick chooser

| Situation | Best first command |
|---|---|
| "Sage isn't working" | `sage doctor` |
| "Is the daemon healthy?" | `sage daemon status` |
| "Can my wallet sign?" | `sage wallet status --format json` (inspect `data.daemon.source`) |
| "Are MCP servers up?" | `sage mcp hub status` |
| "Are hooks wired correctly?" | `sage doctor --scope hooks` |
| "Is the RPC or only one provider down?" | `sage doctor --scope rpc --include-details` |
| "Set this project up" | `sage init --help` |

## Good output shape

- current runtime posture
- exact blocking layer
- smallest corrective action
- whether writes are safe yet
- one concrete next command

## Verification

- [ ] `doctor`, `daemon status`, `wallet status`, and `mcp hub status` were considered
- [ ] legacy/local wallet reports were not mistaken for fresh readiness or approval
- [ ] MCP issues used the §1a three-check (daemon / hub list / security policy) before mutate
- [ ] repair advice matched the actual failing layer
- [ ] setup/root-context issues were not confused with auth issues
- [ ] hook problems were checked separately when relevant
- [ ] no mutation was recommended before required reads were healthy

## Related Skills

- `sage-workflow` — broader command-family routing once runtime posture is healthy
- `sage-wallet-ops` — deeper wallet/auth handling when the blocker is session, funding, or approvals
- `sage-discover-adopt-skill` — discovery and install/expose lifecycle once setup is healthy
- `sage-runtime-refresh` — rebuild/replace stale binaries or daemon processes after source changes
- `sage-p2p` — direct peer-sync/connectivity issues that are not generic runtime posture
- `sage-governance-participation` — governance actions after runtime/auth readiness is green

### Suggestion context budget

```bash
sage config set suggest.emission.default distilled
sage config set suggest.emission.distill_budget_chars 6000
sage config set suggest.emission.min_score 25 && sage config set suggest.emission.min_gap 0.10
SAGE_SUGGEST_EMISSION=distilled  # per-invocation override
```

Run `sage config show` before and after to verify the intended profile and all
four persisted values. Distilled output is an attention-quality guardrail: it
retains useful routing context that bare `headers` omit without full-body prompt
stuffing. The 6000/25/0.10 values are a starting policy, not a measured universal
optimum. Load the selected complete procedure before execution.

Suggestion emission is model-agnostic: min_score/min_gap can abstain to trailer-only while preserving feedback capture.
JSON callers inherit the same suggestion emission policy; use `--emission full` when a consumer needs full `content`.
An explicit `--emission full` (or `SAGE_SUGGEST_EMISSION=full`) is an operator override and should be reserved for consumers that truly need full skill bodies.

### Find and evaluate better local models

Revisit model choices as releases improve. Search HuggingFace and
`onnx-community` for the properties below, then inspect the model card, license,
export revision, tokenizer, input/output tensor shapes and local runtime support.
Family names are search seeds, not blanket endorsements or supported Sage IDs.

- **Embedding bi-encoders:** search for ONNX `model.onnx` plus `tokenizer.json`,
  code- and instruction-aware training, and at least 2,048 tokens (prefer 8,192
  where latency allows). Test full `SKILL.md` contracts, including late
  `USE WHEN`, `DON'T USE WHEN` and CLI flags. Legacy MiniLM's 256-token setup
  can omit those constraints. Seek native 384-dimensional output or Matryoshka
  representation learning (MRL) with a documented 384-dimensional projection
  for the `skill_vectors` index. Never truncate arbitrary vectors and assume
  equivalence. Search BGE, Jina Embeddings v2/v3 and successors, Snowflake Arctic
  Embed and Qwen3-Embedding families; verify each specific export. The registered
  BGE small English v1.5 is a modest 512-token, 384-dimensional option, not a
  long-context solution. Its CLS pooling differs from MiniLM mean pooling.
- **Cross-encoder rerankers:** search compact tool/function-calling-trained
  models that jointly attend to `(query, skill_contract)`. Measure exclusion
  and negation cases; joint attention does not guarantee respect for
  `DON'T USE WHEN`. Compare typed decision classifiers such as Jev / TypeSafe AI
  only when their current API/export provides typed choices or probabilities.
  Validate calibration, abstention and p50/p95 latency on held-out tasks.
  `ModelBackend::Onnx` is an integration surface, not a promise that arbitrary
  graphs plug into the built-in learned linear reranker. Run shadow gate
  evaluation before any supported swap; unsupported backends need code work.
- **Local RLM models:** search instruction-tuned ONNX exports in the 0.6B–4B
  class with `q4` / `q4f16` quantization. Qwen3, Gemma3/Gemma-4, Llama-3.2 and
  successors are search seeds. Check operator support, external weight files,
  memory, tokenizer/chat template and structured JSON validity. Benchmark pattern
  extraction, security-guard decisions and session analysis on sanitized cases.
  A larger model is not automatically a better security guard.

```bash
sage model list
sage model download <registered-id>
sage model default <installed-rlm-id>
sage model list
sage config set default_embedding_model <installed-embedding-id>
sage model load
```

The registry is not a HuggingFace search engine. A new upstream model needs a
compatible registered download and loader before these commands can use it.
Verify `[default]` after switching RLM models; do not leave a tiny 135M test model
as the production choice by accident. Confirm the daemon actually loads the
selected model on the next RLM operation, rather than relying on config alone.
Embedding defaults are separate. Never mix vectors from different models even
at the same dimension: rebuild/invalidate the index and compare against a saved
baseline. Check query prefixes, pooling, normalization and actual truncation.
This loader's two/three-input support does not implement every ONNX architecture.

Keep corpus, queries and hardware fixed. Compare Recall@1/5, nDCG@5, MRR,
negation/adversarial slices, latency and memory; record export hashes and rollback
settings. For built-in learned reranker setup, load `sage-feedback-and-evals`
and follow status → mine → task-success train/explain → digest-pinned gate.
Promotion recommendations do not authorize activation or remote data transfer.
