#!/usr/bin/env python3
"""
self_check.py — Hogwash's own content-quality check, run against itself.

Complements skill-creator's quick_validate.py, which checks frontmatter
format validity. This script checks the content-quality rules Hogwash
itself teaches: em-dash density, banned-vocabulary hits, stale cross-
references left over from file moves, and Sources-section presence.

Usage: python3 scripts/self_check.py [path-to-skill-root]
Defaults to the directory this script's parent folder lives in.
"""

import glob
import os
import re
import sys

TIER1_WORDS = [
    "delve", "utilize", "leverage", "leveraging", "leveraged", "seamless",
    "robust", "comprehensive", "foster", "fostering", "showcase",
    "underscore", "underscores", "harness", "unleash", "embark",
    "crucial", "meticulous", "commendable", "boast", "boasts", "realm",
    "tapestry", "testament to", "landscape", "in today's world",
    "in the ever-evolving", "navigate the complexities", "it's worth noting",
]

STALE_PATHS = [
    "vocabulary.md", "phrases.md", "structural-patterns.md",
    "code-patterns.md", "domain-patterns.md", "design-patterns.md",
    "language-notes.md", "resume-patterns.md", "resume-industries.md",
    "model-tells.md",
]

# Files that are process/methodology or list-format content rather than
# claims needing external sourcing. Flagged as informational, not errors.
SOURCES_EXEMPT = {"audit-checklist.md", "README.md", "SKILL.md"}

# Repo directories that sit alongside the skill but aren't part of it: the
# ADR set, the raw research rounds, and repo tooling. Their prose is not
# written to these rules, so scanning them buries the real signal.
EXCLUDED_DIRS = {"adr", "research", ".githooks", "node_modules", ".git"}

# Repo-root files that belong to the repository rather than the skill.
# CLAUDE.md is agent configuration and ships with no skill bundle.
EXCLUDED_FILES = {"CLAUDE.md"}


STRUCTURAL_LINE = re.compile(r"^\s*([-*+]|\d+\.|#{1,6}|\||>)\s*")


def em_dash_density(text):
    """Counted over flowing prose only, per core/structural-patterns.md.

    Reference-list labels, headings, and table cells use the
    `- **Term** - definition` construction as an ordinary documentation
    convention, and that section exempts them explicitly. Counting them
    against a whole-document word count inflates the rate badly: measured
    against a 225-file corpus, roughly 60% of a naive flag list was this
    artifact rather than a property of the writing. Numerator and
    denominator both come from prose lines so they stay comparable.
    """
    prose = "\n".join(
        line for line in text.split("\n")
        if line.strip() and not STRUCTURAL_LINE.match(line)
    )
    words = len(prose.split())
    dashes = prose.count("\u2014")
    rate = (dashes * 1000 / words) if words else 0
    return dashes, words, rate


def find_stale_paths(text):
    hits = []
    for name in STALE_PATHS:
        for m in re.finditer(r'(?<![\w/.])' + re.escape(name), text):
            line_no = text[: m.start()].count("\n") + 1
            hits.append((name, line_no))
    return hits


def find_banned_words(text):
    hits = []
    for word in TIER1_WORDS:
        for m in re.finditer(r'(?i)\b' + re.escape(word) + r'\b', text):
            line_no = text[: m.start()].count("\n") + 1
            hits.append((word, line_no))
    return hits


# Language that signals a research doc is proposing a change to the skill.
# Three times this session, research produced a merge recommendation that
# never landed in the shipped files, and the gap was invisible without
# diffing the two by hand. A doc containing any of these owes a ## Ship
# Status ledger reconciling each recommendation, or the check keeps flagging.
RECO_MARKERS = [
    "worth adding", "worth considering", "consider adding", "should add",
    "should ship", "not shipped", "not yet in", "isn't in", "aren't in",
    "add to", "merge into", "flagged for your call", "worth pursuing",
    "recommend adding", "belongs in", "hasn't shipped", "never shipped",
]
SHIP_LEDGER_HEADING = "## Ship Status"


def scan_research_reconciliation(root):
    """Flag research docs whose recommendations have no reconciliation ledger.

    Heuristic, not a parser: a hit means 'this doc proposes changes and
    hasn't recorded whether they shipped', which is a prompt to reconcile,
    not a verdict. Docs with a ## Ship Status section are assumed handled;
    the human writing that section is the actual reconciliation step.
    """
    research_dir = os.path.join(root, "research")
    results = []
    if not os.path.isdir(research_dir):
        return results
    for path in sorted(glob.glob(os.path.join(research_dir, "*.md"))):
        text = open(path, encoding="utf-8").read()
        low = text.lower()
        markers = sorted({m for m in RECO_MARKERS if m in low})
        has_ledger = SHIP_LEDGER_HEADING.lower() in low
        if markers and not has_ledger:
            results.append((os.path.relpath(path, root), markers))
    return results


def check_description_length(skill_md_path):
    text = open(skill_md_path, encoding="utf-8").read()
    m = re.search(r'description:\s*"(.*?)"\n', text, re.DOTALL)
    if not m:
        return None
    return len(m.group(1))


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), ".."
    )
    root = os.path.abspath(root)
    md_files = sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True))
    md_files = [
        p for p in md_files
        if not EXCLUDED_DIRS.intersection(os.path.relpath(p, root).split(os.sep))
        and os.path.basename(p) not in EXCLUDED_FILES
    ]

    print(f"Checking {len(md_files)} files under {root}\n")

    dash_flags, word_flags, path_flags, sources_missing = [], [], [], []

    for path in md_files:
        rel = os.path.relpath(path, root)
        text = open(path, encoding="utf-8").read()

        dashes, words, rate = em_dash_density(text)
        if rate > 6:
            dash_flags.append((rel, dashes, words, rate))

        banned = find_banned_words(text)
        if banned:
            word_flags.append((rel, banned))

        stale = find_stale_paths(text)
        if stale:
            path_flags.append((rel, stale))

        base = os.path.basename(rel)
        if base not in SOURCES_EXEMPT and "## Sources" not in text:
            sources_missing.append(rel)

    print("=== Em-dash density above 6/1,000 words ===")
    print("(Manually verify: headers, reference-list labels, and table cells")
    print(" are an established exemption in this skill, not flowing prose.)")
    if dash_flags:
        for rel, d, w, r in sorted(dash_flags, key=lambda x: -x[3]):
            print(f"  {rel}: {d}/{w} words = {r:.1f} per 1000")
    else:
        print("  none")

    print("\n=== Possible Tier-1 banned-word hits ===")
    print("(Manually verify: citing a banned word as an example is fine,")
    print(" using it in the skill's own connective prose is not.)")
    if word_flags:
        for rel, hits in word_flags:
            words_str = ", ".join(f"{w} (L{n})" for w, n in hits)
            print(f"  {rel}: {words_str}")
    else:
        print("  none")

    print("\n=== Stale cross-references to pre-restructure filenames ===")
    if path_flags:
        for rel, hits in path_flags:
            for name, line_no in hits:
                print(f"  {rel}:{line_no}: bare '{name}'")
    else:
        print("  none")

    print("\n=== Files with no Sources section ===")
    print("(Informational. vocabulary.md's inline [E]/[D]/[W]/[C] tiers and")
    print(" audit-checklist.md's process content are legitimate exceptions;")
    print(" verify anything else here actually has no external claims to cite.)")
    if sources_missing:
        for rel in sources_missing:
            print(f"  {rel}")
    else:
        print("  none")

    print("\n=== Research docs with unreconciled recommendations ===")
    print("(A research doc that proposes changes owes a '## Ship Status'")
    print(" ledger recording whether each shipped. Without one, good")
    print(" material goes invisible. Add the ledger to clear the flag.)")
    reco = scan_research_reconciliation(root)
    if reco:
        for rel, markers in reco:
            print(f"  {rel}: proposes changes ({', '.join(markers[:4])}"
                  f"{'...' if len(markers) > 4 else ''}), no {SHIP_LEDGER_HEADING}")
    else:
        print("  none")

    skill_md = os.path.join(root, "SKILL.md")
    if os.path.exists(skill_md):
        length = check_description_length(skill_md)
        print(f"\n=== SKILL.md description field ===")
        if length is not None:
            flag = "  <- approaching the 1024 limit" if length > 900 else ""
            print(f"  {length} / 1024 characters{flag}")


if __name__ == "__main__":
    main()
