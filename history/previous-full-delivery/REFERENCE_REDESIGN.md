# LEDGER-Q reference redesign v2

The existing application and persisted API workflow are retained. This revision replaces presentation on landing, authentication, command center, quality workbench, change map, human review and audit/export with a hybrid of the six supplied reference images.

| Reference | Implementation | Data boundary |
| --- | --- | --- |
| Landing page 1 | Compact icy-blue hero, glass document stacks and amber human gate, 3-step journey, 3×2 capability grid | Supplied synthetic case; no copied sample metrics |
| Command center 2 | Wide navy navigation, glass model and three saved counts, evidence debt chart, release states, quality/review queues | Counts read from persisted workspace records |
| Workbench 3 / dashboard 5 | Sources/investigation/risk/CAPA/history tabs; source paper, chronology, gap/review dock, CAPA and closure readiness | Original 94.2% / 99.1% conflict retained; no fabricated root cause |
| Change review 4 / navigation 6 | Connected dependency map with selectable nodes, current revision strip, dependencies and review dock | Curves represent saved dependency edges only |
| Human review | Inline queue and exact-revision dock; request/reject/approval controls | Existing role, version, password, TOTP and evidence checks remain server-enforced |
| Audit/export | Saved counts, timeline, decisions, packets, replay, backup and restore | Controlled export cannot bypass HOLD or current approval |

## Motion and assets

The hero is one generated transparent 1536×1024 glass/silver document-stack asset with an amber review gate, optimized as WebP. Prompt: premium photorealistic glass document stacks connected to a central amber human-review gate on chrome base, icy blue/periwinkle/cyan reflections, three-quarter landscape composition, transparent background, no text or logos. Built-in image generation was used. This is a raster 3D render with depth/hover/continuous floating motion, not a rigged mesh or physical simulation. The evidence map is precise code-native geometry based on saved relationships.

Opening and route entry display only the brand/logo for about 520 ms, with no input blocking or simulated backend progress. Scroll reveal and motion respect reduced-motion settings. Reference mockup data, source dates and example numbers are not copied into the live records.

## Retained workflow

Full record details and existing edit, extraction, change impact, support, revalidation, signing and packet actions remain accessible through the review dock's “Inspect details & workflow actions”. Other workspace pages and URLs are preserved. Read-only roles do not receive editing controls.

## Verification and boundaries

TypeScript, production build, the existing 39 integration checks and six server-rendered presentation checks are run for this delivery. The suite uses actual SQLite statements, synthetic R2 data and explicitly mocked provider responses; it is not evidence of live provider quality or professional validation. Browser visual/interaction QA remains unavailable in this execution environment, so no pixel-perfect or complete browser-validation claim is made. Live provider configuration, external identity verification/recovery, professional evaluation and production qualification remain as disclosed in the implementation checklist.
