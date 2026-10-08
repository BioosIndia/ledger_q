# LEDGER_Q latest bilingual walkthrough

Source revision: 0e2d96d92006026018e36c6747cc380aced7c457. Date: 2026-10-08.

LEDGER-Q quality records, investigation, corrective action aur AI use ko evidence aur human QA responsibility ke saath jodta hai.

LEDGER-Q connects quality evidence, investigations, corrective actions and AI-use controls to accountable human QA decisions.

## What it is

Hinglish: LEDGER-Q quality records, investigation, corrective action aur AI use ko evidence aur human QA responsibility ke saath jodta hai.

English: LEDGER-Q connects quality evidence, investigations, corrective actions and AI-use controls to accountable human QA decisions.

## Why I made it

Hinglish: Quality ka result sirf closed likhne se prove nahi hota. Original failure, kya investigate hua, kya action liya aur kya action effective tha - sabka proof chahiye. Maine missing proof aur premature closure visible rakhne ke liye LEDGER-Q banaya.

English: A closed status alone does not prove a quality problem was investigated or corrected. I built this independent work sample to keep original findings, actions, effectiveness evidence and responsible decisions connected.

## How the work proceeds

Hinglish: Original record aur requirement se event link hota hai. Investigation mein facts aur suggested cause alag rehte hain. Human reviewed action plan ke baad implementation aur agreed window ka actual evidence dekha jata hai. QA exact version par decision deta hai; changed evidence fresh review mangta hai.

English: Original evidence is linked to a requirement and quality event. Investigation facts remain separate from hypotheses. A reviewed action plan precedes implementation and effectiveness evidence. QA decides on the exact revision, and changed dependencies reopen affected review.

## What the user should receive

Hinglish: User ko kya issue hai, kis proof se, kya missing hai, kaun responsible hai, next action kya hai aur closure kis basis par hua - ye clear report milna chahiye. AI root cause ya batch release decide nahi karta.

English: The useful output explains the issue, supporting evidence, remaining gaps, responsible owner, next action and basis for closure. AI does not establish root cause, CAPA effectiveness or batch release.

## Preparation

- Open /app?demo=1 for the original saved proof. A newly signed-in personal workspace must remain empty; do not load the proof into that fresh workspace by accident.
- Prepare /sources?demo=1, /events?demo=1, /changes?demo=1, /ai-registry?demo=1 and /batch-review?demo=extra in tabs.
- The original and additional proof are separate scopes. Introduce the switch clearly: 'A separate synthetic batch example'. Never join their counts or pretend they represent one real customer batch.
- Public proofs are read-only. Check that an additional saved assessment and Download synthetic report are visible before choosing the last shot. If not, retain the visible evidence gap and use the original audit view.

## Routes

| Screen | Route | Action |
| --- | --- | --- |
| Landing | / | Inspect working proof |
| Original proof | /app?demo=1 | Command Center / Controlled Sources / Quality Events / Change & Blast Radius / AI Use & Release |
| Human boundary | /review?demo=1 | Human QA Review |
| Original audit | /audit?demo=1 | Replay & Export; public actions stay read-only |
| Additional batch proof | /batch-review?demo=extra | Saved findings & next actions -> Inspect checks, evidence and next action -> Download synthetic report |
| Additional quality checks | /quality-checks?demo=extra | Source-linked saved assessment, not a newly executed live check |
| Private work | /app | Sign in off-camera and select the explicitly separate working-proof copy if needed |


## 1. Introduce the quality decision problem (00:00-00:12)

Route: / -> /app?demo=1

Action: Show the landing identity and click Inspect working proof. Wait for the saved case to load.

Cursor: Rest beside the proof CTA, then move once. Do not cut before the case-load result is visible.

Proof: LEDGER-Q identity and separate synthetic proof selection.

Hinglish: LEDGER-Q mein quality evidence aur AI assurance connected hain. Inspect working proof se synthetic case kholo. Fresh personal dashboard mein proof already fitted dikhana nahi; dono alag hain.

English: Quality decisions depend on evidence that stays connected. I am Rahul Dewangan, and LEDGER-Q is my independent work sample for linking quality records, AI-use controls and human review.

## 2. Show the controlled original (00:12-00:27)

Route: /sources?demo=1

Action: Click Controlled Sources. Open the laboratory original associated with the conflicting assay and inspect its exact value/version.

Cursor: Point beside the source ID/version and the 94.2% value; leave it visible for four seconds.

Proof: The permitted original, source identity/version and recorded 94.2% assay.

Hinglish: Original lab evidence mein 94.2% hai. Uska source ID aur version dikhao. Yeh synthetic result hai. Original ko dekhna pehla step hai, dashboard number ko hi final truth nahi maana jaata.

English: The original laboratory evidence records ninety-four point two percent. Its source identity and version remain attached, so the original can be inspected before a conclusion is made.

## 3. Make the quality conflict visible (00:27-00:43)

Route: /events?demo=1

Action: Click Quality Events and select the conflicted assay event. Show the original 94.2% and 99.1% transcription together with HOLD and the first-failure/gap notes.

Cursor: Point between the two values; finish beside HOLD and stop moving.

Proof: Unresolved mismatch, original value retained and missing investigation support.

Hinglish: Transcription 99.1% hai, original 94.2%. System original ko badal nahi raha. Conflict HOLD par rahta hai. Root cause khud invent nahi karni; missing investigation evidence visibly pending hai.

English: The transcription shows ninety-nine point one percent. That mismatch stays visible and the event remains on HOLD. The original is preserved; missing investigation evidence is not replaced with a guessed cause.

## 4. Show what a source change affects (00:43-00:58)

Route: /changes?demo=1

Action: Click Change & Blast Radius. Select an existing source or connected node and inspect its saved links/revision. Do not edit the public proof.

Cursor: Follow one saved edge with a slow pointer movement, then select its node and let the detail remain still.

Proof: Saved dependencies and affected records; changed evidence requires renewed review.

Hinglish: Graph ka ek actual link samjhao. Source change hone par downstream work affected ho sakta hai. Purana review automatically current nahi rehna chahiye. Public proof mein change execute karne ka pretend nahi karna.

English: The dependency view shows which saved work is connected to the evidence. When a source changes, affected work needs fresh checks and review. Earlier approval cannot silently remain current.

## 5. Separate AI-use assurance from batch authority (00:58-01:13)

Route: /ai-registry?demo=1

Action: Click AI Use & Release. Inspect AI-QA-01, its intended/excluded use and SUSPENDED state.

Cursor: Point beside SUSPENDED and the excluded-use text, without covering either.

Proof: An AI-use passport, dependency limits and a suspended state; it does not authorize batch release.

Hinglish: AI passport ka intended use aur excluded use dikhao. SUSPENDED actual state hai. AI-use assurance aur medicine/batch release do alag authorities hain; is record se release claim nahi karna.

English: AI-use assurance is connected to the same evidence. This example use is suspended, and its limits are explicit. An AI-use record does not authorize a batch decision.

## 6. Inspect a separate saved batch assessment (01:13-01:30)

Route: /batch-review?demo=extra

Action: Switch to the prepared additional-proof tab. Say that it is a separate synthetic example. Scroll to Saved findings & next actions; expand Inspect checks, evidence and next action on one saved assessment.

Cursor: Point left to right through one check row: Check -> Finding -> Evidence -> Result. Keep status and scope in frame.

Proof: A saved, server-computed assessment with source references, check results, gaps and next steps.

Hinglish: Ab separate extra proof mein switch kar rahe hain; original case ke numbers se mix nahi karna. Ek saved assessment ki row dikhao: check, finding, source evidence aur result. Gaps ko readiness bolna nahi.

English: A separate synthetic batch example shows the added assessment workflow. Each saved check displays its finding, evidence and next action. Gaps and missing prerequisites remain visible rather than being converted into readiness.

## 7. Return to the named review boundary (01:30-01:44)

Route: /review?demo=1

Action: In the original-proof tab click Human QA Review. Select a held record and inspect its source/version and review controls.

Cursor: Rest beside the current version and review reason. Do not click a disabled or unauthorized signing button.

Proof: Named reviewer role, exact record revision and read-only public-proof boundary.

Hinglish: Human QA Review mein exact revision aur source support inspect hota hai. Public proof read-only hai. Reviewer ki role permission alag hai; software pass ya AI candidate final judgement nahi.

English: A named reviewer must inspect the exact record revision before a decision is signed. The public proof is read-only. Software checks and AI candidates do not replace qualified Quality judgement.

## 8. Open the readable evidence report (01:44-01:53)

Route: /batch-review?demo=extra -> Download synthetic report

Action: Return to the selected additional assessment and click Download synthetic report. Open the downloaded/readable HTML and show summary, sources, gaps, next action and unapproved/synthetic scope.

Cursor: Point beside the report state and next action. Do not crop away the unapproved or synthetic label.

Proof: The actual saved assessment report with its evidence and review state; HTML can be printed to PDF.

Hinglish: Actual report open karo. Finding ke saath sources aur next action hona chahiye. Synthetic aur unapproved label frame mein rahe. Print-to-PDF possible hai, lekin commercial release certificate nahi ban jaata.

English: The readable report carries the finding, source evidence, gaps and next action together. Its synthetic and unapproved status stays visible; it is not automatic batch release.

## 9. Close with quality work that can be checked (01:53-02:00)

Route: /events?demo=1 or /batch-review?demo=extra

Action: End on the held finding or readable assessment summary, with the product identity visible.

Cursor: Park in a clear corner.

Proof: Traceable quality evidence, linked review and no unsupported closure.

Hinglish: Closing mein four cheezein bolo: evidence preserve, gap visible, next action clear aur human accountable. Real-user performance ya validation ka claim tabhi jab actual proof ho.

English: LEDGER-Q demonstrates my approach to quality work: preserve the evidence, expose the gap, connect the next action and keep the human decision accountable.

## Latest additions in Hinglish

New workspace: personal dashboard zero data se shuru hota hai. Public synthetic proof explicitly choose karna hai. Real records process karne ki permission separate saved action hai.

Transcription: binary original se critical text lene par original hash, page/location aur different QA reviewer ka exact-version confirmation chahiye. Ye complete automated OCR qualification nahi.

OOS: out-of-specification investigation mein first-phase evidence, second-phase decision/rationale aur retest status/original result ka relation chahiye. Retest karke original failure erase nahi hota.

Cause: confirmed, likely aur unresolved cause alag hain. Likely/unresolved ko automatically final root cause nahi bolna; rationale, residual controls aur human disposition chahiye.

CAPA: implementation se pehle independent signed plan chahiye. Agreed criterion aur observation window ke actual evidence ke bina effective/closed claim nahi.

OOT: unusual trend tab compare karo jab data ka context comparable ho aur agreed rules available hon. Non-comparable data ko result ki tarah force nahi karna.

Notices: saved in-app delivery, failed target, retry aur acknowledgment visible hain. In-app notice ka matlab email bhej diya nahi.

AI and history: model/prompt/policy/source dependencies aur review gates retain hain. Actual AI quality, real effectiveness, retention/deletion aur production recovery qualification alag evidence mangte hain.

Feature allocation: original F01-F20 aur 45-item register retained hain: 11 reuse, 24 refinements, five additions, five deferred. Ye allocation hai; sab 45 fully qualified enterprise features ka claim nahi.

## Latest delivery

# LEDGER-Q current delivery

Recorded: 2026-10-08T09:25:12.793269+00:00

**Scope: bounded engineering refinements; enterprise production qualification is NOT ESTABLISHED.**

Existing design, data, roles, URLs and human release boundaries were preserved. No private customer evidence, human approval or credentials were changed by this delivery.

| Requirement | Implemented / retained | Remaining proof or limitation |
|---|---|---|
| L01 Real-data scope | Owner can authorize source use in a separate empty workspace; synthetic public proof remains unchanged. | Professional qualification and commercial data-handling approval not inferred. |
| L02 Critical transcription | Different QA reviewer, exact-version confirmation, page/location and original-byte integrity before binary-transcription approval. | Representative transcription accuracy and complete automated OCR not established. |
| L03 OOS investigation | Phase 1 evidence, phase 2 decision/rationale and evidence when required; retest status/rationale and original reference. | Qualified investigation and disposition remain human decisions. |
| L04 OOT | Existing comparable-context controls retained and extension adverse tests rerun. | Customer-approved statistical rules and representative comparable data are still required. |
| L05 Cause certainty | CONFIRMED / LIKELY / UNRESOLVED distinction; unresolved/likely rationale and residual controls, named disposition. | System does not determine root cause or batch disposition. |
| L06 CAPA effectiveness | Independent signed plan before implementation, exact criterion/window, actual evidence and observation-date closure gates. | Historical formats require revision; real effectiveness observation cannot be manufactured. |
| L07 PQR/APQR | Existing typed coverage and quality-context extension tests retained. | Comprehensive customer product/period source completeness remains partial. |
| L08 Notifications | Saved bounded in-app delivery, failed target/retry state, channel and acknowledgement; no false email claim. | External email/webhook delivery requires a configured provider and delivery evidence. |
| L09 AI qualification | Existing model, consent, exact dependency and evaluation gates preserved. | Representative independent expected answers, live quality and revalidation qualification remain external. |
| L10 Retention/offboarding | Existing owner request, audit-preserving history, bounded backup/copy-restore controls retained. | Legal hold, verified deletion, production archive/offboarding and disaster recovery qualification are not complete. |

## Shared acceptance boundaries

| Item | Current status |
|---|---|
| Authoritative current status | This report is authoritative for changes in this delivery. Earlier status/proof files describe their dated scope; they are not upgraded by a build. |
| Independent evaluation | Synthetic controls and public-document intake are separate from held-out reviewer-labelled scientific/regulatory evaluation. |
| Live model outcomes | Configured credentials and local protocol mocks do not establish fresh successful hosted inference or model quality. |
| Professional outcomes | No real-user pilot results, time savings or accuracy percentages were invented. |
| Identity/security | Existing roles, signed decisions, tenant scope and auth retained. Production identity recovery, external OAuth and complete security qualification remain separate. |
| Operations | Build/local persistence/export checks pass only within their stated scope; target load, alert delivery, restore/rollback/incident drills remain unqualified. |
| Cross-product handoff | No automatic permission bypass or transferred approval. Existing exact-revision/manual intake controls retained; receiving-system reconciliation remains scoped. |
| Human-readable outcomes | Visible gaps, HOLD, source references and next review owner retained. No automatic regulatory release. |

## Current source handling

Checked 8 October 2026: FDA M4Q(R2), January 2026, is draft guidance not for implementation. EU EudraLex lists revised Annex 19 as applicable from 24 September 2026; applicability must be assessed for the actual scope, not assumed for every customer.

- https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m4qr2-common-technical-document-registration-pharmaceuticals-human-use-quality
- https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en

See the repository test evidence for executed checks. Hosted browser journeys and real professional evaluation remain separate from a successful deployment.


## Interview answers

### Is this commercial work?

Hinglish: Ye independent portfolio work hai; synthetic/public proof ko real client experience nahi bolunga.

English: This is independent portfolio work. Synthetic and public cases are not commercial client experience.

### Why can the output be HOLD?

Hinglish: HOLD weakness nahi: required proof ya qualified decision abhi pending hai. Guess karke green status dena galat hoga.

English: HOLD makes missing evidence or review visible. It prevents an unsupported accepted output.

### Does AI make the final decision?

Hinglish: AI candidate ya explanation de sakta hai. Named qualified human exact version ka decision deta hai.

English: AI produces bounded candidates; a named qualified human remains responsible for the scoped decision.

### Is it agentic or only rules?

Hinglish: Saved plan, specialist routing, shared task state aur human gate code mein hain. Safety checks explicit rules bhi use karte hain. Actual provider result alag proof se dikhana hoga.

English: The implementation combines bounded orchestration, specialist work and explicit safety rules. A successful live provider run must be evidenced separately from configuration and mocks.

### What if the source changes?

Hinglish: Affected current output stale hota hai aur fresh review chahiye. Purana decision history mein rehta hai.

English: Changed dependencies mark affected current work stale and require fresh review while preserving history.

### What is the main output?

Hinglish: Report/export ke saath supported finding, gap, owner aur next action. Sirf PDF ban jana poora outcome nahi.

English: The output combines supported findings, gaps, review responsibility and next action. A PDF alone is not the whole user outcome.

### How accurate is it?

Hinglish: Main engineering tests ka scope bataunga; unko regulatory/scientific accuracy percentage nahi bolunga. Qualified unseen-case evaluation aur pilot abhi alag kaam hain.

English: Recorded engineering checks do not establish regulatory or scientific accuracy. Qualified held-out evaluation and supervised professional use remain separate.

### How much time does it save?

Hinglish: Measured baseline aur real supervised results ke bina percentage claim nahi karunga.

English: I would measure matched manual and assisted tasks, including corrections and failures, before claiming a time-saving percentage.

### Is it production-ready?

Hinglish: Deployment aur bounded working proof hai; complete enterprise qualification claim nahi. Security, restore, target load aur real professional acceptance ke gaps openly bataunga.

English: It has a bounded implementation and work sample, but full enterprise qualification is not established. Remaining operating and professional evidence must be stated openly.

### What did you personally learn?

Hinglish: Original evidence preserve karna, uncertainty explain karna, review boundary define karna aur useful next action dikhana.

English: I learned to preserve original evidence, explain uncertainty, define review boundaries and present an accountable next action.