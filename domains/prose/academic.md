# Academic Writing

Part of domains/prose/. Load alongside core/structural-patterns.md.

## Banned Phrases

- "Further research is needed." → name what specific research would determine what specific outcome, or cut.
- "This study aims to explore..." → state what the study found.
- "Findings suggest..." without citation → cite or restate as your own claim.
- "Novel," "robust," "comprehensive," "significant" in abstracts → empirically overrepresented post-ChatGPT (Kobak et al., 15M PubMed abstracts). Replace with specific claims.

## Citation Problems

- **Citation padding:** AI cites uncontroversial facts that need no citation, and omits citations on claims that do.
- **Vague attribution at 269x multiplier:** "objective studies aimed..." in academic register is flagged at 269x AI frequency (GPTZero corpus). Always cite specific author, year, finding.
- **Over-attribution in body text:** "According to the 2024 report by McKinsey Global Institute, which was published in October of last year, the findings indicate..." → "McKinsey (2024) found..."

## Literature Review: Synthesis vs. Summary

The single most consistent complaint about AI-assisted literature reviews, confirmed across multiple independent academic-writing sources: the output summarizes each paper in sequence instead of synthesizing across them. "Smith (2020) found X. Jones (2021) found Y. Patel (2023) found Z" is a stack of mini-abstracts, not a review, no matter how accurate each individual sentence is.

The fix is organizing by theme or claim instead of by paper: "Three approaches to measuring X have emerged. The first, used by Smith (2020) and Lee (2022), focuses on..." Synthesis tells the reader how the literature fits together, where it disagrees, what it assumes, and what it still can't explain. Summary just tells the reader what each paper says, one at a time.

A clean diagnostic test for this, worth running on any literature review section: could the paragraphs be reordered without changing the meaning of the piece? If yes, it's organized around papers, not around ideas, and it's a summary wearing a review's structure. This is Paragraph Symmetry from core/structural-patterns.md again, showing up specifically in how sources get organized rather than in paragraph-to-paragraph structure generally.

## Structural Problems

- Passive voice for methodology is standard, active for results is also standard. AI often inverts this.
- Hedging cluster followed by confident assertion: "may potentially possibly... [then] clearly demonstrates." The hedging is cosmetic. Pick a register.
- The PAS (problem-agitate-solution) structure used as default: fine once, a tell when it's the only structure you use.

## The Limitations Section, Specifically

Worth its own entry because the hedging-cluster pattern above shows up here in a sharper, more nameable form. One craft source names two recognizable failure modes directly: **the Confessional**, where the writer asks the reader to forgive a flaw in study design without explaining its actual impact ("Data collection occurred in a single institutional setting due to limited study resources"), and **the Dismissal**, where a real concern gets acknowledged only to be waved off in the same sentence ("Observational research can produce the Hawthorne effect... however, we are confident that the practices described represent a robust range of possible strategies"). Both are the admit-dismiss pattern from Structural Problems above, just localized to one section and easier to catch there because the section has exactly one job.

The plainest version of the same failure: "This study had several limitations." Names nothing, explains no impact, does none of the work a limitations section exists to do. The fix isn't hedging less, it's naming the specific limitation and stating plainly what it does to the findings: a small sample affects statistical power and generalizability, not just "may have affected results."

## What Human Academic Writing Does

- Named theories, specific scholars, concrete examples with real citations
- Appropriate hedging ("may suggest," "appears to," "potentially") applied to specific claims, not as a general fog
- Genuine critical engagement with sources: where they agree, where they conflict, what questions remain open
- Shows the author's position, even if tentative

## Sources

Original vocabulary and attribution content part of the v2.2 domain-patterns.md synthesis (see SKILL.md frontmatter for the full source list): Kobak et al., Science Advances 2025, and GPTZero corpus, both cited inline above. Literature Review and Limitations Section content added July 2026: proofreaderpro.ai, SciSpace, EvalCommunity Academy, and literfy.ai (summary-vs-synthesis diagnostics), "The art of limitations" via PMC/NCBI (the Confessional and the Dismissal), San Francisco Edit (vague-limitations canonical example).
