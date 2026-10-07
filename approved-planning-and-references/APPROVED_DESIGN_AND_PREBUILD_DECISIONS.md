# LEDGER-Q — consolidated pre-build decisions

Prepared 6 October 2026. **Planning package only. App implementation has not started.** Rahul accepted the visual previews and requested this consolidation; building the application requires his next approval. Approval of a design preview does not approve a quality decision or establish production readiness.

## Read this package in order

1. Original 16-page Enterprise SaaS Master Blueprint in `references/` defines the product meaning and boundaries.
2. `LEDGER_Q_Master_Rulebook.md` defines development and acceptance gates.
3. `LEDGER_Q_Full_Mapping_and_Flowcharts.md` connects every feature, layer, agent, saved object, API, reference and failure path.
4. `LEDGER_Q_Feature_Traceability.csv` is the feature-by-feature acceptance register.
5. This file records Rahul's latest visual, motion, navigation and approval decisions.
6. Four files in `approved-design-previews/` are the accepted design direction. They are generated design previews, not captures of a functioning application. All illustrated record counts are fixtures.
7. Use the original videos in `references/`; contact sheets in `analysis-aids/` help locate frames. Recorded clips were inspected across their full timelines at 0.5-second sampling plus selected detailed frames; this is not an every-frame playback claim.

The original PDF, rulebook, mapping, flowcharts and traceability register are retained. This addendum refines presentation and acceptance, without replacing canonical requirements or adding a second architecture.

## Scope retained together

| Requirement family | Included scope | Where to inspect | Implementation state |
|---|---|---|---|
| Core features | F01–F20, all 20 | Mapping + traceability CSV | Specified; not built |
| Shared layers | L01–L12, all 12 | Mapping: Shared layers | Specified; not built |
| Agent roles | Parent orchestrator + seven bounded specialists | Mapping: agent handoff contract | Specified; not built |
| Data sharing | Permission-scoped revision/hash/span packets; 16 saved objects | Mapping: shared data + core saved objects | Specified; not built |
| Proposed additions | LQ-P01–P05, all five | Mapping: proposed child controls | Specified; not built |
| Additional challenges | LQ-R01–R04, all four | Mapping: challenge controls | Specified; not built |
| Other PDF controls | Vision intake, outage protocol, signing, MDM, 12 API allocations | Mapping: enhancements + API contracts | Specified; not built |
| Agentic architecture | Nine parts allocated within the 12 shared layers | Table below + mapping | Specified; not executed |
| Visual references | Three original videos + four approved previews | references/ + approved-design-previews/ | Design direction accepted |
| Delivery controls | Source traceability, test families, failure/recovery and release gates | Master rulebook + acceptance register | Must be demonstrated during build |

## Nine agentic parts: where they belong

| Part | Existing layers | Working behavior that must be proven |
|---|---|---|
| 1. Goal interpretation and planning | L08, L09 | Save a bounded plan, dependencies and permitted next actions; conflict/failure can replan without bypassing review. |
| 2. Tool integration | L03, L05, L12 | Use permission-checked parsing, database, provider and export adapters; blocked actions stay blocked. |
| 3. Memory and access | L04, L06, L07 | Retrieve approved, versioned tenant context; never mix workspaces or silently learn a correction. |
| 4. Orchestration and runtime | L08, L12 | Save tasks/checkpoints; bounded waits, retries, timeouts, leases, cancellation and restart recovery. |
| 5. Multi-agent collaboration | L09, L11 | Route to scoped specialists; merge exact-revision candidates; preserve disagreements and independent checks. |
| 6. Human review | L02, L08, L10 | Named authorized reviewer acts on an exact revision; approve, revise, reject, suspend or escalate with a recorded reason. |
| 7. Safety and policy | L01–L03, L06, L10 | Tenant/role/purpose boundaries, document-injection defense, safe file/network handling and restricted actions. |
| 8. Observability and evaluation | L11, L12 | Saved traces, actual expected/observed checks, errors, attempts, timing/cost where measured and visible failures. |
| 9. Governance and accountability | L04, L06, L10, L11 | Source history, AI contribution, decisions, retention and version-bound audit/passport/export. |

Calling the app agentic requires actual planning, routing and collaboration execution evidence. A deterministic path is labelled deterministic. Live model receipts do not establish scientific validation. Agents cannot determine regulated root cause, batch disposition, CAPA closure or regulatory release.

## Reference allocation and customization

| Original file | Use | Preserve | Adapt for LEDGER-Q |
|---|---|---|---|
| Screen Recording 2026-10-05 182302.mp4 | Landing composition + automatic hero mechanism | Icy-blue framed scene, silver articulated object, balanced whitespace and restrained CTA | An original quality/AI evidence mechanism; understated LEDGER-Q background word; moderate readable heading; no factory ROI or fake production metrics. |
| Screen Recording 2026-10-05 182549.mp4 | Distinct visual tiles and supporting sections | Six-tile rhythm, editorial typography, controlled lilac/orange accents and depth | Source, quality event, review, passport, trace and trend tiles, each different; no foreign logos or invented customers. |
| Screen Recording 2026-10-05 182643.mp4 | Assurance dashboard and data hierarchy | Compact navigation, pale-blue canvas, clear cards, restrained charts/logs | Saved quality/AI queues, evidence debt, review status and audit history; denominators and source links attached. |

The clips do not demonstrate the complete sign-in, graph selection or scroll behavior. Those interactions are proposed customizations, to be implemented and verified separately.

## Keep the accepted visual direction

Use the four approved previews as composition/palette references, not background screenshots for functional screens. Preserve the paired-loop LEDGER-Q brand, ice-blue/slate surfaces, silver/glass evidence object, clear cards and visible human boundary. Keep space around the object and headline; do not enlarge typography until it overwhelms the page.

| Token | Color / rule |
|---|---|
| Main text | Navy #122338 |
| Supporting text | Slate #273E55 |
| Canvas | Ice #E5EEF8 |
| Cards | Soft #F5F7FB |
| Accent | Cyan #2AB7D1 |
| Attention | Amber #B67512 |
| Critical state | Red #B73642 |
| Approved state | Green #197650, state only |

Final foreground/background pairs must pass contrast checks; a palette alone is not proof of accessible contrast.

## Motion: cinematic but readable

- Hero: one slowly moving articulated evidence mechanism, approximately 12–18 seconds per loop. The two linked streams suggest quality records and AI assurance. Use subtle pivot/compression/translation inside its reserved space. It runs automatically during normal viewing.
- Public landing: short 180–280 ms reveal when a section enters the viewport from above or below. No dramatic page jumps, flashing or prolonged hidden content. All content remains accessible if scripting fails.
- Hover: a small lift of at most 3 px or scale up to 1.015 on selected visual cards; clear keyboard focus gives an equivalent affordance.
- Pointer motion: bounded gentle tilt/parallax on the decorative hero object only, for fine pointers. No custom cursor that blocks selection, no text-following object and no pointer-dependent essential information.
- Dashboard: quiet live state transitions and short panel changes. Evidence text, tables and forms remain steady. Do not animate numbers without a saved record change or let decorative motion imply processing.
- Charts/graph: highlight actual selected dependencies and affected nodes; underlying counts and states come from saved records.
- Touch: no hover-only actions. Mobile object scales inside its container and never covers controls.
- Respect reduced-motion settings with a static view. Pause rendering automatically when hidden/offscreen to preserve performance. Automatic normal motion does not mean overriding user accessibility preferences.
- No visible decorative pause/action buttons are required by the requested design. Do not use continuous moving content that needs a user control under accessibility rules; keep the automatic object decorative and nonessential, and provide a static experience through reduced-motion preference.
- These are real 3D/depth and motion behaviors; do not label them scientifically as 5D/7D/8D.

## A simpler, distinct user journey

Keep all 14 canonical destinations and their data/role boundaries. Do not copy BEACON/FORGE's permanent long left workflow list with a generic right panel. Use a compact grouped navigation rail and a task-first stage bar, with full labels available on expansion/mobile. The approved palette/card hierarchy stays intact; navigation grouping is a refinement, not a new scope.

| Group | Destinations |
|---|---|
| Home and records | /app, /sources, /requirements |
| Quality work | /events, /changes, /capa, /training, /inspection, /trends |
| AI assurance | /ai-registry, /ai-evaluation |
| Decisions and controls | /review, /audit, /settings |

**Public visitor:** Landing → labelled read-only synthetic case → original evidence → gap/conflict → human boundary → recorded example outcome. No account is necessary just to inspect this isolated public case; visitors cannot sign or change it.

**Authorized worker:** Landing → sign in → select permitted workspace → Command Center → open assigned quality event or AI use → evidence workbench → check gaps/dependencies → exact-revision review → controlled output or visible HOLD.

Within a case, the horizontal stage bar follows **Source / Check / Review / Record**. The evidence workbench uses a central record with a contextual source drawer and a visible review summary, instead of several always-open competing panels. On mobile, stages and drawers become a simple stacked sequence. Every modal has a visible Close button, Escape dismissal and focus restoration; Back returns to the prior selection. Destructive or externally revealing actions require an appropriate confirmation; simple reading/navigation must remain understandable.

## Build sequence after Rahul approves

1. Lock the supported stack and hosting surface; confirm available project access, secret configuration, roles and provider-processing boundaries. Do not ask for API keys in chat. Preserve earlier provided input where available.
2. Create a source-to-proof register from F/L/P/R and nine-part allocations; every accepted feature needs a saved record, expected behavior, adverse case and observed result.
3. Establish durable isolated storage, originals/version hashes, scoped identities, role checks and audit events before adding impressive visuals.
4. Build one complete synthetic quality slice: source → requirement/SOP mapping → event/investigation gaps → CAPA candidate → named QA review → effectiveness evidence → controlled closure or HOLD.
5. Build the connected AI-use slice: intended use → model/prompt/tool/data versions → provenance → frozen evaluations → human review → use passport. VALID never means product/batch regulatory release.
6. Connect bidirectional changes and blast radius. Changing a source, SOP, prompt, model, tool, data or policy stales affected outputs and invalidates their current approval; history remains reconstructable.
7. Implement seven bounded specialist contracts and the parent workflow. Check late/stale output, disagreements, provider outage, three bounded retries, DLQ/manual continuity and restart recovery. Do not pretend mock inference is live AI.
8. Apply the accepted landing, tile and dashboard visual language, automatic decorative motion, stage navigation and responsive workbench. Add no fake counters or unsupported metrics.
9. Complete F01–F20 and P/R controls using the traceability register, rather than declaring a slice the complete product. Each pending feature stays visible in the delivery checklist.
10. Run adverse, permissions, data integrity, revision/signature, AI contribution, recovery and accessibility checks. Create a saved labelled recruiter case, screenshots and code/package evidence only from actual executed work.
11. Publish only after supported critical gates pass. Deliver the URL, code package and a checklist separating passed, failed, untested and externally dependent items. No fabricated production or clinical validation claims.

## Acceptance gates that prevent avoidable rework

| Gate | Evidence required | Failure behavior |
|---|---|---|
| Source completeness | Every PDF F/L/P/R item, saved object and endpoint accounted for | Flag omission before build expands |
| Preview fidelity | Accepted composition/palette/spacing, moderate typography, three reference allocations | Correct scoped visual mismatch |
| Useful task journey | Public synthetic case and permitted workspace journey reach a understandable record/outcome | No decorative-only dashboard acceptance |
| Evidence correctness | Exact source/version/span, preserved units/batch/context; missing value never invented | UNKNOWN / HOLD / REVIEW REQUIRED |
| Human authority | Current role, exact revision, reason, signing checks; no agent approval | Block invalid decision/export |
| Dependency change | Quality→AI and AI→quality stale propagation, fresh evaluation/review | Suspend affected current assurance |
| Agent execution | Saved actual plan/delegation/merge/review and labelled deterministic fallback | No unsupported live-agent claim |
| Security | Tenant separation, restricted tools, safe uploads, injection/secret checks | Block unsafe paths |
| Operational recovery | Retry/timeout/idempotency/restart, backup/restore and rollback evidence | Explicit failure/debt; no hidden success |
| Usability/accessibility | Keyboard, readable text, Close/Back, touch, motion preference, loading/error states | Fix before release |
| Honest outcome reporting | Actual test denominators, failures, limitations; synthetic data visibly labelled | No invented accuracy/ROI/benefits |

No zero-error or 100% production-readiness guarantee is possible from planning or generated previews. Synthetic tests can prove particular software behaviors; professional validity, real-user benefits and intended-use acceptance require suitable independent evidence and authorized qualified review.

## Decision status

- Requirements/source package: consolidated.
- Four design previews: retained as Rahul's accepted direction.
- Motion/simple journey/distinct navigation: specified here for implementation and testing.
- LEDGER-Q app code, database, live AI, deployment and production results: **not started or proven by this package**.
- Next transition: Rahul approves starting LEDGER-Q, then implement the sequence above.
