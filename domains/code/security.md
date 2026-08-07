# Code Security — What AI Gets Wrong Dangerously

Part of domains/code/. Load alongside patterns.md whenever the code touches untrusted input, authentication, or anything with a blast radius. New in August 2026.

**Why this is a separate file from patterns.md.** That file asks whether code does what it looks like it does. This one asks whether it can be made to do something else. A function can be idiomatic, well-named, fully typed, and exploitable, and nothing in a style pass catches that. Reading for slop and reading for exploitability are different passes with different orders of attention.

**Scope note.** This file locates where AI-generated code is measurably weakest so a human review knows where to look first. It is not a substitute for a security review, a scanner, or a threat model, and no reading-level heuristic can be. Same division this skill keeps between domains/legal.md and actually verifying a citation exists.

## The Gap Is Measured, and It Is Not Closing

Worth stating with numbers, because the alternative is arguing about it. Across independent 2025–2026 studies:

- **2.7× higher vulnerability density** in AI-generated code than human-written, with CVSS 7.0+ findings appearing **2.5×** as often
- **1.75× more logic and correctness errors, 1.57× more security findings**, and **2.74× more likely** to introduce XSS
- Veracode, 100+ models across 80 coding tasks: **45% of samples failed security tests**, worst in Java at **72%**
- AppSec Santa 2026, 534 samples across six models validated against the OWASP Top 10: **25.1% contained confirmed vulnerabilities**
- Enterprise audits report human-written code carrying **30–35% fewer critical flaws**

The consistent direction across studies with different methods is the part that matters. Any single figure here will move; the ordering has not.

## Where to Look First

The defect distribution is uneven, so a review that starts at the top of the file wastes its best attention. From a large-scale study cataloguing 4,241 vulnerabilities across 77 CWE types in AI-generated repositories:

1. **Injection first.** Injection-class weaknesses (CWE-78 command, CWE-89 SQL, CWE-94 code) account for roughly **33% of all confirmed vulnerabilities**. One in three. Every place user-controlled data reaches an interpreter, a shell, a query, or an `eval`.
2. **SSRF (CWE-918)** ranks at the top of individual findings. Any code that fetches a URL the user influenced, which in practice means webhooks, image fetchers, link previews, PDF generators, and integrations.
3. **XSS**, at 2.74× the human rate, wherever output reaches a browser without contextual escaping.

Those three cover most of the measured risk. Start there, then work outward.

## Why AI Fails at Security Specifically

Three mechanisms, each producing a different kind of miss. Naming them helps because they predict *where* the gap will be rather than only that one exists.

**It writes for the happy path, and security lives in the unhappy one.** Already in patterns.md as a correctness matter. The security version is sharper: an attacker's input is by definition the input nobody described in the prompt. Code generated from a description of intended use has no representation of unintended use.

**It reproduces the median of its training data, and the median code on the internet is not secure.** A pattern that appears ten thousand times in public repositories is the likely completion whether or not it was ever correct. This is why deprecated crypto, string-concatenated SQL, and permissive CORS keep reappearing: they are well-represented, not well-regarded.

**Its output is confident regardless of whether the security property holds.** The same confidence inversion domains/prose/security-reporting.md names for vulnerability reports and domains/legal.md names for citations. Code that "validates" input in a function called `validate_input` reads as handled. The name is not the check.

## The Specific Misses Worth Checking By Hand

Beyond the ranked classes above, these recur and are cheap to check:

- **Authorization confused with authentication.** The code proves *who* the user is and never checks *whether they may*. Object-level authorization is the common miss: the endpoint verifies a session, then trusts an ID from the request. This produces IDOR at scale and no type system catches it.
- **Secrets in generated config and examples.** Placeholder keys that became real keys, credentials in a docstring, tokens in test fixtures.
- **Crypto chosen for familiarity.** ECB mode, MD5 or SHA-1 for anything meaningful, hand-rolled comparison of secrets without constant-time semantics, static IVs. Each is well-represented in training data and each is wrong.
- **Permissive defaults.** CORS `*`, `verify=False` on TLS, debug mode, wildcard IAM actions, `0.0.0.0` binds. AI defaults to the configuration that makes the example work, which is the one that removes the control.
- **Error handling that leaks.** Stack traces, SQL fragments, and internal paths returned to the caller because the generated handler echoes the exception.
- **Time-of-check to time-of-use** in generated file and permission handling, which is invisible at the reading level and needs someone thinking about concurrency.

## The Iteration Trap

Covered fully in agentic.md, flagged here because it directly contradicts the intuitive remedy: asking the model to fix or improve the code again does not reliably make it more secure, and measurably makes it less so over several rounds. Do not treat "I asked it to make it secure" as a control.

## Sources

AI-code security measurements, 2025–2026: Cloud Security Alliance research note on the AI-generated CVE surge; Veracode's testing across 100+ models and 80 tasks (45% overall failure, 72% Java); AppSec Santa 2026 (534 samples, six models, OWASP Top 10 validation); the large-scale human-versus-AI comparison at arXiv 2508.21634; the CWE distribution study cataloguing 4,241 vulnerabilities across 77 types; plus 2026 industry statistics compilations (SQ Magazine, Paperclipped, CybeDefend, Kusari) for the density and multiplier figures. The three-mechanism explanation and the by-hand checklist are this skill's own synthesis, generalizing from those findings rather than restating any single source.
