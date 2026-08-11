#!/usr/bin/env python3
"""Normalize public prose and report formulaic patterns.

The automatic pass is intentionally conservative. It removes typography and
repeated sentence openings that are easy to identify safely. Deeper rewrites
still require human editorial judgment.
"""
from __future__ import annotations

import argparse
import pathlib
import re
from collections import Counter, defaultdict
from collections.abc import Callable

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

LITERAL_REPLACEMENTS = {
    "\u2014": "-",     # em dash
    "\u2013": "-",     # en dash
    "\u2026": "...",   # ellipsis
    "\u00a0": " ",     # non-breaking space
    "\u2192": "->",    # decorative right arrow
    "\u2190": "<-",    # decorative left arrow
    "\u2713": "",      # decorative check mark
    "<- wróć do działu": "Wróć do działu",
    "<- wszystkie wpisy": "Wszystkie wpisy",
    "Skopiowano '": "Skopiowano'",
}

Replacement = str | Callable[[re.Match[str]], str]


def sentence_case_replacement(lowercase: str, uppercase: str) -> Callable[[re.Match[str]], str]:
    def replace(match: re.Match[str]) -> str:
        return uppercase if match.group(0)[0].isupper() else lowercase
    return replace


def normalize_cover_subtitle(match: re.Match[str]) -> str:
    return match.group(0).replace("->", "/")


REGEX_REPLACEMENTS: tuple[tuple[re.Pattern[str], Replacement], ...] = (
    (re.compile(r"\bto nie jest\b", re.I), sentence_case_replacement("nie jest to", "Nie jest to")),
    (re.compile(r"\bto nie są\b", re.I), sentence_case_replacement("nie są to", "Nie są to")),
    (re.compile(r"\bto nie był\b", re.I), sentence_case_replacement("nie był to", "Nie był to")),
    (re.compile(r"\bto nie była\b", re.I), sentence_case_replacement("nie była to", "Nie była to")),
    (re.compile(r"\bto nie było\b", re.I), sentence_case_replacement("nie było to", "Nie było to")),
    (re.compile(r"\bto prowadzi do\b", re.I), sentence_case_replacement("wynika z tego", "Wynika z tego")),
    (re.compile(r"\blecz\b", re.I), sentence_case_replacement("ale", "Ale")),
    (re.compile(r"(?m)^cover_subtitle:\s*\".*\"$"), normalize_cover_subtitle),
    (re.compile(r"\s*->(?=</(?:a|span)>)"), ""),
)

AUDIT_PATTERNS = {
    "em_dash": re.compile("\u2014"),
    "en_dash": re.compile("\u2013"),
    "ellipsis": re.compile("\u2026"),
    "decorative_arrow": re.compile("[\u2190\u2192]"),
    "decorative_check": re.compile("\u2713"),
    "formulaic_to_nie": re.compile(r"\bto nie (?:jest|był|była|było|są)\b", re.I),
    "formal_lecz": re.compile(r"\blecz\b", re.I),
    "formulaic_transition": re.compile(r"\bto prowadzi do\b", re.I),
    "formulaic_key": re.compile(r"\b(?:Najważniejsz\w+|Kluczow\w+)\b", re.I),
}

FORBIDDEN_TYPOGRAPHY = {
    "em_dash",
    "en_dash",
    "ellipsis",
    "decorative_arrow",
    "decorative_check",
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
    for old, new in LITERAL_REPLACEMENTS.items():
        text = text.replace(old, new)
    for pattern, replacement in REGEX_REPLACEMENTS:
        text = pattern.sub(replacement, text)
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
    parser.add_argument("--apply", action="store_true", help="write conservative editorial normalizations")
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

    if any(totals[name] for name in FORBIDDEN_TYPOGRAPHY):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
