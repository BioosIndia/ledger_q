# First observed implementation failures and corrections

- API integration check: unconfigured live run rejected through an unawaited promise outside the response error handler. Corrected to await the run inside the guarded API boundary; rerun required.
- Type check: response JSON inferred as unknown in the client adapter. Added explicit boundary response typing; no domain approval logic changed.
- Test harness: esbuild was not a direct dependency. Reused the installed TypeScript transpiler rather than adding an unneeded dependency.

These engineering failures are retained; synthetic control results are not professional accuracy.
