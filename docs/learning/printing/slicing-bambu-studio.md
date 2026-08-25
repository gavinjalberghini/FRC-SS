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

## Description

A printer cannot read a CAD model. A **slicer** turns geometry into
layer-by-layer moves: walls first (usually), then infill, then the next
layer. This team standardizes on **Bambu Studio**. This ticket takes you
from a real STL to a sliced **3MF project** a mentor can open.

You already picked a filament in
[Choosing the Right Material](../choosing-materials/). The slicer is
where that choice becomes temperatures, plate type, and a toolpath.
You are not starting the printer yet — that is
[Running Your First Print](../first-print/), with a mentor.

**STL** is geometry only. **3MF** can store the model *and* the Studio
settings (printer, filament, process). Save 3MF for anything you might
reprint. Start from Bambu's default process profiles and change one
thing at a time.

Orientation is the most important slicing decision, because FDM parts
are **weakest between layers**:

- **Strength** — put the load *along* layers, not peeling them apart.
  A hook printed with layers stacked the wrong way snaps at the layer
  line.
- **Supports** — overhangs steeper than about 45° need support.
  Orient to need fewer of them.
- **Finish** — the face on the plate is smooth; up-facing overhangs
  are rougher.

Use **place-on-face** to drop a flat face to the plate, then rotate if
strength and supports fight each other. There is often a compromise,
not a perfect answer.

Core settings you must be able to name:

- **Layer height** — 0.20 mm is the everyday default on a 0.4 mm
  nozzle. 0.28 mm is faster; 0.12 mm is finer and slower.
- **Walls / shells** — 2–4 wall loops for functional parts. Walls
  carry most of the strength.
- **Infill** — 10–20% for general parts; higher when the part is
  loaded. Gyroid and grid are the usual patterns.
- **Top / bottom layers** — enough solid layers to close the part
  (typically 3–5).
- **Supports** — on only when overhangs need them. Tuning them is
  [Dialing In Print Settings](../dialing-in-settings/).

After **Slice plate**, open **Preview** and scrub the layers. Look for
floating islands, missing supports, a seam on a show face, and a time
and filament estimate that is in the same universe as the part. Then
send over the network or export for SD / offline print.

This site does not track whether you finished. The 3MF is the artifact.
A mentor opens it; they do not take your word that you sliced.

## Prerequisites

- [Choosing the Right Material](../choosing-materials/) completed.
- Bambu Studio installed from
  [bambulab.com/en/download/studio](https://bambulab.com/en/download/studio)
  and the shop printer added (or a mentor account you can use).
- A real STL or STEP: a team practice part, a spacer, a hook, or a
  small functional model — not an empty plate.

## What you'll learn

- How to set printer, filament, and plate in Bambu Studio so they
  match the machine you will actually use.
- How to orient for strength and for fewer supports.
- How to set layer height, walls, and infill on purpose.
- How to preview a slice and save a 3MF a mentor can reopen.

## Tasks

1. **Install Studio and bind a printer.** If it is not already done,
   install
   [Bambu Studio](https://bambulab.com/en/download/studio)
   and follow the
   [Studio quick start](https://wiki.bambulab.com/en/software/bambu-studio/studio-quick-start)
   far enough to select your real printer and nozzle size (usually
   0.4 mm). You do not have to send a job yet.

2. **Watch someone slice once, then do it yourself.** Watch or read
   [All3DP: Bambu Studio tutorial](https://all3dp.com/2/bambu-studio-tutorial-beginner/)
   and skim
   [Setting slicing parameters](https://wiki.bambulab.com/en/software/bambu-studio/how-to-set-slicing-parameters).
   Then put the video away. Typing is the practice.

3. **Import a real model.** **File → Import** (or drag) an `.stl`,
   `.step`, or `.3mf`. Select the **printer**, **plate type**, and
   **filament** that match what is actually in the shop — the material
   you would have chosen in the last ticket for this kind of part.
   Place it on the plate. Use auto-arrange if you have more than one
   object.

4. **Orient on purpose.** Use place-on-face and rotate. Write two
   sentences in the same note as your material picks: *I put this face
   on the bed because …* (strength or supports) and *The trade-off is
   …*. If the strongest orientation needs a forest of supports, say
   so. Do not hide the compromise.

5. **Set the three strength knobs.** Starting from a Bambu 0.20 mm
   default profile, set:

   - layer height (0.20 mm unless you have a reason)
   - wall loops (at least 3 for a functional part)
   - infill density and pattern (name the pattern)

   Skim
   [Print settings explained](https://wiki.bambulab.com/en/software/bambu-studio/parameter)
   if a control is unnamed in the UI. Change one thing at a time so
   you can tell a mentor what you changed.

6. **Slice, preview, and save a 3MF.** Click **Slice plate**. Scrub
   Preview from layer 1 to the top. Check:

   - the first layer is a solid contact patch, not a tiny point
   - walls and infill look like what you set
   - overhangs that need support actually have support
   - estimated time and filament are written down

   **File → Save Project** as a `.3mf` named something like
   `firstname-practice-part.3mf`. That file is the acceptance
   artifact. Send to the printer or export only if a mentor is ready
   for the next ticket; this ticket is complete when the 3MF exists.

7. **Hand the 3MF to a mentor.** They should be able to open it in
   Studio, see your printer / filament / process, and hear your
   orientation sentences. If tickets are exported, attach the 3MF (or
   a link to it on the team's drive) and move the card to In Review.

## Acceptance Criteria

- [ ] Bambu Studio opens with the correct shop printer and nozzle
      selected.
- [ ] A real STL / STEP / 3MF — not a blank plate — was imported.
- [ ] Orientation is justified in two written sentences (strength and
      the support or finish trade-off).
- [ ] Layer height, wall count, infill density, and infill pattern
      were set on purpose and match a functional part (not 2% infill
      on a load-bearing bracket).
- [ ] Preview was scrubbed; time and filament estimates are written
      down.
- [ ] A mentor can open your saved `.3mf` project and see those
      settings without you clicking for them.

## Resources

- [Bambu Studio Wiki](https://wiki.bambulab.com/en/software/bambu-studio)
- [Bambu Studio quick start](https://wiki.bambulab.com/en/software/bambu-studio/studio-quick-start)
- [Setting slicing parameters](https://wiki.bambulab.com/en/software/bambu-studio/how-to-set-slicing-parameters)
- [Print settings explained](https://wiki.bambulab.com/en/software/bambu-studio/parameter)
- [Bambu Studio download](https://bambulab.com/en/download/studio)
- [All3DP: Bambu Studio tutorial](https://all3dp.com/2/bambu-studio-tutorial-beginner/)

## Notes

- Start from Bambu defaults. Over-tuning a first slice is how you
  make a worse part and cannot say which change did it.
- Save the 3MF. A screenshot of Preview is not a project file.
- Do not send a job to a printer that is already running someone
  else's part. Ask.
- The next ticket ([Running Your First Print](../first-print/)) is
  the same file, on a real machine, with a mentor at the first
  layer. Bring the 3MF.
