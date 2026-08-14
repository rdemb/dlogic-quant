#!/usr/bin/env python3
"""Validate public source content without rewriting author files."""
from __future__ import annotations

import pathlib
import re
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]
INCLUDE_SUFFIXES = {".md", ".html", ".yml", ".yaml"}
EXCLUDED_PARTS = {".git", ".github", "assets", "vendor", "_site"}

AUDIT_PATTERNS = {
    "em_dash": re.compile("—"),
    "en_dash": re.compile("–"),
    "unicode_ellipsis": re.compile("…"),
    "decorative_arrow": re.compile("[←→]"),
    "decorative_check": re.compile("✓"),
    "formulaic_to_nie": re.compile(r"\bto nie (?:jest|są|był|była|było)\b", re.I),
    "formal_lecz": re.compile(r"\blecz\b", re.I),
    "formulaic_transition": re.compile(r"\bto prowadzi do\b", re.I),
    "formulaic_key": re.compile(r"\b(?:najważniejsz\w+|kluczow\w+)\b", re.I),
    "legacy_desk_markup": re.compile(r"\bdk-[a-z0-9-]+", re.I),
    "legacy_desk_dependency": re.compile(
        r"(?:site\.data\.desk|assets/js/desk\.js|window\.DESK)"
    ),
}
FORBIDDEN = {
    "em_dash",
    "en_dash",
    "unicode_ellipsis",
    "decorative_arrow",
    "decorative_check",
    "legacy_desk_markup",
    "legacy_desk_dependency",
}


def iter_public_sources() -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in INCLUDE_SUFFIXES:
            continue
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    totals: Counter[str] = Counter()
    by_file: dict[str, Counter[str]] = defaultdict(Counter)

    files = iter_public_sources()
    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT).as_posix()
        for name, pattern in AUDIT_PATTERNS.items():
            count = len(pattern.findall(text))
            if count:
                totals[name] += count
                by_file[relative][name] += count

    print(f"PUBLIC_SOURCE_FILES={len(files)}")
    print("EDITORIAL_AUDIT_TOTALS")
    for name in sorted(AUDIT_PATTERNS):
        print(f"{name}={totals[name]}")

    if by_file:
        print("EDITORIAL_AUDIT_BY_FILE")
        for relative, counts in sorted(by_file.items()):
            summary = ", ".join(
                f"{name}:{counts[name]}" for name in sorted(counts)
            )
            print(f"{relative} | {summary}")

    forbidden_total = sum(totals[name] for name in FORBIDDEN)
    if forbidden_total:
        print(f"EDITORIAL_SOURCE_AUDIT=FAIL forbidden={forbidden_total}")
        return 2

    print("EDITORIAL_SOURCE_AUDIT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
