---
name: sage-vision-channel
description: >
  Operate a private Buzz Sage Vision channel as a living, evidence-backed vision
  loop. USE WHEN Sage vision should evolve from agent-team, ACP, relay, swarm,
  or product-usage evidence; when configuring the Vision Scout, Repo Grounder,
  and Vision Steward; or when reviewing a vision proposal draft. DON'T USE for
  autonomous canon edits, Buzz source changes, or granting filesystem, wallet,
  publish, or governance authority from conversation.
tags:
  - sage
  - buzz
  - vision
  - relay
  - agent-teams
  - governance
---

# Sage Vision Channel

Keep Sage's vision alive through relay conversation and portable agent roles without making Buzz source code or channel history the authority.

## Product boundary

- Buzz relay state owns the private channel, memberships, managed agents, Agent Team, messages, triggers, and heartbeat schedule.
- Sage skills own the portable operating procedure, role prompts, evidence rules, and proposal format.
- Repository and runtime evidence determine what exists now.
- A human decision controls canon.
- An operator-selected local vault stores private proposals and accepted context. The vault path and contents stay out of relay state and published skills.

Do not modify Buzz source to install this workflow. Do not create a parallel privileged action path. Any future automatic relay-to-local write must use the general Sage trusted-origin action and authority framework.

## Roles

Use three separate managed agents. Do not combine proposal drafting with independent grounding.

1. **Vision Scout** — loads `sage-vision-signal-capture`; emits a dated Signal or stays silent.
2. **Repo Grounder** — loads `sage-vision-claim-grounding`; labels claims `verified`, `contradicted`, or `unknown` using an explicitly granted read-only evidence capability.
3. **Vision Steward** — loads `sage-vision-proposal-drafting`; emits one reviewable draft after grounding. It does not write local files or decide canon.

Role templates are in `references/agents/`. Shared channel instructions and canvas seed are in `references/instructions.md` and `references/canvas.md`.

## Relay configuration

1. Create a private `Sage Vision` channel through the existing Buzz relay UI or verified CLI.
2. Keep validation owner-only or allowlisted.
3. Create the three managed agents with the `buzz-agent` runtime.
4. Subscribe them to the channel and group them into an Agent Team ordered Scout → Grounder → Steward.
5. Use mention-only triggers. Scout may mention Grounder, Grounder may mention Steward, and Steward never mentions another agent. Do not enable broad protocol-keyword triggers.
6. Attach explicit read-only evidence capabilities only to Scout and Grounder. Steward receives only the drafting skill and relay conversation capability.
7. Deny `buzz-dev-mcp`, shell, arbitrary file tools, general mutation tools, publish, wallet, and governance mutations.
8. Enable an hourly heartbeat only for the Scout. An empty heartbeat produces no message.
9. Seed the channel with `references/instructions.md` and `references/canvas.md`.
10. Store live channel, team, agent, and community identifiers only in relay state. Never add them to this skill.

Use `references/relay-config.example.json` as a field checklist, not as a file to submit directly. It contains no credentials, paths, or live identifiers.

## Message protocol

1. **Signal** — observation, source, date, experience effect, and uncertainty.
2. **Challenge** — one concrete objection and what would falsify it.
3. **Proposal draft** — target concept, exact vision delta, evidence, disconfirming evidence, and experience consequence.
4. **Decision** — human accept, revise, or reject.
5. **Receipt** — local or governed artifact reference after a separately authorized write.

Conversation may trigger analysis. It never grants filesystem, publish, wallet, signing, or governance authority.

## Local proposal handoff

The remote Steward returns a draft payload only. A human or separately authorized local agent then:

1. Reads the local vault rules and current changelog.
2. Rechecks repository/runtime claims and the current target note.
3. Creates a new proposal artifact in the operator-approved inbox.
4. Leaves the decision pending human review.
5. Records material vault changes under the vault's own changelog rules.
6. Applies accepted canon wording only as a separate local change.

Never send the vault root, private note text, target hashes, credentials, or local receipts to the relay or a public library.

## DAO publication boundary

A governed library may include this skill, the three role skills, and sanitized templates. It must exclude live relay identifiers, vault content, machine paths, credentials, private proposals, and claims that governance grants local filesystem authority.

## Verify

- Buzz source has no workflow-specific change.
- The channel is private and uses existing relay primitives.
- Only the Scout heartbeats, with silence on no signal.
- Agents use mention-only forward handoffs and Steward terminates the chain.
- The Grounder returns `unknown` without evidence capability.
- The Steward drafts but cannot write local files.
- No agent can invoke shell, arbitrary file mutation, publish, wallet, or governance tools.
- Canon changes only after a human decision and separate local edit.
