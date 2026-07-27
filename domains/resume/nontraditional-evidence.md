# Non-Traditional Evidence

Part of domains/resume/. Load alongside patterns.md when a candidate's strongest material is not employment: bug bounty findings, CTF placements, published advisories or CVEs, open-source contributions, self-built tooling, or a home lab.

New in July 2026. Mainstream resume guidance handles this material poorly, usually reducing it to "add a projects section," which is why a capable candidate's best evidence often arrives as the weakest part of the page.

## Why This Material Behaves Differently

Almost everything on a resume is unverifiable by the reader: employment dates get confirmed eventually, but scope, contribution, and impact rest on the candidate's word. This material inverts that. A CVE number, a HackerOne profile, a merged pull request, and a public repository are all checkable in under a minute by someone who cares to look.

That cuts both directions, and both are worth stating plainly.

**It is the strongest evidence on the page.** Third-party verified, permanent, and specific. A published advisory carries a kind of proof that no employment bullet can, because a stranger with authority to say no already said yes.

**It fails fast when inflated.** An overstated employment bullet survives until the interview. An overstated CVE claim survives until someone opens the link, which may be while the resume is still in the stack. See domains/resume/fabrication.md; this is the one claim class where fabrication has a near-immediate detection path.

## Simulated Is Not Production, and the Distinction Is Load-Bearing

The single most important honesty line in this file. CTFs, HackTheBox, and lab environments reward finding bugs in systems built to contain them. Bug bounties and disclosed vulnerabilities are findings in systems built to work. Both are real skill; they are not the same claim.

A resume that lists CTF placements among professional experience, or describes lab work in the register of production work, is making a scope claim it cannot support. This is the widened verb from fabrication.md operating on an entire section rather than one bullet. Keep them visually separate and let the reader see which is which. A reviewer who spots the blur stops trusting the rest of the page, and reviewers in this field are specifically alert to it.

The honest framing costs nothing and reads as confidence: "Top 5% HackTheBox, 40+ retired machines" is a strong line precisely because it does not pretend to be an incident response.

## Bug Bounty Findings

**The disclosure constraint comes first.** Most programs restrict naming the target, and a candidate who names one anyway has demonstrated something worse than an empty resume. Write to the constraint rather than around it: "Reported a stored XSS in a mid-size fintech's customer portal via HackerOne, resolved and disclosed under program terms" says everything a reviewer needs without breaching anything. If the program permits disclosure and the writeup is public, link it, since that converts a claim into an artifact.

**Bounty amounts are a severity proxy with a known flaw.** They read as objective and are not comparable across programs, since payout tables differ by an order of magnitude for identical findings. Total earnings across a year is a reasonable summary line. A single bounty amount attached to a single bug invites a comparison the candidate does not control.

**Severity is the field's inflation point.** Calling a low a high, or reporting the CVSS the candidate calculated rather than the one the program assigned, is the supplied-number problem from fabrication.md with a public record attached. Use the program's rating where one exists.

**Volume without severity reads badly.** "300+ reports submitted" is a number that invites the question of how many were valid, and the honest ratio is usually the stronger line.

## CVEs and Published Advisories

The strongest artifact available to a candidate in this field, and the most under-used. A CVE identifier is permanent, third-party assigned, and searchable, which means it functions as a citation rather than a claim.

Write it with the identifier, the affected software, the class of bug, and the candidate's actual role, because advisories frequently have multiple credited researchers and the resume has one author. *Co-discovered*, *reported*, and *authored the advisory* are different contributions.

What not to do: list identifiers alone as a wall of numbers. Two CVEs with one sentence each about what the bug actually was beats twelve bare identifiers, for the same reason the long stack list fails in full-stack.md.

## Self-Built Tools and Open Source

The question a reviewer is actually asking is whether anyone other than the author has used the thing. That reframes what belongs on the page.

- **Adoption over activity.** Stars are weak evidence and downloads are better, but the strongest line is a named user: another team, a distribution package, a mention in someone else's tooling.
- **A solved problem beats a built feature.** "Wrote a parser for X" describes labor. "Wrote it because the existing three all failed on malformed input, which is the case we actually had" describes judgment, which is the property being hired for.
- **Contributions to others' projects carry a signal your own repositories cannot**, because a maintainer reviewed and accepted the work. A merged pull request to a project the reader has heard of is worth more than a repository the reader has not.
- **Abandoned work is fine and does not need hiding**, but a portfolio of eight half-finished projects makes an argument about follow-through. Show the two that shipped.

## Home Labs

Legitimate evidence, routinely oversold. A home lab demonstrates initiative and hands-on familiarity, and it does not demonstrate operating under constraint: no change control, no other people, no consequence when it breaks, no scale. Those absences are the entire difference between lab work and the job.

Write it as what it is. "Built a three-node Proxmox cluster running a Windows domain and an ELK stack, mostly to have somewhere to break things on purpose" is honest, specific, and does not invite the question the inflated version does.

## Where It Goes on the Page

Position encodes a claim, so it should track actual career stage rather than enthusiasm.

- **No professional experience in the field:** skills, certifications, and projects sit above employment, because the candidate competes on demonstrated capability rather than history. This is the one case where a projects section belongs high on the page.
- **Some professional experience:** employment moves above projects, and the projects section contracts to the two or three strongest items.
- **Established professional experience:** this material becomes a short section near the end, or disappears into the bullets where it is directly relevant. A long projects section on a senior resume reads as compensating for something, whether or not it is.

One structural note that applies at every stage: certifications with verification links are worth more than certifications without them, for the same reason as everything else in this file. The link converts an assertion into a fact.

## Sources

Security-portfolio and hiring guidance, 2025–2026: HackerOne (bug bounty versus CTF distinction, hacker-profile guidance), FolioX (cybersecurity portfolio structure and section ordering by career stage), Unihackers cybersecurity resume guide, Web Asha Technologies (bug bounty and CTF writeups), plus the 2026 cybersecurity career-path sources cited in industries/cybersecurity.md on portfolios differentiating candidates who hold identical certifications. The disclosure-constraint phrasing, the bounty-comparability caution, the severity-inflation and CVE-authorship material, and the home-lab framing extend this skill's own fabrication and specificity positions into a claim class those sources treat only as a resume section to add.
