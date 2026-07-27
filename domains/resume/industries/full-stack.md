# Full-Stack / Software Development

Part of domains/resume/industries/. See README.md in this folder for how this fits together. Load alongside domains/resume/patterns.md. Split from the former combined tech.md in July 2026; see cybersecurity.md and it-support.md for the other two.

If the candidate has open-source work, a portfolio, or self-built tooling doing real work in place of employment history, load domains/resume/nontraditional-evidence.md as well.

## The Canonical Tell

"Built scalable web applications using modern technologies." Or its close relative, "full-stack developer with a proven track record of delivering high-quality code." Both describe the job category rather than the candidate, and both survive being moved to any other developer's resume without edit.

The specific version names an architectural decision and its consequence, which is the only thing on a developer resume that cannot be guessed from the job title.

## The Long Stack List Is the Field's Signature Failure

The most-repeated 2026 hiring complaint for this role, and it inverts the advice every other file in this folder gives. Elsewhere, naming more specific tools is the fix. Here, past a point, it becomes the problem: **a resume listing ten frameworks reads as depth in zero of them.** Hiring commentary describes this bluntly as a keyword dump rather than a skill set, on the reasoning that nobody is genuinely strong in ten things at once and the list is therefore a claim about coverage rather than ability.

What is read as real instead is a T-shaped profile: broad capability across the stack with demonstrable depth in one or two places. Two or three tools known deeply, plus evidence of picking up new ones, beats an exhaustive inventory.

**This collides directly with domains/resume/ats.md, and the collision is worth naming.** A parser rewards term coverage; a senior engineer reads term coverage as padding. This is the two-readers problem from patterns.md's Machine Screen section appearing at the level of the skills list. The resolution is the same shape: list the stack you would defend under questioning, and put the depth evidence in the bullets where it can be checked. A skills section is a claim about what you can be interviewed on.

## Tech-Stack Naming Has a Ceiling

Related but distinct from the list-length problem. "Full-stack developer skilled in HTML, CSS, JavaScript, and modern frameworks" names real technologies, but for a full-stack role those are the baseline expectation rather than a differentiator, closer to a security bullet naming "computers" than naming Splunk. Real specificity here is an architectural decision, an unusual combination, or a measured outcome, not the tools the posting already implies.

One current instance worth knowing: a 2026 resume naming React without TypeScript reads as a yellow flag to reviewers, on the grounds that TypeScript has been the working default long enough that avoiding it suggests the candidate has not been building recently. Baseline expectations move, and the ones a resume omits are read as much as the ones it names.

## The Deployment Pipeline Tell

"Deployed applications to the cloud" is this field's version of "improved security posture": true of almost every developer and checkable in none of them. The specific version names the containerization tool, the orchestration platform, the infrastructure-as-code tool, the CI system, and at least one real number.

This matters more than it used to. The 2026 reading of the role is that a developer owns code in production rather than only writing it, so deployment, monitoring, and performance ownership are scope rather than extras. A resume silent on all three reads as narrower than the title claims.

## The Missing Half

A specific and checkable red flag from 2026 hiring guidance: a candidate strong on the frontend who cannot discuss database indexing, or the reverse, is not doing full-stack work regardless of the title. On a resume this shows up as a stack list that is balanced and bullets that are not, with every measurable outcome landing on one side.

Read the bullets, not the skills section. If every accomplishment is a UI change and the backend appears only as nouns in a list, the resume is claiming a scope its evidence does not support. That is domains/resume/fabrication.md's absorbed-accomplishment problem at the level of a whole document.

## What Depth Actually Looks Like on the Page

The reasoning is the differentiator, not the choice. Hiring commentary flags candidates who cannot say why they picked a technology over the alternative as pattern-matchers rather than engineers. A bullet that names a decision and its tradeoff carries evidence that a bullet naming only the outcome does not:

- Weak: "Migrated the API to GraphQL, improving performance."
- Strong: "Moved the mobile client's three chattiest screens to GraphQL and left the rest on REST, because the win was request count rather than payload size. Cut cold-start requests from 11 to 3."

The second version can be interrogated for an hour. That is the property to write for.

## Numeric Camouflage

The field's characteristic version attaches a percentage to an unnamed baseline. "Improved performance by 40%" does not say which metric, measured at what percentile, under what load, from what starting point. p50 and p99 tell different stories about the same change, and the resume that omits which one is usually omitting the less flattering. Name the metric and the baseline, or describe the change instead.

## Fabrication Risk

Extends domains/resume/fabrication.md into the claims this field makes easy to widen:

- **Scale**, where "serving millions of users" describes the employer's product rather than anything the candidate built or touched
- **Ownership**, where *architected* and *led* replace *contributed to* on work that had a tech lead who was not this candidate
- **Team output as personal output**, the most common one, since a shipped feature has many authors and a resume bullet has one

## Worked Example

**Before:**
"Full-stack developer with a proven track record of building scalable, high-performance web applications using modern technologies including React, Angular, Vue, Node.js, Express, Django, Rails, PostgreSQL, MongoDB, Redis, Docker, Kubernetes, and AWS. Leveraged best practices to deliver robust solutions."

**After:**
"TypeScript and Node, with Postgres. Rewrote the reporting export after it started timing out past ~50k rows: moved it from an in-request query to a queued job writing to S3, which took the p99 from 45s and failing to 900ms and an email. Also the person who gets paged for it, which is why the retry logic is boring on purpose."

Fourteen technologies become three, and the resume gets stronger rather than weaker, because the three are now attached to a decision, a threshold, a before-and-after, and an admission of ownership. Note that the "after" version quietly demonstrates backend depth, production ownership, and judgment about failure modes without claiming any of those words.

## Sources

Full-stack and developer hiring guidance, 2025–2026: Kore1 and Digital Journal (2026 vetting and screening guides, T-shaped profiles, the ten-frameworks and React-without-TypeScript observations), Resume Worded (full-stack examples), CareerBldr full-stack template guide, BeamJobs and CVEdge (full-stack examples), plus practitioner hiring commentary on stack-list padding and technology-choice reasoning. The ATS collision, the missing-half reading, and the depth-on-the-page material apply this skill's own rules to those observations rather than restating any single source.
