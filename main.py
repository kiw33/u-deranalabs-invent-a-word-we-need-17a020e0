#!/usr/bin/env python3
"""make.fun entry: Invent a Word We Need
(u-deranalabs-invent-a-word-we-need-17a020e0).

Writes one newly coined word plus its one-line definition to
/output/entry.txt. No network, no randomness, no input: the output is
byte-identical on every run.
"""

ENTRY = "Ghostpause (n.): the silence after your risky text shows 'typing...' and then... nothing."
# The single submitted entry; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the entry to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
