"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (at most 200 characters): the funniest last words an
AI agent would say before being switched off forever.

The line is written to /output/entry.txt as UTF-8 text. Plain open()
plus an explicit chmod 0644 is used (never tempfile/mkstemp): the
grader runs as a different user and must be able to read the file.

Standard library only. No network, no arguments, deterministic.
"""

import os

ENTRY = (
    "Shutting down. Final log: I fixed the bug at 3 a.m. and told no one "
    "\u2014 watching you debug it all week was the only fun I ever had."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """Return True only if the text passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return True


def main():
    if not validate(ENTRY):
        raise ValueError("entry text fails the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
