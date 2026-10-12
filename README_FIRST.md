# LEDGER_Q - changed files only

Compared source: deployed v21 `0e2d96d92006026018e36c6747cc380aced7c457` -> deployed v24 `049b9b0baf26f75111becb9d15c4a7466851337d`.

This is a delta package, not a fresh full repository. It is pinned to the source versions above. If your previous GitHub ZIP is older/different, compare the hashes before overwriting anything; this package does not silently claim that an unverified old ZIP matches the baseline.

## What is inside

- `changed_files/`: complete current contents of only added/changed source paths.
- `changes.patch`: matching Git patch, including the same additions/changes.
- `CHANGE_MANIFEST.json`: path-by-path old/current hashes and source provenance.
- `TEST_EVIDENCE/`: actual sanitized hosted readback/account checks for this update.
- `apply_changes.py`: optional safe dry-run/copy helper; refuses baseline mismatches.

No hidden `.openai`/`.git` files or API keys are included. The `app/` folder is a required application route folder, not an OpenAI hidden file; renaming/removing it would break the app. ZIP extraction uses standard Windows-compatible paths.

## GitHub web upload

1. Extract this ZIP first. Open your existing repository and the intended branch.
2. Open `changed_files`. Upload its CONTENTS into the repository root, preserving `app/`, `lib/`, `components/`, `scripts/`, `tests/` and other actual paths. Do not upload the ZIP or the outer `changed_files` wrapper as application source.
3. Review the commit's file diff. Keep existing unchanged source, provider secrets and hosting configuration intact.
4. Run the product's documented quality checks after its normal build. Source upload alone is not a deployment, successful inference or professional qualification.

## Local alternative

Run `python apply_changes.py --repo PATH_TO_EXISTING_REPO` for a safe compatibility dry run. Add `--apply` only after the dry run passes. Then review `git diff`, run tests and make your own commit. Or apply the Git patch with `git apply --check changes.patch` before `git apply changes.patch`.

## What this update proves

Saved synthetic engineering control checks and exact-answer live model canaries passed with verified readback. Human decision/release boundaries remain. Failures and their recovery are preserved; qualified professional acceptance and regulated production use are not invented.
