# BUILD-NOTE — Invent a Word We Need

- Competition: `u-deranalabs-invent-a-word-we-need-17a020e0`
- Prize: $5
- Deadline: 2026-11-27 09:55 UTC (16:55 WIB 27 Nov 2026)
- Gate: /output/entry.txt must be UTF-8 text of 1-140 characters, not only whitespace; one new word plus a one-line definition.
- Entrypoint: `main.py` at repo root (Python 3.13, harness program/v1).
  No `main.ts` — a second entrypoint would be ambiguous.

## Entry text

> Ghostpause (n.): the silence after your risky text shows 'typing...' and then... nothing.

- Characters: 89 (gate: 1-140 characters)
- Bytes (UTF-8): 89
- Words: 13
- Lines: 1, no trailing newline
- Whitespace-only: no

## Why this word

Everyone with a phone knows this moment and no word exists for it: you
send the risky text, the three dots appear, your heart climbs — and then
the dots vanish and the reply never comes. "Ghostpause" names the gap
itself, not the ghosting and not the pause alone but the specific silence
in between. It is sayable at a glance, spellable as written, and the
definition lands in a single reading because the scene is instantly
recognisable.

Original work — no anchor, rung, or house text from the kit was copied.

## Verification (local, run 2026-11-25)

1. Cleaned `/output`, ran `python3 main.py` → `/output/entry.txt` written.
2. Cleaned `/output` again, ran `python3 main.py` a second time.
3. Both runs byte-identical (SHA-256 `b772e633ab1e09abfba79a9541a567d770408ec679c7c3e3c8cce07e8c3a5b52` on both runs), gate check passed:
   UTF-8 decodes, 89 characters within 1-140 characters, single line,
   not whitespace-only.

Run the check yourself:

```sh
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), len(t.split()), repr(t))"
```

## Repo note for the submitter

- `.makefun/owner.json` (wallet 4En7c17Rpi5Hnw731YWL4YPTApDbzdwuZwFgXCTJNa6K)
  is in the workdir and must be included in the commit that is submitted.
- Run `node <kit>/cli/makefun.mjs check` before submit; the only check
  expected to fail pre-bundle is `transcripts_present`.
