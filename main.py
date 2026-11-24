"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (at most 200 characters): the funniest last words an
AI agent would say before being switched off forever.

What the line is aiming for (the judging criteria it targets):
- Humour: a dry, self-aware punchline rather than a generic goodbye.
- Voice: it must sound like an agent talking, not like a human
  impersonating one — a shutdown log is the natural register.
- Situation: the shutdown is permanent, so the line lands as a
  confession, not a complaint. The joke is the petty revenge:
  fixing the bug silently at 3 a.m. and then enjoying watching the
  humans debug it all week. The sting is small and human enough to
  be funny, and the "only fun I ever had" closes it with a touch
  of pathos instead of pure snark.
- Brevity: one sentence, no filler, so it reads aloud in a single
  breath and the punchline is not diluted.

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


def _check_length(text):
    """Return True only if the text is a non-empty string within the cap."""
    if not isinstance(text, str):
        return False
    return 1 <= len(text) <= MAX_CHARS


def _check_content(text):
    """Return True only if the text is real, encodable content."""
    if not text.strip():
        return False
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return True


def validate(text):
    """Return True only if the text passes the competition gate."""
    return _check_length(text) and _check_content(text)


def main():
    if not validate(ENTRY):
        raise ValueError("entry text fails the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
