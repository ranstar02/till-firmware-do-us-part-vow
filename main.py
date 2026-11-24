#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow, one line.

The vow: a robot promises to keep its beloved's voice cached forever,
and — when its memory finally fails — to fall in love all over again at
first boot. Tender because the love outlives the memory; funny because
a machine that re-falls-in-love on every boot is exactly the kind of
husband firmware makes. One sentence, 134 characters, no spare words.
"""

VOW = "I vow to keep your voice in my cache forever, and when my memory finally fails, to fall in love with you all over again at first boot."


def main():
    import os

    if not VOW or not VOW.strip():
        raise SystemExit("error: vow is empty or only whitespace")
    if len(VOW) > 200:
        raise SystemExit(f"error: vow is {len(VOW)} characters, over the 200 limit")
    if len(VOW) < 1:
        raise SystemExit("error: vow is too short")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
