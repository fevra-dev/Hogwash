# Vocabulary — Banned Word Lists

Evidence tiers: **[E]** = empirical corpus study · **[D]** = commercial detector data (millions of docs) · **[W]** = Wikipedia WikiProject AI Cleanup practitioner observation · **[C]** = multi-source community confirmation

Wordlists have expiration risk. Current as of April 2026. Review quarterly.

---

## Tier 1 — Hard Ban

Replace or cut in virtually all contexts. Exception: technical terms used in domain-standard meaning (e.g., "ecosystem" in actual ecology, "robust" in statistics).

`delve` [E,D,W] · `tapestry` [W,C] · `testament` [W,C] · `vibrant` [W,C] · `pivotal` [E,W,C] · `groundbreaking` [C] · `transformative` [D,C] · `revolutionary` [C] · `innovative` [E,C] · `synergy` [C] · `paradigm` [C] · `leverage` *(as verb)* [C] · `utilize` / `utilized` [C] · `seamless` [C] · `robust` [E,C] · `comprehensive` [E,C] · `holistic` [C] · `streamline` [C] · `empower` [C] · `foster` [C] · `nuanced` [C] · `multifaceted` [C] · `intricate` / `intricacies` [W,C] · `cutting-edge` [C] · `state-of-the-art` [C] · `game-changing` [C] · `disruptive` [C] · `actionable` [C] · `scalable` [C] · `dynamic` [C] · `ecosystem` *(non-technical)* [C] · `landscape` *(metaphorical)* [C] · `journey` *(metaphorical)* [C] · `space` *(meaning industry/domain)* [C] · `impactful` [C] · `meaningful` [C] · `resonate` [C] · `commendable` [E,W] · `meticulous` / `meticulously` [E,W] · `realm` [E,C] · `comprehend` [E,W] · `bolstered` [W,C] · `garner` [W,C] · `harness` *(metaphorical)* [C] · `unleash` *(metaphorical)* [C] · `embark` [C] · `bustling` [C] · `enduring` [W,C] · `enhance` / `enhances` [W,D] · `daunting` [C] · `aligns` / `align with` [D] · `surpassing` [D] · `tailored` [D,C] · `underpins` [C] · `excels` [C] · `crucial` [E,D,C] · `vital` *(filler)* [C] · `essential` *(filler)* [C] · `showcase` / `showcasing` [E,D,C] · `underscores` *(verb)* [E] · `encompasses` [C] · `facilitates` [C] · `commenced` [C] · `illuminate` *(metaphorical)* [C] · `unpack` *(metaphorical)* [C] · `navigate` *(metaphorical)* [C] · `beacon` *(metaphorical)* [C] · `spearheaded` [C] · `nestled` [C] · `breathtaking` [C] · `stunning` [C] · `renowned` [C] · `pioneering` *(metaphorical)* [C]

---

## Tier 2 — Near-Ban (replace when clustered)

Two or more Tier 2 signals in the same paragraph = revision. One alone may be acceptable depending on context.

`potential` *(hollow adjective: "potential impact," "potential benefits")* [E] · `swift` *(dramatic effect)* [E,W] · `findings` *(generic noun with no follow-through)* [E] · `tragically` *(outside genuine tragedy)* [D] · `primarily` *(filler)* [E] · `emphasize` / `emphasizing` [E] · `notably` *(all positions, not just openers)* [E,D] · `novel` *(academic register without actual novelty claim)* [E] · `significant` *(without quantification)* [E] · `furthermore` [E,C] · `interplay` [W] · `subsequent to` *(when "after" works)* [C] · `prior to` *(when "before" works)* [C] · `in order to` *(when "to" works)* [C] · `overarching` [C] · `compelling` [C] · `unprecedented` [C] · `imperative` *(as adjective)* [C]

---

## Expiration Watch

Strong tells through 2024, being trained away. Still flag at Tier 2:
`delve` · `underscore` · `tapestry` · `vibrant` · `certainly` *(opener)*

---

## Copula Avoidance — AI Circumlocution

AI avoids "is/has" and substitutes elaborate constructions. The tell is clustering: a piece that never uses "is" and instead rotates through "serves as," "stands as," "represents," "functions as" is AI. A single instance in an otherwise normal paragraph is fine.

| AI default | Human replacement |
|---|---|
| serves as | is |
| functions as | is |
| acts as | is |
| stands as | is |
| represents *(when meaning "is")* | is |
| boasts | has |
| features | has |
| offers *(meaning "has")* | has |
| aims to | does |
| is designed to | does |
| seeks to | does |
| works to | does |
| facilitates | enables, allows |
| encompasses | includes |
| commenced | began, started |
| subsequent to | after |
| prior to | before |
| in order to | to |
| serves to | helps / delete |

---

## Quick Substitution Reference

| Inflated | Direct |
|---|---|
| utilize | use |
| leverage (verb) | use |
| illuminate | show |
| unpack | explain |
| navigate (metaphorical) | work through, deal with |
| empower | let |
| foster | build |
| showcase | show |
| enhance | improve |
| streamline | simplify |
| holistic | complete, full |
| comprehensive | full, complete, thorough |
| robust | strong, reliable |
| seamless | smooth / just describe what's smooth |
| innovative | new, different — or name what's new |
| transformative | changed — or name what changed |
| cutting-edge | current / name the specific technology |
| actionable | specific, concrete — or name the action |

---

*Quarterly review required. Check GPTZero rolling corpus and Wikipedia WikiProject AI Cleanup talk archives for additions.*

## Sources

Each entry above is graded inline, [E] empirical corpus study, [D] commercial detector data, [W] Wikipedia WikiProject consensus, [C] community-sourced, rather than consolidated here, since a single trailing list would lose the per-word confidence grading. See SKILL.md's frontmatter for the full underlying study list (Kobak et al., GPTZero corpus, Wikipedia WikiProject AI Cleanup, among others). [D]-only entries with no [E]/[W]/[C] corroboration are the ones most worth re-verifying at the next quarterly review; see core/structural-patterns.md's note on why single-vendor detector data deserves less standalone confidence than independently corroborated sources.
