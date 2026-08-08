---
name: hogwash
description: "Eliminates AI-generated writing, code, and design patterns through manual line-by-line audit. Use when writing, editing, or reviewing content that may contain AI slop: banned vocabulary, structural tells, code anti-patterns, formatting artifacts. Two-pass process: rewrite then self-critique. Evidence-tiered, synthesized from 20+ academic, industry, and community sources (see each reference file for citations). Covers English prose, code, and design (domains/); cross-lingual content and model-family tells as cross-cutting lenses (lenses/); resumes/CVs with field-specific vocabulary (domains/resume/)."
metadata:
  version: 2.28.0
---

# HOGWASH

*For a human-facing map of this architecture and why it's shaped this way, see README.md. This file is Claude's dispatch logic; that one is for a person navigating the repo.*

Strip AI defaults from writing, code, and design. Read each line manually with full context. Do not use regex or automated substitution. Automated substitution without judgment produces wrong results.

**Core files — always relevant once this skill triggers:**
- **[core/vocabulary.md](core/vocabulary.md)** — banned word lists with evidence tiers
- **[core/phrases.md](core/phrases.md)** — banned phrases, openers, structural formulas
- **[core/structural-patterns.md](core/structural-patterns.md)** — durable rhetorical and structural tells
- **[audit-checklist.md](audit-checklist.md)** — full self-audit checklist

**domains/ — load based on what kind of content this actually is:**
- **domains/code/** — five files, four different questions about the same artifact: **[patterns.md](domains/code/patterns.md)** (what it looks like when you read it), **[security.md](domains/code/security.md)** (is it exploitable; AI code carries 2.7× the vulnerability density of human code, and injection alone is a third of confirmed findings), **[supply-chain.md](domains/code/supply-chain.md)** (does that package exist, and did someone register it because models keep inventing it), **[agentic.md](domains/code/agentic.md)** (who wrote it and how many times; iterating five rounds raises critical vulnerabilities 37.6%), **[enforcement.md](domains/code/enforcement.md)** (make the rest impossible to commit). Load patterns.md always; add the others by scope.
- **domains/design/** — **[patterns.md](domains/design/patterns.md)** (static visual, layout, and copy slop; opens with why removing every flagged default lands you on the current AI default), **[motion.md](domains/design/motion.md)** (does the movement communicate a state change, or perform), **[accessibility.md](domains/design/accessibility.md)** (does it exclude someone; uncorrelated with whether it looks generic), **[expressive.md](domains/design/expressive.md)** (when loud is the brief, the design counterpart to fiction.md). Load patterns.md always.
- **[domains/fiction.md](domains/fiction.md)** — fiction, creative writing, and screenwriting. A different aim from the rest of this skill: optimizes for experience, not a clear claim.
- **[domains/presentations.md](domains/presentations.md)** — slide decks, mostly slide-scale instances of patterns already in core/ and domains/design.md, plus real new material for investor pitch decks specifically.
- **[domains/legal.md](domains/legal.md)** — legal writing. Formal hedging and boilerplate structure are often correct here, not tells. Centered on the highest-stakes finding in this skill: fabricated case citations in real court filings.
- **domains/prose/** — one file per genre, load only the one that matches: [academic.md](domains/prose/academic.md), [technical-docs.md](domains/prose/technical-docs.md), [marketing.md](domains/prose/marketing.md), [support.md](domains/prose/support.md), [email.md](domains/prose/email.md), [security-reporting.md](domains/prose/security-reporting.md), [social-linkedin.md](domains/prose/social-linkedin.md), [tone-calibration.md](domains/prose/tone-calibration.md) (intent, not genre, cuts across the others)
- **[domains/resume/patterns.md](domains/resume/patterns.md)** — resumes/CVs: a different medium, mostly overrides everything above. Cover Letters and LinkedIn Profiles included as hybrid cases. US conventions; carries the flagged tension between what an automated screen rewards and what a human reviewer rejects.
- **[domains/resume/ats.md](domains/resume/ats.md)** — machine parsing, a separate axis from writing quality. Load with patterns.md whenever the resume goes through an online application system.
- **[domains/resume/fabrication.md](domains/resume/fabrication.md)** — the highest-stakes file in the resume domain, and the resume counterpart to domains/legal.md. Load whenever a resume is being *rewritten* rather than written: that's when a widened verb or a supplied number gets introduced on top of true employers and true dates. Flag, never silently fix.
- **[domains/resume/nontraditional-evidence.md](domains/resume/nontraditional-evidence.md)** — when the candidate's strongest material isn't employment: bug bounty findings, CTF placements, CVEs and advisories, open-source work, self-built tooling, home labs. Unusually verifiable evidence, which makes it both the strongest thing on the page and the fastest to fail if overstated.
- **domains/resume/industries/** — field-specific resume vocabulary, load alongside patterns.md: [full-stack.md](domains/resume/industries/full-stack.md), [cybersecurity.md](domains/resume/industries/cybersecurity.md), [it-support.md](domains/resume/industries/it-support.md), [administrative.md](domains/resume/industries/administrative.md), [healthcare.md](domains/resume/industries/healthcare.md), [finance-sales.md](domains/resume/industries/finance-sales.md). Load exactly one. See that folder's README.md before adding a new one.

**lenses/ — cross-cutting, apply on top of whichever domain file you loaded:**
- **[lenses/language.md](lenses/language.md)** — scope note for non-English content: what's universal vs. English-specific
- **[lenses/model-tells.md](lenses/model-tells.md)** — supplementary: vocabulary/structure/framing tells by model family. High-churn, review monthly. Not part of the core audit.

**Medium check, before loading anything else:** prose (blog, docs, email, report) → the matching domains/prose/ file + core/structural-patterns.md. Fiction, screenwriting, or other creative writing → domains/fiction.md instead; most of core/structural-patterns.md's specificity-focused rules don't apply the same way here, telling is sometimes correct. Slide deck or presentation → domains/presentations.md, loaded alongside domains/design.md and core/structural-patterns.md rather than instead of them. Legal writing → domains/legal.md instead; formal hedging and boilerplate are often the correct convention there, not a tell, and this is not a citation-verification tool. Code → domains/code/patterns.md, plus security.md if it touches untrusted input or auth, supply-chain.md if it adds a dependency or an agent can install, agentic.md if an agent wrote it rather than a person with autocomplete. Visual design → domains/design/patterns.md, plus motion.md if it animates, accessibility.md if it ships to users, and expressive.md first if the brief is a portfolio, brand moment, or culture site rather than a product surface. Resume or CV → domains/resume/patterns.md instead, most of the rest of this skill doesn't apply; add domains/resume/ats.md if it's going through an online application system, domains/resume/fabrication.md if you're rewriting an existing resume rather than writing one, domains/resume/nontraditional-evidence.md if their strongest material is bug bounty, CTF, CVE, open-source, or lab work rather than employment, and the matching domains/resume/industries/ file if the candidate's field is covered there. Non-English content, any medium → check lenses/language.md first for what transfers. Know which model wrote it? → lenses/model-tells.md is a supplementary check, not required.

---

## CORE PRINCIPLES

**AI smell is the absence of a writer, not the presence of specific words.** No visible edge where a specific person could be wrong. Generic subjects ("many developers struggle with...") stand in for "I." Every ban in this skill is downstream of that one fact, which is also why fixing stance and structure matters more than fixing vocabulary and symbols. See "Fix Order" below.

**Wordlists expire. Structure patterns don't.** Now measured rather than asserted. Wikipedia's WikiProject AI Cleanup tracks its vocabulary observations by era: the 2023-to-mid-2024 cohort holds 19 words, and the mid-2025-onward cohort holds four (emphasizing, enhance, highlighting, showcasing). "Delve" was heavily overused through early 2024, then dropped off sharply in 2025; it has now been a weak signal for longer than it was a strong one. Over the same period the *phrase* multipliers did not decay, because a formula encodes a rhetorical move and a word only encodes a preference. Weight structure most heavily, phrases next, formatting and single words least. Formatting belongs at the bottom with vocabulary rather than with structure, which the July 2026 review of core/structural-patterns.md corrected: em-dash frequency decayed exactly like "delve" once vendors began suppressing it (GPT-5.1 was instructed to use fewer). The test that generalizes: if a vendor could switch a signal off with one line of a system prompt, it decays. How a model composes is expensive to change; what it prefers on the surface is not. Both review records are at the end of their respective files.

**Voiceless sterile prose is just as obvious as slop.** The goal is not neutral. It is actual thought on the page. Avoiding AI patterns is half the job; the other half is putting a human behind the writing.

**Fixing slop badly just swaps one uniformity for another.** The common failure after cutting AI phrasing is smoothing everything back into tidy, even prose, correct this time, still flattened toward a different target. Keep genuine unevenness on purpose: short lines where they were actually short, one long sentence left in where the original writer really did ramble into a point. Slightly uneven and specific beats flawless and blank, every time.

**Write toward something, not just away from a list.** Before auditing, apply the positive principles below. Bans alone produce sanitized nothing.

---

## PASS 0 — POSITIVE PRINCIPLES (Apply Before Banning)

Derived from Strunk's *Elements of Style*: what to do, not just what to avoid.

1. **Use active voice.** Passive voice hides actors. Name who does the thing.
2. **Put statements in positive form.** "He was not honest" → "He lied." State what is, not what isn't.
3. **Use definite, specific, concrete language.** Prefer the particular to the general, the concrete to the abstract. A number beats "significant." A name beats "experts."
4. **Omit needless words.** Every word should earn its place. "Due to the fact that" → "because." "At this point in time" → "now."
5. **Place emphatic words at the end of the sentence.** The last word carries the most weight. Don't waste it on a preposition.
6. **Vary sentence length deliberately.** Short when the idea is done. Longer when it needs room. The variance signals a mind pacing itself against the content.
7. **Have an opinion.** Don't just report facts. React to them. "I don't know how to feel about this" is more human than neutral lists of pros and cons.
8. **Allow some confusion.** Perfect structure feels algorithmic. Tangents, asides, half-formed thoughts are human. Let some mess in where it serves the piece.
9. **Name limitations honestly.** What the thing doesn't do. What edge cases it fails on. What versions it requires. AI claims comprehensive coverage; humans name the gaps.
10. **Use subheadings as scannable statements (English-language content).** Not "Background": "Why the existing approach fails." Not "Results": "Query time dropped from 847ms to 12ms." This is an English convention, not a universal one: claim-shaped headings read as a foreign, performed AI tell in at least Japanese. For non-English content, see lenses/language.md before applying this rule.

---

## AUDIT METHODOLOGY

### Pattern Stacking
When multiple weak signals converge on the same phrase (bold emphasis, an em dash, and a coined term, all in one sentence), that is one strong tell, not three separate flags. Consolidate overlapping patterns on the same phrase into one finding. Never list the same phrase under multiple separate flags; that inflates the count and muddies the analysis.

### Fix Order
Audit stance and structure before vocabulary and punctuation. A piece with a real, specific, falsifiable claim behind it barely reads as AI even with a stray tell left in. A piece with every banned word and em dash removed still reads as AI if there's no actual claim being made. Hitting every quantified threshold in this skill is not the goal; it's a byproduct of fixing the actual writing. If time-constrained, run PASS 0 and the structure/specificity portions of the audit first; treat vocabulary and formatting passes as the last 20%, not the first.

### Severity Model
- **Tier 1 — Replace automatically.** Wrong in virtually all contexts.
- **Tier 2 — Replace when clustered.** Two or more Tier 2 signals in the same paragraph warrant revision. One alone may be acceptable.
- **Tier 3 — Replace at high density.** Flag when pattern appears more than twice per 500 words.

### False Positive Protection
Do not flag these as AI tells without additional context:

| Pattern | When it's NOT a tell |
|---|---|
| Curly quotes | Standard in Word, Google Docs, and formatted content — only a tell in plain-text/code contexts |
| "As of [date]" | Standard journalism for time-sensitive data — only a tell when hedging rather than citing a real source |
| Title case headings | Weak signal alone — only meaningful when stacked with other tells |
| Single "serves as" | One instance in an otherwise normal paragraph is fine — copula avoidance requires clustering |
| Group of three items | Only flag tricolons when the third item adds nothing or near-duplicates the first two |
| Negative parallelism | One "It's not X, it's Y" per 1,000 words is fine — the tell is frequency relative to piece length |

Also exempt: technical terms in domain-standard meaning, quoted source material, legal/compliance required phrasing, code identifiers.

### Density Thresholds

| Metric | Clean | Light | Moderate | Heavy |
|---|---|---|---|---|
| Slop markers per 100 words | 0–1.0 | 1.0–2.5 | 2.5–5.0 | 5.0+ |
| Em dashes per 1,000 words | 0–2 | 3–5 | 6+ = strong signal | — |
| Bullets as % of content | <40% | 40–60% | >60% = AI tendency | — |
| Sentence length SD | >10 = human | 5–10 | <5 = AI monotony | — |

**Co-occurrence flag:** Three Tier 1 words in any 100-word window = definitive AI signal regardless of individual density. Full rewrite required.

**Type-Token Ratio (TTR):** Low TTR = synonym cycling, even when individual synonyms aren't obvious. If the same concept cycles through 4+ different words in one paragraph, that's the pattern.

**Consecutive sentence similarity:** Flag any two adjacent sentences with the same subject position, same clause structure, and same length, regardless of whether individual sentences trigger other rules.

---

## DIAGNOSTIC TESTS

Run these before and after revision.

**The Specificity Test (root cause):** For every generalization ("in recent years," "industry leaders," "significant growth"), ask: "What specific fact has AI replaced with a generic?" A name, date, number, location. Supply it or acknowledge the uncertainty directly.

**The Distinctiveness Test:** "Would a reader immediately identify this as AI-generated?" Find the sentence that gives it away first. Fix that one. Repeat.

**The Company Test:** "Could this sentence appear in any other company's blog by swapping a few nouns?" If yes, make it specific to this product, project, or context.

**The Read-Aloud Test:** Read the piece out loud. Flag anything that: no human would actually say in conversation, makes you cringe slightly, feels like it's trying too hard to sound smart, or could describe any topic by swapping nouns.

**The Golden Sentence Test:** If a sentence sounds like it was designed to be screenshot and shared, a quotable aphorism, rewrite it. "Innovation is not a destination; it is a journey." Delete.

---

## TONE CALIBRATION BY POST TYPE

Match voice to intent, not just content. Condensed here; full version with evidence per intent is domains/prose/tone-calibration.md.

**Technical** (knowledgeable peer): Reader knows basics, wants specifics. Evidence = code, numbers, named packages. No setup, no inspiring framing. Start with what it does.

**Vision** (opinionated builder with receipts): Reader is skeptical, needs convincing. Evidence = real-world examples, before/after, objections addressed. State the position first, then the evidence.

**Tutorial** (experienced guide who made the mistakes): Reader wants to follow along. Evidence = runnable examples, expected output, common pitfalls named explicitly. Complete walkthrough, no missing steps.

For voice matching to a specific person: see Voice Calibration section below.

---

## SCORING RUBRIC

Rate 1–10 per dimension. Below 35/50: revise.

| Dimension | Question |
|---|---|
| **Directness** | Statements or announcements? Statements score higher. |
| **Rhythm** | Varied or metronomic? SD > 5 words across 500-word sample scores higher. |
| **Trust** | Respects reader intelligence, or over-explains? |
| **Authenticity** | Sounds like a person, or a demo of a writing assistant? |
| **Density** | Anything cuttable? Less cuttable = higher. |

---

## WRITER / REVIEWER SEPARATION

For high-impact work, separate the passes. The same pass must not write and self-approve.

**Writer pass:** Make changes. Lock behavior with regression tests first (code). Run one smell-focused pass at a time. Stay within the requested scope. Do not silently expand into adjacent files.

**Reviewer pass:** Do not start by editing. Review the plan, changed files, verification evidence. Produce a verdict. Hand changes back to a separate writer pass.

---

## VOICE CALIBRATION

Provide 2–3 paragraphs of the target person's actual writing. Analyze:
- Average sentence length and variance
- Preferred connective words (they have some and avoid others)
- Fragments vs. complete sentences
- First-person presence or avoidance
- Ratio of declarative to qualifying statements
- Recurring vocabulary or metaphor patterns

Apply as a positive template. The goal is not neutral. It is the person's voice.

---

## QUICK REFERENCE

**Delete without replacement:**
Great question · I hope this helps · Let me know if you need any modifications · It's worth noting · Needless to say · Let's dive in · In today's world · Certainly · Moreover · Furthermore · Additionally · Here's the thing · Let me be clear · Let that sink in · The best part? · That's it. That's the [noun]. · And here's the kicker · Enter: [thing]

**Replace with simpler verbs:**
serves as → is · boasts → has · showcases → shows · leverages → uses · fosters → builds · empowers → lets · aims to → does · encompasses → includes · facilitates → enables · commenced → began · utilized → used · illuminate → show · unpack → explain · navigate → work through

**Always name the actor:**
"the data suggests" → "the 2024 Pew study found" · "experts believe" → "[Name] (year) argues" · "the market rewards" → "buyers pay more for" · "technology enables" → "this library lets you"

**Structural tells (load core/structural-patterns.md for full list):**
Specificity erasure · Rule of Three · Symmetric conclusions · Tricolon alliteration · Challenges-Triumph boilerplate · Emotional register uniformity · Every-paragraph-resolves · Conjunctive headings · Sentence-length monotony · Sentence-opener concentration · Bullet overuse

**Thresholds** (ordered by current strength, July 2026):
Sentence SD: <5 words = AI monotony — the strongest single signal; 3+ consecutive sentences of 17–23 words is the quick hand check
Sentence openers: >50% starting The/This/It/In = flag
Bullets: >60% = AI tendency
Cluster: 3 Tier 1 words in 100-word window = full rewrite
Em dashes: 6+/1,000 words **of flowing prose only** (list labels and table cells are not prose) = look closer, not a conclusion; vendors are actively suppressing this one

---

*v2.28.0 — August 2026. Wordlist section (core/vocabulary.md) reviewed July 2026; next review due October 2026. Structural patterns reviewed July 2026 and confirmed stable, with one correction: formatting is not structure. Next structural review January 2027. v2.8 restructured the whole skill into core/, domains/, and lenses/. v2.9–v2.15 added domains/fiction.md, domains/presentations.md, domains/prose/email.md, deepened academic.md, closed the em-dash debt, added README.md, and added code.md's Workflow Layer. v2.16 added scripts/self_check.py. v2.17 standardized the Sources-section convention across 6 files and closed a real gap: a detector-data-reliability caution that was researched but never shipped past the standalone research doc. v2.18 adds domains/legal.md, the highest-stakes file in this skill: fabricated case citations tracked in a maintained academic database (roughly 200 cases mid-2025, past 1,800 as of this writing, real sanctions, one canceled trial), the sharpest possible instance of domains/code.md's structurally-plausible-but-functionally-empty question, and a fifth independent confirmation of Untailored Is the Real Tell, this time from Anthropic's own claude-for-legal plugin documentation. v2.19 renames the skill Hogwash, closing the naming decision that had been open since v2.18: the old name was already taken by several unrelated projects. Rename plus a scripts/self_check.py scope fix (it now skips adr/, research/, and repo tooling, which aren't written to these rules); no audit rule changed. v2.20 deepens the resume domain: adds domains/resume/ats.md, which backs the Parseability rubric dimension that previously had no supporting content; adds domains/resume/industries/healthcare.md and finance-sales.md; scopes the resume material to US conventions explicitly; and records the sharpest open tension in this skill, that automated screens prefer LLM-written resumes 67 to 82 percent of the time (arXiv 2509.00462, June 2026) while human reviewers reject the same register on sight. The skill takes the human side, with the reasoning stated in patterns.md rather than assumed. v2.21 closes the two gaps v2.20 left open. domains/resume/fabrication.md promotes the Fabrication Risk from a paragraph to the resume counterpart of domains/legal.md, on the finding that resume fabrication is structurally unlike the legal kind: it is inflation on a true base (a widened verb, a supplied number) sitting on real employers and real dates, so it survives every background check and fails in the interview. Stakes attached: 46% of resumes carry a background-check discrepancy, 41% of those candidates lose the offer, 18% are terminated after starting. Worked examples added for every register the domain covers, cover letter and LinkedIn in patterns.md and one per industry file, since a domain spanning four industries had exactly one example. v2.22 is the overdue quarterly vocabulary review, and it changed the shape of core/vocabulary.md rather than just its contents: the list is now stratified by era, following Wikipedia's cohort model, because a flat undated list made a 2023 word and a current word look equally diagnostic. Current-era core is four words. Expiration Watch grew from 5 to 19. The [D]-only entries flagged at the April review were re-verified, with `align with` gaining corroboration and `surpassing` and `tragically` failing to; their sole source is dated October 2024 and is now labeled as such. The finding worth carrying forward: single words in that dataset decayed since 2024 while the phrase multipliers did not, which is the wordlists-expire principle confirmed from inside the data instead of assumed. v2.23 is the first review of core/structural-patterns.md, and its job was to test that file's durability claim rather than add to it. The claim held: nothing structural decayed, and the sentence-cadence rule was independently reinforced, since 2026 detection writing now names cadence uniformity the strongest current tell after demoting punctuation. One correction: the Formatting Patterns section does not belong under "durable" and is now its own tier, because em-dash frequency decayed the same way "delve" did once vendors suppressed it. The generalizable test, now in CORE PRINCIPLES: if a vendor could switch a signal off with one line of a system prompt, it decays. Also corrects the em-dash denominator to flowing prose only, from this skill's own measurement against a 225-file corpus, where roughly 60% of a naive flag list turned out to be the `- **Term** — definition` convention rather than prose. v2.24 splits the former combined tech.md into full-stack.md, cybersecurity.md, and it-support.md, after counting found that a file titled "IT / Software Development / Cybersecurity" gave IT support zero of its nine sections; grouping fields by industry label rather than by shared tell is now warned against in the industries README. Adds domains/resume/nontraditional-evidence.md for bug bounty, CTF, CVE, open-source, and home-lab evidence, a claim class that is unusually verifiable and therefore both the strongest material on a page and the fastest to fail when overstated. v2.25 reviews lenses/model-tells.md, the file on the shortest cadence in this skill. Its central addition corrects a threshold elsewhere: em-dash frequency runs 0.0 per 1,000 words in the Llama family to 9.1 in GPT-4.1 under explicit suppression (Freeburg, arXiv 2603.27006), which makes it a fine-tuning signature and a family fingerprint rather than an AI tell, so no single threshold serves all families. Also records that vendor families separate at roughly 0.96 ROC-AUC while individual models within a family mostly do not, that GPT's vocabulary surface is weakening as a direct consequence of the vocabulary review, and that models prefer their own output when grading text. v2.26 splits domains/code.md into domains/code/, five files answering four different questions about the same artifact. The material that justified it did not exist when the original file was written: AI-generated code carries 2.7x the vulnerability density of human-written code with injection-class weaknesses alone at a third of confirmed findings (security.md); hallucinated package names recur across 43% of identical prompt runs, which is what made them predictable enough for attackers to register, turning a failed install into a working supply-chain attack (supply-chain.md); and iterating on AI code raises critical vulnerabilities 37.6% after five rounds, so asking a model to make its code more secure is not a control (agentic.md, arXiv 2506.11022). enforcement.md carries the structural layer, on the argument that review is slower than generation and therefore relaxes, while a failing gate does not. v2.27 splits domains/design.md into domains/design/ and closes the largest conceptual gap in the skill: patterns.md catalogued what to remove, and what you land on by removing all of it is clean, quiet, rounded minimalism, which is the current AI default rather than the escape from it. The 2025-26 neo-brutalist revival defines itself explicitly against that aesthetic, which is the evidence. The file now opens with that correction, the design counterpart to the voiceless-sterile-prose principle already in CORE PRINCIPLES. Adds motion.md and accessibility.md, both previously absent entirely, and expressive.md, which does for design what fiction.md does for prose: says most of this domain does not apply here and states what applies instead, bounded by the disciplined-versus-chaotic usability split. Also merges five anti-patterns the operator's own design corpus had researched and scoped for this file without ever shipping them. v2.28 ships the two round-2 research items that had never landed (Wh- rhetorical-question setups and the narrator-from-a-distance voice, both in core/structural-patterns.md) and adds the mechanism that should have caught them: scripts/self_check.py now flags any research/ doc proposing changes without a ## Ship Status ledger, and both existing research rounds are reconciled. The recurring failure this session was research-but-never-shipped, found three times by accident; the check makes it surface on every run.*
