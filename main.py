"""One-Liner Laughs entry.

Writes a single original one-line joke to /output/entry.txt.

Deterministic: no clock, no randomness, no network, no model calls.
The line is 104 characters, one line, inside the 1-200 gate.
"""

from pathlib import Path

SETUP = "I asked the gym for a refund."
PUNCH = "They said my membership expired \u2014 just like my motivation, on January 3rd."


def build_joke() -> str:
    """Assemble the single joke line from its two beats.

    The setup asks the gym for a refund, which primes the reader for a
    membership-expiry date; the punch hands over exactly that date, but
    attaches it to the speaker's motivation instead of the membership,
    so the New Year resolution dies on January 3rd and the twist lands
    on the last three words. Nothing is trimmed from the middle: every
    word earns its place.
    """
    return f"{SETUP} {PUNCH}"


def main() -> None:
    """Write the joke to /output/entry.txt, exactly as the gate reads it.

    No trailing newline: the file holds the line alone, 104 characters
    of UTF-8, so the sealed scorer counts the joke itself and nothing
    else.
    """
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    line = build_joke()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"joke line is {len(line)} characters, must be 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("joke line must be a single line")
    # Write exactly the joke line: no trailing newline, so the file
    # holds one line of 1-200 characters and nothing else.
    output.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
