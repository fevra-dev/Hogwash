# ADR-0017 — Trivy scoping & vulnerability risk register (per-repo opt-in)

**Status:** Accepted · **Date:** 2026-07-26
**Supersedes:** — · **Superseded-by:** — · **Refines:** ADR-0001 (Zero-Trust Dependencies)
**Threat-model:** carried from kiln ADR-0017 (grilled 8 vectors, 2026-07-23); re-confirmed for the per-repo-opt-in framing (adds no new surface) · **Sign-off:** operator, 2026-07-26

## Context
ADR-0001 wires `trivy fs --scanners vuln,secret,license --severity HIGH,CRITICAL --exit-code 1 .` into the pre-push gate and fails on any finding. On a low-dependency repo that is correct and stays the default. On a **dependency-heavy** repo it breaks down: the first real run against a JS/Solana app (`kiln`) surfaced **65 vuln findings (4 CRITICAL, 61 HIGH)**, ~60 of them **transitive** and not unilaterally fixable (`@solana/*`, `react-native`, `@stellar/*` chains — `axios`, `lodash`, `protobufjs`, `shell-quote`, …). A gate permanently red on unactionable upstream CVEs trains developers to `git push --no-verify`, which disables the **entire** gate — oxlint, biome, secret-scan, license — a strictly worse posture than an honest, scoped gate. **A gate that is always red is a gate that is ignored.** kiln solved this locally (its own ADR-0017); this ADR lifts the *policy* to WORKFLOW as a **per-repo opt-in** a repo adopts when it hits that wall. The shared gate is unchanged (ADR-0008 consolidation — no forced machinery on repos that don't need it; and per-scanner scoping is inherently ecosystem-specific, so it cannot live in one shared gate anyway).

## Decision
A repo MAY opt into the **Trivy risk-register pattern** when its dependency graph makes the ADR-0001 gate permanently red on unactionable transitive CVEs. The pattern is ecosystem-agnostic in policy, ecosystem-specific in wiring:

1. **Per-scanner scope (a principle, not one lockfile).** **Vuln** scanning targets the repo's **dependency lockfile/graph** (`pnpm-lock.yaml` · `uv.lock`/`requirements.txt` · `Cargo.lock` · `go.sum`) — foreign-ecosystem manifests vendored under `node_modules`/`vendor` are out of scope. **License** scanning runs against the **full filesystem** (real `LICENSE` files live inside dep trees; lockfile-only detects zero). **Secret** scanning is filesystem-scoped (minus vendored dirs for FP noise), fail-closed, and keeps **no register** (a leaked secret is always repo-actionable).
2. **Fail condition.** The gate MUST fail on any HIGH/CRITICAL vuln — or `forbidden`/`restricted` license — **not** present in the version-controlled register `.trivyignore.yaml`.
3. **Register discipline.** Every entry carries: the CVE id, a `statement` recording `direct|transitive` + why accepted (no upstream fix · not repo-reachable · breaking-bump-deferred), and an `expired_at` review date. Append-only; entries are removed only when the dependency is fixed, never to silence a live finding.
4. **Expiry is hard-capped and fails (never warns).** `expired_at` MUST be ≤ **30 days** for `direct:` entries, ≤ **90 days** for `transitive:`; the hygiene check *fails* the gate on any entry over its cap or already past `expired_at`. A direct-dep HIGH/CRITICAL is remediated by upgrade, or accepted under the 30-day cap with a tracked follow-up.
5. **Reachability at seed.** Any CVE in a package imported from the repo's source MUST get an **individual** `statement` with a reachability note; only build/dev-only transitive deps may be batch-accepted.
6. **Security-sensitive paths are a reviewed surface** — this **implements the lockfile-justification control ADR-0001 named but never built.** A change to the dependency lockfile, `.trivyignore.yaml`, or any patched-dependency set (`patches/`, `pnpm.patchedDependencies`, equivalent) MUST carry a `SECURITY-REVIEW:` commit trailer; the gate fails otherwise.
7. **Shared gate unchanged.** A repo that never hits the wall keeps the plain ADR-0001 `trivy fs .` gate. This ADR ships **no default machinery** and is not seeded as code — only as this documented pattern in `templates/adr/`.

## Considered Options
- **Risk register (`.trivyignore.yaml`) + per-scanner scope, per-repo opt-in — chosen.** Every accepted risk is explicit, justified, dated, and expiring; new/unaccepted findings still fail; the gate is green-able without being disabled; low-dep repos pay nothing. Strengthens ADR-0001: acceptance now requires a written, expiring justification instead of a silent pass or a blanket `--no-verify`.
- **Bake into the shared gate** — rejected: forces register overhead on low-dep repos, and the shared gate cannot hardcode one ecosystem's lockfile.
- **`--ignore-unfixed`** — rejected: removes ~1/62 in practice; hides fixed-upstream-but-transitive risk with no audit trail or expiry.
- **Severity CRITICAL-only** — rejected: transitive CRITICALs still wedge the gate, and it silently drops every HIGH.
- **Drop trivy / tolerate `--no-verify`** — rejected: disables secret + license + new-CVE detection wholesale — the exact failure ADR-0001 exists to prevent.

## Consequences
Easier: a dependency-heavy repo's gate greens on its baseline while every accepted CVE is documented, dated, and expiring; new direct deps, new CVEs, and license changes still fail; ADR-0001 is intact and tightened; low-dep repos are untouched. Harder: an adopting repo maintains the register (re-triage on expiry and on `pnpm up`/`uv lock`); the register discipline must be policed. Explicitly **not** reduced: actual transitive risk today — this makes it explicit, owned, and time-boxed instead of a push-blocker that gets bypassed.

## Security Considerations & Mitigations
Carried from kiln ADR-0017's grill (8 vectors), unchanged by the per-repo-opt-in lift:
- **Known-CVE-only false assurance.** Trivy matches CVE ids; it does **not** defend against the supply-chain threats ADR-0001 names — typosquats, dependency-confusion, maintainer-compromise — which ship with no CVE id. Those stay owned by lockfile-integrity hashes + human dependency review. The register is explicitly **not** a supply-chain-integrity control.
- **Local-advisory enforcement / `--no-verify`.** The pre-push hook is a local, bypassable control (`core.hooksPath` is local git config). Durable enforcement requires the same three scans in **CI branch protection**, failing closed if trivy is absent or its vuln DB is > 7 days stale (`--skip-db-update` forbidden in CI). **Until a repo adds that CI mirror, its register is advisory** — stated honestly, not claimed closed.
- **Smuggled dep behind a same-PR register edit.** Mitigated by §6: the lockfile / `.trivyignore.yaml` / patches are the security-sensitive path set; a change without a `SECURITY-REVIEW:` trailer fails the gate; register edits are reviewed under the ADR-0007 lens.
- **License detection regressed by lockfile scope.** Real: lockfile-only misses `LICENSE` files that live in dep trees; hence §1 keeps **license** on the full filesystem while only **vuln** moves to the lockfile.
- **Blanket seed amnesty hides a reachable HIGH.** Mitigated by §5 (individual reachability statement for any source-imported CVE).
- **Transitive expiry as a permanent silent accept.** Mitigated by §4 (hard caps; the check fails, never warns).
- **Scanner-absent fail-open.** The local dev hook MAY self-skip when trivy is absent (fast-feedback ergonomics); the CI mirror MUST fail closed (ADR-0005).

## Enforcement
- **Canonical mechanism (follow-on build, opt-in template):** a stdlib **Python** register-hygiene checker (`ccost.py`/`loop-contract.py` house style) shipped under `~/.claude/templates/` as an opt-in drop-in — FAILS on any `.trivyignore.yaml` entry lacking `statement`/`expired_at`, past `expired_at`, `direct:` over 30d, or `transitive:` over 90d. Ecosystem-specific parameters (the vuln lockfile target; the security-sensitive path set) are filled per adopting repo. kiln's `check-trivyignore.mjs` is the JS reference implementation; the WORKFLOW canonical is the Python one. **Not built in this session — tracked as the post-map follow-on (→ `writing-plans`).**
- **Gate wiring (per adopting repo):** the trivy stage splits into three scoped scans (vuln→lockfile, license→full-tree, secret→fs-minus-vendored), each `--exit-code 1 --ignorefile .trivyignore.yaml`, plus a security-sensitive-path change-review check.
- **CI mirror (required for durability):** the same three scans in branch protection, fail-closed on absent/stale trivy.
- **Not enforced on the shared gate / low-dep repos:** by decision §7, this ADR ships no default rule; its "enforcement" is the opt-in template above.

## Output Schema Impact
**Schema Change Type:** none

## Semantic Drift Assessment
- n/a — no tool output schema changes; `.trivyignore.yaml` is a new opt-in config, not a modified tool output.
- **Verification plan:** the follow-on Python checker is unit-tested against a fixture register (valid entry, missing-statement, expired, over-long `direct:` expiry) and dogfooded (ADR-0010) before the template ships.
