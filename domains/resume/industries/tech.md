# Tech — IT / Software Development / Cybersecurity

Part of domains/resume/industries/. See README.md in this folder for how this fits together. Load alongside domains/resume/patterns.md.

## The Canonical Tell

"Improved the company's security posture" (or "Helped improve the company's overall security posture and reduce risk") shows up as the flagged bad example across independent 2026 cybersecurity-resume guides, not just one. Annotate it the way they do: "helped" hides the candidate's actual role, and "security posture" carries no number, tool, or framework a hiring manager could check.

## Named Category Instead of Named Tool

"Used various security tools to protect the network from threats." The category word, various, tools, solutions, technologies, is doing the work a proper noun should be doing. A hiring manager or ATS searching for Splunk, CrowdStrike, Nessus, or Microsoft Sentinel finds nothing to match, because nothing specific was ever named. Same mechanism as Specificity Erasure elsewhere in this skill; this field just makes it easy to test directly. Can the candidate name the actual tool, or not?

## Tech-Stack Naming Has a Ceiling

A full-stack-specific trap the security examples above don't have: naming your own stack isn't automatically specific. "Full-stack developer skilled in HTML, CSS, JavaScript, and modern frameworks" names real technologies, but for a full-stack role those are the baseline expectation, not a differentiator, closer to a security bullet naming "computers" than naming Splunk. Real specificity here is an architectural decision, an unusual combination, or a measured outcome, not the tools the job posting already implies.

## The Deployment Pipeline Tell

"Deployed applications to the cloud" is this field's version of "improved security posture," true of almost every developer and checkable in none of them. The specific version names the containerization tool, the orchestration platform, the infrastructure-as-code tool, the CI system, and at least one real number: which services, which platform, which pipeline, what changed and by how much. Same test as the security section above: can the candidate point to the actual tool and number, or is "the cloud" doing all the work?

## "Best Practices" Specifically

Worth calling out on its own here, because unlike most vocabulary tells this one carries an internal contradiction: it's reached for to sound authoritative while actually signaling that no specific practice is being named. Every organization that has ever suffered a major breach was, at the time, also following what it called best practices. The phrase means nothing until it's replaced with a specific control, a framework clause, or an actual policy.

## Numeric Camouflage

A more sophisticated version of specificity erasure worth watching for here: a bullet with a real-looking number attached to a still-vague noun. "Achieved 99.8% compliance with industry standards" has a precise figure, but "industry standards" names nothing, compliance with what, measured how, against which framework. A number doesn't make a claim specific if the thing it's measuring is still undefined. Ask what standard, whose framework, which system, before accepting the sentence at face value.

## Compliance and Framework Name-Dropping

NIST, ISO 27001, SOC 2, PCI-DSS, MITRE ATT&CK: naming a framework isn't the same as showing you worked inside it. "Aligned with NIST" and "mapped detection coverage against three MITRE ATT&CK tactics the team had zero prior visibility into" are different claims. Only one of them is checkable.

## Certification Status Honesty

A direct extension of domains/resume/patterns.md's Fabrication Risk. An in-progress or expired certification phrased as currently active, "CISSP" with no date attached, when the exam is still six weeks out, is a specific, checkable version of the same risk: easy for a model asked to "strengthen this resume" to introduce by smoothing over a status it was never told mattered.

## A Caution About the Advice Sources Themselves

Several cybersecurity- and developer-resume guides recommend example phrases that are themselves slop by this skill's own standard: "engineered robust information systems security protocols," "orchestrated cloud security implementations." Robust and orchestrated are already Tier 2 territory in domains/resume/patterns.md, and protocols/implementations are exactly the vague nouns this file flags above. A phrase isn't good writing just because a resume-advice site presents it as a positive example. Run it through the same test as everything else here.

## Worked Example

**Before:**
"Helped improve the company's overall security posture and reduce risk. Utilized various security tools to monitor for threats and respond to incidents. Achieved 99.8% compliance with industry standards and implemented security best practices across the organization."

**After:**
"Second of two analysts on a 24/7 SOC, roughly 60 alerts a shift in Splunk. Wrote the detection content for credential-stuffing against the customer portal after we missed one for eleven days; it caught the next attempt in under an hour. Mapped our coverage against MITRE ATT&CK and found three tactics with no telemetry at all, which became the FY25 logging budget request."

Three vague claims become one scoped role and two checkable outcomes. "Second of two analysts" is the kind of detail a candidate inflating their scope would never volunteer, and it makes everything after it more believable rather than less. Admitting the eleven-day miss is the same move: it is the detail that proves the story is a memory rather than a construction. Note that "99.8% compliance with industry standards" disappeared entirely rather than being made specific, because the underlying claim was never anything the candidate could name.

## Sources

Jobscan cybersecurity resume guide, ResumeVera (Cybersecurity Analyst 2026), Resume Worded, CVCompiler, TealHQ, Forbes Technology Council (on "best practices" as a cybersecurity cliche), Coding Temple, AiApply, Resumly certifications guide, BeamJobs and CVEdge (full-stack developer examples). All 2025–2026.
