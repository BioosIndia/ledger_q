# LEDGER-Q Extra Features — complete GitHub source package

Site: https://ledger-q.r4dewangan.chatgpt.site
Source revision: `87a3664a48b28102f663cddee3650dcfe43e9f29`

Yeh sirf text package nahi hai. `source/` mein current complete application code, original assets, diagrams, bilingual demo media, Docker/configuration files, schema/migrations, workflows, tests aur documentation hain. `Git_History.bundle` mein available source history hai. `changes/Extra_Features_From_v15.patch` batata hai pichhle v15 se kya badla.

## Kya add/refine hua

20 existing canonical areas retained; 11 shared capabilities reused; 24 partial areas refined within bounded working scope; 5 additions: Batch Record Validator, authorized Regulatory Update Intake, Batch Quality Review, OOT Detection, Batch Readiness. Supplier qualification, predictive quality risk, environmental/microbial monitoring, visual packaging/label inspection and incoming-material qualification are deferred.

- Naya sign-in workspace zero se shuru hota hai.
- Working proof alag hai; additional synthetic proof explicitly select/load hota hai.
- Batch / regulatory / quality checks source se compute hokar save hote hain.
- Missing values, wrong context/units, unresolved conflicts aur changed evidence HOLD/STALE rehte hain.
- Existing saved agent orchestration candidate support deta hai; human reviewer hi decision deta hai.
- Reports readable HTML (Print / Save as PDF) + exact structured JSON evidence ke saath milte hain.
- Signed AI-use rollback nayi suspended revision banata hai; old history rehti hai.

## Folder guide

- `source/app`, `source/components`: landing, sign-in, dashboards, review, navigation and reports.
- `source/lib/ledger`: saved workflow, quality checks, provider routing, signing, permissions and storage.
- `source/public`, `source/media-src`: actual supplied/generated assets, diagrams, bilingual media and media-generation source.
- `source/Dockerfile`, `source/docs/CONTAINER_NOTES.md`: container setup and its limitations.
- `source/drizzle`, `source/db`: database schema and migrations.
- `source/tests`: reproducible integration, adverse, outcome and presentation checks.
- `source/docs/LEDGER_Q_45_Feature_Coverage.csv`: all 45 names, reuse/refine/add/defer decision, screen, connected action and boundary.
- `source/docs/LEDGER_Q_Extra_Features_Review.md`: detailed delivery review and nine-part allocation.
- `verification/`: current executed check receipts and release identity.

## Run / verify

Use Node 22.13+ and the pinned pnpm version in `source/package.json`. Read the existing source README and container notes for the Worker/D1/R2 runtime requirements. Provider keys belong in secure runtime settings; no API key, session, private workspace or runtime database is included here.

```sh
cd source
pnpm install --frozen-lockfile
node node_modules/typescript/bin/tsc --noEmit
node tests/integration.mjs
node tests/extensions.mjs
node tests/presentation.mjs
node --experimental-strip-types --test tests/outcome.test.mjs
pnpm build
```

The SQLite/R2-memory integration fixture is isolated test data. It does not substitute for the deployed database. Production uses the existing Sites Worker/D1/R2 bindings. Docker alone does not provision those managed services.

## Honest readiness boundary

Executed checks: 86 API/integration + 37 unit/adverse + 9 server-render checks + 15 outcome tests. Typecheck and production build passed. Provider contract tests use mocks unless explicitly identified as live. Browser/device automation and new live provider qualification were not performed.

This is a bounded working portfolio/MVP. Synthetic proof cannot establish real-user time savings, representative quality/fairness, legal compliance, qualified human judgement or enterprise validation. No automatic batch/regulatory release is included.
