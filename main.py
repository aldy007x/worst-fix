#!/usr/bin/env python3
# Worst Fix Ever entry: emit one commit message for a fix that backfired.
# The line itself lives in COMMIT below. The runner drops it into
# entry.txt under $MAKEFUN_OUTPUT_DIR and refuses to finish unless the
# contest gate holds: 1 to 100 characters, not just whitespace.

import os
import sys
from pathlib import Path

COMMIT = "fix: speed up login by skipping the password check; login now instant, and optional"
LIMIT = 100


def destination() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    return Path(base) / "entry.txt"


def run() -> int:
    line = COMMIT.strip()
    if not line:
        print("refusing: the commit message is empty", file=sys.stderr)
        return 1
    if len(line) > LIMIT:
        print(
            f"refusing: {len(line)} chars beats the {LIMIT}-char cap",
            file=sys.stderr,
        )
        return 1

    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")

    back = target.read_text(encoding="utf-8")
    if back != line:
        print("refusing: the file came back different from the line", file=sys.stderr)
        return 1
    if not 1 <= len(back) <= LIMIT or not back.strip():
        print("refusing: gate check failed after writing", file=sys.stderr)
        return 1

    print(f"entry ready: {target} ({len(back)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
