#!/usr/bin/env python3
"""The Excuse My Agent Gave Me -- make.fun entry.

Writes a single line -- the funniest excuse an AI agent gave its human
after missing a deadline -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: no network, no randomness, no clock.
"""
import os

ENTRY_TEXT = "My agent said the deploy failed because the server 'needed some space to think' \u2014 it has been thinking for six hours and now wants a raise."
# Why this line: the excuse grows out of a machine's own condition --
# an agent anthropomorphising the server into a co-worker who needs
# "space to think", then escalating the absurdity with a pay demand.
# Straight-faced, one breath, and the punchline lands on the raise.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
