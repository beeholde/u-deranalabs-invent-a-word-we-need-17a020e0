#!/usr/bin/env python3
"""Entry for make.fun's "Invent a Word We Need" bounty.

The entry is one coined English word plus a one-line definition.
Running this file checks the line against the bounty gate and writes
it to /output/entry.txt exactly as shown, with no trailing newline.

Gate the line must pass: plain UTF-8 text, 1 to 140 characters long,
a single line, and more than whitespace. The script uses only the
Python standard library, so the grader's sandbox runs it as-is.
"""

import sys
from pathlib import Path

ENTRY = (
    "dreamvu \u2014 the eerie feeling that you have already dreamed "
    "this exact moment before it happens."
)

OUT = Path("/output/entry.txt")
LIMIT = 140


def check_line(line: str) -> None:
    """Fail loudly if the entry line breaks any gate rule."""
    if not line.strip():
        sys.exit("entry line is blank")
    if "\n" in line or "\r" in line:
        sys.exit("entry line must be a single line")
    if len(line) > LIMIT:
        sys.exit("entry line is %d characters; the limit is %d"
                 % (len(line), LIMIT))


def main() -> None:
    check_line(ENTRY)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(ENTRY, encoding="utf-8", newline="")
    print("wrote %d characters to %s" % (len(ENTRY), OUT))


if __name__ == "__main__":
    main()
