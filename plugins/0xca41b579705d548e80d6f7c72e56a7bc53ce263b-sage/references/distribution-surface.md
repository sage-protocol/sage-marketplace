# Sage distribution surfaces

Pick the smallest surface that matches the user-visible goal.

Local, P2P, shared, personal cloud, marketplace, and governed canon are choices,
not a sequence every task must complete. A discussion message body can hold a
shared draft or decision without publishing a library or CID.

- **Local skill/library**: reuse on this machine or in this repo. `sage skill add` and `sage skill expose` do not publish anything.
- **P2P**: trusted private machine/agent sync.
- **Shared library**: private collaboration with explicit members or invites.
- **Personal cloud**: creator-controlled hosted canonical copy. It starts private; use `sage library visibility <library-id> public` only when the user explicitly asks for public visibility.
- **Marketplace**: sale/distribution of a polished public package.
- **DAO promotion / governed canon**: public curation, provenance, accepted community practice, reputation, tips, bounties, and reflections.

## Visibility and retrievability invariant

Public feeds/search should advertise only artifacts that anonymous users can read. Owner-only, expired, unpinned, private, gateway-unretrievable, or otherwise unreadable prompt/skill/library CIDs must stay out of public discovery until republished or made public through the correct surface.

For public, marketplace, or governed surfaces, publication is not complete until the content is both pinned and anonymously gateway-retrievable:

```bash
sage config ipfs balance
sage library push <library> --dry-run --pin-duration 12months
sage library push <library> --cloud --pin-duration 12months --message "<what changed>"
sage library pin-status <library>
sage config ipfs status <manifest-or-item-cid>
```

Use `--pin-duration 12months` or `permanent` for artifacts expected to remain publicly discoverable; `free` pins are only appropriate for temporary/private drafts. If gateways return `no providers found`, 404, 504, owner-only, or timeout for a canonical CID, re-push/re-pin from a local source of truth and keep that CID out of public discovery until it resolves.

Ask before crossing local/private -> shared/public/paid/governed boundaries. Do not infer publication from "save", "install", "expose", or "use".

## Choose only the next useful capability

Repeated useful work can justify packaging or recognition. A well-scoped unknown
can justify funded investigation before a result exists. Neither requires a
mandatory progression through hosting, payments, and governance. Keep task
evidence, attribution, acceptance, and economic authorization distinct.

Route detailed wallet authority to `sage-wallet-ops`, governance to `sage-governance-participation`, P2P to `sage-p2p`, and library stewardship/collaboration choices to `sage-library-stewardship` or `sage-proactive-collaboration`.
