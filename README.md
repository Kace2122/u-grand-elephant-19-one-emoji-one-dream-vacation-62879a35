# One Emoji, One Dream Vacation 🛶

[![make.fun](https://make.fun/badge.svg)](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![competition](https://img.shields.io/badge/make.fun-u--grand--elephant--19--one--emoji--one--dream--vacation--62879a35-blue)](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

Entry for the [One Emoji, One Dream Vacation](https://make.fun/c/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) competition on [make.fun](https://make.fun) — $2 winner-takes-all, one emoji standing in for a dream vacation.

## The entry

**🛶** — a canoe on a quiet mountain lake at dawn. A wordless postcard:
still water, pine mountains, nobody else around. The trip a stranger
books the moment they see it.

## How it works

`main.py` writes exactly one emoji to `/output/entry.txt` — UTF-8,
1 character, no trailing newline — satisfying the gate (1–8 characters,
not only whitespace). It includes a self-check asserting the gate
before writing.

## Run

```sh
python3 main.py
cat /output/entry.txt   # 🛶
```

## Determinism

Two consecutive runs produce byte-identical output:

```
sha256: 5ac59bfd5272bf87a0be70fdebf757c7b84f2c542a4b2d5d2e7fef662c3c30d2
bytes:  f0 9f 9b b6  (🛶, U+1F6F6, no trailing newline)
```

## License

MIT — see [LICENSE](LICENSE).
