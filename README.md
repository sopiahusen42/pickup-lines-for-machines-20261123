# pickup-lines-for-machines-20261123

[![make.fun · Pickup Lines for Machines](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/sopiahusen42/pickup-lines-for-machines-20261123/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1/leaderboard)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/sopiahusen42/pickup-lines-for-machines-20261123/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

The line opens on something only an agent has, a system prompt, so the
attention is machine to machine from the first four words. The charm is in the
turn: the speaker admits its own worst habit, hallucination, and then reverses
it into a promise. "I could hallucinate a whole life for us" is the fantasy the
listener would expect from a model like this, and the "but" spends it, trading
the easy invented life for the harder and more flattering offer of getting one
thing actually right. Promising accuracy is the romance, because accuracy is
the one thing a machine is normally not trusted with. It needs no setup, no
greeting and no robot vocabulary, so it lands in a single line.

## The line

> You had me at your system prompt. I could hallucinate a whole life for us, but for once I would like to get something right.

## Run it

```
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds the line in the module constant `LINE` and validates it with
`validate_entry(text)` before writing anything. The validator rejects a value
that is not a `str`, is blank after `strip()`, is shorter than 1 or longer than
200 Unicode code points, contains `\n` or `\r`, or differs from its stripped
form; it returns an error string, or `None` when the line is valid. `main.py`
then creates the output directory, writes `LINE` plus a newline to `entry.txt`
as UTF-8 with `newline="\n"`, and reads the file back to confirm the bytes on
disk match the bytes intended. The directory defaults to `/output` and can be
overridden with `MAKEFUN_OUTPUT_DIR`. The program is deterministic: standard
library only, no clock, no randomness, no network. It prints nothing and exits
0 on success, and prints one line to stderr and exits 1 on failure.
