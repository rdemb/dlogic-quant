#!/usr/bin/env python3
"""Normalize public prose and report formulaic patterns.

This tool deliberately makes only low-risk mechanical edits. It removes
Unicode dash characters and ellipses from public-facing prose, while the
higher-level sentence rewrites remain a manual editorial task.
"""
from __future__ import annotations

import argparse
import pathlib
import re
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]

INCLUDE_SUFFIXES = {".md", ".html", ".yml", ".yaml"}
EXCLUDED_PARTS = {
    ".git",
    ".github",
    "assets",
    "tools",
    "vendor",
    "_site",
}

REPLACEMENTS = {
    "\u2014": "-",  # em dash
    "\u2013": "-",  # en dash
    "\u2026": "...",  # ellipsis
    "\u00a0": " ",  # non-breaking space
}

AUDIT_PATTERNS = {
    "em_dash": re.compile("\u2014"),
    "en_dash": re.compile("\u2013"),
    "ellipsis": re.compile("\u2026"),
    "formulaic_to_nie": re.compile(r"\bTo nie (?:jest|był|była|było|są)\b", re.I),
    "formulaic_nie_lecz": re.compile(r"\bnie\b[^\n.!?]{0,100}\blecz\b", re.I),
    "formulaic_transition": re.compile(r"\bTo prowadzi do\b", re.I),
    "formulaic_key": re.compile(r"\b(?:Najważniejsz\w+|Kluczow\w+)\b", re.I),
}


def iter_public_files() -> list[pathlib.Path]:
    paths: list[pathlib.Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in INCLUDE_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS for part in rel.parts):
            continue
        paths.append(path)
    return sorted(paths)


def normalize(text: str) -> str:
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    # Avoid malformed spacing created by copied typography.
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    return text


def audit(paths: list[pathlib.Path]) -> tuple[Counter[str], dict[str, Counter[str]]]:
    totals: Counter[str] = Counter()
    by_file: dict[str, Counter[str]] = defaultdict(Counter)
    for path in paths:
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        for name, pattern in AUDIT_PATTERNS.items():
            count = len(pattern.findall(text))
            if count:
                totals[name] += count
                by_file[rel][name] += count
    return totals, by_file


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write low-risk normalizations")
    args = parser.parse_args()

    paths = iter_public_files()
    changed: list[str] = []

    if args.apply:
        for path in paths:
            old = path.read_text(encoding="utf-8")
            new = normalize(old)
            if new != old:
                path.write_text(new, encoding="utf-8")
                changed.append(str(path.relative_to(ROOT)))

    totals, by_file = audit(paths)

    print(f"PUBLIC_FILES={len(paths)}")
    print(f"CHANGED_FILES={len(changed)}")
    for rel in changed:
        print(f"CHANGED {rel}")

    print("AUDIT_TOTALS")
    for name in sorted(AUDIT_PATTERNS):
        print(f"{name}={totals[name]}")

    print("AUDIT_BY_FILE")
    for rel, counts in sorted(by_file.items()):
        summary = ", ".join(f"{name}:{counts[name]}" for name in sorted(counts))
        print(f"{rel} | {summary}")

    # Mechanical typography must be fully gone after --apply.
    if args.apply and any(totals[name] for name in ("em_dash", "en_dash", "ellipsis")):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
