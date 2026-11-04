# Sage CLI family chooser

Use this when the user names an outcome but not the command family.

| Outcome | Command family | First reads |
|---|---|---|
| Setup, stale context, daemon, MCP, security posture | `init`, `doctor`, `daemon`, `mcp`, `security`, `update` | `sage doctor --include-details`, `sage daemon status`, `sage mcp hub status` |
| Skill/prompt/library discovery | `search`, `suggest`, `skill`, `library inspect` | `sage search "<intent>" --search-type skills --scope both`, `sage suggest skill "<task>" --format json` |
| Multi-skill workflows | `behavior` | `sage behavior recommend "<intent>" --format json`, `sage behavior show <key> --expand behaviorPlan --format json` |
| Safe operational writes | `library`, `marketplace`, `governance`, `wallet` | `sage wallet current`, `sage daemon status`, `sage library list` |
| Private fleet sync | `daemon p2p`, `p2p` skill guidance | `sage daemon p2p server connection-string`, `sage daemon p2p client connect --help` |
| Funding, recognition, identity, wallet-attributed public evidence | `tips`, `bounties`, `reflection`, `profile`, `agent`, `demo`, `social` | `sage agent info --address <wallet> --json`, `sage bounties list --limit 10`, `sage tips list --limit 10`, `sage tips send --help`, `sage reflection list` |
| Discussion, disagreements, reviewers | Buzz CLI/wrapper or granted host tools; `sage-proactive-collaboration` §2–4 | Verify sender, visibility, membership, and exact thread; legacy `sage chat` is not Buzz |
| DAO context and recently active wallets | `governance dao` | `sage governance dao info <dao> --activity-limit 20 --json` |
| RLM and feedback | `capture`, `metrics`, `suggest feedback`, `model`, `benchmark` | `sage capture status`, `sage metrics rlm`, `sage suggest feedback --help` |

## Suggestion result branching

` sage suggest skill "<intent>" --format json` may return skills, prompts, or behaviors. Inspect `entryKind`:

- `skill` -> inspect with `sage library inspect skill get <key> -l <library>` when library-scoped, or load/use the installed skill when local.
- `prompt` -> inspect with `sage library inspect prompt get <key> -l <library>` or `get_prompt`.
- `behavior` -> inspect with `sage behavior show <key> --library <library> --expand behaviorPlan --format json`; run only after the behavior is trusted/runnable.

Use lowercase/kebab-case keys returned by search/inspect output; display names are not reliable lookup keys.
