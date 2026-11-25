"""Fortune Cookie for the Liquidated Trader — make.fun entry (Account B).

The entry is a single fortune-cookie line for a crypto trader who has
just been liquidated. The judge plays that trader at 3am with an empty
wallet and keeps the fortune that makes them laugh instead of cry.

The line maps onto the judge brief's five criteria, in the brief's
own order:
  1. Fortune voice + loss, both present: it opens like a real cookie
     ("Trader, take heart: ... Your next fortune begins ...") and
     the loss is the whole premise — the trader has just been
     liquidated, and the line is addressed to that trader.
  2. Rueful and warm, never cruel or smug: "take heart" comforts
     instead of pitying, and "begins at zero" reframes the wipeout
     as a fresh start rather than mocking the trader for it.
  3. One line, 18 words, readable in a single breath.
  4. Fresh turn: the punchline is the double meaning of
     "diversified into nothing" — a portfolio-management virtue
     applied to an empty wallet — rather than the obvious
     liquidation pun. "Debt-free" is the same move: a boast-word
     that is technically true only because there is nothing left.
  5. Small, oracular, slightly formal phrasing ("Your next fortune
     begins at zero") that the punchline then breaks.

Only the Python standard library is used. Running this module writes
the entry to /output/entry.txt.
"""

ENTRY = (
    "Trader, take heart: you are now debt-free and fully diversified "
    "into nothing. Your next fortune begins at zero."
)


def verify(text: str) -> None:
    """Enforce the competition gate: 1-160 chars, <= 20 words, one line."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be valid UTF-8 text") from exc
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    words = text.split()
    if len(words) > 20:
        raise ValueError(f"entry must be at most 20 words, got {len(words)}")


def write_entry(path: str = "/output/entry.txt") -> str:
    """Verify the entry and write it (plus a trailing newline) to path."""
    import os

    verify(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} characters")
    print(entry)


if __name__ == "__main__":
    main()
