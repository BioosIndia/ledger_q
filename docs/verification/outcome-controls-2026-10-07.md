# LEDGER-Q outcome-control verification

Date: 7 October 2026. Scope: engineering fixes and bounded synthetic evidence; not qualified professional or regulatory validation.

## Changes

- Added a clearly unapproved readable run-brief download to the existing saved-outcome view. Audit/export remains the route for saved integrity-bound packets.
- Rejected malformed, duplicate, non-current and gapped candidate citations.
- Frozen-answer evaluation now requires the complete exact expected fact set, source and revision; extra facts and duplicate facts fail. Failed evaluations stay on HOLD.
- Blocked provider redirects and explicitly incomplete model responses; no completed receipt is recorded for those failures.

- Added bounded independent-reviewer fallback for transient provider failure using only the configured/discovered alternate model IDs. Failed attempts remain recorded; authentication denial cannot route around the denial.
- Explicitly held empty live fact results, and made provider-recovery actions readable.
- Used the documented low thinking level for supported Gemini 3 Flash models while retaining exact evidence and human review controls. This configuration is not an accuracy or latency claim.

## Executed checks

| Check family | Result |
|---|---|
| API/storage, model protocol, roles, recovery and adverse evaluation checks | 65/65 passed |
| Saved-outcome adverse tests | 15/15 passed |
| Server-rendered presentation checks | 9/9 passed |
| TypeScript | Passed |
| Managed Worker build | Passed |

## Boundaries

- Deterministic source, schema and safety checks supplement bounded model execution and human review. They do not prove semantic accuracy or suitability for a real customer.
- Model/provider fixtures are explicitly simulated; they are not live API execution. Any live check has a separate dated receipt and result.
- Evidence changes invalidate current use of old output/approval; historical audit and exported packets remain historical records.
- No automatic regulatory approval, batch disposition or release was added.
- Real-user benefit, regulatory accuracy, intended-use qualification and enterprise readiness are not established by these checks.
- Browser interaction/visual QA was not performed because the required managed browser-control capability is unavailable. Server render and compiled API checks have narrower scope.
- Production monitoring schedules were not resumed or altered. A paused/overdue radar is a gap, not a claim of continuous successful monitoring.

## Live failure and recovery scope

A fresh pre-update synthetic run reached independent review after successful planner/specialist calls, then the reviewer returned HTTP 503 on four attempts. The failure was saved and read back; no successful complete run was claimed. Connection tests had passed, demonstrating why connection alone cannot establish a working end-to-end workflow. See `live-outcome-before-fix-2026-10-07.json`. A fresh post-publication check is reported separately.

Provider configuration reference: https://ai.google.dev/gemini-api/docs/generate-content/thinking (checked 7 October 2026).
