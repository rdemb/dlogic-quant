#!/usr/bin/env python3
"""Apply safe editorial normalizations without touching indentation or code layout."""
from __future__ import annotations

import argparse
import pathlib
import re
from collections import Counter, defaultdict
from collections.abc import Callable

ROOT = pathlib.Path(__file__).resolve().parents[1]
INCLUDE_SUFFIXES = {".md", ".html", ".yml", ".yaml"}
EXCLUDED_PARTS = {".git", ".github", "assets", "tools", "vendor", "_site"}

Replacement = str | Callable[[re.Match[str]], str]


def preserve_case(lowercase: str, uppercase: str) -> Callable[[re.Match[str]], str]:
    def replace(match: re.Match[str]) -> str:
        return uppercase if match.group(0)[0].isupper() else lowercase
    return replace


def cover_subtitle(match: re.Match[str]) -> str:
    return match.group(0).replace("→", "/").replace("->", "/")


REPLACEMENTS: tuple[tuple[re.Pattern[str], Replacement], ...] = (
    (re.compile(r"[ \t]*[—–][ \t]*"), " - "),
    (re.compile("…"), "..."),
    (re.compile("\u00a0"), " "),
    (re.compile(r"(?m)^cover_subtitle:\s*\".*\"$"), cover_subtitle),
    (re.compile(r"\s*→(?=</(?:a|span)>)"), ""),
    (re.compile(r"←\s*wróć do działu", re.I), "Wróć do działu"),
    (re.compile(r"←\s*wszystkie wpisy", re.I), "Wszystkie wpisy"),
    (re.compile(r"\bto nie jest\b", re.I), preserve_case("nie jest to", "Nie jest to")),
    (re.compile(r"\bto nie są\b", re.I), preserve_case("nie są to", "Nie są to")),
    (re.compile(r"\bto nie był\b", re.I), preserve_case("nie był to", "Nie był to")),
    (re.compile(r"\bto nie była\b", re.I), preserve_case("nie była to", "Nie była to")),
    (re.compile(r"\bto nie było\b", re.I), preserve_case("nie było to", "Nie było to")),
    (re.compile(r"\bto prowadzi do\b", re.I), preserve_case("wynika z tego", "Wynika z tego")),
    (re.compile(r"\blecz\b", re.I), preserve_case("ale", "Ale")),
    (re.compile("✓"), ""),
    (re.compile("→"), "->"),
    (re.compile("←"), "<-"),
)

AUDIT_PATTERNS = {
    "em_dash": re.compile("—"),
    "en_dash": re.compile("–"),
    "ellipsis": re.compile("…"),
    "decorative_arrow": re.compile("[←→]"),
    "decorative_check": re.compile("✓"),
    "formulaic_to_nie": re.compile(r"\bto nie (?:jest|są|był|była|było)\b", re.I),
    "formal_lecz": re.compile(r"\blecz\b", re.I),
    "formulaic_transition": re.compile(r"\bto prowadzi do\b", re.I),
    "formulaic_key": re.compile(r"\b(?:Najważniejsz\w+|Kluczow\w+)\b", re.I),
}

FORBIDDEN = {"em_dash", "en_dash", "ellipsis", "decorative_arrow", "decorative_check"}


def iter_public_files() -> list[pathlib.Path]:
    result: list[pathlib.Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in INCLUDE_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS for part in rel.parts):
            continue
        result.append(path)
    return sorted(result)


def normalize(text: str) -> str:
    for pattern, replacement in REPLACEMENTS:
        text = pattern.sub(replacement, text)
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
    parser.add_argument("--apply", action="store_true")
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

    return 2 if any(totals[name] for name in FORBIDDEN) else 0


if __name__ == "__main__":
    raise SystemExit(main())
