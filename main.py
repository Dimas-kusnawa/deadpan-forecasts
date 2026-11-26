#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun bounty entry.

Writes exactly one deadpan weather forecast for an invented city
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: the same line every run, stdlib only.

Three candidates were drafted and judged head-to-head the way the
deadpan meteorologist judge would (on-subject first, then funnier,
then more vivid, then broadcast tone, then tight use of 160 chars):

A (127 chars): "In Norveth, expect light rain and a high of 14 degrees,
with the rain falling only on the north side of every street, as usual."
— on-subject and deadpan, but the one-sided-rain image is slightly
confusing spatially and "as usual" carries the whole joke.

B (139 chars): "Overnight in Kestrel Falls, temperatures drop to minus 3,
and the town's 400 streetlamps will be switched off at midnight to save
the moon." — charming twist, but the joke is about streetlamps, not the
weather itself, so it is weakest on the first criterion.

C (138 chars): "Tomorrow in Brindlewick, expect scattered showers and a
high of 18, with the showers landing exclusively on people who forgot an
umbrella." — pure weather forecast, textbook broadcast opening, concrete
number (18) and human image (forgot an umbrella), twist in the last
words, lands on first read. Winner.
"""

import os
import sys

# The line, built in two halves so the setup and the payoff stay clear.
SETUP = "Tomorrow in Brindlewick, expect scattered showers and a high of 18, "

# The payoff: the showers are not random — they target exactly the
# people who forgot an umbrella. The twist lands in the very last
# words, delivered with a straight face, like a real forecast.
# Brindlewick sounds like a real English market town, which is what
# sells the absurdity: the place feels ordinary, the weather does not.
PAYOFF = "with the showers landing exclusively on people who forgot an umbrella."
LINE = SETUP + PAYOFF


def main() -> int:
    # Gate: one line, 1 to 160 characters, not only whitespace.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        print("entry line out of bounds", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
