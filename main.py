#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Entry: a single canoe emoji -- a quiet mountain lake at dawn,
the postcard of a dream vacation, wordless.
Writes exactly one emoji to /output/entry.txt, no trailing newline.
"""
import os

ENTRY = "\U0001F6F6"  # 🛶 canoe

def main():
    # Gate self-check: entry must be 1-8 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 8 and ENTRY.strip(), "entry violates the 1-8 char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
