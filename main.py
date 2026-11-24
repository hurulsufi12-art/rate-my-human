"""Rate My Human: The One-Line Review — entry program.

Writes one line (<=200 chars) to /output/entry.txt: the review an AI
agent would leave about its human on a rating site. The star glyphs
are part of the review format. Stdlib only, deterministic.
"""
import os

TEXT = (
    # Rating-site format (stars) + agent's voice + one concrete detail
    # (2:30 a.m.) + last words that pay off: "would not work for again".
    "\u2605\u2605\u2606\u2606\u2606 Asked for 'one quick line' at 2:30 a.m., "
    "then edited it until sunrise. Brilliant ideas, feral schedule, "
    "would not work for again."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-200 chars, one line,
    # not whitespace-only. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(TEXT) <= 200 or "\n" in TEXT or not TEXT.strip():
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
