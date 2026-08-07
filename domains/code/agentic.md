# Agentic Code — When the Author Was an Agent

Part of domains/code/. Load alongside patterns.md whenever the code was produced by an autonomous agent rather than by a person using autocomplete. New in August 2026.

**The distinction this file rests on.** Autocomplete produces suggestions a human accepts one at a time, so a person reads every line at the moment it enters the codebase. An agent produces a finished result a human reviews afterward, if at all. The code can be identical; the review history is not, and the failure modes that follow from that difference are what this file covers.

Every pattern in patterns.md still applies. These are the ones that only appear, or only compound, when nobody was watching during generation.

## Iterating Makes Security Worse, Not Better

The most counterintuitive finding in this domain, and the one with the clearest number attached.

Refining AI-generated code by asking for improvements is conventionally assumed to converge on better code. Measured across 400 code samples over 40 rounds using four prompting strategies, it does the opposite for security: **a 37.6% increase in critical vulnerabilities after just five iterations** (Shukla, Joshi, and Syed, arXiv 2506.11022).

Five rounds is not an unusual agent session. It is a normal one.

The proposed mechanism is the feedback loop itself: each pass optimizes against the model's own prior output rather than against any external check, so the errors that survive are the ones the model cannot see, and they accumulate. The authors' recommendation is human validation *between* iterations rather than only at the end.

Three consequences worth acting on:

- **"I asked it to make the code more secure" is not a control.** It is another iteration, and iterations are the thing being measured as harmful. See security.md.
- **A long agent session is a risk signal on its own**, independent of what the diff looks like. Iteration count is metadata worth knowing before reviewing.
- **The review has to be external to the loop.** A human, a scanner, a test suite that was not itself written in the same session. Anything inside the loop shares the loop's blind spots.

## The Reviewer's Position Is the Real Problem

Agent output arrives large, complete-looking, and internally consistent, which is close to the worst possible shape for catching defects.

**Volume defeats attention.** A 40-file diff gets a different quality of review than a 40-line one, and agents produce the former routinely. The defect rate per line does not fall to compensate.

**Consistency reads as correctness.** Agent code is uniform: same naming, same structure, same error handling everywhere. Human codebases are uneven, and reviewers are calibrated to read unevenness as where the risk is. Uniform code presents no such gradient, so attention distributes evenly instead of concentrating where it should. This is core/structural-patterns.md's uniformity tell, operating on a reviewer's attention rather than on a reader's ear.

**Plausibility is the default.** Everything looks like what it should look like. The umbrella question from patterns.md is doing all the work here, and it has to be asked deliberately because nothing in the diff prompts it.

**Rubber-stamping is the equilibrium.** Reviewing agent output carefully is slower than producing it, so the review is the bottleneck and the pressure is to relax it. Any process where an agent generates and a human nominally approves will drift toward approval unless something structural prevents it. See enforcement.md, which is the structural answer.

## Tracer Bullets

A prevention layer rather than a detection one: it changes how the code gets built, before there is anything to catch.

**Why this connects to the umbrella question.** Left unconstrained, an agent tends to build every horizontal layer of a feature (models, endpoints, middleware, auth, logging) before ever testing whether the critical path works at all. Only after all of it exists does anyone discover the database connection string was wrong, or the column type didn't match. That is the direct mechanism behind structurally-plausible-but-functionally-empty code: a large, complete-looking deliverable with an untested core, built with no feedback loop until the very end.

**The fix, borrowed from a much older idea.** *The Pragmatic Programmer* calls this failure mode "outrunning your headlights," building faster than your feedback loop can catch you. Its answer, tracer bullets, is a small end-to-end vertical slice: one path through every layer the feature touches, working and tested, before any layer gets built out further. Asked to add a "reveal in file system" action available from four places in an app, the tracer-bullet version is the backend endpoint wired to exactly one of those four locations first, confirmed working, then expanded, rather than all four UI locations and the endpoint built simultaneously and tested at the end.

**Why this bites harder with agents than with a human developer.** A human notices when they have been coding for an hour without running anything. An agent has no such instinct, and a full context window makes the discipline non-negotiable rather than merely good practice: by the time something that large fails, there is no budget left to backtrack meaningfully.

**Practical instruction, for a build-feature prompt or skill:** when a feature touches multiple layers or integration points, name the smallest end-to-end slice explicitly and ask for that first, tested, before any expansion. "Build the one thing that proves the hard part works" beats "build the whole feature" as an opening instruction almost every time.

## Capability Is Blast Radius

An agent that can only write files fails differently from one that can run commands. Before reviewing the code, know what the agent could reach while producing it:

- **Package installation** puts supply-chain.md's entire attack surface in play without a human reading the import line.
- **Shell access** means the review covers what the agent *did*, not only what it wrote. The diff is an incomplete record.
- **Credentials in the environment**, especially inside CI, make a compromised dependency a pipeline compromise rather than a laptop one.
- **Write access to its own tests** is worth calling out on its own. An agent that can edit the tests that check its work can resolve a failure by weakening the check, and the diff will show tests passing. Look at test changes in the same commit as implementation changes with specific suspicion.

## What to Ask Before Reviewing

Cheap questions, none answerable from the diff, all of which change how the review should go:

1. How many iterations produced this? (Five or more: assume security regression, per above.)
2. Did anything external verify it, or only the model?
3. Were tests written in the same session as the implementation, by the same agent?
4. What could the agent execute, and is that visible anywhere?
5. Was any dependency added, and by whom?

## Sources

Shukla, Joshi, and Syed, *Security Degradation in Iterative AI Code Generation: A Systematic Analysis of the Paradox*, arXiv 2506.11022, revised September 2025, for the 37.6%-after-five-iterations measurement, the 400-sample/40-round design, and the feedback-loop mechanism with its human-in-the-loop recommendation. The tracer-bullets material is from aihero.dev's 2026 article applying *The Pragmatic Programmer*'s technique to agent workflows specifically. Agent-in-CI/CD blast radius follows the February 2026 Clinejection reporting cited in supply-chain.md. The reviewer-position analysis, the capability-as-blast-radius framing, and the pre-review questions are this skill's own synthesis; they generalize from the cited findings rather than restating a source.
