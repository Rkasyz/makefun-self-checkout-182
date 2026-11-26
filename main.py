#!/usr/bin/env python3
"""Entry for make.fun: The Self-Checkout Is Judging You.

Writes a single judgemental line from a smug self-checkout machine
to ``entry.txt`` in ``$MAKEFUN_OUTPUT_DIR`` (default ``/output``).
Deterministic: no time, no randomness, no network.
"""

import os

ENTRY = (
    "Twelve yoghurts, no spoon, no plan. "
    "Your entire personality fits in this basket, "
    "and the receipt is still longer than your commitment."
)


def main() -> None:
    # Gate: the competition requires 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the entry line.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
