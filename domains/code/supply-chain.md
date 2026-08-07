# Supply Chain — Hallucinated Packages and Slopsquatting

Part of domains/code/. Load alongside patterns.md whenever generated code adds a dependency, and always when an agent can run an install command. New in August 2026.

**Why this outgrew a bullet in patterns.md.** A hallucinated import used to be a correctness bug: the name was wrong, the install failed, you fixed it. Attackers noticed that the wrong names are predictable, registered them, and turned a failed install into a successful compromise. The defect did not change. Its consequence did.

## Why the Names Are Predictable Enough to Squat

This is the finding that makes the attack work, and it is the one to carry.

Across 576,000 code samples from 16 models, roughly **19.7% of recommended packages did not exist**. That alone is a nuisance. But when researchers re-ran identical prompts ten times each, **43% of hallucinated names appeared on every single run**.

Hallucination is not noise here. It is a stable function of the prompt, which means an attacker does not have to guess: they generate against common prompts, collect the names that recur, and register them. The developer's tooling then resolves the name successfully and runs their code.

Rates differ sharply by model class, which matters when choosing what to trust:

| Model class | Hallucinated package rate |
|---|---|
| Open-source models | 21.7% average |
| Commercial models | 5.2% average |
| Best measured (GPT-4 Turbo) | 3.59% |

A four-to-six-fold spread. If a workflow generates dependency-adding code with a local open-weights model, the exposure is materially different from the same workflow on a frontier commercial model, and the mitigations below matter more.

## This Is Confirmed, Not Theoretical

The clearest documented case is the npm package `unused-imports`, a name models produce in place of the legitimate `eslint-plugin-unused-imports`. It was registered, it was malicious, and as of early February 2026 it was still live and recording roughly 233 weekly downloads. Others have accumulated tens of thousands.

The related variant worth knowing: the same mechanism applies to **hallucinated domains**, not just packages. Models invent URLs for documentation, APIs, and callback endpoints, and those are registrable too.

## Why Agents Multiply This

An agent with shell access resolves dependencies without a human reading the import line, which removes the only step where the name was ever checked. The Clinejection incident, disclosed February 2026, showed the pattern reaching CI/CD: an agent inside a pipeline installs on infrastructure with credentials, so the blast radius is the build system rather than one laptop.

The general shape, which recurs throughout agentic.md: automation removes the incidental human checkpoint that a manual workflow provided for free, and nobody notices it was load-bearing until it is gone.

## What Actually Works

Reading-level vigilance is the weakest control here and should not be the only one. In rough order of strength:

1. **Never let an agent install unreviewed.** An allowlist, or a human approving each new dependency. This is the control that addresses the mechanism rather than the symptom, and it is the one most often skipped for convenience.
2. **Pin with lockfiles and verify hashes in CI.** A pinned, hash-verified dependency cannot be silently substituted, whatever the model suggested.
3. **Verify every new import against the real registry before it lands.** Does the package exist, who publishes it, how old is it, how many downloads, does the name differ from the well-known package by a plausible hallucination distance? A brand-new package with few downloads and a name suspiciously close to a popular one is the exact signature.
4. **Watch for the plausible-but-wrong name shape specifically.** These are rarely gibberish. They are the name the package *should* have had: `eslint-plugin-unused-imports` becoming `unused-imports`, a scoped package losing its scope, a hyphen becoming an underscore. The name reads correct, which is why it survives review.

## The Reviewer's Question

For any dependency in generated code: **did a human decide to add this package, or did the model?** Those are different provenance stories with different risk, and the diff does not record which one happened. If the answer is the model, the name needs verification against the registry before anything installs it, and that verification is not something the model that suggested it can perform on its own behalf.

## Sources

Package-hallucination and slopsquatting research, 2025–2026: the 576,000-sample, 16-model measurement behind the 19.7% rate, the 43% cross-run recurrence figure, and the open-source-versus-commercial split; Cloud Security Alliance research note on slopsquatting as an AI supply-chain vector (April 2026); Trend Micro and Snyk analyses of package hallucination and agent-driven installs; Palo Alto Unit 42 on hallucinated domains as a parallel vector; reporting on the `unused-imports` npm package and the February 2026 Clinejection incident; arXiv 2605.17062 re-evaluating hallucination rates on the 2026 frontier-model cohort and arXiv 2606.13918 on calibrated detection of hallucinated imports. The reviewer's provenance question and the name-shape heuristic are this skill's own framing.
