# Design Patterns — AI Slop in Visual and UI Design

Part of domains/design/. This file is the static catalog: what AI design output looks like when you look at it. Three companions cover what it cannot.

- **[motion.md](motion.md)** — does the movement communicate a state change, or is it decoration? A separate axis with its own vocabulary.
- **[accessibility.md](accessibility.md)** — does it fail for someone? AI design has characteristic accessibility failures, and they are not the same as its aesthetic failures.
- **[expressive.md](expressive.md)** — is loud actually the brief? Read this before applying anything below to a portfolio, a brand moment, or a culture site.

AI design outputs have recognizable defaults. Apply the Distinctiveness Test: "Would a viewer immediately identify this as AI-generated?"

## Sanded-Down Is Also a Tell

Read this before the catalog, because it changes what the catalog is for.

Every entry below tells you what to remove. Removing all of it lands you on clean, quiet, rounded, softly-shadowed, generously-spaced minimalism, and **that is the current AI default**, not the escape from it. The evidence is that the 2025–26 neo-brutalist revival defines itself explicitly as a reaction against this exact aesthetic: soft shadows, rounded corners, generic minimalist templates, described by its own advocates as total aesthetic exhaustion. A movement organized around being tired of a look is good evidence that the look has become the default.

This is the design version of a principle this skill already holds for prose: voiceless sterile writing is as obvious as slop, and the goal is not neutral. A design with every flagged element stripped out and nothing put in its place has the same problem as a paragraph with every banned word removed and no claim behind it. It is inoffensive and it is anonymous.

So the catalog below is a list of things to notice, not a specification to converge on. The question after removing a default is always what specific decision replaces it, and "nothing" is an answer only when undecorated genuinely serves the task (see expressive.md on pure brutalism, where it sometimes does).

---

## VISUAL SLOP

### The AI Default Palette
Generic purple/pink/cyan gradients. Not a design choice. A training artifact. Pick a specific color rationale tied to the content or brand. If you cannot articulate why this color, you are using the default.

### Glassmorphism and Neumorphism Applied Universally
These are valid treatments for specific contexts. As a universal aesthetic applied to everything regardless of content, they are an AI tell.

### Floating 3D Shapes Without Purpose
Decorative geometric 3D shapes that do not carry semantic meaning. If a shape is present, it should communicate something.

### Every Element the Same Visual Treatment
Cards for everything, regardless of whether the content is card-shaped. Identical visual hierarchy for items that do not have identical semantic weight.

---

## LAYOUT SLOP

### The Template Layout
Layouts that follow the template structure without regard for the actual content, because the template is statistically common in the training data. Signs:
- Hero: headline + subtitle + CTA button, always in that order
- Features: 3-column card grid with icon + title + description
- Testimonials: card carousel with quote + name + role
- Pricing: 3-tier card with highlighted middle option

These structures are not wrong. They are wrong when applied automatically regardless of what the content actually needs.

### Center-Alignment as Default
Center-aligned everything regardless of reading direction or content type. Centered body copy is harder to read than left-aligned. Center-align is appropriate for short display text and headings, not paragraphs.

### Excessive Whitespace Without Hierarchy
Space should signal relationships: proximity signals grouping, distance signals separation. Whitespace applied uniformly to fill area without hierarchy signals AI-generated layout.

### Card Grid with Identical Treatment
Every item receives the same visual weight, same card size, same typographic treatment, regardless of whether some items are more important than others. Human designers establish hierarchy.

---

## COPY SLOP IN DESIGN

### Headline Slop
"Empower your business" type headlines: no specificity, no differentiator. Replace with what the specific thing does or achieves.

AI headline pattern: adjective + abstract noun + for/with + audience
"Seamless collaboration for modern teams" → what does it let teams do? Say that instead.

### Generic CTAs
"Get Started" with no context is the most common AI CTA. Describe what happens when you click:
- "Start your free trial" (describes the action)
- "Download the SDK" (describes what you get)
- "See a live demo" (describes the experience)

### Buzzword Descriptions
Benefit statements that describe no specific mechanism: "Save time, money, and effort." How? On what specifically? Replace with the actual mechanism: "No more searching docs for edge cases, they're encoded in the package."

### Stock Photo Aesthetic in Illustration
AI-generated illustrations that mimic the aesthetic conventions of stock photography: generic diverse smiling people, abstract business imagery, floating geometric elements. These signal the same training distribution as stock photo sites.

---

## FORMATTING TELLS IN DESIGN COPY

### Emoji as Decoration
🚀 ✅ 💡 ❌ used as bullet substitutes or section decorations in non-casual contexts. Fine in informal channels; a tell in product marketing or technical documentation.

### Bold Spam
Every other phrase in bold in feature descriptions. Bold should mark the thing the reader needs to find when scanning. If everything is bold, nothing is.

### Icon + Title + One-Sentence Description
The three-column feature grid with this exact structure is AI's default for any "features" section. Either differentiate the structure or use a different presentation entirely (prose, before/after comparison, demo).

---

## HARDENED TELLS (field-tested on AI-frontend generation specifically)

*Sourced from taste-skill, a 30.8k★ sibling project focused entirely on AI-frontend slop. Their independently-arrived-at complete em-dash ban (zero, anywhere: headlines, buttons, alt text, captions) matches this skill's own em-dash threshold exactly: cross-confirmation from an unrelated codebase.*

### Section-Numbering Eyebrows
"00 / INDEX," "001 · Capabilities," "06 · how it works." Ban outright.

### Fake Product-Launch Signals
Version labels ("V0.6," "BETA," "INVITE-ONLY PREVIEW") and version footers ("v1.4.2," "Build 0048"). Only legitimate when the brief is an actual product launch.

### Decorative Non-Functional Elements
Status dots with no state to indicate. Scroll cues ("Scroll to explore," "↓ scroll"). Fake photo-credit captions with no real attribution behind them. Locale, weather, or time strips ("Lisbon, working with founders") for briefs that aren't actually about location.

### Div-Based Fake Product UI
Fake dashboards, task lists, or terminal windows built from styled divs rather than real interface elements: a visual placeholder pretending to be a product.

### Section-Layout-Repetition Rule
Across N page sections, require at least N/2 distinct layout families. The page-level version of this skill's own Paragraph Symmetry rule (core/structural-patterns.md), same principle one level up.

### Bento Cell Count Rule
N items get exactly N cells. No empty filler cells, no trailing gaps.

### Color and Shape Consistency Locks
One accent color, one corner-radius system, for the whole page. No unexplained mid-page swaps.

### Long-List-Divider-Overuse
`border-t` plus `border-b` on every row of a list longer than about 5 items is the lazy default. Use cards, tabs, or a different component instead.

### Hand-Rolled Icons
Custom-drawn SVG icons where a named library exists are a soft tell. Prefer Phosphor, HugeIcons, Radix, or Tabler.

---

## BORROWED-DOCTRINE FAILURES

A different failure shape from the ones above. These are not defaults a model reached for; they are real design doctrines applied where their preconditions do not hold. The output looks considered, which is why a style pass misses it.

### Decoration That Mimics the Subject
Paul Rand's cliché-thinking. A security tool skinned in matrix-green because the subject is security, faux-calligraphy on anything about writing, circuit-board motifs on anything about hardware. The decoration restates the topic instead of doing work. Ask what the treatment contributes that the words do not already say.

### Stacked Translucency
Glass or blur layers composited over each other. Apple's own current guidance calls this out directly as hierarchy-destroying: translucency works by letting one layer read against a background, and stacking removes the background. One glass layer at a time, over content, never over more glass.

### Restraint Without the Assets That Justify It
A photo-led calm system applied to content with no real photography behind it. Airbnb's register depends on the images; the same layout without them reads as empty rather than as composed. The general form: adopting a system's visual restraint while missing the asset quality that restraint was designed to frame.

### Uniformity Mistaken for Consistency
GOV.UK's distinction, and the sharper phrasing is theirs: **consistent, not uniform.** Forcing one treatment onto components solving genuinely different user needs is not a design system, it is a template. This is the same error as Card Grid with Identical Treatment above, arriving from doctrine rather than from laziness, and it is harder to spot because it can cite a principle.

### Expressive Type on Functional Copy
Distressed, sliced, or heavily expressive display type applied to form labels, error messages, prices, or data values. The register belongs to brand and hero moments. Break legibility where the job is to be felt; never where the job is to be used. See expressive.md, which covers the legitimate version of this at length.

---

## Sources

Hardened tells (section-numbering eyebrows, fake version badges, Section-Layout-Repetition, and the rest under that heading): Leonxlnx/taste-skill, a 30.8k★ sibling project for AI-frontend slop, cited inline above. Everything else in the original catalog (AI Default Palette, glassmorphism, template layouts, headline slop) is part of the v2.2 skill; see SKILL.md's frontmatter for that broader source list.

Added August 2026, from the operator's own design-philosophy corpus (`~/Apps/UI:X/Design Principles/`, last checked July 27 2026), which had scoped these extensions and never merged them. The Borrowed-Doctrine Failures section implements that corpus's Cluster E merge instruction directly: Rand's cliché-thinking from Cluster A, Apple's stacked-translucency guidance from Cluster B, the Airbnb restraint-without-assets and GOV.UK consistent-not-uniform observations from Cluster C, and the expressive-type-on-functional-copy boundary from Cluster D. The Sanded-Down Is Also a Tell framing is this skill's own, prompted by that corpus's Cluster D finding that the 2025–26 neo-brutalist revival defines itself explicitly against the aesthetic this file catalogs; the underlying principle (voiceless sterile output is as obvious as slop) was already in SKILL.md for prose and had no design equivalent.
