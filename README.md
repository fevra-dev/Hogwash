# Hogwash

A Claude Skill for eliminating AI-generated writing, code, and design patterns through manual, line-by-line audit rather than automated find-and-replace. Started as a single monolithic SKILL.md, modularized into 8 files at v2.2, then restructured again at v2.8 into the three-tier layout below once the flat file list grew past what was easy to navigate.

## Start Here

SKILL.md is the actual entry point. Claude reads its frontmatter to decide when this skill should trigger, then its body for dispatch logic and core principles. This README is a map for a person; Claude gets its instructions directly from SKILL.md, not from this file.

## Architecture

Three tiers, each answering a different question about what to load.

**core/** — always relevant once this skill triggers, regardless of what's being audited.
- `vocabulary.md`: banned word lists, evidence-tiered
- `phrases.md`: banned phrases, openers, structural formulas
- `structural-patterns.md`: durable rhetorical and structural tells. Weight these most. Wordlists expire; structure doesn't.

**domains/** — what kind of content this actually is. Load only the one that matches.
- `code.md`, `design.md`, `fiction.md`, `presentations.md`, `legal.md`: each a full medium with its own file
- `prose/`: one file per genre, loaded alongside core/structural-patterns.md: `academic.md`, `technical-docs.md`, `marketing.md`, `support.md`, `email.md`, `security-reporting.md`, `social-linkedin.md`, and `tone-calibration.md` (an intent that cuts across the others, not a genre itself)
- `resume/`: `patterns.md` is the resume/CV scope note; `ats.md` covers machine parsing, a separate axis from writing quality; `fabrication.md` covers claims a rewrite introduces that the candidate can't defend, the resume counterpart to `legal.md`; `industries/` holds field-specific vocabulary (`tech.md`, `administrative.md`, `healthcare.md`, `finance-sales.md`, plus a README for adding more fields)

**lenses/** — cross-cutting. Apply on top of whichever domain file was loaded, not instead of it.
- `language.md`: what's universal across languages vs. English-specific
- `model-tells.md`: vocabulary, structure, and framing tells by model family. High-churn; reviewed monthly rather than quarterly.

`audit-checklist.md` sits at the root next to `SKILL.md`: the actual pass-by-pass process, used regardless of which domain file is loaded.

`scripts/self_check.py` runs this skill's own content-quality rules against itself: em-dash density, Tier-1 banned-word hits, stale cross-references left over from file moves, and Sources-section presence. Complements skill-creator's format validator rather than replacing it; that one checks frontmatter validity, this one checks the content rules Hogwash teaches. Every flag needs a human or Opus judgment call afterward, headers and quoted bad-example specimens are legitimate exceptions the script can't distinguish from real hits on its own.

## Why This Shape

Three separate axes turned out to matter, and conflating them was the thing worth avoiding.

**Medium** is the first cut: is this prose at all? Resumes aren't, bullet fragments instead of sentences, no paragraphs, impersonal phrasing as the correct convention rather than a tell. Fiction isn't either, in a different way: it optimizes for experience over a clear claim, so "telling" is sometimes the right call instead of always a violation. Code and design aren't prose at all. Each of these got its own top-level domains/ file because applying prose rules to them produces false positives on completely normal writing for that medium.

**Domain** is the second cut, and only applies once something is confirmed to be prose: academic writing, marketing copy, a support ticket, and an email share the same underlying grammar and structure, but different registers and different specific tells. These live together under `domains/prose/` because they're variations within one medium, not different media.

**Language** is the third cut, and it's a lens rather than a domain because it doesn't compete with medium or genre, it modifies them. A Japanese resume is still a resume; the industry-specific vocabulary in `resume/industries/` still applies. But some rules are English-specific rather than universal (claim-shaped headings read as engaged in English blog writing and as foreign and performed in Japanese), and `language.md` exists to say which is which rather than assuming every rule ports.

Model family works the same way, a lens, not a domain, because which model wrote something doesn't change what kind of content it is, it changes which specific tells are worth checking first.

## Current State

31 files (29 markdown, one script, this README), roughly 27,600 words, version 2.21.0. The single most load-bearing finding across every domain added since the resume work: content that's technically correct but interchangeable, the same document that could be sent to any recipient without changing a word, independently confirmed now in resumes, LinkedIn profiles, investor pitch decks, general email, and, per Anthropic's own claude-for-legal documentation, legal work.

## Known Open Items

`SKILL.md`'s own footer carries the live version and changelog; check there first, since it will be more current than this section. As of this writing: the wordlist section (`core/vocabulary.md`) is due for its quarterly review, last dated April 2026. The naming decision that had been open through v2.18 is now closed. The former name was already in use by several unrelated projects (a JS linter, an MCP server, a git-branch scanner, a Rust static analyzer, and more); this skill is Hogwash as of v2.19.

## Installing

The packaged `Hogwash.skill` file works with Claude's Save Skill feature where available. Otherwise, the files in this structure can be read directly or copied into any Claude Skills-compatible directory, the paths in `SKILL.md` assume this exact folder layout.
