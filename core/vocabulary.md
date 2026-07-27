# Vocabulary — Banned Word Lists

Evidence tiers: **[E]** = empirical corpus study · **[D]** = commercial detector data (millions of docs) · **[W]** = Wikipedia WikiProject AI Cleanup practitioner observation · **[C]** = multi-source community confirmation

Wordlists have expiration risk. **Reviewed July 2026. Next review due October 2026.**

## Read This Before Using the List

Wikipedia's WikiProject AI Cleanup now stratifies its AI-vocabulary observations by era, and the eras differ enough that an undated list is misleading. Their cohorts, as of the July 2026 revision of *Signs of AI writing*:

| Era | Words observed |
|---|---|
| 2023 to mid-2024 | additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate/intricacies, interplay, key, landscape, meticulous/meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant |
| mid-2024 to mid-2025 | align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant |
| mid-2025 onward | **emphasizing, enhance, highlighting, showcasing** |

Two consequences, and they cut in opposite directions.

**The current-era set is small.** Four words carry most of the present-day signal. Weight them accordingly, and treat a hit on one of them as worth more than a hit on a word whose cohort ended two years ago.

**The long list below is cumulative, not current.** Most of Tier 1 is 2023-era vocabulary. Those words are still worth replacing, because they are still inflated writing and the substitutions still improve the sentence, but a hit on one is now weak evidence of AI authorship specifically. A human writer who says "pivotal" in 2026 is more likely to be a human writer who says "pivotal" than a model. Fix the word; do not draw the inference.

This is the wordlist half of the skill's own principle that wordlists expire and structure does not. If the two disagree, core/structural-patterns.md wins.

---

## Tier 1 — Hard Ban

Replace or cut in virtually all contexts. Exception: technical terms used in domain-standard meaning (e.g., "ecosystem" in actual ecology, "robust" in statistics).

**Current-era core [W, July 2026]:** `emphasizing` · `enhance` / `enhances` · `highlighting` · `showcasing`

These four are the only items Wikipedia's practitioners still observe in the mid-2025-onward cohort. All four also appear in at least one earlier cohort, which is what makes them durable rather than merely current. Everything after this line is the cumulative list.

`delve` [E,D,W] · `tapestry` [W,C] · `testament` [W,C] · `vibrant` [W,C] · `pivotal` [E,W,C] · `groundbreaking` [C] · `transformative` [D,C] · `revolutionary` [C] · `innovative` [E,C] · `synergy` [C] · `paradigm` [C] · `leverage` *(as verb)* [C] · `utilize` / `utilized` [C] · `seamless` [C] · `robust` [E,C] · `comprehensive` [E,C] · `holistic` [C] · `streamline` [C] · `empower` [C] · `foster` [C] · `nuanced` [C] · `multifaceted` [C] · `intricate` / `intricacies` [W,C] · `cutting-edge` [C] · `state-of-the-art` [C] · `game-changing` [C] · `disruptive` [C] · `actionable` [C] · `scalable` [C] · `dynamic` [C] · `ecosystem` *(non-technical)* [C] · `landscape` *(metaphorical)* [C] · `journey` *(metaphorical)* [C] · `space` *(meaning industry/domain)* [C] · `impactful` [C] · `meaningful` [C] · `resonate` [C] · `commendable` [E,W] · `meticulous` / `meticulously` [E,W] · `realm` [E,C] · `comprehend` [E,W] · `bolstered` [W,C] · `garner` [W,C] · `harness` *(metaphorical)* [C] · `unleash` *(metaphorical)* [C] · `embark` [C] · `bustling` [C] · `enduring` [W,C] · `enhance` / `enhances` [W,D] · `highlighting` [W] · `emphasizing` [E,W] · `exemplifies` [W] · `diverse array` [W] · `commitment to` *(promotional)* [W] · `in the heart of` [W] · `rich` *(metaphorical)* [W] · `profound` [W] · `daunting` [C] · `aligns` / `align with` [D,W] · `surpassing` [D 2024, uncorroborated] · `tailored` [D,C] · `underpins` [C] · `excels` [C] · `crucial` [E,D,C] · `vital` *(filler)* [C] · `essential` *(filler)* [C] · `showcase` / `showcasing` [E,D,C] · `underscores` *(verb)* [E] · `encompasses` [C] · `facilitates` [C] · `commenced` [C] · `illuminate` *(metaphorical)* [C] · `unpack` *(metaphorical)* [C] · `navigate` *(metaphorical)* [C] · `beacon` *(metaphorical)* [C] · `spearheaded` [C] · `nestled` [C] · `breathtaking` [C] · `stunning` [C] · `renowned` [C] · `pioneering` *(metaphorical)* [C]

---

## Tier 2 — Near-Ban (replace when clustered)

Two or more Tier 2 signals in the same paragraph = revision. One alone may be acceptable depending on context.

`potential` *(hollow adjective: "potential impact," "potential benefits")* [E] · `swift` *(dramatic effect)* [E,W] · `findings` *(generic noun with no follow-through)* [E] · `tragically` *(outside genuine tragedy)* [D 2024, uncorroborated] · `primarily` *(filler)* [E] · `emphasize` *(promoted to Tier 1 as `emphasizing`, July 2026)* [E] · `notably` *(all positions, not just openers)* [E,D] · `novel` *(academic register without actual novelty claim)* [E] · `significant` *(without quantification)* [E] · `furthermore` [E,C] · `interplay` [W] · `subsequent to` *(when "after" works)* [C] · `prior to` *(when "before" works)* [C] · `in order to` *(when "to" works)* [C] · `overarching` [C] · `compelling` [C] · `unprecedented` [C] · `imperative` *(as adjective)* [C]

---

## Expiration Watch

Words whose cohort has passed. Still replace them, since they are still inflated writing, but stop treating a hit as evidence of AI authorship. Demoted to Tier 2 weight for inference purposes regardless of their Tier 1 listing above.

**Confirmed decayed [W, July 2026]:** `delve` · `underscore` · `tapestry` · `vibrant` · `pivotal` · `crucial` · `bolstered` · `enduring` · `garner` · `intricate` / `intricacies` · `interplay` · `meticulous` / `meticulously` · `testament` · `boasts` · `landscape` · `additionally` · `key` · `valuable` · `certainly` *(opener)*

On `delve` specifically, which is the most-cited AI tell in circulation: Wikipedia's practitioners record that it was heavily overused in 2023 and early 2024, became less frequent later in 2024, then dropped off sharply during 2025. It has now been a weak signal for longer than it was a strong one.

**A caution about where wordlists come from.** A large ecosystem of "AI words to avoid" pages, most of them attached to text-humanizing products, republishes the 2023-era list every year with the current year in the title. Several checked during this review present 2026-dated guidance whose underlying figure is the Kobak 2020–2023 PubMed measurement, and cite `delve` as a top current tell on that basis. Date the evidence, not the page. This is the same failure this skill already flags for consumer AI detectors, appearing one layer up in the supply chain that produces wordlists.

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
| showcase / showcasing | show |
| enhance | improve |
| highlighting | shows, points out — or just make the point |
| emphasizing | stresses — or delete and let the sentence carry it |
| exemplifies | is an example of, shows |
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

*Quarterly review required. Check Wikipedia WikiProject AI Cleanup's era cohorts first, since they are dated and revised; treat any undated wordlist as 2023-era until proven otherwise.*

## July 2026 Review Record

What changed, so the next review can tell movement from noise:

- **Adopted era stratification** from Wikipedia's cohort model. This is the substantive change; the list had been flat and undated, which made a 2023 word and a current word look equally diagnostic.
- **Promoted to Tier 1:** `highlighting` (new, current cohort), `emphasizing` (from Tier 2, present in all three cohorts).
- **Added from the promotional/puffery set [W]:** `exemplifies`, `diverse array`, `commitment to`, `in the heart of`, `rich`, `profound`.
- **Expanded Expiration Watch** from 5 words to 19, moving the whole 2023-to-mid-2024 cohort into it. `delve` confirmed decayed rather than suspected.
- **Re-verified the [D]-only entries**, which the April 2026 review flagged for exactly this. Outcome: `align with` gained independent Wikipedia corroboration and is now [D,W]. `surpassing` and `tragically` did not, and their sole source is GPTZero's list of October 7, 2024, now roughly 21 months old. Both are re-tagged to show it. If the next review finds no corroboration, cut them.
- **No change to Tier 2 or the copula table.** Copula avoidance is structural rather than lexical, which is consistent with it not decaying the way the wordlist has.

## Sources

Each entry above is graded inline, [E] empirical corpus study, [D] commercial detector data, [W] Wikipedia WikiProject consensus, [C] community-sourced, rather than consolidated here, since a single trailing list would lose the per-word confidence grading. See SKILL.md's frontmatter for the full underlying study list (Kobak et al., GPTZero corpus, Wikipedia WikiProject AI Cleanup, among others). [D]-only entries with no [E]/[W]/[C] corroboration are the ones most worth re-verifying at the next quarterly review; see core/structural-patterns.md's note on why single-vendor detector data deserves less standalone confidence than independently corroborated sources.

July 2026 review sources: Wikipedia *Signs of AI writing* (WikiProject AI Cleanup, era cohorts and promotional-language set, revision current as of this review) for all [W] gradings and every era claim in this file. GPTZero's most-common-AI-vocabulary list, published October 7, 2024, for the [D] gradings and the frequency multipliers behind `showcasing` (20x), `aligns` (16x), `surpassing` (12x), and `tragically` (11x); that publication date is now part of the grading because it bounds what the [D] tier can currently support. The wordlist-recycling caution in Expiration Watch comes from checking several 2026-dated "AI words to avoid" pages against their own underlying citations during this review, not from any single source.
