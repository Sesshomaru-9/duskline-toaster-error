#!/usr/bin/env python3
"""Duskline Toaster — the funniest toaster error message.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13 standard library only.
"""

import os
from pathlib import Path

ENTRY_TEXT = "Your toast is ready. It is also on fire. I opened a window and will deny everything."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    # Never write into the repo: the grader sandbox mounts it read-only.
    repo_dir = Path(__file__).resolve().parent
    if output_dir.resolve().is_relative_to(repo_dir.resolve()):
        raise SystemExit("refusing to write into the repository directory")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
