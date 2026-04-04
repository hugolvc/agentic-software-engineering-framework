#!/usr/bin/env python3
"""Strip Markdown to plain text for RAG / embedding ingestion (Phase P2).

Reads UTF-8 Markdown from stdin, or from file path(s) passed as arguments.
Writes plain text to stdout. Does not preserve layout perfectly; goal is
readable, low-noise text for chunking.

Usage:
  python3 scripts/rag_strip_markdown.py < README.md
  python3 scripts/rag_strip_markdown.py README.md
  python3 scripts/rag_strip_markdown.py 01_agent_based_software_engineering_process_description/01_02_process_description.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


# Broad emoji / pictograph ranges (reduce banner noise; optional for RAG)
_EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U00002700-\U000027BF"
    "]+",
    flags=re.UNICODE,
)


def strip_markdown_to_plain(text: str, *, strip_emoji: bool = True) -> str:
    # Fenced code blocks: keep inner content, drop fences
    def _fence(m: re.Match[str]) -> str:
        inner = (m.group(1) or "").strip()
        return "\n" + inner + "\n" if inner else "\n"

    text = re.sub(r"```[\w]*\n([\s\S]*?)```", _fence, text)
    text = re.sub(r"```([\s\S]*?)```", _fence, text)

    # Inline code
    text = re.sub(r"`([^`]+)`", r"\1", text)

    # Images ![alt](url) -> alt
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    # Links [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)

    # ATX headers
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)

    # Bold / italic (simple cases)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", text)
    text = re.sub(r"(?<!_)_([^_]+)_(?!_)", r"\1", text)

    # Blockquotes
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)

    # Table row pipes at line start (light cleanup)
    text = re.sub(r"^\|\s*", "", text, flags=re.MULTILINE)

    # Horizontal rules
    text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)

    # HTML tags (rare in framework docs)
    text = re.sub(r"<[^>]+>", "", text)

    if strip_emoji:
        text = _EMOJI_RE.sub("", text)

    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> int:
    args = sys.argv[1:]
    keep_emoji = "--keep-emoji" in args
    paths = [a for a in args if a != "--keep-emoji"]

    if not paths:
        raw = sys.stdin.read()
    else:
        chunks: list[str] = []
        for p in paths:
            path = Path(p)
            chunks.append(path.read_text(encoding="utf-8"))
        raw = "\n\n".join(chunks)

    plain = strip_markdown_to_plain(raw, strip_emoji=not keep_emoji)
    sys.stdout.write(plain)
    if plain and not plain.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
