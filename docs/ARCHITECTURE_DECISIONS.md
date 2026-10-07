# LEDGER-Q implementation decisions

6 October 2026. The user approved starting the consolidated package.

- Sites requires a Cloudflare-compatible Worker. Use the bundled React/TypeScript Vinext application, D1 for server state, R2 for originals and exported packets. This explicitly replaces the blueprint's suggested FastAPI/PostgreSQL/n8n stack while preserving evidence, authorization, state and parent-orchestration contracts. No n8n or PostgreSQL execution is claimed.
- Sixteen canonical logical objects are represented by typed records inside a revisioned workspace aggregate. Source bytes remain in R2. Every mutation uses a D1 compare-and-swap workspace revision and append-only historical snapshot/audit event. This is bounded for a portfolio/initial workload, not claimed globally scaled.
- App-owned email/password sessions are requested in the planning package and earlier application requirements. Account email is not externally verified. Password plus a real authenticator TOTP is required at decision signing. New accounts get Owner/Investigator only; synthetic reviewer roles require explicit acknowledgement. No real QA qualification is inferred.
- Native publication remains owner-private by default. App accounts do not bypass the outer Site audience boundary. Public sharing requires the owner to change audience explicitly.
- Seven bounded specialist roles and independent model routing are implemented with an optional configured Groq connection. No keys are copied from BEACON or FORGE. Missing provider setup never becomes fake live inference. Explicit deterministic support remains available.
- Original source, exact version, gaps and permitted decisions take precedence over motion. Approved colors, card rhythm and hero material references are preserved. Compact grouped navigation and task stages customize the interaction.
