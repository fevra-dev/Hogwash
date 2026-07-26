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

---

## GPT / ChatGPT Family

### Primary surface: vocabulary

Generic AI detectors report accuracy above 96% on ChatGPT text specifically, well above their accuracy on Claude or Gemini output, largely because vocabulary-level tells are what most detectors were built and trained to catch first, and GPT provides the clearest version of them.

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

## Review Cadence

Monthly, not quarterly. Treat every line under "Current specifics" as provisional and check it against something dated within the last month before using it to make a real judgment call. The three-surface distinction at the top is the part expected to hold up longer; individual examples under each family are the part that won't.

---

## Sources

Pangram Labs (Sonnet 5 detection testing), Noren (Fable 5 / Sonnet / Opus comparative writing test), QuillBotAI Pro (Claude detection patterns and hedging-style analysis), HumanizeThisAI (cross-family detection-surface comparison and detection-rate data), AI/ML API Blog and Fluent Support (GPT vs. Gemini default-style comparisons). All dated March–July 2026; several reference model versions that will already be out of date by the time this file is next reviewed.
