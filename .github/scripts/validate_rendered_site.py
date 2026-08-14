#!/usr/bin/env python3
"""Validate the built Jekyll artifact, publication boundary and local links."""
from __future__ import annotations

import argparse
import pathlib
from collections import Counter
from dataclasses import dataclass, field
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

FORBIDDEN_SYMBOLS = {
    "em dash": "—",
    "en dash": "–",
    "Unicode ellipsis": "…",
    "right arrow": "→",
    "left arrow": "←",
    "check mark": "✓",
}
FORBIDDEN_EXACT_PATHS = {
    ".gitignore",
    "_config.yml",
    "EDITORIAL_STYLE.md",
    "README.md",
}
FORBIDDEN_TOP_LEVEL_DIRS = {
    ".github",
    "tools",
    "vendor",
}
FORBIDDEN_SUFFIXES = {
    ".bat",
    ".env",
    ".md",
    ".py",
    ".sh",
    ".yaml",
    ".yml",
}


@dataclass
class Document:
    path: pathlib.Path
    ids: Counter[str] = field(default_factory=Counter)
    references: list[tuple[int, str, str, str]] = field(default_factory=list)


class DocumentParser(HTMLParser):
    def __init__(self, path: pathlib.Path) -> None:
        super().__init__(convert_charrefs=True)
        self.document = Document(path=path)

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = {name.lower(): value for name, value in attrs}
        line, _ = self.getpos()

        element_id = values.get("id")
        if element_id:
            self.document.ids[element_id] += 1

        anchor_name = values.get("name")
        if tag.lower() == "a" and anchor_name and anchor_name != element_id:
            self.document.ids[anchor_name] += 1

        for attribute in ("href", "src"):
            value = values.get(attribute)
            if value:
                self.document.references.append(
                    (line, tag.lower(), attribute, value.strip())
                )


def parse_document(path: pathlib.Path) -> Document:
    parser = DocumentParser(path)
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    parser.close()
    return parser.document


def strip_baseurl(path: str, baseurl: str) -> str:
    normalized = "/" + baseurl.strip("/") if baseurl.strip("/") else ""
    if normalized and path == normalized:
        return "/"
    if normalized and path.startswith(normalized + "/"):
        return path[len(normalized):]
    return path


def resolve_local_target(
    *,
    root: pathlib.Path,
    source: pathlib.Path,
    url_path: str,
    baseurl: str,
) -> pathlib.Path | None:
    decoded = unquote(url_path)
    if decoded.startswith("/"):
        decoded = strip_baseurl(decoded, baseurl)
        candidate = root / decoded.lstrip("/")
    else:
        candidate = source.parent / decoded

    try:
        candidate = candidate.resolve()
        candidate.relative_to(root)
    except (OSError, ValueError):
        return None

    options: list[pathlib.Path]
    if decoded.endswith("/") or candidate.is_dir():
        options = [candidate / "index.html"]
    else:
        options = [candidate]
        if not candidate.suffix:
            options.extend([candidate.with_suffix(".html"), candidate / "index.html"])

    for option in options:
        if option.is_file():
            return option.resolve()
    return None


def is_forbidden_artifact(relative: pathlib.PurePosixPath) -> bool:
    if relative.as_posix() in FORBIDDEN_EXACT_PATHS:
        return True
    if relative.parts and relative.parts[0] in FORBIDDEN_TOP_LEVEL_DIRS:
        return True
    if relative.suffix.lower() in FORBIDDEN_SUFFIXES:
        return True
    return any(part.startswith(".env") for part in relative.parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=pathlib.Path, help="built Jekyll directory")
    parser.add_argument(
        "--baseurl",
        default="",
        help="configured Jekyll baseurl, for example /dlogic-quant",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Rendered site directory not found: {root}")

    failures: list[str] = []
    all_files = sorted(path for path in root.rglob("*") if path.is_file())

    for path in all_files:
        relative = pathlib.PurePosixPath(path.relative_to(root).as_posix())
        if is_forbidden_artifact(relative):
            failures.append(f"publication-boundary | leaked artifact: {relative}")

    html_files = [path for path in all_files if path.suffix.lower() == ".html"]
    documents: dict[pathlib.Path, Document] = {}

    for path in html_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(root).as_posix()

        for label, symbol in FORBIDDEN_SYMBOLS.items():
            count = text.count(symbol)
            if count:
                failures.append(
                    f"typography | {relative} | {label}={count}"
                )

        document = parse_document(path)
        documents[path.resolve()] = document
        for element_id, count in document.ids.items():
            if count > 1:
                failures.append(
                    f"duplicate-id | {relative} | id={element_id!r} count={count}"
                )

    checked_references = 0
    for source_path, document in documents.items():
        source_relative = source_path.relative_to(root).as_posix()
        for line, tag, attribute, raw_value in document.references:
            if not raw_value or raw_value == "#":
                continue

            parsed = urlsplit(raw_value)
            scheme = parsed.scheme.lower()
            if scheme == "javascript":
                failures.append(
                    f"unsafe-url | {source_relative}:{line} | "
                    f"{tag}[{attribute}]={raw_value!r}"
                )
                continue
            if scheme or parsed.netloc or raw_value.startswith("//"):
                continue
            if not parsed.path:
                target = source_path
            else:
                target = resolve_local_target(
                    root=root,
                    source=source_path,
                    url_path=parsed.path,
                    baseurl=args.baseurl,
                )

            checked_references += 1
            if target is None:
                failures.append(
                    f"broken-link | {source_relative}:{line} | "
                    f"{tag}[{attribute}]={raw_value!r}"
                )
                continue

            fragment = unquote(parsed.fragment)
            if fragment and target.suffix.lower() == ".html":
                target_document = documents.get(target.resolve())
                if target_document is not None and fragment not in target_document.ids:
                    failures.append(
                        f"missing-fragment | {source_relative}:{line} | "
                        f"{raw_value!r} -> {target.relative_to(root).as_posix()}"
                    )

    print(f"PUBLISHED_FILES={len(all_files)}")
    print(f"RENDERED_HTML_FILES={len(html_files)}")
    print(f"LOCAL_REFERENCES_CHECKED={checked_references}")

    if failures:
        print(f"RENDERED_SITE_AUDIT=FAIL issues={len(failures)}")
        for failure in failures:
            print(failure)
        return 2

    print("PUBLICATION_BOUNDARY=PASS")
    print("LOCAL_LINK_AUDIT=PASS")
    print("RENDERED_SITE_AUDIT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
