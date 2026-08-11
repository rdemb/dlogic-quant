#!/usr/bin/env python3
"""Fail when the built site reintroduces forbidden editorial symbols.

Markdown renderers and SEO plugins can transform harmless-looking source text,
for example three ASCII dots, into Unicode typography. This audit inspects the
actual HTML artifact rather than relying only on source files.
"""
from __future__ import annotations

import argparse
import pathlib

FORBIDDEN = {
    "em dash": "—",
    "en dash": "–",
    "Unicode ellipsis": "…",
    "right arrow": "→",
    "left arrow": "←",
    "check mark": "✓",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=pathlib.Path, help="built Jekyll directory")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Rendered site directory not found: {root}")

    failures: list[tuple[pathlib.Path, str, int, str]] = []
    html_files = sorted(root.rglob("*.html"))

    for path in html_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, symbol in FORBIDDEN.items():
            count = text.count(symbol)
            if count:
                index = text.find(symbol)
                excerpt = text[max(0, index - 80): index + 81].replace("\n", " ")
                failures.append((path.relative_to(root), label, count, excerpt))

    print(f"RENDERED_HTML_FILES={len(html_files)}")
    if not failures:
        print("RENDERED_EDITORIAL_AUDIT=PASS")
        return 0

    print("RENDERED_EDITORIAL_AUDIT=FAIL")
    for path, label, count, excerpt in failures:
        print(f"{path} | {label}={count} | {excerpt}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
