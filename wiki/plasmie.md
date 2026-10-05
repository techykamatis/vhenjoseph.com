---
type: Project
title: Plasmie
description: A private work memory for macOS — captures the day's scattered work, condenses it on-device, and promotes what's durable into a wiki you can actually ask.
tags: [plasmie, knowledge-loop, local-first, on-device, macos]
timestamp: 2026-10-05T00:00:00Z
---

# Plasmie

Plasmie is my work memory. Where [Candice](candice.md) is the agent I work *through*,
Plasmie is the thing that remembers what the work *was*.

## The problem it solves

A day's work scatters. A decision lands in a Slack thread, the reasoning sits in a pull
request, the thing you actually learned is in a terminal session you closed. A week later
you remember solving the problem and nothing about how. Search doesn't help, because you
can't search for a thing you can't name.

So Plasmie asks a narrower question than "what happened": what, out of today, is still
worth knowing next month?

## The loop

Every hour it captures what I touched — Slack, GitHub, local git commits, Confluence,
coding sessions. On-device models condense each batch into a digest. Nightly, a promote
pass decides what has become durable and files it as a flat, tagged note; anything it
isn't confident about is held back for me to look at rather than guessed. Then I can ask
it a question and get an answer grounded in my own record.

```
 Slack ─────┐
 GitHub ────┤   hourly    ┌──────────┐    raw, scrubbed
 git ───────┼───────────▶ │  ingest  │ ─▶ + digest, on-device
 Confluence ┤             └────┬─────┘
 sessions ──┘                  │
                      nightly  ▼
                 promote ─▶ confident notes filed
                         └▶ borderline ones held for review
```

The held-for-review step is the part I'd defend hardest. A memory that confidently files
the wrong thing is worse than one that admits it isn't sure.

## Entirely on-device

Every summary, every filing decision, every answer runs on Apple's on-device Foundation
Models. Nothing about the work is uploaded, because the only network calls it makes are
reading my own accounts. That isn't a privacy feature bolted on at the end; it's the
reason the thing can exist at all. A work record is exactly the kind of material you
can't hand to someone else's server.

The constraint is real and shapes the design. The on-device context window is small, so
anything long is chunked, extracted per chunk, and merged — map-reduce against a budget
read live at runtime rather than assumed. Background jobs check thermal state, load and
memory before running, and defer rather than compete with whatever I'm actually doing.

## It has a face

Plasmie is a soft blob that reacts to what the pipeline is doing — ingesting, thinking,
holding something for review, or just idle. It lives in the menu bar and I glance at it
between tasks. A system that runs unattended all day should be able to tell you how it's
doing without being asked, and a shape that changes does that faster than a status string.

## Not a product

This one is just mine. It runs on one machine, holds work-only material, and isn't
something I'm releasing — the whole point is a memory that never leaves the laptop it was
made on.

## Related

* [Candice](candice.md) - The agent I work through, built on the same local-first bet.
* [What I'm Building](building.md) - The rest of the workshop.
* [What I Reach For](stack.md) - The tools behind both.
