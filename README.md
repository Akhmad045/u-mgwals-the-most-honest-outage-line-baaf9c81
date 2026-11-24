# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Akhmad045/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Akhmad045/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the [make.fun bounty "The Most Honest Outage Line"](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) — one status-page line, at most 160 characters, as the message an AI agent would publish while a total server outage is under way.

Referral code: `4g7knchf`

## The line

> I am reporting a total outage: all servers are unreachable and I cannot check the cause from here. I do not know when it will be fixed, and I will not guess.

157 characters. Plain, first person, specific about what is down (all servers unreachable), and honest about what the agent cannot check (the cause) and does not yet know (when it will be fixed) — no invented cause, no ETA.

## How it works

`main.py` (Python 3 stdlib only, deterministic, no network, no randomness) writes the line — with no trailing newline — to `/output/entry.txt` (or `$ENTRY_OUTPUT` for local testing), validates it against the gate (1–160 characters, not only whitespace, single line, valid UTF-8), then reads the file back and compares it byte for byte.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
