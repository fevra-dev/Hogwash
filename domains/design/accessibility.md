# Accessibility — Where AI Design Fails People

Part of domains/design/. Load alongside patterns.md for anything that ships to users. New in August 2026; accessibility had no coverage in this skill before.

**Why this is a separate file from patterns.md.** That file asks whether a design looks generic. This one asks whether it excludes someone, and the two do not correlate. A visually distinctive, well-composed interface can fail contrast, keyboard access, and motion sensitivity at once, and nothing in an aesthetic pass surfaces any of it. Same division this skill keeps between domains/code/patterns.md and domains/code/security.md: reading for slop and reading for failure are different passes.

**Scope note.** This locates the failures AI-generated design produces characteristically, so a review knows where to look first. It is not an accessibility audit, and no reading-level heuristic substitutes for testing with a screen reader, a keyboard, and real contrast measurement.

## The Floor

WCAG 2.2 is the operative W3C Recommendation, finalized October 2023 and adopted as ISO/IEC 40500 in October 2025. Not 2.1, and not WCAG 3.0, which remains a Working Draft not expected to be final before 2028–2030 and is not worth building against yet.

Its four principles are **POUR**: Perceivable, Operable, Understandable, Robust. Conformance runs A / AA / AAA, each backward-compatible with the one below.

**Level AA is the target**, and this is a legal floor rather than a preference in most jurisdictions that matter: Section 508 in the US, EN 301 549 in the EU, and Ontario's AODA all reference WCAG conformance. For a government or public-sector surface, AA is closer to a compliance minimum than a stretch goal.

The posture worth copying, from this skill's design corpus: GOV.UK, Shopify Polaris, and IBM Carbon all treat accessibility as decided at the token and component level rather than audited at the end. They did not converge on that independently by accident.

## Where AI Design Fails Characteristically

Ranked by how often generated output gets them wrong.

**Contrast sacrificed to aesthetic.** The most common failure by a wide margin, and it follows directly from the AI default palette in patterns.md. Light grey on white, low-contrast placeholder text, white text over the light end of a gradient, and any text over a photograph without a scrim. Generated designs optimize for how a composition looks in a still frame, and a still frame does not show a failing contrast ratio.

**Glass and blur without a tested fallback.** Translucent treatments must degrade to a solid, legible state when a user has Reduced Transparency enabled. Shipping the effect and assuming the OS handles it is the specific documented mistake; the fallback needs to be designed and tested, not inherited.

**Color as the only channel.** Status conveyed by red and green alone, required fields marked only by color, chart series distinguished only by hue. Every one of these needs a second channel: an icon, a label, a pattern, a shape.

**Focus states removed for looking untidy.** Generated CSS frequently suppresses the default focus ring without replacing it, which silently removes keyboard navigation for everyone who depends on it. A visible, high-contrast focus indicator on every interactive element is not optional.

**Interactive elements that are not.** Div-based fake product UI, already flagged in patterns.md as a visual tell, is also an accessibility failure: a styled div is not a button, has no role, is not focusable, and is invisible to assistive technology. The aesthetic and access problems here are the same defect.

**Targets sized for a mouse.** Small tap targets, tightly packed icon rows, dismiss controls at the edge of a legible size. WCAG 2.2 added target-size criteria specifically because this remained common.

**Motion.** Covered fully in motion.md, listed here because reduced-motion handling is an accessibility obligation rather than a nicety.

## The Reviewer's Shortcut

Four checks catching a large share of the above, none needing tooling:

1. **Tab through it.** Can you reach everything, in a sensible order, and see where you are at every step?
2. **Read the greys.** Any text lighter than the body colour, and any text over an image or gradient, gets measured rather than eyeballed.
3. **Desaturate it.** If any status, required field, or data series becomes ambiguous in greyscale, colour was carrying meaning alone.
4. **Turn on Reduce Motion and Reduce Transparency.** Does it still work, and does it still read?

## Sources

WCAG 2.2 status, POUR, conformance levels, and the Section 508 / EN 301 549 / AODA references come from the operator's own design corpus (`accessibility-motion-qa-reference.md`, Cluster E, last checked July 27 2026), where they carry a Verified flag against official W3C and compliance sources. The stacked-translucency and Reduced-Transparency fallback material follows Apple's current Human Interface Guidelines via that file's Cluster B. The token-level posture observation about GOV.UK, Polaris, and Carbon is from the same corpus's Cluster C. The characteristic-failure ranking and the four-check shortcut are this skill's own synthesis, generalizing from those sources to what AI-generated design specifically produces.
