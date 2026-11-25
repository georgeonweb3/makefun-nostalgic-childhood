#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory — make.fun entry.

Writes one sentence to /output/entry.txt:

    My grandfather let me sweep the sawdust in his workshop and
    paid me in nails I did not need, and I still keep one in my
    pocket because his hands are gone but the smell of cut wood
    still takes me back to his bench.

Why it lands: a grandfather's workshop, a child paid in nails he
did not need (setup), one nail kept in a pocket years later
(turn), and the smell of cut wood carrying the narrator back to
the bench (payoff). Three beats, concrete anchors throughout
(sawdust, nails, a pocket, cut wood, the bench), 213 characters
in a single clean sentence. The ache is loss held quietly, not
sentimentality: his hands are gone, the bench remains.

Python 3.13, standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "My grandfather let me sweep the sawdust in his workshop and "
    "paid me in nails I did not need, and I still keep one in my "
    "pocket because his hands are gone but the smell of cut wood "
    "still takes me back to his bench."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 280 characters, not only whitespace, and one sentence:
    # an embedded newline would break the single-sentence read.
    # Verified live: 213 characters, one sentence, no trailing newline.
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, gate wants 1-280"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single sentence"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on disk,
    # not the string in memory — confirm the bytes landed exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )


if __name__ == "__main__":
    main()
