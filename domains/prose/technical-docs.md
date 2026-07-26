# Technical Documentation and READMEs

Part of domains/prose/. Load alongside core/structural-patterns.md.

## Structural Tells

- **Template README cloning:** Introduction → Features → Installation → Usage → Contributing → License, every AI README has exactly this structure. Break it deliberately. Lead with what makes a developer stop scrolling.
- **Happy-path-only documentation:** error conditions, edge cases, rate limits, failure modes are absent or vague.
- **Over-specifying obvious operations:** explaining what `len()` does in a Python docstring, explaining what HTTP 200 means in an API doc.
- **False compatibility claims:** "works with all versions of Python 3," AI asserts compatibility it cannot know.
- **Bullet-stacking features with checkmarks:** ✅ Fast ✅ Secure ✅ Scalable, marketing copy in technical docs. Replace with prose that explains what "fast" means in measurable terms.

## Missing the Why

AI documents what and how. It rarely documents why, why this design was chosen, what tradeoffs were made, what the alternatives were and why they were rejected. If your README would look the same if someone else built the same tool a completely different way, it's missing the why.

## What Good Technical Docs Include

- Specific numbers: "Tested on Next.js, Remix, SvelteKit, and Astro" not "works with popular frameworks"
- Honest limitations: "This won't catch dynamic imports or string templates. Fix those manually." "Expect about 5% of edge cases to need manual review."
- Real edge cases named explicitly, not "handles edge cases gracefully"
- Runnable examples with expected output
- Common pitfalls named before the user hits them

See domains/prose/security-reporting.md for the security-specific version of specificity erasure (vulnerability findings and advisories rather than general project docs).

## Sources

Part of the original v2.2 domain-patterns.md synthesis (see SKILL.md frontmatter for the full source list).
