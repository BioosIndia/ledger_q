# PRAMANEX LEDGER-Q

A working synthetic quality-record and AI-assurance application by Rahul Dewangan.

## Run and verify

Requires Node 22.13+ and pnpm 11.25 (lockfile included).

```sh
npm run install:ci
node tests/integration.mjs
node node_modules/typescript/bin/tsc --noEmit
npm run build
```

The Sites build command wraps the framework build and produces a Cloudflare-compatible Worker with D1 and R2. Schema-only migration is in `drizzle/`. Do not place user data or seeds in migrations. Synthetic workspaces are created through authorized runtime operations.

## Environment

`DB` and `BUCKET` are runtime bindings. Set `LQ_ENCRYPTION_KEY` to a randomly generated server secret. Provider keys are optional encrypted workspace settings; `GROQ_API_KEY` and `GEMINI_API_KEY` are optional server-wide keys only for an explicitly authorized deployment. Never commit secrets. A provider call requires configured model IDs and explicit workspace document consent.

## Product journey

1. Inspect `/app?demo=1` for an isolated read-only saved Drug Q case.
2. Create an app account to get a fresh empty workspace. Login opens a zero-record private dashboard. Compact Workspaces and Working proof controls open saved work only when selected. Existing evidence is preserved; no proof is added implicitly.
3. Add permitted sources, or explicitly choose and confirm the Drug Q working proof into an empty workspace. The public original stays separate. Read originals, inspect requirements, conflicting assays, investigation, CAPA and training.
4. In Controls, explicitly assign synthetic reviewer permissions and enroll a real authenticator.
5. Record an exact-revision human decision; missing evidence blocks approval.
6. Revise source evidence to reopen dependent quality and AI work.
7. In Controls, connect and test Gemini using the secure configured key and selected-evidence permission. Two distinct discovered models support the saved bounded team. Alternatively configure Groq.
8. Inspect run/evaluation history, unapproved/controlled packets and backup-copy reconstruction.

The app-owned account does not bypass the owner-private Site audience boundary. Real Google login/email recovery is not configured or simulated.

## Source-of-truth documents

`docs/LEDGER_Q_Master_Rulebook.md`, mapping/flowcharts and original traceability retain the approved specification. `docs/LEDGER_Q_Implementation_Traceability.csv` and `docs/LEDGER_Q_Delivery_Checklist.md` record actual behavior and remaining evidence gaps. See `docs/ARCHITECTURE_DECISIONS.md` for explicit infrastructure substitutions.

## Honest scope

Synthetic working product, bounded multi-agent candidate support and optional live provider routing. Integration tests use actual SQLite SQL with a D1-compatible adapter and in-memory object storage; local provider responses are mocked. Actual hosted Gemini connectivity and saved team execution are separately verified with the configured key against the synthetic Drug Q case; see docs/verification/hosted-v3-results.json. No enterprise qualification, professional accuracy, unrestricted swarm, regulatory release or measured percentage benefit is claimed.

See docs/Fresh_Dashboard_and_Personalization_v5.md for compact proof/workspace controls, the model-cover fix and functional browser-local preferences.
