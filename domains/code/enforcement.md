# Enforcement — Making the Rest Impossible

Part of domains/code/. The structural layer under every other file in this folder. New as its own file in August 2026, expanded from a section of patterns.md.

**The argument.** Every other file here describes something to notice. Noticing does not scale, and agentic.md explains why it scales worst exactly where it is needed most: review is slower than generation, so the review relaxes. A rule that fails a build does not relax. An agent that hits it has to write something real.

Advisory guidance and structural enforcement are not two strengths of the same thing. They are different mechanisms, and the structural one is categorically more reliable than any post-hoc audit, including this skill.

## The Ordering Principle

Prefer, in this order:

1. **Impossible** — the operation cannot happen (no credentials, no network, no install permission)
2. **Blocked** — it happens and fails a gate (lint error, failing CI, rejected commit)
3. **Visible** — it lands but is surfaced loudly (a required review, an alert, a diff annotation)
4. **Documented** — someone wrote down that it is bad

Most teams write documentation and call it a control. Documentation is the weakest tier and the one that degrades silently, because nothing tells you when it stops being read. Move rules up this ladder wherever the cost allows.

## Lint Rules Worth Writing

Each of these makes a specific pattern from patterns.md unwriteable rather than merely discouraged:

1. **Mock echo** — a mock return value asserted on directly, with no intervening behavior. The highest-value rule in this list, because the failure is a test that passes while testing nothing, which is invisible in every other way.
2. **`@ts-ignore` / `@ts-expect-error` without an explanation comment**
3. **`any` without an explanation comment**
4. **`console.log` / `print` / `debugger` outside test files**
5. **Bare `except:` and empty exception bodies**
6. **`pass  # TODO` and equivalent placeholder bodies** — catches shipped stubs directly
7. **Functions over N lines without documentation**

Semgrep or a custom ESLint/Ruff rule handles all of these. The skill's own repo runs a pre-push gate on this principle, which is the smallest working version of it.

## CI Gates for the Supply Chain

These address supply-chain.md, and unlike the lint rules they cannot be replaced by careful reading, because the thing being checked is not visible in the diff:

- **Lockfiles required, hashes verified.** A pinned, hash-verified dependency cannot be silently substituted regardless of what a model suggested.
- **New-dependency review as a required gate.** Any commit adding a dependency needs a human approving that specific package. This is the single control that addresses slopsquatting at its mechanism.
- **Agents cannot install.** No package manager in the agent's permitted command set, or an allowlist. If an agent needs a dependency, it asks.
- **Fail the build on a package that did not exist at the last known-good resolve.** Cheap, and catches the exact case where a name became registrable between then and now.

## Gates for Agentic Work

From agentic.md, and these are the least commonly implemented:

- **Test changes and implementation changes in the same commit get flagged for review.** An agent resolving a failure by weakening the assertion produces a green build and a diff that looks like progress.
- **Record iteration count** where the tooling allows. Five or more rounds carries a measured security regression, and a reviewer who knows that reviews differently.
- **Require one external check** that did not come from the generating session: a scanner, a human, or a test suite written separately. Anything inside the loop shares its blind spots.

## The Limit of This File

Enforcement catches what someone anticipated. It cannot catch a novel logic error, a wrong abstraction, or a requirement misunderstood, and a codebase with an excellent gate can still be wrong about what it was supposed to do. The gate raises the floor; it does not raise the ceiling. Use it to make the known failures unwriteable so human attention is free for the ones a rule cannot express, which is the entire argument for having it.

## Sources

The lint-rule catalog originates in the Bootoshi enforcement-layer material carried in this skill since v2.2. Supply-chain gates follow the mitigations recommended in the Cloud Security Alliance's April 2026 slopsquatting research note and Snyk's package-hallucination guidance, both cited in supply-chain.md. The agentic gates follow from arXiv 2506.11022's human-validation-between-iterations recommendation, cited in agentic.md. The four-tier ordering principle and the closing limitation are this skill's own framing.
