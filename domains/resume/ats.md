# ATS and Machine Parsing

Part of domains/resume/. Load alongside domains/resume/patterns.md when the resume is being submitted through an online application system, which in practice is almost always.

This file covers the Parseability dimension of the rubric in patterns.md. It is a different axis from the rest of this skill: everything else asks whether the writing is empty, and this asks whether a machine can read it at all. A resume can be specific, tailored, and genuinely well written and still arrive as scrambled text. Both failures end the same way, so both are worth checking, but do not confuse one for the other.

## What Actually Breaks a Parser

Ranked by how badly it fails, worst first.

- **Text boxes used to fake columns.** The worst case, because it fails silently and completely. The parser reads the full contents of one box before starting the next, so a two-column layout arrives with every job title collected in one block and every date in another, correctly extracted and permanently disconnected.
- **Image-only PDFs, password-protected PDFs, and PDF/A.** All three lock or remove the text layer the parser needs. There is nothing to extract, so the submission arrives blank or near-blank. A resume that was scanned or printed-then-photographed is the common way this happens by accident.
- **Tables used for page layout, and any nested table.** Simple single-level tables usually survive modern parsers. Tables holding the document's structure, and tables inside tables, do not.
- **Non-standard section headings.** "Where I've Been" instead of "Work Experience" and "My Toolkit" instead of "Skills" defeat the section classifier. The parser is matching against a known list of headings; a clever one is a heading it does not recognize.
- **Graphics, icons, and skill-rating bars.** Ignored rather than misread, which means a skills section built from five-star icons parses as no skills at all.

## PDF or Word

Modern systems (Workday, Greenhouse, Lever, Ashby, iCIMS) handle a text-based PDF as well as or better than .docx, and PDF is the only format that guarantees the layout a reviewer sees matches the one that was sent. Default to text-PDF exported from a word processor, not printed or scanned. Switch to .docx when the posting explicitly asks for it, because a posting that asks is often running something older.

The safe format underneath both: single column, a common sans-serif at 10 to 11 point, standard section headings, real text rather than graphics, no tables carrying structure.

## Keywords Without Stuffing

Parsers match the posting's own terms, so the posting's vocabulary should appear in the resume where it is honestly true. That requirement sits directly against patterns.md's Repeated Word Clustering rule, and the resolution is not a compromise between them: use the posting's term once, in the bullet where the candidate actually did that thing, rather than sprinkling it. The stuffed version fails both tests at once, since it reads as machine-written to a human and as low-quality keyword spam to the systems that weight term density.

## A Caution About ATS Scores

Consumer tools that return an "ATS score" out of 100 are not running the employer's actual system, and no such universal score exists. They are pattern-matchers with their own heuristics, sold as a service. Treat their output the way this skill treats consumer AI-detector output elsewhere: a prompt to look at something, never a verdict. The checkable claims in this file (does it have a text layer, is it one column, are the headings standard) can be verified directly by opening the file and selecting the text, which is more reliable than any score.

## Sources

ATS formatting guidance, 2026: OwlApply, Scale.jobs, FastApply, JobWizard, ResumeAdapter, ATSAlign, AutoTailor, Resume Optimizer Pro. Parser behavior on text boxes, nested tables, and locked PDF text layers is consistent across all of them. Vendor coverage (Workday, Greenhouse, Lever, Ashby, iCIMS) reflects the same 2026 guidance. The ATS-score caution is this skill's own detector-reliability position applied to a second tool category, not a claim sourced from those guides.
