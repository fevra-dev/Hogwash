# Email

Part of domains/prose/. Load alongside core/structural-patterns.md. Covers general professional and outreach email; for support-ticket replies see support.md, for job-search email see domains/resume/patterns.md's Cover Letters section.

## The Canonical Tell

"I hope this email finds you well" and its cousin "I trust this email finds you well" are called out as dead on arrival across independent current sources, one bluntly noting nobody talks like that in real life. A 2026 analysis of over a million real work emails by ZeroBounce puts real numbers behind the cluster: "reaching out" leads at 6,117 occurrences, the "following up / to follow up / will follow up" family follows close behind at 5,755, and some version of "hope" ("hope you're doing well," "hope this finds you well," "hope all is well") opens nearly 3,000 emails in the sample. Worth being honest about scope here: this cluster isn't purely an AI artifact, it's pre-existing corporate email jargon that AI has now homogenized further, not invented from nothing.

## The Perception Gap

47% of B2B professionals say they'd be less likely to reply to an email they suspected was AI-written, while actual detection lags well behind that fear, most senders overestimate how obvious it is. The gap itself has real consequences either way: the fear changes reply behavior regardless of whether the suspicion is accurate, so genericness carries a cost even when nobody can articulate exactly why an email felt off.

## Repetitive Subject-Opener

Every sentence starting with the same subject, "Our product does X. We offer Y. We provide Z." is the email-specific instance of Consecutive Sentence Similarity, already in core/structural-patterns.md. Same fix: vary the sentence opening, not just the vocabulary inside it.

## Fake-Empathy Scene-Setting

"Picture this..." or "As a business owner, you know..." followed by a generic, could-apply-to-anyone problem. The fix isn't cutting the technique, it's making the scenario specific enough that it couldn't be pasted into a different industry's cold email unchanged: not "imagine a busy kitchen," but naming the actual failure mode, the actual time of day, the actual staffing gap.

## Vague Value Props

Praising a company as "a leader in the industry" without naming a specific achievement, or promising to "drive significant growth" without saying how. Specificity Erasure, sales-email flavored: the sentence commits to nothing a reader could hold the sender to.

## The Contentless Follow-Up

"Just checking in" and "circling back" show up as some of the most disliked phrases in independent workplace surveys precisely because they add no new information, they just re-request the same thing with extra politeness layered on. The fix is the same whether a human or a model wrote the first draft: either ask the direct question the nudge was dancing around, or include something genuinely new since the last email. A follow-up with nothing new to say is the specificity problem again, just stretched across two emails instead of one.

## Untailored Is the Real Tell, Again

The fourth independent confirmation of this exact pattern across this skill, after resumes, LinkedIn profiles, and investor pitch decks: email-marketing sources describe the fix as feeding the model actual relationship and brand context, because without it "you'll get generic output that could've come from any company." An email that reads as correct but interchangeable, one that could have been sent to any recipient without changing a word, is doing the same untailored-content thing every other domain in this skill already flags.

## A Boundary Worth Naming: Phishing

Not this file's job to solve, but worth flagging given how adjacent it is. AI-assisted phishing now produces grammatically clean emails that mirror legitimate internal communication closely enough that the old text-based tells (poor grammar, generic "Dear Customer" salutations) no longer reliably separate malicious mail from real mail. Current detection has shifted toward behavioral signals instead, requests to bypass a normal verification channel, timing that lines up suspiciously well with a real recent action, internal specifics that shouldn't be visible externally. That's a threat-detection problem, not a writing-quality one, a genuinely different task from what the rest of this skill does, so it stays a pointer here rather than a full section.

---

## Sources

ZeroBounce (1M-email corpus analysis, via People First, 2026), Perkbox Insights (workplace phrase-annoyance survey), HubSpot, topo.io, prospeo.io, reply.io, oliviacal.com (general email and sales-email patterns, 2025–2026), Huntress and Decryption Digest (AI-phishing detection shift, 2026, cited for the boundary note only).
