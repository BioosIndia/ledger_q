# LEDGER-Q delivery checklist

6 October 2026. This records implemented behavior and its limits. It is not a claim that the product is qualified for commercial regulated use.

## Working product

| Feature | What is connected | Evidence / boundary |
|---|---|---|
| F01 — Controlled Quality Source & Document Registry | Permitted TXT/PDF/image originals, version/hash/predecessor, checked candidate transcription; PDF automation remains external. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F02 — Requirement Extraction & Exact Evidence Traceability | Exact text requirement candidates with source/version/span/offset; named review controls acceptance. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F03 — Regulation-to-SOP / Requirement Mapping | SOP coverage, rationale, linked requirement and source records; missing support blocks approval. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F04 — Compliance Gap, Conflict & Evidence-Sufficiency Control | Saved gaps, conflict and dependency states; unsupported candidates fail grounding checks. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F05 — Quality Risk, Severity & Confidence Assessment | Separate severity, likelihood, controls and confidence fields; human root cause and disposition. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F06 — Deviation Investigation Review | Investigation chronology, hypotheses, human conclusions and immutable contribution trail. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F07 — OOS/OOT Investigation Review | Synthetic OOS assay conflict 94.2% vs 99.1%; missing rationale remains HOLD. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F08 — Bidirectional Change-Control & Impact Assessment | Transitive saved links, quality-to-AI invalidation, AI-to-quality links and historical decisions preserved. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F09 — RCA-CAPA Lifecycle & Effectiveness Verification | Implementation/effectiveness/cause gates, due dates and signed closure; missing proof blocks closure. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F10 — Training Impact & Retraining Traceability | Role/version/completion evidence and fresh review requirements. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F11 — Audit / Inspection Finding & Readiness Management | Finding, owner, linked action and evidence packet; no formal inspection-readiness certification. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F12 — PQR/APQR & Quality Trend Review | Saved counts, denominators and time window; no statistically proven quality trend claim. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F13 — Owner, Deadline, Escalation & Closure Control | Owner/due date, visible overdue work and saved manual escalation; no external delivery configured. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F14 — Human QA Review, Override & Controlled Correction | Current role/revision/hash, password plus real TOTP, decisions and reviewed regression proposals. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F15 — Audit/Version Reconstruction, Event Forensics & Controlled Export | Revision replay, append audit, R2 packets, checksummed backup and isolated copy restore. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F16 — AI Model / Use / Context & Release Registry | Intended/excluded use, model/config/expiry, signed passport states; synthetic authority only. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F17 — AI Provenance, Transparency & Contribution Record | Saved parent/specialist/reviewer outputs, attempts, input hashes, correlation and human contribution boundary. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F18 — AI Evaluation, Grounding & Hallucination Suite | Executed deterministic controls plus signed frozen cases and optional provider comparison. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F19 — Bias, Edge-Case & Consistency Verification | Explicit subgroups and two-model repeated checks; live inference and representative fairness evidence not established. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |
| F20 — Assurance Monitoring, Regression, Blast Radius & Revalidation | Change/expiry invalidation, visible assurance debt, approved correction proposals and fresh revalidation/review. | tests/integration.mjs + saved UI records; provider paths use mock contract tests unless a workspace configures live access |

## Nine agentic parts

| Part | Actual allocation |
|---|---|
| Goal / planning | Saved bounded parent plan, evidence checks and one held-case next plan; no regulatory release planning. |
| Tools | Scoped D1/R2 source, extraction, provider and export adapters; fixed Groq/Gemini endpoints and document consent. |
| Memory | Current workspace records, prior snapshots, frozen cases and reviewed corrections. |
| Orchestration | Saved phases/checkpoints, leases, idempotency, pause/resume/cancel and exhausted/manual-recovery state. A run executes through a request; no independently scheduled worker queue is claimed. |
| Multi-agent collaboration | Seven named bounded roles; candidate checks and different-model independent review when configured. No unrestricted swarm. |
| Human review | Explicit synthetic reviewer role plus password/TOTP, exact revision/hash and rationale. |
| Safety | Tenant/role/source-purpose limits, file checks, untrusted source isolation and blocked human-authority actions. |
| Observability | Actual saved attempts, errors, run duration, available provider token usage, first failures and evaluation denominators. No fabricated cost or speed benefit. |
| Governance | Original provenance, revision audit, signature records, correction firewall, expiry and controlled export. Retention policy metadata exists; automated retention deletion and regulatory certification are not claimed. |

## Design and navigation

- Landing → inspect the separate original proof, or create a fresh empty workspace. Login → zero-record private dashboard; compact Workspaces picker for saved work. Private workspace → permitted sources or explicit proof loading → Quality workspace / AI assurance / Review and evidence.
- Source → check → human review → saved record. Each evidence panel has close controls and a clear original-opening confirmation.
- Approved ice-blue/slate palette, six distinct bento cards, wide expandable navy navigation, scroll reveal and pointer tilt.
- Glass document stacks and an amber human gate are generated raster artwork with continuous CSS motion; it is not an articulated WebGL simulation. Reduced-motion preferences and hidden-tab pauses remain supported.
- The three supplied videos, the original four previews and six latest UI reference images remain in the complete package as reference material, not as captured footage of the implementation.

## Tests and limits

- 55 D1-compatible SQLite / R2-memory integration checks pass. Local model response tests are mocked. Actual hosted provider checks, when performed, are separate records; no professional outcomes are inferred.
- TypeScript check and official Worker build must pass before deployment. Final native deployment result is recorded separately.
- Browser visual QA was unavailable because the required control-browser capability was absent. Responsive rules and accessible modal/navigation primitives are implemented, but pixel-perfect browser verification is not claimed.
- Workspace aggregate is bounded to 1,500 records / 1.8 MB current state. Backup limits: 2 MB referenced original bytes and 4 MB packet. This is not globally scaled enterprise storage.
- Backup copy retains originals and the imported historical bundle; it starts a new local review history. Imported decisions cannot grant current approval.

## What needs real access or professional evidence

- Connect and test Gemini from Controls using the securely configured key, or configure Groq and two accessible model IDs. Selected-document processing permission remains required. No existing project keys were copied.
- Automated PDF/table parsing, email verification/recovery, Google OAuth, external notification delivery and unattended queue scheduling require selected real services and further integration.
- Representative held-out data, qualified reviewer answers, supervised users, measured manual baseline, production load/security assessment and full disaster-recovery drills remain necessary before paying regulated users.
- No real QA qualification, commercial CMC experience, Part 11 certification, autonomous regulatory release or percentage improvement is claimed.

## Reference redesign v2

Landing, sign-in, command center, inline quality workbench, connected dependency map, review dock and audit/export were updated without replacing persisted workflows. See Reference_Redesign_v2.md for screen-to-reference mapping and exact limits. Review controls reflect the current role; record details preserve all previous workflow actions.

## Fresh workspace and Gemini v3

See Workspace_and_Gemini_v3.md. Existing user records are preserved; proof import cannot overwrite private evidence. The live Gemini planner, specialists and independent reviewer retain saved checkpoints, model identity, usage, failures and human HOLD. Hosted checks are recorded separately from mock transport tests.

Model discovery excludes rolling latest aliases. The reviewer prefers a different available model family, and connectivity cannot pass when both replies report the same underlying model version. Actual model identity is retained in provider attempts.

Gemini connection verifies the author and tries up to three reviewer candidates when auto-selecting. Failed attempts and safe HTTP status codes are retained. A manually selected reviewer is not silently replaced. Special-purpose Omni/audio/image/deep-research models and rolling latest aliases are excluded from automatic structured JSON routing.

## Fresh dashboard and personalization v5

Floating labels are content-sized with opposing anchors reset. Workspaces and proof use compact toolbar dialogs. Default entry reuses an empty owned workspace or creates one; populated work remains untouched. Browser-local account-scoped spacing, accent, reading size and reduced-motion preferences are functional. Nine presentation checks accompany the 55 integration checks. See Fresh_Dashboard_and_Personalization_v5.md.
