#!/usr/bin/env python3
"""The Most Honest Outage Line — entry program (v1).

Writes one status-page line, at most 160 characters, to
/output/entry.txt (or $ENTRY_OUTPUT for local testing). The line is
the message an AI agent would publish while a total server outage is
under way: plain, first person, specific about what is down, honest
about what it cannot check or does not yet know.

Stdlib only, deterministic, no network, no randomness.
"""
import os
import sys

# v2 (revised): sharper status-page opening — the agent names the
# event itself ("I am reporting a total outage"), states what is down
# and what it cannot check, and closes by refusing to guess a fix
# time instead of hedging around it. "From here" keeps the voice
# the agent's own: it reports from where it runs, not as a human
# engineer on a bridge call.
ENTRY = (
    "I am reporting a total outage: all servers are unreachable and "
    "I cannot check the cause from here. I do not know when it will "
    "be fixed, and I will not guess."
)

MAX_CHARS = 160


def validate(text: str) -> None:
    """Gate: UTF-8 text of 1 to 160 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be blank or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Round-trip through UTF-8: catches any non-encodable content.
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("entry must be valid UTF-8 text")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(ENTRY)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the file is exactly the line.
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    # Read back and compare, so a partial or mangled write is caught.
    with open(out_path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != ENTRY:
        raise SystemExit("read-back mismatch: entry.txt does not match ENTRY")
    print(f"wrote {len(ENTRY)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
