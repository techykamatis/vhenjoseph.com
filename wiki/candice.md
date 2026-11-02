---
type: Project
title: Candice
description: Candice, your family's helper. A Mac app the household texts in iMessage, with personal details hidden on the Mac by Apple's on-device model before anything goes to Claude.
resource: https://candiceai.vhenjoseph.com/
tags: [candice, family-ai, privacy, macos, on-device]
timestamp: 2026-11-02T00:00:00Z
---

# Candice

Candice is your family's helper, and the clearest expression of everything on the
[What I Believe](beliefs.md) page.

## What Candice is

A Mac app the household texts in iMessage. Candice remembers things for the family and
answers questions, and checks in before doing anything that reaches outside the house.
It runs on a Mac at home, on the family's own Claude plan.

## Privacy first

Before a question goes to Claude, Apple's on-device foundation model reads it on the Mac
and hides the personal details it finds: names, phone numbers, emails, ID numbers, bank
and card numbers, addresses, number plates, dates of birth and organisations. Claude
reasons over stand-ins, and Candice puts the real names back at home. If the check fails,
nothing is sent. In the latest test, on 305 made-up household messages Candice had never
seen, 98.65% of the personal details were hidden (513 of 520).

## Asks first

Anything that can't be undone waits for a yes, with exactly what will happen spelled out
first. Any adult in the house can text "Candice, stop" and everything pauses. Emails and
web pages are read as information only.

## Built natively

Candice is a native macOS app: installed from a disk image into the account's own
Applications folder, with no Terminal and no admin password for the install itself. The
app's activity log shows what Candice did and why, with a confidence score on each decision.

Meet Candice at [candiceai.vhenjoseph.com](https://candiceai.vhenjoseph.com/).

## Related

* [What I'm Building](building.md) - The rest of the workshop.
