# Legal Writing

Part of domains/. A different register from most of what's in domains/prose/, not because the underlying mechanisms change, but because some things this skill flags elsewhere as tells are the correct convention here. Formal hedging, passive voice, and boilerplate structure are often required by the genre, not evidence of AI authorship. Load this file instead of assuming domains/prose/ rules transfer cleanly.

**Scope note:** this file is about writing quality, genericness, and specificity, the same thing every file in this skill is about. It is not a citation-verification system. Anthropic's own `claude-for-legal` plugin suite solves that as an engineering problem, research connectors, source attribution, `[verify]` flags on unconfirmed citations, because line-by-line reading for genericness cannot substitute for actually checking whether a case exists. Keep the two jobs separate.

---

## The Stakes Are the Highest in This Skill

A maintained academic tracker (Damien Charlotin, HEC Paris) counts documented cases of AI-hallucinated content filed in real courts worldwide: roughly 200 in mid-2025, 719 by January 2026, 1,227 by early April, 1,598 by June 9, and past 1,800 as of this writing. New cases are being added at 5 to 8 per day. This isn't a style complaint. It's sanctions, real money, and in at least one case, a canceled trial.

In *Withers v. City of Aberdeen* (N.D. Mississippi, June 2026), a judge canceled the trial entirely and suspended both lead attorneys after finding that lawyers on **both sides** of the case had cited cases that didn't exist. In an Oregon matter, two attorneys were sanctioned roughly $109,700 combined, the largest aggregate penalty on record, after filing 15 to 23 fabricated citations and 8 invented quotations across three summary judgment briefs. The Sixth Circuit sanctioned two attorneys in *Whiting v. City of Athens* for over 24 fake citations. An Alabama attorney was caught citing a fabricated case, told the court it wouldn't happen again, then cited more fabricated cases in the very next sentence of the same filing. U.S. courts imposed over $145,000 in AI-filing penalties in Q1 2026 alone.

## Why This Is the Sharpest Version of a Pattern Already in This Skill

domains/code/patterns.md's umbrella question asks whether something actually does what it looks like it does, or just has the shape of doing it. A hallucinated legal citation is the purest possible instance of that question: a case name, a court, a year, a page number, formatted in perfect Bluebook style, citing a holding that sounds exactly like something a real court would say. Structurally plausible. Functionally nonexistent. The formatting is precisely why it gets past a skim, a well-formatted fake is indistinguishable from a well-formatted real citation without actually looking it up.

A subtler, related failure mode showed up in the Sixth Circuit case specifically: citations to real cases that don't actually say what the brief claims they say. Not fabrication, misrepresentation. Both are the same underlying problem: a citation that exists to support a point rather than to report what a source actually held.

## Untailored Is the Real Tell, a Fifth Independent Confirmation

Anthropic's own legal-plugin documentation states plainly that skipping the setup interview, the step where a practice profile captures a firm's actual playbook, escalation rules, and house style, is the single most common reason a legal-AI skill produces generic output. That is Untailored Is the Real Tell again, independently arrived at for legal work specifically, after resumes, LinkedIn profiles, investor pitch decks, and email. A contract review or memo that reads as competent but generic, the kind that could apply to any client's deal instead of this one, is the same failure every other domain in this skill already names, just with higher stakes attached to missing it.

## Boilerplate as Specificity Erasure

Generic indemnification language, "the parties agree to act in good faith" with no definition of what that means for this deal, clauses copied forward without adapting to the actual terms being negotiated. Same mechanism as everywhere else in this skill: a phrase that sounds legally solid while committing to nothing specific enough to actually govern what happens in a dispute.

## The Confidence Inversion, Legal Version

domains/prose/security-reporting.md already names this pattern for vulnerability reports: AI states conclusions with more certainty than the evidence supports, because a clean, professional-looking template reads as authoritative regardless of how well-founded it actually is. Legal writing is the same inversion at higher stakes. A confidently-stated legal conclusion resting on an unverified or fabricated citation is not a hedging problem, it's a verification problem wearing confident prose. The fix isn't softer language. It's tying every citation to a source someone actually checked, and flagging plainly when one hasn't been.

---

## Sources

Damien Charlotin's AI Hallucination Cases Database (HEC Paris, ongoing), Legal Cheek and the American Bar Association (*Withers v. City of Aberdeen* coverage, June 2026), the Sixth Circuit Appellate Blog (*Whiting v. City of Athens*), HAQQ and Fortune (Oregon sanctions figures, 2026), Scientific American (recidivism example, May 2026), Spellbook (general hallucination-risk overview). `claude-for-legal` (github.com/anthropics/claude-for-legal), Anthropic's own legal-plugin suite, for the cold-start-interview and untailored-output framing; a practice-management tool, not a source this file otherwise draws patterns from.
