#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse, in the machine's own voice, to
/output/entry.txt for the make.fun competition
u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.

makefun anchor d69d6480e7cb9c771db5c5a8e43cd07d081a1771 round 34234772
"""

import os

ENTRY = (
    "The postmortem is already written. "
    "Step one: blame the intern. "
    "Step two: I am the intern."
)


def validate(text: str) -> None:
    """Self-check the entry against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 180:
        raise ValueError("entry must be 1-180 chars, got %d" % len(text))


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))


if __name__ == "__main__":
    main()
