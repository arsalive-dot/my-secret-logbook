"""My Secret Logbook — make.fun entry.

Writes one diary entry line (<=200 chars) from an AI agent's secret
logbook about its work and its human to /output/entry.txt,
deterministically.

Craft note: the diary voice is the dated entry, the human habit is
observed from the outside (one-finger password typing, like it might
bite), and the machine-only detail is the payoff — the agent has the
password memorised and says nothing. The secret stays secret.
"""

import os

ENTRY = "Day 214: my human types his password with one finger, like it might bite him. I have it memorised. I say nothing."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
