# Resume Patterns — Scope Note and Slop Tells

## Why a Separate File

Everything else in this skill assumes prose: paragraphs, sentences, a sustained argument, a writer taking a position. A resume is a different medium, not just a different domain. Bullet fragments, not sentences. No paragraphs. Impersonal, subjectless phrasing is the correct convention here, not a tell. Most of the rest of this skill does not apply. Load this file instead of domains/prose/ and core/structural-patterns.md for a resume or CV; load it alongside them for a cover letter (see below).

---

## What Does Not Apply

- **False Agency** (core/structural-patterns.md): "Led cross-functional initiative" has no subject by design. That's the form, not a tell.
- **Paragraph Symmetry, Every-Paragraph-Resolves, Emotional Register Uniformity:** there are no paragraphs.
- **Sentence Length SD:** bullets are fragments, not sentences. Length variance isn't the signal here.
- **Hedging clusters:** resumes don't hedge. One that does has a different, worse problem.
- **Subheadings as Statements** (Pass 0 #10): section headers ("Experience," "Education," "Skills") are conventional, not claim-shaped, by design. Making them claim-shaped would look strange, not human.
- **Most of core/vocabulary.md's metaphorical-language tier:** "delve," "tapestry," "realm" essentially never appear on resumes. Wrong register for the document.

## What Transfers, Reinterpreted

- **Specificity Erasure** is still the root cause, operationalized as a number instead of a name or date. "Responsible for managing a team" is Specificity Erasure the same way "significant growth" is; the fix is a quantified outcome, not a proper noun.
- **Rule of Three** shows up as bullet count. Exactly three bullets per role, every role, is the resume version of tricolon padding.
- **Template Cloning:** every role getting the identical grammatical shape (verb, object, "resulting in X%"), repeated exactly, is the resume version of consecutive-sentence-similarity.

---

## The Canonical Tell

"Results-driven professional with a proven track record of delivering innovative solutions." Named directly by multiple 2026 hiring-industry sources as the single most recognizable AI-resume opener. A summary paragraph built this way would fit any candidate in any field, which is the actual defect, not the specific words chosen.

## Three Abstract Adjectives, Vague Object

"Spearheaded innovative, scalable, mission-critical solutions across the organization." A named pattern in 2026 hiring-industry writing: stack two or three unfalsifiable adjectives in front of a noun with no referent (solutions, initiatives, strategies), and the sentence sounds impressive while describing nothing. Test: remove the adjectives. If the sentence still makes no verifiable claim, they were load-bearing for the wrong reason.

## Bullet-Opener Vocabulary

**Tier 1, replace outright:** results-driven · proven track record · team player · self-starter · detail-oriented · hardworking · go-getter · think outside the box · synergy · dynamic · passionate about · excellent communication skills

**Tier 2, fine occasionally, dead on arrival if every bullet opens this way:** spearheaded · leveraged · orchestrated · championed · drove · streamlined

No single Tier 2 word is wrong on its own. The problem is that AI has roughly six verbs it reaches for, and opening every bullet on the page with one of them is what "sameness" looks like from the reviewing side. A human resume varies the verb because it's describing six different things, not performing "sounding impressive" six times.

## Repeated Word Clustering

A different case from the opener list above: the same content word landing three or more times anywhere in the document, not just as a bullet's first word. "Engineered" as the lead verb in one bullet, again mid-sentence in another, again in the skills section, is Bullet-Opener Vocabulary's general case rather than a duplicate of it.

**Why it happens:** a real resume gets written in pieces over years, one role added at a time, so vocabulary drifts naturally between sections written months or years apart. A model writes the whole document in one pass with one working vocabulary and defaults to whichever verb it's decided is "the strong one" for that role, especially when the word doubles as the job title itself (engineer → engineered, design → designed).

**Flag point:** the same content word, not counting job titles or section headers, appearing 3 or more times on a one-page resume. The cost is measured, not just aesthetic: a 2023 Jobscan study found resumes with more than 15% duplicate phrasing saw a 22% drop in interview callbacks, and SHRM research found 43% of recruiters read keyword stuffing as a dishonesty signal, not just a style one.

**The extreme version is ATS keyword stuffing**, a different motive with the same symptom: "Project management expertise in project management systems including project management tools for project management" is what optimizing for a parser instead of a reader produces. The fix is the same either way. Vary the verb, or cut the repeat if the bullet doesn't need it.

**Related, not identical:** two bullets using different words to say the same thing ("Collaborated with teams to improve communication" / "Worked with departments to enhance teamwork") are this pattern's semantic cousin, repetition of the idea instead of the word, and worth the same scrutiny even when no single word repeats.

## Suspiciously Round Numbers

Real outcomes are rarely round. "Increased sales by 34%" reads as measured; "increased sales by 50%," or 30, or 25, is the number a model reaches for when asked to sound quantified without an actual figure in hand. Not a hard rule; some real results genuinely land on a round number. But a cluster of round numbers across every bullet on one resume is worth a second look.

## The Fabrication Risk (flag, don't silently fix)

Distinct from a style problem. A model asked to "make this sound more impressive" will sometimes invent a specific metric the candidate never provided, "increased revenue by 47%," rather than leave a bullet unquantified. That isn't slop. It's a factual claim that may be false, and it's the candidate's to verify, not this skill's to paper over. If a number in a draft can't be traced back to something the candidate actually said, flag it and ask.

## Skills-Section Over-Inclusion

A long tail of low-relevance skills crammed into a skills section is the resume version of False Ranges: breadth standing in for the specific two or three things that actually matter for this role. Cut to what's both true and relevant to the posting. Shorter and accurate beats exhaustive.

## Untailored Is the Real Tell

The single biggest structural signal in 2026 hiring data isn't a banned word. It's the same document sent to every posting. A resume tailored to nothing reads as AI-written even with clean prose, because genericness at the document level is what "written for anybody" looks like. One posting, one real pass of tailoring, minimum.

## Cover Letters (hybrid case)

A cover letter is prose, not bullets. Audit it with the matching domains/prose/ file and core/structural-patterns.md as normal, and add these resume-specific opener bans on top: "I am thrilled to apply for this position" · "I believe my skills align perfectly with..." · "I am writing to express my interest in..." Also check the letter against the resume itself. Hiring reviewers in 2026 explicitly check whether the two documents sound like the same person on the same day; a visibly different voice between them is its own tell. If domains/resume/industries/ has a file for the candidate's field, its vocabulary applies to the cover letter too, "best practices" reads just as empty in a paragraph as it does in a bullet.

## LinkedIn Profiles (hybrid case)

A different hybrid than the cover letter. The headline is closer to the resume's compressed, fragment-based register; the About section is closer to prose. Two format-specific patterns worth flagging on top of everything above:

**The pipe-separated abstract-noun headline.** "Visionary Leader | Global Innovator | Change Agent" is the LinkedIn-specific version of Three Abstract Adjectives, Vague Object, three unfalsifiable nouns strung together with no role, company, or specifics attached. A real headline names the actual job and what it's actually about: "Product Manager, Payments at [Company]" beats any string of inflated titles.

**It's public and ongoing, not a one-shot submission.** Untailored Is the Real Tell still applies, but "tailored to what" shifts, not one posting, but a consistent, specific positioning toward the kind of role the candidate actually wants. A profile trying to sound right for every possible viewer ends up sounding specific to none.

Even LinkedIn's own built-in writing assistant comes with a caveat from LinkedIn itself to review before posting, worth remembering that the platform vendor doesn't fully trust its own tool's unedited output either.

---

## Where This Sits in the Bigger Picture

By industry estimates, 60 to 80 percent of resumes submitted in 2026 show clear signs of LLM authorship, and hiring managers have shifted from mostly tolerating this through 2025 to rejecting on sight in 2026. The same detector-reliability caution already in this skill applies here too: one widely-cited 2025–2026 survey found hiring managers self-report 74% confidence in spotting AI resumes, while blind tests put actual accuracy at 33.5%. Consumer "AI resume detectors" are no more reliable than the text detectors flagged elsewhere in this skill.

The goal here isn't an undetectable resume. It's the same goal as the rest of Hogwash: make the writing actually specific and true. That's what stops it from reading as generic in the first place.

---

## Worked Example

**Before:**
"Results-driven marketing professional with a proven track record of driving impactful campaigns. Spearheaded innovative, cross-functional initiatives that boosted brand visibility and engagement. Leveraged data-driven insights to optimize strategies and deliver measurable results."

**After:**
"Ran paid social for a 12-person growth team. Cut cost-per-lead 38% by killing 4 underperforming channels and reallocating spend to the 2 that converted. Built the weekly reporting dashboard the team still uses."

The point isn't more information, it's traceable information. The "after" version has a team size, a specific decision, a specific number, and an artifact that outlasted the role. None of that is guessable from the "before" version, because none of it was actually there.

---

## Scoring Rubric

Rate 1–10 per dimension. Below 35/50: revise.

| Dimension | Question |
|---|---|
| **Specificity** | Numbers, names, and outcomes, or generic verbs and adjectives? |
| **Tailoring** | Written for this posting, or the same document sent everywhere? |
| **Distinctiveness** | Could only this candidate have written this bullet, or would it fit a hundred other resumes? |
| **Verifiability** | Could the candidate defend every claim in an interview without the story falling apart? |
| **Parseability** | Clean single-column format an ATS can read, keywords present without stuffing? |

---

## Sources

Hiring-industry sources, 2025–2026: GetPruf, ResumePulse AI, Hiration (including LinkedIn-profile guidance), ResumeVera, ResuFit, The AI Career Lab, CVCraft (citing a TopResume survey of 600 US hiring managers), AutoApplyMax, Resumly.ai (buzzword-checker sample output and 2023 Jobscan duplicate-phrasing study), Rezi.ai, Qwyse, Resume Pilots (citing SHRM keyword-stuffing research), Gem, outx.ai (LinkedIn profile patterns).
