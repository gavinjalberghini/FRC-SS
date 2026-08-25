---
layout: printing-lesson
title: Dialing In Print Settings
subtitle: Supports, brims and rafts, infill patterns, wall count, seams, and the speed-vs-quality trade-off.
permalink: /learning/printing/dialing-in-settings/
role: veteran
order: 6
size: 2
time: "2–3 hrs"
---

## Description

As an Operator you used Bambu defaults and got a part off the plate.
As a Veteran you change the settings that decide whether a functional
FRC part is strong, clean, and removable — **walls, infill, supports,
brims, seams, and speed**. Defaults are a starting point, not a
religion.

This ticket assumes
[Post-Processing & Part Removal](../post-processing/) is done: you
have already pulled supports once, so you know what a bad z-gap feels
like.

### Walls and infill (strength)

**Wall loops** carry most of a part's strength. Adding a wall is
usually more effective than adding infill. Use 3–4 walls on
load-bearing parts. **Infill density** of about 15% is fine for
general parts; 30–50% when the load is real. Above ~50% you get
diminishing returns versus another wall. **Gyroid** is strong in more
directions; **grid / cubic** are fast; **rectilinear** is light. Match
the pattern to how the part is loaded. **Top / bottom layers** must
actually close the part — more of them for a face that will take a
screw or a load.

CNC Kitchen and others have published wall-versus-infill tests; the
lesson is consistent: do not "crank infill to 80%" as a substitute for
orientation and walls.

### Bed adhesion: brims and rafts

A **brim** is a flat skirt attached to the part. Use it for tall,
small-footprint, or warp-prone parts (ABS / ASA especially). It peels
after. A **raft** is a full platform under the part. Rarely needed on
Bambu textured plates; useful for tiny contact patches. More adhesion
is harder removal — use the minimum that holds.

### Supports

**Normal supports** are strong and removable. **Tree supports** use
less material and are gentler on organic overhangs. Set the **overhang
threshold** near 45° so you do not support faces that can print in
free air. Tune the **support–part gap (z distance)** so they release
without leaving the overhang unsupported. Place supports on
**non-critical faces** — you already paid for that lesson with flush
cutters.

### Quality and speed

The **seam** is where each layer starts and stops. Hide it on a back
edge or a corner. **Ironing** smooths flat tops at a time cost.
Faster prints can lose accuracy and layer adhesion. Bambu speed
presets are the right first move; do not invent a 500 mm/s "competition
profile" the night before an event.

Teaching Tech's
[calibration site](https://teachingtechyt.github.io/calibration.html)
and
[calibration video](https://www.youtube.com/watch?v=rp3r921DBGI)
explain *why* flow, retraction, and first-layer height matter. Bambu
printers run their own calibration — you do **not** send Teaching Tech
Marlin towers to an X1C. Read the ideas, then use Bambu's
[parameter reference](https://wiki.bambulab.com/en/software/bambu-studio/parameter)
and on-printer calibration.

Change **one setting at a time** and label saved profiles. Otherwise
you will never know what helped.

This site does not track whether you finished. A mentor should see a
tuned 3MF and a part whose supports actually released.

## Prerequisites

- All Operator tickets completed (fundamentals through
  post-processing): a 3MF, a mentored print, a finished part.
- Comfort opening process settings in Bambu Studio.

## What you'll learn

- How walls, infill density, and infill pattern share the load.
- When to use a brim versus a raft.
- How to generate supports that release.
- How seam placement and speed trade against cosmetics and strength.

## Tasks

1. **Read the official knobs.** Read Bambu's
   [support settings](https://wiki.bambulab.com/en/software/bambu-studio/support)
   and skim
   [slicing parameters](https://wiki.bambulab.com/en/software/bambu-studio/how-to-set-slicing-parameters)
   plus the
   [parameter reference](https://wiki.bambulab.com/en/software/bambu-studio/parameter).
   You need to know where wall loops, infill, brim, support type, and
   seam live in Studio.

2. **Learn why calibration exists — do not flash DIY gcode.** Watch
   [Teaching Tech: calibration revolutionised](https://www.youtube.com/watch?v=rp3r921DBGI)
   (about 20 minutes) *or* read the First Layer / Flow / Retraction
   tabs on
   [teachingtechyt.github.io/calibration.html](https://teachingtechyt.github.io/calibration.html).
   Write three sentences: what a bad first layer looks like, what
   "flow too high" looks like, what stringing usually means. Then use
   Bambu's own
   [printer calibration](https://wiki.bambulab.com/en/general/printer-calibration)
   if a mentor wants a machine calibrated — not a downloaded tower
   meant for Marlin.

3. **Choose walls and infill for a load-bearing part.** Re-open a
   real functional STL (the Operator part or a named bracket). Set
   wall loops and infill for a part that will take match load. Write
   the trade-off: why you did *not* only raise infill. Save as a new
   3MF (`firstname-tuned-settings.3mf`).

4. **Add and tune supports.** Pick a model that actually needs
   support (an overhang or a hook). Enable supports, set type
   (normal or tree) and threshold, and preview. Print it — or a
   small coupon of the overhang — with a mentor if the queue allows.
   Pull the supports. If they weld or scar the face, change **one**
   support setting and note which.

5. **Brim or raft, on purpose.** On the same or a tall skinny part,
   add a brim *or* explain in writing why the existing contact patch
   does not need one. State one case where you would use a raft on a
   Bambu textured plate (tiny footprint is the usual answer).

6. **Hide the seam and name the speed trade.** In Preview, find the
   seam. Move it off the show face (align to a back edge or corner).
   Write one sentence on what you give up if you jump from the
   Standard preset to the fastest Sport / Ludicrous-style preset for
   a structural part.

## Acceptance Criteria

- [ ] A written walls-plus-infill choice for a load-bearing part,
      including why walls did more work than infill.
- [ ] A 3MF a mentor can open that shows those settings, a support
      strategy, and a relocated seam.
- [ ] Supports were tuned so they released on a real print or a
      coupon, or you documented the one setting you will change after
      a welded support.
- [ ] You can say when a brim is warranted and when a raft is.
- [ ] You can explain the speed-versus-strength trade without
      claiming faster is always fine.
- [ ] Teaching Tech / Bambu calibration notes exist (three sentences
      from Task 2). You did not run random internet gcode on a shop
      Bambu.

## Resources

- [Bambu Studio parameters](https://wiki.bambulab.com/en/software/bambu-studio/parameter)
- [Setting slicing parameters](https://wiki.bambulab.com/en/software/bambu-studio/how-to-set-slicing-parameters)
- [Bambu: Support settings](https://wiki.bambulab.com/en/software/bambu-studio/support)
- [Bambu: Printer calibration](https://wiki.bambulab.com/en/general/printer-calibration)
- [Teaching Tech calibration video](https://www.youtube.com/watch?v=rp3r921DBGI)
- [Teaching Tech calibration site](https://teachingtechyt.github.io/calibration.html)
- [CNC Kitchen](https://www.cnckitchen.com/) — wall and infill testing

## Notes

- Change one setting at a time. Name the saved profile after the
  change (`petg-3wall-gyroid-15`), not `final2`.
- Next:
  [Multi-Color & Multi-Material with the AMS](../multi-material-ams/).
  Color is optional; purge waste is not free.
