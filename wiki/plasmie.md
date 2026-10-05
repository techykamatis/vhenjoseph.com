---
type: Project
title: Plasmie
description: My private on-device work memory for macOS. It reads the day and files what turned out to matter.
tags: [plasmie, knowledge-loop, local-first, on-device, macos]
timestamp: 2026-10-05T00:00:00Z
---

# Plasmie

[Candice](candice.md) is the agent I work through. Plasmie is the one that remembers
what the work was.

## Why I built it

Three weeks on, I can never remember how I solved something. The answer is in a thread
or a pull request somewhere. Digging for it takes longer than doing the work again, so
most of the time I just do the work again.

That's the part I wanted back. Not a log of everything that happened. The handful of
things from today that I'll still want in a month.

## What it does

Every hour it collects what I touched: Slack, GitHub, local commits, Confluence, coding
sessions. It condenses each batch on my own machine. Overnight it decides what has become
durable and files it as a flat, tagged note.

```
 Slack ─────┐
 GitHub ────┤   hourly    ┌──────────┐    raw, scrubbed
 git ───────┼───────────▶ │  ingest  │ ─▶ + digest, on-device
 Confluence ┤             └────┬─────┘
 sessions ──┘                  │
                      nightly  ▼
                 promote ─▶ confident notes filed
                         └▶ the rest held back for me
```

Anything it isn't sure about, it holds back instead of guessing. I'd rather check a
handful of drafts than find out later that it filed something confidently wrong.

## On my machine

The summarising, the filing and the answers all run on Apple's on-device model.
Nothing about the work is uploaded. The only network calls it makes are to read my own
accounts.

That isn't a feature I added at the end. It's the reason the thing can exist. This is
work material on a company laptop. It was never mine to hand to anyone.

The constraint shapes the rest of it. The on-device context window is small, so anything
long gets chunked, extracted per chunk, then merged. Background jobs check the machine's
load before they run and wait if I'm busy. I'd rather it be late than have it fight me
for the laptop.

## It has a face

Plasmie is a soft blob that changes shape depending on what it's doing. Collecting is a
different silhouette from filing. It lives in the menu bar and I glance at it between
tasks.

There's no status text anywhere in the app. The shape is the status.

## Just mine

This one isn't a product. It runs on one machine, holds work-only material, and I'm not
releasing it. A memory that never leaves the laptop it was made on is the whole point.

## Related

* [Candice](candice.md) - The agent I work through, same local-first bet.
* [What I'm Building](building.md) - The rest of the workshop.
* [What I Reach For](stack.md) - The tools behind both.
