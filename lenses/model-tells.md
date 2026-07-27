# Model Tells — Vocabulary vs. Structure vs. Framing by Family

## Why This File Works Differently From the Rest of This Skill

Everything else here is built to be durable. This file can't be, not fully. Which model is current changes on a timescale of weeks, not the quarterly cycle core/vocabulary.md already runs on. In a single research pass in July 2026, four different "current" GPT labels turned up across sources dated weeks apart, and a Gemini update was already rumored on top of the latest shipped version.

The fix is to split this file into two tiers. The **primary surface** for each family (vocabulary, structure, or framing, see below) is the part with some claim to durability, it held up across a comparative source testing multiple models directly. The **current specifics** under each family are a July 2026 snapshot and should be treated as provisional. Re-verify before leaning on them, and expect to revisit this file monthly, not quarterly.

This file is supplementary, not part of the core audit. core/structural-patterns.md's durable, model-agnostic patterns are still the main tool for making writing better regardless of which model touched it. Load this file only when the question is specifically "what does this model tend to do" or "which model likely wrote this."

---

## The Core Finding

Three families, three different primary detection surfaces. Not the same tell wearing different clothes, genuinely different mechanisms:

| Family | Primary surface | What that means in practice |
|---|---|---|
| GPT / ChatGPT | Vocabulary | Caught on word choice. The classic wordlist tells (delve, in today's world) are disproportionately a GPT signature. |
| Gemini | Structure | Caught on organization. Rigid, heavily nested hierarchy, even when individual sentences read fine on their own. |
| Claude | Framing | Caught on how uncertainty gets integrated, not whether it appears. |

If the model is known, check that family's surface first. If it isn't, the surface itself is a diagnostic: heavy nesting with clean sentences points one direction, generic vocabulary with a flat structure points another.

### Families are separable; individual models mostly are not

Strengthened at the July 2026 review. Vendor identity is recoverable from prose style alone at roughly 0.96 ROC-AUC between the OpenAI and Anthropic families. Asked to name the exact model rather than the vendor, a classifier reaches about 50% against a 20% chance baseline, and the errors are the informative part: models get confused with their own siblings and almost never across families. The families form tight stylistic blocks.

Practical reading: "which vendor" is a question worth asking of a document, and "which specific model" mostly is not. Set expectations accordingly before spending effort on the latter.

This does not contradict the stylometric finding in core/structural-patterns.md that most LLMs cluster together against human writing. Both hold. The human-to-machine gap is the large one; vendor-to-vendor is a smaller but learnable structure inside the machine cluster. Only the first is worth acting on when the question is whether a person wrote something.

---

## Em Dash Is a Family Fingerprint, Not an AI Tell

The most useful finding of the July 2026 review, and it corrects a threshold used elsewhere in this skill.

Em dashes appear to be markdown leaking into prose: the smallest structural artifact of markdown-saturated training data, surviving after headers, bullets, and bold have been suppressed. Measured across twelve models from five providers (Freeburg, arXiv 2603.27006, March 2026), the per-family spread is not subtle:

| Model | Em dashes per 1,000 words |
|---|---|
| Llama family | 0.0 |
| GPT-4.1, *under explicit suppression* | 9.1 |
| Anthropic, Google, DeepSeek families | intermediate |

A model instructed not to use em dashes still produced them at above this skill's own 6-per-1,000 threshold, while another family produced none at all without being asked. That makes em-dash frequency a signature of the fine-tuning procedure rather than a property of machine writing, which is why a separate 2026 analysis titles its result "the em dash is a Claude tell, not an AI tell."

Two consequences worth carrying:

**A single universal em-dash threshold is wrong, and core/structural-patterns.md's version should be read with this file open.** A document at 4 per 1,000 is unremarkable for one family and near-impossible for another. The count alone cannot support an authorship judgment without knowing which family is in question, which is usually the thing being asked.

**Suppression resistance is itself the signal.** Frequency is a tuned lever, publicly acknowledged as such by OpenAI's own leadership, and the reduction across the GPT-4.1-to-5.4 line tracks RLHF changes rather than anything about the underlying capability. What survives explicit instruction not to do it is more diagnostic than what appears by default, because the default can be changed in an afternoon and the residue cannot.

---

## GPT / ChatGPT Family

### Primary surface: vocabulary

Generic AI detectors report accuracy above 96% on ChatGPT text specifically, well above their accuracy on Claude or Gemini output, largely because vocabulary-level tells are what most detectors were built and trained to catch first, and GPT provides the clearest version of them.

**This surface is weakening, and the July 2026 vocabulary review is why.** The classic wordlist tells are disproportionately a GPT signature, and that wordlist is exactly the material that decayed: Wikipedia's practitioner cohorts shrank from 19 words in 2023–mid-2024 to four from mid-2025 onward, with `delve` dropping off sharply during 2025. A family whose primary detection surface is vocabulary loses more than the other two families when vocabulary stops working. Expect GPT text to become harder to identify on this surface specifically, and shift weight toward structure and the em-dash residue above. The three-surface model still holds; the surfaces are not equally durable.

### Current specifics, July 2026, re-verify before relying on this

Default prose tends toward tighter, more conventionally polished business writing than Gemini's more utilitarian default. In a same-prompt email test across all three families, ChatGPT's version opened with a general well-being check before getting to the actual request, the "I hope this email finds you well" tendency already in core/phrases.md, confirmed here as a comparatively GPT-specific default rather than a universal one.

---

## Gemini Family

### Primary surface: structure

A comparative source's framing, worth keeping close to verbatim because it's precise: where GPT gets caught on vocabulary, Gemini gets caught on organizational patterns. Detectors increasingly flag rigid, list-heavy, deeply nested hierarchical content even when the sentence-level writing sounds human. The tell isn't in any one sentence. It's in the shape of the whole document.

### Current specifics, July 2026, re-verify before relying on this

Default register reads as more direct and functional than conversational, matter-of-fact rather than warm. Good fit for structured summaries and factual synthesis; the same directness reads as flat or robotic in anything meant to sound like one person talking to another.

---

## Claude Family

### Primary surface: framing, specifically how hedges get integrated

GPT's default hedge pattern states a conclusion, then adds a caveat afterward. Claude's default hedge weaves the uncertainty into the initial framing itself, something closer to "while this is the general view, there are meaningful dissenting positions," rather than a flat claim followed by a footnote. Same underlying caution, structurally different move, and specific enough to function as a fingerprint independent of any particular word choice.

### Current specifics, July 2026, re-verify before relying on this

Sentence-length variance runs higher than GPT's by default, closer to natural human burstiness, which is part of why generic detectors historically underperformed on Claude text relative to GPT text. Worth the same caution the source itself gives: this reflects both writing style and how much training data detector vendors have accumulated on each family, and the gap has been closing as Claude's usage grows.

One structural pattern, not vocabulary, confirmed across current Claude-family models directly: given no voice to imitate, multiple current models independently reached for a historical-frame opener on a "change is coming" topic, "for a long time, the safest bet was..." "for most of the last fifty years, the deal was..." Different models, nearly the same move. Worth adding to core/structural-patterns.md's default-pattern list, not just here, since it showed up model-to-model rather than being one model's individual quirk.

### On self-report

This section describes patterns found in external comparative testing, not a self-report. A model cannot reliably introspect on its own statistical tendencies, and this file doesn't treat any Claude output, including this one, as evidence about itself.

---

## Models Prefer Their Own Output

A cross-family property rather than any one family's tell, and the one item in this file with direct consequences for a real decision.

Asked to evaluate text, models favor output from their own family. Measured across 24 occupations in a hiring context (Xu, Li, and Jiang, arXiv 2509.00462, final version June 2026), LLM evaluators preferred LLM-written material over human-written material 67 to 82 percent of the time, and candidates whose documents came from the same model the evaluator ran were 23 to 60 percent more likely to advance than equally qualified people who wrote their own. The paper reports the bias falling by more than half under simple interventions targeting self-recognition.

Two things follow for anyone using this file:

**Any pipeline where a model grades text has a thumb on the scale toward its own family.** That includes automated screening, LLM-judge evaluations, and this skill applied by a model to its own output. domains/resume/patterns.md works through the hiring case in full.

**It sharpens the self-report caution below.** A model's preference for its own output is measurable, and its introspective account of that preference is not evidence about it.

---

## Review Cadence

Monthly, not quarterly. Treat every line under "Current specifics" as provisional and check it against something dated within the last month before using it to make a real judgment call. The three-surface distinction at the top is the part expected to hold up longer; individual examples under each family are the part that won't.

**Version currency, checked July 2026:** the GPT line has moved past the labels used in this file's original sources, with 5.1, 5.3-Codex, 5.4, and 5.5 all documented. This is the churn the file warns about, arriving on schedule. Nothing in the durable tier depends on a version number, which is the reason the tier split exists; every specific below one does.

## July 2026 Review Record

Second pass, one month after the file was written. What changed:

- **Added the em-dash family-fingerprint finding**, which is the strongest material to arrive since the file was created and corrects a threshold in core/structural-patterns.md. Em-dash frequency spans 0.0 to 9.1 per 1,000 words across families, so no single threshold serves all of them.
- **Strengthened the core finding** with the vendor-separability result: families form tight blocks at roughly 0.96 ROC-AUC, individual models within a family mostly do not separate. Recorded why this does not conflict with the human-versus-machine clustering result in core/structural-patterns.md.
- **Flagged GPT's primary surface as weakening**, which follows directly from the vocabulary review rather than from any new source about GPT. A family caught on vocabulary loses the most when the wordlist decays.
- **Added the self-preference finding** as a cross-family property. It was already in the resume domain and belonged here too, since it is a fact about model families rather than about hiring.
- **No change to the three-surface model**, which held up across everything found this round.

---

## Sources

Pangram Labs (Sonnet 5 detection testing), Noren (Fable 5 / Sonnet / Opus comparative writing test), QuillBotAI Pro (Claude detection patterns and hedging-style analysis), HumanizeThisAI (cross-family detection-surface comparison and detection-rate data), AI/ML API Blog and Fluent Support (GPT vs. Gemini default-style comparisons). All dated March–July 2026; several reference model versions that will already be out of date by the time this file is next reviewed.

Added at the July 2026 review: E. M. Freeburg, *The Last Fingerprint: How Markdown Training Shapes LLM Prose*, arXiv 2603.27006, March 2026, for the twelve-model five-provider em-dash measurement, the markdown-residue explanation, and the fine-tuning-signature framing. *Every Model Has an Accent* (2026) for vendor separability at 0.96 ROC-AUC, the roughly 50%-against-20% exact-model result, the within-family confusion pattern, and the em-dash-as-family-tell conclusion, which corroborates Freeburg independently. Xu, Li, and Jiang, arXiv 2509.00462, final version June 2026, for self-preference, cited in full in domains/resume/patterns.md. Public acknowledgment that em-dash frequency is a deliberately tuned parameter comes from OpenAI leadership statements reported across 2026 coverage rather than from a paper. The observation that GPT's vocabulary surface is weakening is this file's own inference from core/vocabulary.md's July 2026 review, not a claim any source makes.
