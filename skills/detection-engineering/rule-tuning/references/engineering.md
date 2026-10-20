## Diagnose before excluding

High alert volume can come from a parser change, a duplicated source, a scheduler overlap, a new rollout or a genuinely broad hypothesis. Identify the cause. Repairing ingestion or alert grouping may preserve coverage better than modifying the behavior predicate. Keep raw search counts and generated alert counts separate.

For legitimate automation, verify the initiating account, managed asset group, signed binary/path, parent context and change record that actually distinguish it. A common username, writable directory or hostname prefix alone may create a large blind spot. Record exception criteria, supporting evidence, scope, owner, review date and expiry. Do not use reputation lookup absence as an allowlist.

## Compare fairly

Use identical datasets, schemas and time bounds for before/after runs. Compare event matches, entity/window groups and generated alerts at the appropriate stages. Track known-positive losses individually. Do not report precision without adjudicated labels, or false-positive rate without a meaningful benign denominator. Unknown and unlabeled alerts remain unknown.

Use time-separated evaluation when possible to reduce overfitting to one noisy week. Include attacks that mimic the proposed allowlisted process/account and cases just outside the exception. Check whether a threshold changes coverage for small or slow attacks. An exclusion's reduced volume is directly observable; its effect on future attacks is an uncertainty to explain.

## Deliverable

Provide a minimal diff with each change justified, dependency and configuration changes, exact before/after measurements, unresolved risks and a rollback trigger. Preserve the original artifact. If no backend is available, provide the proposed diff and test plan while marking impact as unmeasured. Never label a rule tuned or production-ready from static review alone.
