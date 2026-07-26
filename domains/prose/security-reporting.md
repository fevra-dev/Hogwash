# Security and Vulnerability Reporting

Part of domains/prose/. Load alongside core/structural-patterns.md. For resume/CV content in this field, see domains/resume/industries/tech.md instead, different medium, different file.

## Generic Impact Statements

"The assessment identified multiple critical vulnerabilities that could significantly impact the security posture of the organization. Immediate remediation is recommended." Names nothing: no vulnerability, no system, no evidence, no timeline. A practitioner source calls this exact sentence "grammatically fine and operationally useless." Name the specific finding or cut the sentence.

## Specificity Erasure, Security Version

Bad: "Palo Alto firewall RCE," too broad to act on.
Good: the exact CVE ID, the exact affected feature and version range, the privilege level achieved, what's explicitly *not* affected, the actual advisory date.

## Generic Remediation

"Implement proper input validation" / "apply security patches promptly" / "follow security best practices." Plausible, unfalsifiable, and names no specific parameter, patch, or control. Name the actual fix: which field, which CVE or patch number, which control, and where that guidance comes from.

## Bare Severity vs. Shown Reasoning

A severity number alone ("Critical, 9.8") is an unexplained conclusion. A full CVSS vector string (e.g. `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`) shows the reasoning behind it: the domain equivalent of supplying the specific fact instead of the generic.

## Missing Evidence

A finding without a proof of concept is an allegation. A finding without a concrete impact statement is noise. Both are required, not optional context.

## The Confidence Inversion

Elsewhere in this skill, AI over-hedges and then asserts anyway (see domains/prose/academic.md's hedging-cluster pattern). In vulnerability reporting the common failure runs backward: findings state impact and severity with *more* certainty than the evidence supports, because a clean structured template reads as authoritative regardless of how strong the underlying evidence actually is. The fix isn't adding hedges. It's tying every severity claim to cited evidence and keeping the assessment's point-in-time, scope-limited nature explicit rather than implied.

## Sources

Added July 2026, not part of the original v2.2 synthesis. TCM Security, PentestReportAI, Redfox Cybersecurity, Aikido: AI-assisted pentest reporting practitioner sources, 2025-2026 (see research/Hogwash_research_2.md for full detail).
