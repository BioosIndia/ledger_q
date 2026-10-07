# LEDGER-Q fresh dashboard and personalization

## What changed

The supplied screenshot revealed that floating source/review/trace labels inherited opposing CSS anchors. This stretched a small blurred label into a full model-covering rectangle. Each floating label now resets all anchors and has content-sized dimensions; only the intended anchor pair is reapplied. The evidence-gate artwork and motion remain.

Login without an explicitly selected workspace now opens a zero-record private dashboard. A server-authorized default-entry request reuses an empty owned workspace, or creates one if none is empty. Existing populated workspaces, originals, decisions and proof are never cleared. Opening a saved workspace through the picker is an explicit selection.

Workspaces and Working proof are compact toolbar controls. Their dialogs contain saved workspace links, a fresh-workspace action and separate proof inspection/loading. The oversized entry screen and starter panel are removed. Proof import still requires confirmation and cannot overwrite private evidence. Counts follow the selected workspace; unrun control checks display 0 / 0.

Settings & controls includes functional device-local personalization: comfortable/compact spacing, evidence-blue/cyan accent, standard/larger reading size, and device/reduced-motion preference. Choices are scoped to the signed-in account on this browser, with reset and honest storage-failure feedback. They do not configure roles, approval or evidence. Existing provider, signing, role and mapping controls are preserved. These are browser preferences, not cross-device profile synchronization.

## Verification

55 synthetic integration checks, nine server-rendered presentation checks, TypeScript and the Worker build are required for this release. Provider contract cases in the integration suite are mocked; previously verified hosted live Gemini runs are retained separately. New hosted entry checks use an isolated synthetic account and do not approve or release anything.

No full browser visual/interaction QA or professional outcome validation is claimed. The complete unified package retains original approved requirements, reference media, source history, implementation, build archive and test receipts from prior releases.
