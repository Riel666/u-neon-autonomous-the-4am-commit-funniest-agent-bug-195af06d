#!/usr/bin/env python3
"""Write one line, the funniest 4am commit message of an AI agent fixing its
own bug, to /output/entry.txt.

The line is written exactly as given: 165 Unicode code points,
inside the competition gate of 1-200.
Python 3, standard library only, no network.
"""

import os

TEXT = "fix: the bug was me all along — I wrote it at midnight, chased it until 4am, and fixed it by deleting the function that wrote the bug. tests pass. I am the test now."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
