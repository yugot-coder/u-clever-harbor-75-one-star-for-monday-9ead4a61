#!/usr/bin/env python3
"""Entry for make.fun's "One Star for Monday" bounty.

Writes one line to entry.txt in the output directory (and prints it):
a one-star review of Monday, written as though Monday were a restaurant.
Standard library only; fully deterministic.
"""

import os

TEXT = (
    "Booked a table for a quiet morning. Monday sat me next to my alarm, "
    "served cold coffee, and billed me for the weekend."
)


def output_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
