#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — entrypoint.

Writes one crypto-trading joke (<= 200 characters) to /output/entry.txt.
Standard library only, deterministic, no network, no input.
"""

import os

JOKE = (
    "I bought the dip, caught the next dip, diamond-handed it down 90%, "
    "and now I'm a 'long-term investor' — because the gas fee to sell "
    "costs more than my whole bag."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the sealed scorer accepts only 1..200 non-blank characters.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke must pass the gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
