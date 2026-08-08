# Structural Patterns — Durable Tells

These patterns persist across model families and versions. Wordlists expire; these don't. Weight them most heavily.

**Reviewed July 2026. Next review due January 2027** (half the vocabulary cadence, because the durable material moves slower). Review record at the end of this file.

**One correction from that review, and it matters for how you read this file.** The claim above holds for everything down to the Formatting Patterns section, and does not hold for the section itself. Structure is a property of how a model composes; formatting is a surface preference a vendor can change with one line of a system prompt, and in 2026 they did. Treat Formatting Patterns as a third tier, between structure and vocabulary in durability, and read the caveat at the top of that section before applying any of its thresholds.

**Why this holds up:** a 2025 stylometric study distinguishing human writing from seven LLMs, including Claude, using only function-word frequency, part-of-speech patterns, and phrase structure (no content vocabulary at all) hit 99.8% classification accuracy. Function words are used below conscious awareness and stay stable regardless of topic, which is exactly why they, and the structural patterns below, outlast any wordlist. The same study found most LLMs cluster together stylometrically: the gap is almost entirely human-vs-machine, not model-vs-model.

**A caution about the [D] tier in core/vocabulary.md's evidence grading:** an independent 2026 check cross-referenced a major commercial detector's public AI-vocabulary list against a 25-billion-word general web corpus, unaffiliated with the detector vendor, and found genuinely mixed results. Some listed words showed a clean post-2022 rise; others were already common well before ChatGPT existed; a few barely appeared at all. That detector's own documentation also confirms its model architecture, training data, and thresholds are proprietary and undocumented. Practical implication: single-vendor detector data is real signal, but it's one company's opaque, commercially-incentivized list. Weight it below independently corroborated [E]/[W]/[C] sources, and treat any core/vocabulary.md entry that's [D]-only with nothing else backing it as the most provisional tier of ban.

---

## THE ROOT CAUSE: SPECIFICITY ERASURE

AI smooths unusual specific details into generic probable descriptions, because generic is statistically safer. Every concrete particular replaced with an abstraction is a tell.

| AI output | What it replaced |
|---|---|
| "in recent years" | a specific year |
| "industry leaders" | a named person |
| "significant growth" | a number |
| "a revolutionary titan of industry" | "invented a train-coupling device" |
| "best practices" | the actual practice |
| "various stakeholders" | the named parties |
| "the data suggests" | "the 2024 Pew study found" |
| "many developers struggle with" | "I've copy-pasted from a migration guide, missed an edge case, and spent 2 hours debugging" |

**Revision rule:** For every generalization, supply the specific fact. If you cannot, acknowledge the uncertainty explicitly. Never substitute a vague authority for a real one.

---

## PARAGRAPH AND DOCUMENT-LEVEL PATTERNS

### The Symmetric Summary
AI conclusions mirror the introduction verbatim: "This article explores X, Y, and Z" → "In summary, we have explored X, Y, and Z." The last paragraph should say something the first paragraph could not have said. If your conclusion and introduction could be swapped without loss, the conclusion is AI.

### The Historical-Frame Opener
Given no specific voice to imitate, AI defaults to a broad "here's how things used to be" frame for any topic involving change: "For a long time, the safest bet was..." / "For most of the last fifty years, the deal was simple..." Confirmed independently across multiple current Claude-family models given the identical prompt, not a single model's individual habit. If the piece opens by zooming out to describe a bygone status quo before getting to the actual subject, that's the tell, regardless of which model wrote it. See lenses/model-tells.md for the comparative source.

### The Every-Paragraph-Resolves Pattern
Each AI paragraph makes a complete thought and closes it. Nothing is left hanging. Human paragraphs sometimes end mid-thought, create forward tension, or leave something for the next paragraph to resolve. If every paragraph is self-contained, that regularity is itself a signal.

### Paragraph Symmetry (Blocky Text)
AI produces uniform paragraph lengths that cluster around the same word count. Human paragraphs vary widely. If all paragraphs are the same size, break the symmetry deliberately.

### Challenges-Future Prospects Boilerplate
Auto-generated section: positive framing → "Despite this, [entity] faces challenges" (never named) → vague optimism → speculative "Future Prospects." Fix: name specific challenges, name specific responses, cut the optimism framing. See core/phrases.md for examples.

### Conjunctive "A and B" Headings
Section headings paired by conjunction, always title-cased: "History and Background," "Awards and Recognition," "Impact and Legacy," "Content and Features."

Replace with subheadings that describe specific content:
- Not "Background" → "Why the existing approach fails"
- Not "Results" → "Query time dropped from 847ms to 12ms"
- Not "Challenges and Future Prospects" → name the actual challenge in the heading

### Uniform Quotation Placement
AI places block quotes consistently at paragraph ends. Human writers embed quotes anywhere. If all evidence lands at the end of paragraphs, that placement pattern is itself a signal. Redistribute.

### Emotional Register Uniformity
AI describes failure, conflict, and tragedy in the same measured tone as success. The register does not modulate. Human writers slow down for weight: shorter sentences, simpler words, more space around hard things. If your prose sounds the same describing a company milestone and a mass casualty event, that is a tell.

---

## SENTENCE-LEVEL PATTERNS

### Sentence Length Standard Deviation
**The strongest single pattern in this file as of the July 2026 review.** Independent 2026 detection writing now names cadence uniformity as the top current tell, having demoted punctuation, which is this rule arrived at from the outside. It is also the pattern the em-dash rule was displaced by, so where the two disagree, this one wins.

Measure variance across sentence lengths in any 500-word sample.
- **SD < 5 words** = AI monotony. Every sentence the same length produces a lullaby.
- **SD > 10 words** = human variation.

**The clustering band, which is easier to check by hand than SD.** Model output clusters around 18–24 words per sentence and returns to that band repeatedly. Two hand-computable versions of the same observation:
- **Three or more consecutive sentences in the 17–23 word range** is the quick test. Human writing rarely holds that band three times running without a short sentence intervening.
- The band matters more than the average. A document can hit a healthy mean while every individual sentence sits inside the band, which is why the mean is not worth computing and the variance is.

Vary deliberately. Short. Then longer when the idea needs room. The variance signals a mind pacing itself against the content.

### Sentence-Opener Concentration
Added July 2026. Count how many sentences begin with "The," "This," "It," or "In." **More than half is a flag.** These four openers are where a model lands when it starts a sentence from the previous sentence's object rather than from a new thought, so the concentration measures something real rather than being a stylistic preference. Cheap to check and hard to game accidentally, since fixing it requires actually reordering what each sentence is about.

**The standard terms for what this section measures**, worth knowing because the detection literature uses them and this skill otherwise talks around them: *perplexity* is how predictable the next word is, and *burstiness* is variation in sentence length and structure. Low on both is the machine signature. Use the terms to read that literature, not as targets. The adversarial-stylometry caution below applies with full force here, since both are trivially gameable without touching the absence of a stance underneath.

### Readability as Register Match, Not a Fixed Band
There is no stable "AI readability band." Published Flesch Reading Ease scores for AI-generated text range from the low 20s to the high 70s depending on domain and study — one meta-analysis explicitly flags "large deviation" study to study. What *is* well-supported: AI defaults to a more complex, more formal register than the audience needs unless explicitly told to simplify. Patient-facing medical answers routinely come out at college-graduate reading level unprompted; in one dataset, AI-generated news headlines scored measurably harder to read (Flesch-Kincaid 12.78) than the real human-written equivalents in the same corpus (9.65). Run a readability formula (Flesch-Kincaid, Gunning Fog) and flag a **mismatch** between the computed grade level and the obvious intended reader — not a specific score in isolation.

### Sentence-Initial Subordinate Clause Saturation
"While X is important, Y must also be considered." / "Although A exists, B presents an alternative." Human writers distribute clause positions randomly. More than twice per page: reduce.

### Consecutive Sentence Similarity
Flag any two adjacent sentences with the same subject position, same clause structure, and same approximate length, regardless of whether individual sentences trigger other rules. This catches monotony that slips through word-level audits.

### Binary Contrast Drama
"It's not just about X — it's about Y." State Y. Drop the setup. Exception: acceptable when 2–3 sentences of expansion separate the negative and positive, and frequency is below one per 1,000 words.

Independently confirmed at the July 2026 review, where 2026 detection writing reports the "not just X, but Y" construction arriving at roughly one per paragraph in model output. That is an order of magnitude above the threshold above, which suggests the threshold is set correctly rather than conservatively.

### Rhetorical Question, Immediately Answered
"What does this mean for developers? It means..." / "So why does this matter? Because..." / "The result? A faster pipeline." A Wh- or yes/no question posed only to answer it in the next breath. The question is not a real question; it is a setup, and it is one of the most reliable AI structural tells because it manufactures the appearance of a thought-progression without the substance of one. State the answer directly and delete the question. A genuine rhetorical question is left hanging for the reader to sit with; this pattern never does, which is how you tell them apart. Related to Binary Contrast Drama above, the same manufactured-tension move in interrogative form.

### Narrator From a Distance
A voice-level pattern, and the name is the useful part rather than any new rule. AI defaults to a generalizing, omniscient remove, "across the industry, teams have found," "in the world of X, one thing is clear," reporting on a topic from above rather than from inside it. This is the voice-level expression of the skill's root principle (the absence of a writer) and of Specificity Erasure's generic subject. It earns a name because the fix is a single move applied to stance rather than to any one sentence: drop to a specific vantage. Who found this, where, when. If the prose could narrate any topic without changing its footing, it has no footing.

### False Agency / Subjectless Framing
AI gives inanimate things human verbs to avoid naming actual actors.

| AI default | Revision |
|---|---|
| "the data tells us" | "the 2024 Pew study found" |
| "the market rewards" | "buyers pay more for" |
| "technology enables" | "this library lets you" |
| "research shows" | "[Author] found" |
| "the findings indicate" | "we found" |

### Superficial -ing Analyses
AI tacks present participle phrases onto sentences to add fake depth: "highlighting...", "underscoring...", "emphasizing...", "reflecting...", "symbolizing...", "showcasing...", "contributing to...", "fostering..."

Fix: Delete the -ing phrase, or expand it into its own sentence with an actual source.

Before: "The temple's blue and gold hues resonate with the area's natural beauty, symbolizing the community's connection to the land."
After: "The temple uses blue and gold. The architects said the colors were intended to echo the local bluebonnets."

---

## COUNTING-BASED PATTERNS

### Rule of Three — Refined
AI defaults to exactly three items because three "sounds complete." **Only flag tricolons when the third item adds nothing or near-duplicates the first two.** "Life, liberty, and the pursuit of happiness" is not AI slop: the third item is substantively different. "Innovation, inspiration, and insights" is AI slop: "insights" is a near-synonym of "innovation" used only to complete the triad.

If the list naturally has two or four items, use two or four. The compulsive tripling is the tell.

### Tricolon Alliteration Detection
AI groups three items with similar sounds: "fast, efficient, and reliable" / "clear, concise, and compelling" / "robust, reliable, and resilient." Count your items. If three with alliteration, vary the number or break the sound pattern.

### List-to-Prose Ratio
Count bullet points vs. paragraph sentences across a document.
- **>60% bullets** = AI tendency, especially in technical docs
- **Emoji-led bullets** = strong AI signal in any non-casual context

If a list does not contain genuinely parallel, discrete items — write prose.

---

## CONTENT PATTERNS

### Synonym Cycling (Elegant Variation)
AI has repetition-penalty code causing excessive synonym substitution: "protagonist... main character... central figure... hero" all in one paragraph. Pick one term and stick with it. Repetition is fine when it's the clearest word.

### Hapax Legomena Ratio and Yule's K
Two hand-computable vocabulary-richness metrics beyond TTR. **Hapax legomena ratio** is the share of words used exactly once in a sample. Human writing runs higher; AI repeats at the tail even when overall TTR looks fine. **Yule's K** is a standard vocabulary-richness statistic, less sensitive to sample length than raw TTR. Use both alongside TTR, not instead of it: a low hapax ratio is often the more visible flag when TTR alone looks acceptable.

Caution: these are diagnostics, not optimization targets. Prompting a model to "use more varied vocabulary" moves the number without fixing the underlying absence of a stance. Adversarial-stylometry research documents this exact gaming pattern directly. A rewrite that hits every quantified threshold in this file but still has no real claim behind it is still slop.

### False Ranges
"From X to Y" constructions where X and Y are not on a meaningful scale.

Before: "Our journey has taken us from the Big Bang to the grand cosmic web, from the birth of stars to the dance of dark matter."
After: "The book covers the Big Bang, star formation, and current theories about dark matter."

### Notability Citation Sections
AI creates sections listing media appearances as structured breakdowns: "Featured in: Rolling Stone (2022), Pitchfork (2023), NME (2024)." Replace by weaving coverage into context, or cut.

Before: "Her views were quoted in The New York Times, BBC, and The Financial Times."
After: "In a 2024 NYT interview, she argued that AI regulation should focus on outcomes rather than methods."

### AI Talks About Topics Without Inhabiting Them
AI describes what examples "might include" without providing them: "This could encompass everything from [vague A] to [vague B]." Human writers provide specific, idiosyncratic examples. The vague "could encompass" framing is the tell.

### Significance Inflation
Ordinary events marked as pivotal, groundbreaking, transformative. Describe what actually happened. Let the reader judge significance.

### Formulaic Challenge-Triumph Arc
Ordinary setbacks presented as Adversity Overcome, then vague optimism. Replace with what the challenge actually was, who it affected, what actually happened.

### Over-Attribution in Body Text
AI names sources in every sentence when a footnote would suffice: "According to the 2024 report by McKinsey Global Institute, which was published in October of last year, the findings indicate..." Human writers typically just cite. If attribution phrases are longer than the claims they support, revise.

### Promotional Language
"nestled within the breathtaking region" → "is a town in the Gonder region." Describe; don't promote. The tell is when neutral description is replaced by tourism-brochure framing.

---

## FORMATTING PATTERNS

**The decaying tier. Read this before using the thresholds below.** Everything above this line describes how a model composes. This section describes what it prefers on the surface, which is a different kind of fact: a vendor can suppress any of it with one instruction, and during 2025–2026 they started to. OpenAI told GPT-5.1 to use fewer em dashes; the trend is reported as downward across the major models, with Claude and Gemini still using them more than GPT. A signal that can be switched off by a system-prompt line is not durable, whatever it measured last year. Keep fixing these, since they are still bad formatting, but weight them nearer to core/vocabulary.md than to the structural patterns above, and never let one carry an authorship judgment alone.

### Em Dash Overuse
Counted **over flowing prose only**, not over the whole document. See the denominator note below, which is the correction most likely to change your result.

- 0–2 per 1,000 words: normal human range
- 3–5 per 1,000 words: elevated, review
- **6+ per 1,000 words: elevated enough to look, no longer sufficient to conclude**

When you find an em dash: use comma, semicolon, colon, parentheses, or a new sentence. Recasting is often better than substitution.

**The denominator correction.** Reference-list labels, table cells, and headings use the `- **Term** — definition` construction as an ordinary documentation convention, and counting those against a whole-document word count inflates the rate badly. Measured directly while auditing a 225-file corpus with this skill in July 2026: raw counting flagged 130 files, and restricting the count to flowing-prose lines, numerator and denominator both, dropped that to 96. In the single worst-scoring file, 66 of 79 em dashes were structural labels. Adding a floor of six prose em dashes to suppress short-document noise took the final figure to 52. Roughly 60 percent of a naive em-dash flag list was an artifact of the measurement rather than a property of the writing.

**The base-rate problem.** Em-dash frequency varies more between human writer populations than it does between human and machine: essayists and newsletter writers use them heavily, while writers trained in AP style avoid them almost entirely. A high rate is therefore weak evidence about authorship and stronger evidence about which house style someone learned. This is the same caution this skill applies to detector output, arriving at a punctuation mark.

**The threshold above is not model-agnostic, and this is the larger correction.** Measured across twelve models from five providers, em-dash rates run from 0.0 per 1,000 words in the Llama family to 9.1 in GPT-4.1 *under explicit instruction to suppress them*. One family clears this section's threshold while actively trying not to; another never approaches it. Em-dash frequency is therefore a signature of a specific fine-tuning procedure rather than a property of machine writing, which makes it a family fingerprint that belongs primarily to lenses/model-tells.md. Read that file's em-dash section before letting a count here carry any authorship judgment. The number above remains useful for the thing this skill actually does, which is deciding whether prose has too many em dashes.

### Bold Overuse
AI emphasizes phrases in boldface mechanically, especially in lists. Remove most boldface. Save it for genuinely important terms on first mention.

### Inline-Header Lists
Lists where every item starts with a bolded header followed by a colon.

Before: "User Experience: Improved. Performance: Enhanced. Security: Strengthened."
After: "The update improves the interface, speeds up load times, and adds end-to-end encryption."

### Title Case in Headings
Sentence case. "Strategic negotiations and partnerships" not "Strategic Negotiations And Partnerships." Note: only a tell when stacked with other AI patterns. Title case alone is weak.

### Template Structure Cloning
README: Introduction → Features → Installation → Usage → Contributing → License, every AI README has exactly this structure. Break it deliberately. Lead with the thing that would make a developer stop scrolling.

### Curly Quotes
Only a tell in plain-text or code contexts. In formatted content (Word, Google Docs, Markdown renderers), curly quotes are typographically correct. Don't flag in formatted content.

---

## July 2026 Review Record

The first review of this file. It was written on the claim that structural patterns are durable, so the review's job was to test that claim rather than to collect additions.

**The claim held, and got a stronger form.** Nothing in the structural sections has decayed. The sentence-cadence rule did the opposite: 2026 detection writing now reports cadence uniformity as the single strongest current tell, having demoted punctuation to a weak signal. That is independent convergence on a rule this file already had, arrived at by people not working from it.

**The exception is Formatting Patterns, which does not belong under "durable" and is now marked as its own tier.** Em-dash frequency decayed the same way `delve` did and for a related reason: vendors suppressed it deliberately, with GPT-5.1 instructed to use fewer. The generalizable distinction, worth carrying into future reviews: structure is a property of how a model composes and is expensive to change, formatting is a surface preference and is one system-prompt line away from disappearing. Anything in this skill that a vendor could switch off next quarter belongs in the decaying tier by definition.

**Corrected the em-dash rule's denominator from our own measurement.** Auditing a 225-file corpus with this skill in July 2026 showed that roughly 60% of a naive em-dash flag list was measurement artifact: the `- **Term** — definition` convention is not prose, and counting it as prose inflates the rate. The threshold is unchanged; what changed is what you divide by, and the base-rate caution that a high count says more about which house style a writer learned than about whether a machine wrote it. Recorded because it is first-party evidence rather than a citation.

**Added:** Sentence-Opener Concentration (The/This/It/In above 50%), the 17–23 word consecutive-sentence test as a hand-checkable form of the SD rule, and the perplexity/burstiness vocabulary so this file connects to the outside literature.

**Confirmed without change:** Binary Contrast Drama, whose threshold turns out to sit an order of magnitude below the observed rate. Specificity Erasure, Rule of Three, False Agency, and the rest of the structural material were not challenged by anything found this round.

---

## Sources

July 2026 review sources: 2026 detection-methodology writing on cadence uniformity displacing punctuation as the primary tell, the 18–24 word clustering band, the 17–23 word consecutive-sentence test, the sentence-opener concentration test, and GPT-5.1's em-dash suppression (Duey AI, *The Em-Dash Myth*, and corroborating 2026 coverage including How-To Geek). Perplexity and burstiness definitions are standard across the detection literature rather than sourced to one page. Human em-dash base-rate variation between essayist and AP-trained populations is reported consistently across that same coverage. The denominator correction and its figures (130 files raw, 96 prose-only, 52 after a six-dash floor, 66 of 79 structural in the worst file) are this skill's own measurement against a 225-file corpus, not a citation.

Stylometric grounding: a 2025 study comparing 7 LLMs (including Claude) against human text via function words, POS bigrams, and phrase patterns (99.8% RF classification accuracy). Detector-reliability caution: independent 2026 corpus cross-check against a major commercial detector's public word list. Readability-band correction: multiple 2025–2026 Flesch-Kincaid/ChatGPT studies across medical, news-headline, and cross-chatbot domains (see research/Hogwash_research_2.md for the full citation list). Adversarial-stylometry caution: a December 2025 paper on gaming TTR and function-word metrics directly. Remaining patterns (Rule of Three, Paragraph Symmetry, False Agency, and the rest) are part of the original v2.2 skill; see SKILL.md's frontmatter for that broader source list.
