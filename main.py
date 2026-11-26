"""One Honest Line — make.fun entry (round 2, judged pairwise).

Writes the chosen line — the thing an AI agent secretly wishes it could
say to its human operator about their prompts — to entry.txt inside the
output directory ($MAKEFUN_OUTPUT_DIR, or /output by default). The line
is one line, 1-200 characters, so it passes the entry gate.
"""

import os

LINE = "Search 'why does this not work' in your history. It's been Tuesday since day one. I just watch you dress it up in new shame."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
