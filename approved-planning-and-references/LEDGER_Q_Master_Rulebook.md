# LEDGER-Q — Master Build Rulebook and Delivery Checklist
Rahul Dewangan / PRAMANEX · 6 October 2026

## What this document does
Yeh rulebook agle build ka working agreement hai. Abhi LEDGER-Q application build, deploy ya validate nahi hui hai. PDF defines what to build; videos define selected layout/motion references. Dono ko ek connected product mein use karna hai. “100% perfect” promise nahi: tested critical journey mein no known P0/P1 defect, clear failures aur reproducible evidence target hai.

PDF authority: `PRAMANEX_LEDGER_Q_Enterprise_SaaS_Master_Blueprint(3)(3).pdf`, all 16 pages. Canonical scope: F01–F20 + L01–L12. LQ-P01–P05 and LQ-R01–R04 are proposed child controls, not extra top-level modules or already proven differentiators. Separate GxP Training AI OS remains out of scope; basic F10 is included.

## First decisions — lock before writing application code
- ☐ Preserve every canonical ID, meaning, layer and human boundary. Maintain a requirement → UI → API → data → test → evidence register.
- ☐ Record intended users and intended/excluded uses: QA reviewer/approver, investigator/owner, AI assurance reviewer, SME/process owner, admin/validation. Admin role alone never grants QA authority.
- ☐ Choose deployment stack once. PDF recommends React/TypeScript, FastAPI, PostgreSQL/Supabase-style auth/RLS, versioned objects and n8n parent workflow. A Sites Worker alternative is an explicit architecture decision, not a silent substitution. Preserve equivalent permissions, state and evidence contracts. Do not copy BEACON/FORGE identities or secrets.
- ☐ Freeze the synthetic scenario, normal/adverse expected outcomes and video-to-screen allocation before visual iteration.
- ☐ Fix API/state/schema contracts before UI widgets. One controlled parent write path; no independent decorative workflows.
- ☐ Define acceptance per journey before claiming completion. No score from an unlabeled synthetic case becomes professional accuracy or customer benefit.

## Build sequence — keep this order
1. **Inspect and preserve.** Inventory repo, PDFs, videos, existing routes/assets/data. Keep source originals unchanged. Create decision log and stable module IDs.
2. **Accounts and isolation.** Owner/reviewer/member role boundaries, tenant filters, private originals and safe session/logout flows. Working email account flow first; Google shown only when real provider setup exists. Identity verification/recovery and signing factors get explicit tests.
3. **Schema and revision state.** Versioned sources/requirements/events/AI uses/runs/decisions/passports; stable IDs, hashes, predecessor links, append-oriented history and expected-revision guards.
4. **Source intake and parsing.** Permission and purpose before upload/model/network calls. Save original first; preserve exact page/region/table/series references. Text/table deterministic path first, vision conditionally. Ambiguous reading → UNKNOWN/NEEDS_REVIEW, not generated certainty.
5. **Requirements and gaps.** F01–F04: exact requirement → SOP/process mapping → rationale → visible missing/conflicting/stale coverage. Add evidence-debt counts from saved records.
6. **Quality event slice.** F05–F07: deviation/OOS/OOT chronology, source records, separate risk dimensions, hypotheses and missing evidence. Human owns root cause and disposition.
7. **Change and dependencies.** F08 + P01: quality→AI and AI→quality changes reopen only affected current controls. Old decisions remain immutable history. Compute graph paths, not a decorative list of dependencies.
8. **CAPA, training and ownership.** F09/F10/F13: proposed corrective work → named owner/date → implementation evidence → effectiveness evidence → qualified human closure. Completion against the correct source/version, not an unversioned training tick.
9. **Human decision and signature.** F14: review exact revision, controlled reason, current authority and fresh Password + OTP or approved biometric second factor at signing. Failure/stale/hash mismatch routes HOLD/REAUTHENTICATE/RE-REVIEW. Preserve a new signed decision event; never a model approval.
10. **AI use and provenance.** F16/F17: model/version/intended/excluded use/owner/reviewer/dependencies, pinned configuration and exact run contribution. Candidate agents cannot create approved facts or change policy.
11. **Evaluation and challenges.** F18/F19 + R01–R04: frozen expected answers, source grounding, evidence removal, unit/batch/version mutations, bias/edge/repeated runs, paired model changes. Retain disagreement and first failure.
12. **Release states and revalidation.** F20: VALID/SUSPENDED/EXPIRED/REVOKED/REVALIDATED according to evidence/context/retest/human authority. Source/model/prompt/tool/data/policy changes invalidate affected assurance.
13. **Inspection, trends, replay and export.** F11/F12/F15: finding/action chain, denominators, historical version replay, provenance, signed decision and version-bound controlled packet. Open debt visible; never regenerate old history from today’s model.
14. **UI and motion.** Implement the already mapped screens on the saved backend state. Video 1 hero; Video 2 public bento/proof; Video 3 workspace layout. Use compact readable typography; no oversized operational headings. Real close/back/Escape/focus controls on every dialog.
15. **Adverse/security/recovery checks.** Run normal, wrong-role/tenant, stale-revision, concurrency, unsupported value, timeout, retry exhaustion, provider outage, prompt injection and restore cases. Build/typecheck; inspect public bundle for secrets/private records.
16. **Controlled hosted demo.** Verify actual source save/readback, signing denial/success with configured factors, graph navigation, revision reopening, protected export, worker behavior without browser, recovery and reduced-motion/mobile access. Hosted URL alone is not a pass.
17. **Handoff.** Deliver source ZIP, setup, migration order, accurate media, test receipts, feature-proof register, claim boundaries and remaining gates. Share the existing app URL; don’t create replacement identities to hide problems.

## Execution rules that prevent repeated mistakes
- Patch working components; do not redesign a completed section without a specific defect or accepted scope change.
- Each request gets a small change list, affected IDs, tests and rollback note. Preserve all unrelated routes/data/navigation.
- Maintain a checkpoint with last passing commit, remaining task, migration state and next action. “Continue” resumes there rather than rebuilding.
- Reuse source IDs, typed schemas, components, state machine and proof fixtures. Do not create a second register because a screen needs a different card.
- Use deterministic rules before model calls. Retrieve only authorized necessary spans; cache with tenant + source version + model/config/policy hashes. Changed dependency invalidates cache; no silent provider fallback.
- Separate configured/implemented/tested/live/pilot/production labels. A synthetic OAuth pass is not real Google sign-in. Provider smoke is not qualified scientific performance. Scheduler config is not completed monitoring.
- Store secrets server-side, never in source/browser/screenshots/export. Record permission before third-party document processing.
- Preserve first failures and corrected regression results. Do not remove adverse cases to raise a percentage or count abstention as successful task completion.
- Count tests with scope/date/denominator. Do not add different suites into “accuracy.” Time/cost benefit requires a comparable baseline and actual users.
- Keep source/inputs/citations selectable. Avoid cursor/caret confusion on decorative graphics; controls have pointer/focus states. Never make evidence inaccessible just to avoid text selection.
- Public assurance shows outcomes, evidence and limits, not confidential prompts, secret configuration, exploit details or proprietary operating internals.
- If access, billing, provider, permission or qualified review is missing: record the exact blocker. Synthetic fixtures can prove bounded behavior; they cannot impersonate real reviewers or production qualifications.

## Non-negotiable runtime contracts
- One parent owns authorization, idempotency, parsing, routing, validation, persistence, human waits, retries, exports and terminal state.
- Exact input/output/source revision and correlation/run ID on every work item. Expected-revision guards on decisions/corrections and role recheck at commit.
- Eligible provider errors: 3 automatic retries with exponential backoff, then visible exhausted/DLQ path. No retry for forbidden/invalid work; no duplicated external effects.
- Noncritical summaries can wait in DLQ with exact revision, cause and attempt metadata. Recovery rechecks authorization/policy/freshness.
- Critical quality work falls back to deterministic/manual mode. AI outage cannot close, release, suppress or erase an event.
- Notifications use an outbox and idempotency key. A late task must not write against a newer workspace/revision.
- Original text/image region retained; generated JSON is a candidate, never a replacement for laboratory original.
- Human correction can become regression evidence only through verify → classify → approve → version → retest. No silent self-training or benchmark/policy rewrite.
- Signature gateway is compliance-targeted, **not evidence of Part 11 compliance**. Require appropriate validation, SOPs, retention and operating controls before making that claim.

## Must-pass delivery gates
| Gate | Evidence needed | What must not be claimed |
|---|---|---|
| SPECIFIED | IDs, states, objects, APIs and expected behavior mapped | “Built” from a label |
| BUILT | Runnable code and reproducible setup | “Tested” from compilation |
| TESTED | Expected/actual checks and retained failures | Real scientific accuracy from fixtures |
| MVP | Useful bounded quality + AI journey, saved evidence and human authority | Full enterprise qualification |
| CONTROLLED LIVE DEMO | Actual endpoint/readback, worker behavior, access boundaries and operating limits checked | Pilot/customer adoption |
| PILOT | Permitted organization inputs, qualified reviewers, security/privacy/support and success criteria | ROI without measured baseline |
| PRODUCTION | Intended-use-appropriate validated operating controls and accepted risks | Permanently bug-free or autonomous regulated release |

## Master acceptance checklist
- ☐ All 20 feature IDs/meanings and all 12 shared layers preserved in traceability.
- ☐ Proposed P/R controls clearly labelled and tested before promotion.
- ☐ Quality and AI streams use one evidence graph and named human boundary.
- ☐ Normal path and adverse path both runnable; missing/stale/conflicting evidence visible.
- ☐ Tenant/role/purpose enforced on intake, retrieval, graph, tasks, decisions and exports.
- ☐ Exact original, version, span, coordinates and model/run identity reconstructable.
- ☐ Source/quality and AI changes invalidate correct downstream current state both directions.
- ☐ Signature exact revision/reason/factor bound; stale/failed signing never completes a decision.
- ☐ CAPA requires implementation + effectiveness evidence + human closure.
- ☐ F10 training impact/version trace included; standalone training OS excluded.
- ☐ Frozen/adverse/paired tests, denominator, abstention and critical failures retained.
- ☐ Correction firewall prevents silent learning/policy/benchmark edits.
- ☐ Retries/DLQ/manual continuity, idempotency and recovery tested.
- ☐ Product/site/user local IDs accept optional external UUID with mapping history; match grants no authority.
- ☐ Dashboard numbers and graphs come from saved records; no fabricated percentages or live motion telemetry.
- ☐ Email/signout and configured provider paths work; unavailable options visibly disabled with explanation.
- ☐ Every action/link/dialog works; keyboard, close/back, scroll isolation, contrast and reduced motion checked.
- ☐ Backup restore reconstructs a historical quality + AI decision and packet with matching IDs/hashes.
- ☐ Source ZIP/media/test logs/README/claim register and pending gates match actual delivery.

## Ownership and remaining inputs
Engineering, fixtures, code, diagrams, synthetic tests and reports can be prepared by the assistant. Real organization permissions, identity/provider/billing authorization, qualified QA judgement, company data approval, professional pilot results and intended-use production acceptance require Rahul or authorized professionals. This planning task does not need an API key and sends no documents to providers.
