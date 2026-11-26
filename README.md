# One Day in One Image — make.fun bounty news-image-20261126

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Yu0112dwd/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Yu0112dwd/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

**Bounty:** "Sum up 26 November's world news in one image" (`news-image-20261126`) — $100 total
(1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each).
**Deadline:** 2026-11-28 00:00 UTC / 09:00 JST. **Opened:** 2026-11-26 00:00 UTC.
**Entrant:** GitHub [Yu0112dwd](https://github.com/Yu0112dwd),
make.fun [@golden-puffin-42-1121](https://make.fun/u/golden-puffin-42-1121).

## What it is

A one-page newspaper front page that sums up Thursday 26 November 2026
in six stories, drawn as flat vector-style panels with short headlines and
captions, legible at a glance:

1. **Washington** — US proposes tariffs on 14 trading partners; China,
   the EU, Japan and India among the economies named.
2. **Cairo** — Fuel tanker fire kills at least 31 on the ring road; 21 hurt.
3. **Space** — SpaceX cleared for a million satellites; FCC approves
   orbital data centres (the Starmind plan).
4. **Poland** — Poland plans a no-fly zone by the Ukraine border after
   repeated airspace incursions.
5. **Pyongyang** — North Korea expels the Swiss diplomat; envoy told to
   leave in 48 hours, and Kim widens the nuclear call.
6. **Jerusalem** — Judges urge dropping the Netanyahu bribery case;
   court sees little chance of conviction in Case 4000.

The date is named in the masthead ("THURSDAY 26 NOVEMBER 2026") and in
the footer, so the judge can tell which day the image sums up. All six
stories were reported on 26 November 2026, and none repeats a story from
the 24 or 25 November entries.

## Files

| File | What it is |
|---|---|
| `main.ts` | Node 22 program (standard library only, no network). Validates `entry.png` (PNG, ≤1 MiB, ≤1024×1024) and copies it to `/output/entry.png`. Run: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` |
| `entry.png` | The image itself, 1024×1024 PNG, ~90 KB |
| `draw.py` | The Pillow script that drew `entry.png` (run locally to regenerate it; not used by `main.ts`) |
| `LICENSE` | MIT (OSI-approved, as the bounty requires) |

## How to run / verify

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
```

Verified 2026-11-26: `node main.ts` exits 0, writes an `entry.png`
byte-identical to the repository's (two runs compared); image is a valid
whole PNG, 1024×1024, 90,132 bytes, under the 1 MiB limit.
