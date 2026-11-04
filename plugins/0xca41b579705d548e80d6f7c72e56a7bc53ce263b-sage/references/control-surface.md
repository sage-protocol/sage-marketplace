# Sage control-surface routing

Use the control surface the host actually exposes, while keeping the same read-before-write discipline.

## Default order

1. **Rust CLI (`sage`)** when shell access is available. Verify uncertain syntax with `sage --help` or `sage <group> --help`.
2. **Code-mode wrappers** when the harness exposes tools instead of shell commands:
   - `sage_search({ domain, action, params })` for both metadata and content reads, including search, list, inspect, `prompts.get`, and `skills.get`.
   - `sage_execute({ domain, action, params })` for supported unsigned local/external mutations such as activation, local creation, and external tool calls.
   - `sage_status({})` for bridge/runtime health.
   - Built-in prompt guidance is available as `sage-code-mode` and `sage-library-write` via MCP `prompts/list` and `prompts/get`.
3. **Raw MCP tools** when the host exposes Sage tools directly: `search_skills`, `get_skill`, `use_skill`, `search_prompts`, `get_prompt`, `hub_list_servers`, `hub_status`, `hub_start_server`, `hub_stop_server`, `hub_session_list`, `hub_add_server`, `get_project_context`, and `suggest_sage_tools`.
4. **Harness plugin commands** only when that harness documents them; do not assume slash commands exist.

## Safety boundaries

- Search/list/inspect/help are read-only and do not need wallet authority.
- Sage MCP cannot sign onchain transactions. Use the CLI for economic or governance mutations and any other signed write.
- Local skill activation or local context scoping is local, not publication.
- MCP hub add/start/call flows are security-gated by the MCP policy in `security.toml`; denylisted IDs fail closed with `blocked by security policy: ...`.
- `hub_add_server` registers a server but does not make tools live. Use `hub_list_servers`/`sage mcp hub list` to distinguish `registered` from `running`, then start it.
- External MCP tools should be called via aliases (`sage mcp call <alias>` or `domain='external', action='call'` with `tool_name: '<alias>'`). Do not use `server_id:tool_name`; colon is reserved for isolated server instances.
- Library cloud push, publish, marketplace listing, DAO promotion, P2P daemon changes, voting, tipping, bounties, claims, and payments require explicit user intent and the relevant wallet/daemon checks.
- Public/marketplace/governed library writes also require IPFS worker auth/credits, an explicit durable pin duration (`12months` or `permanent`), and post-write retrievability checks (`sage library pin-status`, `sage config ipfs status`, plus anonymous gateway verification) before the CID is treated as publicly usable.
- If command availability is unclear, run `sage_status({})`, `sage --help`, or `sage doctor --include-details` before recommending setup changes.
- MCP can be faster for an already-warm read because it avoids process startup,
  but surface selection must follow capability and authority, not presumed speed.

## Discussion and retrieval handoffs

Use `sage-proactive-collaboration` for Buzz identity, visibility, thread, delivery,
and fallback checks. Choose a supported authorized CLI/wrapper or granted tools;
an inactive MCP server does not make a working CLI unavailable. No machine-local
wrapper name or unbundled community skill is an init prerequisite.

For any handoff state purpose, route, required context, authority, output,
verification, and fallback. A local lookup miss, anonymous content denial,
unsupported authenticated route, and stale client/cache are different failures.
Do not infer global inaccessibility, extract credentials, or repair a wallet for
a route that never forwards its authentication. Missing transport or economic
authority does not block unrelated private analysis.

## Code-mode examples

```json
{"domain":"skills","action":"search","params":{"query":"rust testing"}}
{"domain":"skills","action":"use","params":{"key":"sage-discover-adopt-skill"}}
{"domain":"behaviors","action":"recommend","params":{"intent":"review this implementation plan"}}
{"domain":"library","action":"skill_add","params":{"library":"zenith","path":"/path/to/skill-dir"}}
{"domain":"library","action":"prompt_add","params":{"library":"zenith","name":"Paperbridge","content":"..."}}
{"domain":"library","action":"skill_get","params":{"library":"zenith","key":"paperbridge"}}
{"domain":"hub","action":"list_servers","params":{}}
{"domain":"hub","action":"start","params":{"server_id":"fetch"}}
{"domain":"external","action":"call","params":{"tool_name":"fetch_markdown","tool_params":{"url":"https://example.com"}}}
{"domain":"external","action":"call","params":{"tool_name":"fetch","tool_params":{"url":"https://example.com"}}}
```

`behavior run` returns the `controller_plan` execution contract consumed by Sage-aware harness executors to coordinate resolved skill steps.

For deterministic library writes, pass `params.library` by name or CID. Do not call `prompts.create` without `params.library` in a multi-library workspace; use `library.skill_add` for `SKILL.md` directories and `library.prompt_add` for plain prompt content.
