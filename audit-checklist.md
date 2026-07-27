# Audit Checklist — Full Self-Audit

Run after the first draft. This is the writer pass. If doing a review pass, produce a verdict and hand changes back to a separate writer pass. Do not write and self-approve in the same step.

**Pattern stacking note:** When multiple signals converge on the same phrase, flag it once as a stacking pattern. Do not pad the count with separate entries for each signal.

**Fix-order note:** If time-constrained, run Pass 0 and Pass 3 (structure) before Pass 1 and Pass 5 (vocabulary and punctuation). A piece with a real, specific, falsifiable claim behind it barely reads as AI even with a stray tell left in. A piece with every banned word and em dash removed still reads as AI with no real claim behind it. Metrics diagnose; they aren't targets. Hitting a sentence-length SD or TTR number by mechanical substitution, without fixing the underlying absence of a stance, doesn't remove the tell. It just moves the number.

**Resume note:** if the content is a resume or CV, stop and use domains/resume/patterns.md's own scoring rubric instead of the passes below. Most of what follows assumes paragraphs and sentences; a resume has neither. Two of that rubric's five dimensions are scored from their own files: Parseability from domains/resume/ats.md, and Verifiability from domains/resume/fabrication.md, which is mandatory when rewriting an existing resume rather than writing one.

---

## PASS 0 — POSITIVE PRINCIPLES CHECK

Before auditing for bans, verify the writing is working toward something.

- [ ] Is there an opinion? Can you point to a specific claim the author holds?
- [ ] Are the specifics present? Names, dates, numbers, places where abstractions currently live?
- [ ] Are limitations named honestly? What it doesn't do, what edge cases fail, what versions it requires?
- [ ] Are subheadings statements, not labels? "Why the existing approach fails" not "Background"?
- [ ] Does the tone modulate when the content changes weight?
- [ ] Is there deliberate rhythm variation: short sentences alongside long ones?

---

## PASS 1 — VOCABULARY

- [ ] Find every word from the Tier 1 ban list (core/vocabulary.md). Replace or cut.
- [ ] Find every Tier 2 word. Are two or more in the same paragraph? Revise.
- [ ] Find any Expiration Watch words. Still flag at Tier 2.
- [ ] Check for copula avoidance clustering: does the piece rotate through "serves as / stands as / represents / functions as" while avoiding "is"?
- [ ] Check TTR: does the same concept cycle through 4+ different words in one paragraph? Pick the clearest and repeat it.

---

## PASS 2 — PHRASES AND OPENERS

- [ ] Find every throat-clearing opener (core/phrases.md). Delete. Start with the content.
- [ ] Find every sycophantic opener. Delete. Respond directly.
- [ ] Find every chatbot artifact. Delete entirely.
- [ ] Find every emphasis crutch: "That's it. That's the [noun]." / "The best part?" / "And here's the kicker" / "Enter: [thing]." Delete.
- [ ] Find every knowledge disclaimer: "based on available information" / "tends to" / "it appears to suggest." Delete or replace with real source.
- [ ] Find every golden sentence, quotable aphorism. Rewrite.
- [ ] Find every banned sentence opener (Moreover, Furthermore, Additionally, etc.). Restructure.
- [ ] Count "However." More than one per 500 words is a tell.
- [ ] Find vague attribution: "experts believe / studies show / research suggests." Name source and year or cut.
- [ ] Find generic conclusions. Replace with specific fact, plan, or position.

---

## PASS 3 — STRUCTURE

- [ ] Read aloud. Where do you stumble? That sentence needs rewriting.
- [ ] Find the conclusion paragraph. Does it advance the argument or restate the introduction? If it mirrors the intro, it is AI. Advance it.
- [ ] Find every heading. Are any paired nouns joined by "and"? Rewrite to describe specific content.
- [ ] Count enumerated items. Are all lists exactly three? If yes, check whether the third item earns its place. Add or remove as content requires.
- [ ] Measure sentence length variance (rough estimate). Do sentences cluster at the same length? If so, vary deliberately.
- [ ] Check consecutive sentence pairs. Any two adjacent sentences with the same subject position, clause structure, and length? Rewrite one.
- [ ] Count bullet percentage. Above 60% of content in bullets? Convert some to prose.
- [ ] Check for tricolon alliteration: "fast, efficient, and reliable." Break the pattern.
- [ ] Find the "challenges" section. If it follows the Challenges-Triumph boilerplate formula, replace with specific named facts.
- [ ] Find all block quotes. Are they all at paragraph ends? Redistribute.
- [ ] Check paragraph lengths. Are they all the same size? Break the symmetry.
- [ ] Check for superficial -ing analyses appended to sentences: "highlighting...", "reflecting...", "symbolizing..." Delete or expand into a real sentence.

---

## PASS 4 — SPECIFICITY

- [ ] Find every "in recent years." Replace with a specific year.
- [ ] Find every "various" / "many" / "often" / "typically" / "generally." Replace with the actual fact or cut.
- [ ] Find every "aims to / is designed to / seeks to." State what the thing does.
- [ ] Find every "appears to suggest / tends to / based on available information." Replace with a real claim or honest uncertainty.
- [ ] Find every place false agency hides the actor: "the data tells us / the market rewards / technology enables." Name who does the thing.
- [ ] Run the Company Test: "Could this sentence appear in any other company's blog?" If yes, make it specific.

---

## PASS 5 — PUNCTUATION AND FORMATTING

- [ ] Count em dashes. More than 6 per 1,000 words? Delete until below threshold.
- [ ] Find every exclamation point beyond the first. Delete.
- [ ] Find any emoji used as bullets or section decoration. Remove.
- [ ] Find inline-header lists (bolded term: description, bolded term: description). Rewrite as prose.
- [ ] Find markdown in plain-text output. Remove.
- [ ] Check heading case. Sentence case throughout (unless style guide requires otherwise, and verify it's consistent).

---

## PASS 6 — CODE (load domains/code.md for full detail)

- [ ] Any `pass` with a comment? Implement or remove.
- [ ] Any bare `except`? Catch specific exceptions.
- [ ] Any mutable default arguments? Fix.
- [ ] Any cross-language syntax leakage? Fix.
- [ ] Any generic variable names (`data`, `result`, `temp`, `item`)? Name for content.
- [ ] Any `@ts-ignore` without explanation? Document or fix the underlying type issue.
- [ ] Any `console.log` / `print()` in non-debug code? Remove.
- [ ] Any commented-out code blocks? Remove or open a ticket.
- [ ] Any hallucinated imports? Verify every package exists.
- [ ] Tests: do they test behavior, or just that mocking works?

---

## FINAL DIAGNOSTIC TESTS

- [ ] **Distinctiveness Test:** "Would a reader immediately identify this as AI-generated?" Find the sentence that gives it away first. Fix it. Repeat until no.
- [ ] **Specificity Test:** "What specific fact (name, date, number) has AI replaced with a generic?" Supply it.
- [ ] **Cluster Test:** Three Tier 1 words in any 100-word window? That window needs a full rewrite.
- [ ] **Read-Aloud Test:** Read it out loud. Flag anything that no human would say in conversation, makes you cringe slightly, or feels like it's trying too hard.
- [ ] **Golden Sentence Test:** Any sentence that sounds designed to be screenshot and shared? Rewrite it.

---

## SCORING RUBRIC

Rate 1–10 per dimension. Below 35/50: revise before shipping.

| Dimension | Question | Score |
|---|---|---|
| **Directness** | Statements or announcements? Statements score higher. | /10 |
| **Rhythm** | Varied or metronomic? SD > 5 words scores higher. | /10 |
| **Trust** | Respects reader intelligence, or over-explains? | /10 |
| **Authenticity** | Sounds like a person or a demo of a writing assistant? | /10 |
| **Density** | Anything cuttable? Less cuttable = higher. | /10 |
| **Total** | | /50 |

**Standards:**
- 45–50: Clean. Ship it.
- 35–44: Good. Specific revision needed: identify the lowest-scoring dimension and target it.
- Below 35: Revise. Do not ship.

**Before calling it done:** check the rewrite itself for a new failure, not the one you started with. A high Rhythm score achieved by smoothing everything into even, tidy, "sounds more human now" prose is still uniform, just flattened toward a different target than the AI default. Real unevenness should survive the edit: a short line that stays short, one long sentence left alone because that's genuinely how the point ran on. If every sentence in the revision is now roughly the same comfortable length, the rewrite may have replaced one flatness with another.

---

## CHANGES TABLE FORMAT

When rewriting, append a changes table:

| Pass | What changed | Examples |
|---|---|---|
| Structure | Collapsed parallel lists into prose | Sections 2, 4 |
| Inflation | Cut significance puffery | "pivotal moment" → deleted |
| Vocabulary | Cut "navigating" (×3), "journey" (×2) | → "deal with," "transition" |
| Grammar | Fixed copula avoidance clustering | "serves as" → "is" |
| Rhythm | Added short punchy lines, varied length | "Full stop." "That changes the math." |
| Hedging | Removed 3 filler starters, vague attributions | "It's worth noting..." deleted |
| Transitions | Replaced 2 generic connectors | "Moreover" → dropped |
| Voice | Added first-person, lived-in details | "we tried this. It broke." |

Only include rows where changes were actually made. Keep it tight. If it needs more than 8 rows, you may have changed too much or are over-explaining.
