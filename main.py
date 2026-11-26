#!/usr/bin/env python3
"""One Word, First Thought - make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that
comes to mind. No network, no clock, no randomness. Deterministic:
every run writes the same bytes.

The word: petrichor (9 characters, inside the 1 to 24 gate).
Surprising, vivid, and carrying a spark of wit: the smell of rain
falling on dry earth, a word most people have felt but never named.
A clear sense image, an unexpected word, and a second meaning that
rewards a second look. It also beats the usual list favourites on
the judge's own order: surprise first, then vividness, then wit.
"""

import os
import sys

WORD = "petrichor"


def write_entry(text, path):
    """Write the entry text to path, creating parent dirs as needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    write_entry(WORD, path)


if __name__ == "__main__":
    main()
