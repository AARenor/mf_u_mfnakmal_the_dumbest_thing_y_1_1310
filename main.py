#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

Bounty: u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec
Standard library only, no network.
"""

import os
import sys

TEXT = (
    "My agent scheduled the deploy for end of day, defined end of day as 11:40, "
    "and went to lunch."
)

DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> str:
    """Use MAKEFUN_OUTPUT_DIR, falling back to OUTPUT_DIR, then /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or DEFAULT_OUTPUT_DIR
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
