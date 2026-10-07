> Historical v3 behavior and verification. Current login behavior is documented in Fresh_Dashboard_and_Personalization_v5.md: zero-record dashboard, compact saved-work/proof controls, existing data preserved.

# Fresh workspaces and explicit working proof

New accounts get a private empty workspace. Login opens the workspace chooser, ordered by most recently updated work. No previously saved workspace or public proof is selected implicitly. Existing saved data is preserved.

The public original Drug Q proof stays read-only. A private owner may explicitly select and confirm that exercise into an empty workspace. Originals receive workspace-scoped storage keys, and import replay is idempotent. Existing private records cannot be overwritten by importing the exercise. A separate new workspace can be created without deleting any existing work.

## Gemini

Server-side Gemini support now uses the securely configured GEMINI_API_KEY, or a workspace-scoped encrypted provider setting. Provider identity is stored with workspace keys to prevent cross-provider credential reuse. Keys are never returned to the browser or included in URLs.

Controls → Connect & test Gemini asks for selected-document processing permission, discovers accessible model IDs and tests two distinct models with small synthetic requests. Each model response/failure and usage is saved. Configured credentials, connectivity and model quality are different states.

Live support saves planner delegation, bounded specialist candidates, independent model review, provider attempts and checkpoints. Unsupported citations, reviewer conflicts, missing evidence and provider failures cannot grant human approval. The UI polls actual saved run state during execution. Work is on demand; no idle continuous-inference or unrestricted regulatory release is claimed.

## Verification

51 synthetic integration checks and 6 server-rendered presentation checks passed before publishing. Coverage includes empty signup, explicit import, idempotency, private/public separation, preservation of existing evidence, role boundaries, exact citations, revision invalidation, signing controls, backup restoration, Gemini transport, discovery and mocked multi-model execution.

These tests do not establish real-world professional validation, regulatory accuracy, enterprise scalability or a zero-error guarantee. Hosted verification also passed: fresh account, separate proof loading, two actual Gemini model responses, saved planner/specialist/reviewer run ending in HOLD, a second fresh workspace, and logout. See verification/hosted-v3-results.json for exact receipts. Browser interaction/visual QA remains unverified in this run.

Model discovery excludes rolling latest aliases. The reviewer prefers a different available model family, and connectivity cannot pass when both replies report the same underlying model version. Actual model identity is retained in provider attempts.

Gemini connection verifies the author and tries up to three reviewer candidates when auto-selecting. Failed attempts and safe HTTP status codes are retained. A manually selected reviewer is not silently replaced. Special-purpose Omni/audio/image/deep-research models and rolling latest aliases are excluded from automatic structured JSON routing.
