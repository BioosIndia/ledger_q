# LEDGER-Q extra features — verified working scope

This update preserves the existing LEDGER-Q application and its 20 canonical areas. It follows the accepted scope: **11 shared capabilities reused, 24 partial areas refined, 5 bounded functions added, 5 functions deferred**. These categories map the 45-feature source document; they are not 45 independently validated enterprise products.

## What changed

- Batch evidence now follows record completeness → QC review → readiness → named human review. Required missing steps and values stay visible; passing checks never release a batch.
- OOT review uses the source-stated fixed rule, six or more comparable prior batches, explicit method/unit/parameter and date checks. Insufficient history remains HOLD. OOT is separate from OOS.
- Regulatory intake accepts an authorized BEACON/manual handoff and requires official-source URLs plus preserved local old/new originals, exact excerpts and matching hashes. Signed intake review can reopen affected local work; company applicability stays UNKNOWN until reviewed. BEACON remains the source radar; this update does not duplicate its crawler.
- Existing SOP, risk, OOS/investigation, CAPA effectiveness, period review, improvement, model observation, privacy and AI-requirement controls have source-linked assessment views.
- Computed findings cannot be edited into a passing result. Changes to sources, prerequisites or workspace context invalidate dependent assessments and require fresh review.
- Reports include transitive evidence, exact revisions, missing evidence and next action. They are available as JSON and readable HTML, printable to PDF. Public synthetic report snapshots remain unapproved.
- Controlled model-use rollback creates a new suspended revision, preserves old history and requires fresh evaluation/review. Data-handling requests are saved for owner/legal-hold review; they never silently delete evidence.
- New routes are `/batch-review`, `/regulatory-intake` and `/quality-checks`. All original routes, auth, saved workspace separation, seven specialist roles, media, diagrams and human gates remain.

## Simple user journey

1. Sign in; the default workspace starts with zero records.
2. Select a separate original proof copy if you want the synthetic exercise. Add the additional proof only after explicit confirmation.
3. Or set your product/site context and add permission-granted source records. JSON templates are downloadable and uploadable.
4. Choose a check and saved evidence. The result is computed server-side and saved.
5. Inspect actual findings, sources, gaps and next actions. Create a linked held investigation/CAPA/training follow-up where needed.
6. Use the existing bounded specialist orchestration for candidate support. Provider processing remains opt-in; AI cannot override the typed checks or grant approval.
7. A separately authorized named QA or AI reviewer reviews the exact revision and signs with password + a fresh authenticator code.
8. Export an unapproved packet when gaps remain. Controlled export requires current supported human approval. No report grants batch/regulatory release.

## Shared controls reused

- Tamper-Evident Audit Trail — Hash-linked append-only audit and original version history; not an immutable ledger certification.
- Document Version Control — Original predecessor, bytes, version/hash and retained historical snapshots.
- Regulatory Knowledge Graph — Saved source IDs and dependencies, focused readable neighborhood and exact revisions; not a universal ontology.
- Training Requirement Tracker — Affected role, version and completion evidence; current source version required. No automated learning-management system.
- Quality Unit Governance Dashboard — Saved counts, evidence debt, due work and actual assessment entries. Fresh workspace remains empty.
- Role-Based Access Control — Membership-scoped reads/writes and separate QA/AI signing roles; owner is not automatically a reviewer.
- Secure Audit / Decision Logs — Saved actor, operation/revision, signing meaning, password + fresh OTP and retained decisions.
- Model Explainability Dashboard — Exact cited facts, rejected claims, contributions, model receipts, limits and next human action; no model-internal explainability claim.
- AI Guardrails Engine — Source grounding, schema checks, prohibited decisions, missing/stale evidence and fail-closed progression.
- Human Oversight Dashboard — All computed assessments join named exact-revision review; no critical value or approval is generated.
- Adversarial / Edge-Case Testing — Adverse/missing/stale/source/unit/batch/model/provider/role checks; deterministic fixtures are explicitly labelled.

## 24 refined areas

| Feature | Allocation | Working scope |
|---|---|---|
| SOP Compliance Analyzer | /regulatory-intake | Exact requirement + SOP excerpt, linked source and rationale; unsupported coverage cannot pass. |
| Deviation Auto Detector | /batch-review | Detect missing record observations and failed QC criteria; create linked held investigation, never a guessed cause. |
| CAPA Recommendation Engine | /capa + /quality-checks | Evidence-linked proposed CAPA with owner, gaps and human review. No automated cause or closure. |
| Inspection Finding Risk Engine | /quality-checks + /inspection | Reviewer-supplied risk factors prioritize findings; no predictive inspection outcome. |
| Risk Assessment Engine | /quality-checks | Explicit 1–5 factors and rationale; unknown input produces HOLD, not an invented score. |
| Compliance Report Generator | /audit / assessment details | Transitive JSON evidence packet + readable HTML report that can be printed to PDF, with visible HOLD/approval boundary. |
| Change Control Workflow | /changes + /regulatory-intake | Signed verified intake reopens affected local review and dependencies; historical decisions remain. |
| OOS Investigation Engine | /quality-checks + /events | First failure, chronology, hypothesis/evidence/state and separate human cause/disposition checks. |
| Root Cause Investigation Engine | /events + /quality-checks | Hypotheses remain distinct from named established cause; evidence and chronology are visible. |
| CAPA Effectiveness Verification Engine | /quality-checks | Before/after windows, counts, exposure, comparability and documented criterion; no causal benefit inferred. |
| Process Quality Trending Engine | /quality-checks + /trends | Comparable observations, explicit bands, period and denominators. No unsupported process-capability calculation. |
| Laboratory Quality Control Engine | /batch-review | Original QC result, batch/method/unit/specification context; missing or OOS values are held. |
| Annual Product Quality Review Engine | /quality-checks + /trends | Explicit product/site, period, batch denominator and area completeness declaration; saved event counts are not a commercial APQR. |
| Quality Metrics / Management Review Dashboard | /app + /quality-checks | Actual saved count summaries with scope and denominators; no invented improvement percentages. |
| Continuous Quality Improvement Engine | /quality-checks | Linked actions, owner/deadline, measurable criterion and measurement evidence; no predicted benefits. |
| AI Model Validator | /ai-evaluation + /quality-checks | Executed control fixtures remain separate from actual provider observations and exact intended-use qualification. |
| Privacy / Data Governance Engine | /quality-checks + /settings | Documented purpose/owner/provider permission/retention basis/legal-hold/deletion procedure and saved owner requests; automatic evidence deletion is not implemented. |
| Data Security Layer | All saved APIs | CSRF/origin checks, role isolation, uploads, encrypted keys, bounded files and safe escaped report output. No penetration-test certification. |
| Model Performance Monitor | /quality-checks + /ai-evaluation | Actual saved observation counts and latency summaries; no cost estimate without billing records or fabricated live success. |
| Data Quality Validator | /quality-checks | Exact grounding, required source provenance, original-byte hash verification, duplicate/context/number/date checks. |
| Bias / Fairness Assessment | /quality-checks + /ai-evaluation | Reviewer-defined subgroup denominators, critical failures and repeated model observations; representative fairness is not established. |
| Regulatory AI Requirements Mapper | /regulatory-intake | Official authority links, human applicability rationale, control ID, actual local evidence and named reviewer. No legal compliance verdict. |
| Model Versioning / Controlled Rollback | /quality-checks | Signed rollback from verified saved history creates a new suspended configuration revision and invalidates dependents. No provider-weight rollback. |
| Regulatory Documentation Generator | Assessment details + /audit | Readable evidence-backed findings, missing evidence, next action, exact revisions and human decisions; not regulatory submission documents. |

## Five additions

- **Batch Record Validator:** Explicit step manifest, missing record checks, acceptance comparison, performer/date/reference and duplicate checks.
- **Regulatory Update Monitor:** BEACON-compatible authorized source handoff; official URL allowlist, exact local originals/hashes, uncertainty and signed affected-work review. BEACON radar remains the monitor; this does not add another crawler.
- **Batch Quality Review Engine:** Batch/method/unit/sample/specification checks, original failed result and open linked quality work.
- **OOT Detection Engine:** Documented fixed review band, six or more comparable distinct prior batches, dates/units/methods; insufficient history is HOLD. Not a statistical qualification.
- **Batch Release Readiness Engine:** Category-correct QC/deviation/training/document prerequisites and exact current named decisions; no automatic batch release.

## Explicitly deferred

- **Supplier Qualification Tracker:** Supplier qualification is a separate validated supplier workflow; keep this scope focused.
- **Predictive Quality Risk Engine:** No predictive quality-risk claim from small synthetic samples.
- **Environmental Microbial Monitoring Engine:** Environmental/microbial monitoring requires a distinct sample/site/method workflow and validation.
- **Visual Packaging/Label Quality Inspector:** Packaging/label inspection requires representative images and separate validated visual acceptance.
- **Material Incoming Quality Engine:** Incoming material controls require a separate supplier/material qualification flow.

## Nine agentic parts — allocation

| Part | Actual allocation |
|---|---|
| Goal interpretation / planning | Saved parent run + bounded provider planner, and deterministic assessment-type specialist routing |
| Tool integration | Authenticated API actions, D1-compatible saved state, R2 original bytes and configured Groq/Gemini calls |
| Memory | Workspace snapshots, controlled source versions, frozen cases, previous runs and correction records |
| Orchestration | Revision guards, operation identity/replay, checkpoints, leases, bounded retries, pause/resume/cancel and manual-recovery record |
| Multi-agent collaboration | Existing seven bounded specialist roles, merged candidates, different-model independent review and retained contribution evidence |
| Human oversight | Named QA/AI role, exact revision, password/fresh OTP; source changes reopen review |
| Safety | Source/number/unit/context checks, membership, CSRF/origin, file boundaries, secret encryption, escaped reports and prohibition of automatic human decisions |
| Observability | Actual saved attempts, latency/usage where present, failed critical cases, first failures, evaluation observations and explicit unknown cost |
| Governance | Source/decision/export history, hashes, retention-basis records, owner data requests, version-bound release state and controlled rollback |

The original F01–F20 and L01–L12 contracts remain authoritative. Added assessment records share the existing workspace, dependency, review, audit and export path; there is no separate decorative workflow.

## Verification and limits

Receipts are in `docs/verification`. Unit/adverse checks and D1-compatible SQLite/R2-memory API tests exercise actual engine/API behavior. Provider contract tests use controlled mock responses and do not establish new live model quality. Server-render checks cover existing review and navigation components. Browser UI automation is unavailable in this environment; no full browser/device certification is claimed.

Synthetic data can demonstrate missing-value handling, saved state, signatures, invalidation, recovery and reports. It cannot establish commercial CMC/QA experience, qualified professional judgement, independent regulatory validation, representative fairness, actual time savings or production security/load qualification. The application remains a bounded working portfolio/MVP, with human decisions preserved.
