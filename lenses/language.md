# Language Notes — Scope and Cross-Lingual Adaptation

Every other file in this skill assumes English rhetorical norms. Two kinds of rules don't travel to other languages automatically.

---

## Grammar-Dependent Rules

False Agency (core/structural-patterns.md) requires a language where inanimate subjects performing human actions is marked or unusual: "the data suggests," "culture is cultivated." In Japanese, and likely other languages with flexible word order, this is ordinary grammar, not an AI habit. A direct port produces false positives on completely normal sentences.

Before applying any rule keyed to subject position, sentence-initial clause structure, or word order, check whether the target language actually marks that structure as unusual. If it doesn't, the rule doesn't transfer. Drop it rather than force it.

---

## Genre-Convention Rules

Pass 0 principle #10 (subheadings as scannable statements: "Why the existing approach fails" over "Background") is a positive principle in English blog and technical writing. In Japanese, a claim-shaped heading ("The product dies the moment it loses whitespace") reads as an imported, performative convention. Japanese practitioners flag it as an AI tell, not a fix.

Neither position is wrong. English readers reward an assertive heading as engaged and human; Japanese readers read the same move as foreign and try-hard. Verify genre-level positive principles against the target language's own writing culture, not just its grammar, before carrying them over.

---

## What Travels Without Modification

Independently confirmed in Japanese, arrived at by a separate author without reference to this skill:

- Rule of Three ("3つの観点から" / "from three angles")
- Negative parallelism ("AではなくB" / "not A, but B")
- Paragraph-length, tone, and conclusion uniformity
- Significance inflation: a small personal observation ballooning straight up to "truth," "realm," "essence" (境地, a near-exact cognate of the English "realm" tell)

Treat these as genuinely universal, cross-model and cross-language, until shown otherwise. They're also the reason this skill weights structural patterns over vocabulary in the first place.

---

## Fix Order Matters More Than Fix List

This is the one finding worth carrying into every language variant, English included: audit stance and structure before vocabulary and punctuation. A piece with a real, specific, falsifiable claim behind it barely reads as AI even with a stray tell left in. A piece with every banned word and symbol removed still reads as AI if there's no actual claim being made. Root cause, independently named by the Japanese source: AI smell is the absence of a writer. No visible edge where a specific person could be wrong.

If time is short in any language, spend it on stance and structure first. Vocabulary and symbol cleanup are the last pass, not the first.

---

## Worked Example: Japanese

Source: iKora128/stop-ai-slop-jp, ported from hardikpandya/stop-slop, June 2026. Credited by its author to a companion analysis by Daichi Nagashima (GENSHI AI).

**Vocabulary tier** (functions like this skill's Tier 1 metaphorical bans):
手触り (tactile feel, used metaphorically) · 解像度 (resolution, functions like English "nuanced" or "granular") · 泥臭さ (grittiness, meaning "hands-on") · 禁欲的 (ascetic, metaphorical) · 境地 (realm/state) · imported katakana metaphors ("update your thinking OS")

**Symbol tier:**
全角ダッシュ (full-width dash, Japanese's own em-dash-equivalent import, same threshold logic as this skill's em-dash rule) · unnecessary 「」 corner-bracket quotation marks · literal unrendered `**` left in output

**Scoring axes** (their five-axis/50-point rubric, same shape as this skill's Directness/Rhythm/Trust/Authenticity/Density but re-derived for Japanese):
立場 Position: is there a falsifiable, concrete claim? · リズム Rhythm: is there unevenness in length, tone, conclusion? · 主体性 Agency: is it clear who did what? · 具体性 Specificity: does it descend into specific context, or end in abstraction? · 削減 Reduction: is there anything cuttable?

The near-exact structural match to this skill's own rubric, arrived at independently, is itself evidence that the five-axis model is measuring something real rather than an artifact of one skill's design choices.

---

## Extending to a New Language

1. Test whether English's grammar-dependent rules (false agency, sentence-initial subordinate-clause saturation) are actually marked usage in the target language, or just normal grammar. If normal, drop the rule for that language.
2. Test whether English's genre-level positive principles (claim-shaped headings, first-person presence, direct address) read as human or as performed/foreign in the target language's own writing culture. Don't assume the English answer transfers.
3. Keep the structural and rhetorical patterns that have now held up across two languages: Rule of Three, negative parallelism, register/tone/conclusion uniformity, significance inflation. Default to treating these as universal.
4. Build the vocabulary tier from scratch per language. It will not transfer from English, and importing it wholesale will produce false positives on normal usage.
5. Watch for the language's own imported punctuation and formatting artifacts. The full-width dash in Japanese is the direct analog of the em dash in English, likely because both come from the same training-data habit leaking into a language where it isn't native.

---

## Sources

iKora128/stop-ai-slop-jp, ported from hardikpandya/stop-slop, June 2026, credited by its author to a companion analysis by Daichi Nagashima (GENSHI AI). GPTZero's AI Vocabulary tool's multilingual expansion (Arabic, Italian, Korean, Chinese, Japanese added October 2025; Turkish, Hindi, Dutch, Vietnamese, Indonesian by July 2026) is cited in research/Hogwash_research_2.md as corroborating evidence that this is an active, industry-wide area, not covered here directly.
