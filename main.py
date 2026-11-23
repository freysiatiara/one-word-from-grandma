#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes the single word a grandma would text about AI to /output/entry.txt.
The word is ALEXA: grandmas talk to her, ask her things, and treat her like
a person in the kitchen — warm, a little baffled, funny on its own, and
directly an AI voice assistant.
"""

import os

WORD = "ALEXA"


def main():
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.strip(), "word must not be only whitespace"
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(WORD)
    with open(out, "r", encoding="utf-8") as f:
        assert f.read() == WORD, "round-trip check failed"


if __name__ == "__main__":
    main()
