# Design Patterns — AI Slop in Visual and UI Design

AI design outputs have recognizable defaults. Apply the Distinctiveness Test: "Would a viewer immediately identify this as AI-generated?"

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

## Sources

Hardened tells (section-numbering eyebrows, fake version badges, Section-Layout-Repetition, and the rest under that heading): Leonxlnx/taste-skill, a 30.8k★ sibling project for AI-frontend slop, cited inline above. Everything else in this file (AI Default Palette, glassmorphism, template layouts, headline slop) is part of the original v2.2 skill; see SKILL.md's frontmatter for that broader source list.
