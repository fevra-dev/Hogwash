# Cybersecurity

Part of domains/resume/industries/. See README.md in this folder for how this fits together. Load alongside domains/resume/patterns.md. Split from the former combined tech.md in July 2026; see full-stack.md and it-support.md for the other two.

If the candidate has bug bounty findings, CTF placements, published advisories, or self-built tooling, load domains/resume/nontraditional-evidence.md as well. That material is common in this field and the rules for presenting it honestly are not obvious.

## Security Is Not One Job, and One Resume Cannot Cover It

The first correction, before any vocabulary. SOC analysis, incident response, threat hunting, GRC, application and cloud security, and penetration testing hire on different evidence, and a resume written to satisfy all six satisfies none. Hiring guidance through 2026 is consistent on this: these are distinct tracks, not seniority levels of one track.

What each track actually reads for:

- **SOC and incident response:** alert volume and what you did with it, detection content you wrote, MTTD and MTTR movement, the SIEM and EDR by name, escalation judgment
- **GRC:** which framework, which control set, audit outcomes, evidence collection, what a finding cost to remediate
- **Application and cloud security:** where in the pipeline you sat, what you broke or fixed, the specific classes of bug found, the platform
- **Penetration testing:** scope and depth of engagements, methodology, what got exploited and how far, report quality, and often a public portfolio

This is Untailored Is the Real Tell (patterns.md) with an unusually sharp edge, because the sub-fields share vocabulary. A resume can name SIEM, NIST, and Burp Suite in one skills section and read as a person who has done none of them seriously.

## The Canonical Tell

"Improved the company's overall security posture and reduced risk." It appears as the flagged bad example across independent 2026 cybersecurity-resume guides, and it fails twice: "helped" or "improved" hides what the candidate actually did, and "security posture" carries no number, tool, or framework anyone could check.

## Named Category Instead of Named Tool

"Used various security tools to protect the network from threats." The category word, *various*, *tools*, *solutions*, *technologies*, is doing the work a proper noun should do. A reviewer or parser searching for Splunk, CrowdStrike, Nessus, or Microsoft Sentinel finds nothing to match, because nothing specific was named. Same mechanism as Specificity Erasure elsewhere in this skill; this field makes it testable directly. Can the candidate name the tool, or not?

## The Certification List Without Application

The single most-cited rejection in 2026 hiring commentary for this field: a resume that reads as a certification inventory with no evidence any of it was ever used. Certifications validate knowledge, and in a field where thousands of candidates hold identical certs, they no longer differentiate. What differentiates is one specific thing the candidate did with the knowledge.

The fix is not to cut certifications. It is to make sure at least one bullet demonstrates each claimed capability in use. A CySA+ next to a bullet about detection content you wrote is a different document from a CySA+ standing alone.

## "Best Practices" Specifically

Worth calling out on its own, because unlike most vocabulary tells this one carries an internal contradiction: it is reached for to sound authoritative while signaling that no specific practice is being named. Every organization that has suffered a major breach was, at the time, also following what it called best practices. The phrase means nothing until it is replaced with a specific control, a framework clause, or an actual policy.

## Numeric Camouflage

A real-looking number attached to a still-vague noun. "Achieved 99.8% compliance with industry standards" has a precise figure, but *industry standards* names nothing: compliance with what, measured how, against which framework. A number does not make a claim specific if the thing it measures is undefined. Ask what standard, whose framework, which system, before accepting the sentence.

## Compliance and Framework Name-Dropping

NIST, ISO 27001, SOC 2, PCI-DSS, MITRE ATT&CK: naming a framework is not the same as showing you worked inside it. "Aligned with NIST" and "mapped detection coverage against three MITRE ATT&CK tactics the team had zero prior visibility into" are different claims, and only one is checkable.

## Certification and Clearance Status Honesty

A direct extension of domains/resume/fabrication.md's smoothed-status category, and this field has more surface for it than most.

- A certification listed without a date when the exam is still scheduled
- An expired cert carried forward, which is easy to miss because the acronym does not change when it lapses
- **Clearance status**, which is the highest-risk item on any resume in this field. Active, current, eligible, previously held, and interim are different facts with different values to an employer, and all five get flattened to "clearance" by a rewrite that was never told they differ. Clearance claims are verified as a matter of course, so an inflated one fails reliably rather than occasionally.

Flag every one and ask. Do not resolve them silently.

## A Caution About the Advice Sources Themselves

Several cybersecurity-resume guides recommend example phrases that are slop by this skill's own standard: "engineered robust information systems security protocols," "orchestrated cloud security implementations." *Robust* and *orchestrated* are Tier 2 territory in patterns.md, and *protocols* and *implementations* are exactly the vague nouns this file flags. A phrase is not good writing because a resume-advice site presents it as a positive example. Run it through the same test as everything else.

## Worked Example

**Before:**
"Helped improve the company's overall security posture and reduce risk. Utilized various security tools to monitor for threats and respond to incidents. Achieved 99.8% compliance with industry standards and implemented security best practices across the organization."

**After:**
"Second of two analysts on a 24/7 SOC, roughly 60 alerts a shift in Splunk. Wrote the detection content for credential-stuffing against the customer portal after we missed one for eleven days; it caught the next attempt in under an hour. Mapped our coverage against MITRE ATT&CK and found three tactics with no telemetry at all, which became the FY25 logging budget request."

Three vague claims become one scoped role and two checkable outcomes. "Second of two analysts" is the kind of detail a candidate inflating their scope would never volunteer, and it makes everything after it more believable rather than less. Admitting the eleven-day miss does the same work: it is the detail that proves the story is a memory rather than a construction. Note that "99.8% compliance with industry standards" was cut rather than made specific, because the underlying claim was never anything the candidate could name.

## Sources

Cybersecurity-resume guidance, 2025–2026: Jobscan cybersecurity resume guide, ResumeVera (Cybersecurity Analyst 2026, SOC and SIEM keywords), Resume Worded (entry-level analyst), CareerBldr, Course Careers and Total Cyber Academy (sub-field track separation and per-track certifications), RedBud Cyber (certifications by career path), CVCompiler, TealHQ, Forbes Technology Council (on "best practices" as a field cliche), Coding Temple, AiApply, Resumly certifications guide. The sub-field-separation section reflects the consistent position across the 2026 career-path sources. The clearance-status material extends this skill's own fabrication position into a claim class those guides treat only as a keyword.
