---
layout: printing-lesson
title: Slicing in Bambu Studio
subtitle: Import a model, orient it, choose layer height, walls, and infill, and export a print to the printer.
permalink: /learning/printing/slicing-bambu-studio/
role: operator
order: 3
size: 2
time: "1–2 hrs"
---

## Overview

A printer can't read a 3D model directly — a **slicer** converts it into layer-by-
layer instructions. We use **Bambu Studio**. This lesson takes you from a model
file to a sliced print ready to send to a Bambu printer.

## Prerequisites

- [Choosing the Right Material](../choosing-materials/) completed.
- Bambu Studio installed and your printer added.

## Unit 1 — Set up the project

- Select your **printer** (X1C, P1S, A1…) and the **filament** loaded.
- Import the model (**File → Import**, or drag in an `.stl`/`.step`/`.3mf`). 3MF
  keeps settings; STL is geometry only.
- Place it on the plate; use **auto-arrange** for multiple parts.

## Unit 2 — Orient the part

Orientation is the most important slicing decision:

- **Strength** — layers bond weakest across the layer lines, so orient the part so
  loads run *along* layers, not across them.
- **Supports** — orient to minimize overhangs steeper than ~45° so you need fewer
  supports.
- **Surface finish** — the side facing the plate is smooth; up-facing surfaces and
  overhangs are rougher.

Use **place-on-face** to drop a flat face to the plate and **rotate** to find the
best compromise.

## Unit 3 — Core print settings

- **Layer height** — smaller = finer detail but slower (0.2 mm is a good default;
  0.28 mm faster, 0.12 mm finer).
- **Walls / shells** — more wall loops = stronger part. 2–4 walls for functional
  parts.
- **Infill** — internal fill density and pattern (10–20% for general parts; higher
  for strength). Gyroid and grid are common patterns.
- **Top/bottom layers** — enough solid layers to close the part (3–5).
- **Supports** — turn on only if there are overhangs; covered in depth later.

## Unit 4 — Slice, preview, and export

- Click **Slice plate**, then open the **Preview** and scrub through the layers.
- Check the **estimated time and filament** and look for problems (floating
  islands, missing supports, a giant seam on a visible face).
- Send to the printer over the network (**Print**) or export to SD/storage if
  printing offline.

## Steps & acceptance criteria

- [ ] Import a model and orient it for both strength and minimal supports.
- [ ] Set layer height, walls, and infill appropriate to the part.
- [ ] Slice, preview the layers, and read the time/filament estimate.
- [ ] Send a sliced print to a printer (or export it).

## Resources

- [Bambu Studio Wiki](https://wiki.bambulab.com/en/software/bambu-studio) — full slicer documentation.
- [Bambu Studio download](https://bambulab.com/en/download/studio)
- [Bambu: Print settings explained](https://wiki.bambulab.com/en/software/bambu-studio/parameter)

## Notes

- Start from Bambu's default profiles and change one thing at a time — it's easy to
  make a part worse by over-tuning.
- Save a `.3mf` of good setups so they're reusable.
