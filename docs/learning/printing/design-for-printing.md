---
layout: printing-lesson
title: Designing for 3D Printing
subtitle: Orient for strength, set tolerances and clearances, handle overhangs, and add bosses and heat-set inserts.
permalink: /learning/printing/design-for-printing/
role: veteran
order: 8
size: 3
time: "Multi-session"
---

## Description

The best Bambu profile cannot save a part that was modeled as if it
were milled from aluminum. This ticket is the bridge between the
[CAD & Design curriculum](../../cad/) and the printer: **design for
FDM** so the part orients for strength, fits the robot, and does not
need a Christmas tree of supports.

You already know parts are weakest between layers
([Fundamentals](../fundamentals-safety/)), you have sliced orientation
on purpose ([Slicing](../slicing-bambu-studio/)), and you have pulled
supports ([Post-Processing](../post-processing/)). Here you change the
*model*, not only the slice.

### Orientation and layer strength

A bracket in bending should have layers running with the stress, not
stacked across the crack you do not want. Sometimes the strongest
orientation needs more supports. That is a design input: add a chamfer
or a sacrificial tab so the strong orientation still prints.

### Tolerances and clearances

Printers are accurate but not perfect. **Holes print slightly
undersize**; outer dimensions slightly oversize. Leave clearance for
mating parts — a typical slip / easy press needs on the order of
**0.2 mm** of gap per side as a starting point; **test-print a
coupon** before a six-hour job. For shafts, bearings, and bolts,
design the nominal size and plan to **ream or drill** holes to final
size after printing. Do not model a 0.500 in bore and expect a 1/2 in
bearing to press perfectly on the first try.

### Printability rules

- **Overhangs** past ~45° need support — chamfer or redesign to avoid
  them.
- **Bridges** only span short gaps in free air. Keep them short or
  support them.
- **Wall thickness** should be a multiple of nozzle / line width
  (about ≥1.2 mm / several walls) so walls are solid, not a single
  squishy loop.
- **Fillets and chamfers** cut stress concentrations and help the
  first layer.
- Avoid huge flat bottoms that warp, and tiny unsupported pillars.

### Fasteners in plastic

**Heat-set inserts** give reusable metal threads. Design a boss to the
insert manufacturer's hole diameter and install with a soldering iron
— straight, slow, flush. **Captured nuts** (a hex pocket) and
**clearance holes for bolts** are simpler and often stronger. Do not
tap plastic for a high-load joint; it will strip in a pit. Add
**bosses and ribs** at mounts instead of thickening the entire part.

### Print versus machine

Print when the part is complex, low-to-moderate load, or you need
another revision tonight. Choose aluminum or COTS when the part is
highly loaded or is a wear surface. Printed parts excel as brackets,
spacers, guides, mounts, gauges, and prototypes — and, in engineering
materials (next Lead ticket), some structural parts. Material choice
still follows
[Choosing the Right Material](../choosing-materials/): PLA is not a
gearbox.

This site does not track CAD homework. Your Onshape (or other) part
plus a printed coupon is what a mentor reviews.

## Prerequisites

- [Multi-Color & Multi-Material with the AMS](../multi-material-ams/)
  completed (Veteran path through AMS).
- Comfort in a CAD tool — start with
  [Getting Started with Onshape](../../cad/getting-started/) if you
  have not.
- A soldering iron and heat-set inserts the shop actually stocks
  (or a captured-nut fallback a mentor approves).

## What you'll learn

- How to orient and reshape a part so layers take the load.
- How to leave clearances FDM can actually hold.
- How to kill an overhang or bridge in CAD instead of in the slicer.
- How to put a heat-set insert (or captured nut) in a printed boss.

## Tasks

1. **Read a DfAM guide, then come back to Bambu.** Read Bambu's
   [knowledge-sharing / design notes](https://wiki.bambulab.com/en/knowledge-sharing)
   and at least the plastics overview in
   [Markforged: Design for additive manufacturing](https://markforged.com/resources/learn/design-for-additive-manufacturing-plastics-composites).
   For inserts, read
   [CNC Kitchen: threads in 3D prints](https://www.cnckitchen.com/blog/the-amazing-and-easy-way-to-put-threads-in-your-3d-prints).
   Write three rules you will apply to *your* part, not a summary of
   the articles.

2. **Pick a named robot interface.** Choose a real need: a sensor
   mount, a spacer stack, a belt guard, a battery-connector shroud.
   Name the mating COTS parts (bolt size, bearing, tube). You are
   not designing a whole subsystem.

3. **Orient for strength on the model.** In CAD or in Studio,
   show the intended layer direction. Write why the main load does
   not peel layers apart. If the strong orientation needs supports,
   change the model (chamfer, split, sacrificial tab) so it needs
   fewer.

4. **Add clearances you can measure.** Put a bolt clearance hole and
   a mating-part gap on the model. State the numbers (for example
   `#10 clearance` plus `0.2 mm` slip on a printed pocket). Export
   STL / 3MF and print a **small fit coupon** (a hole and a pocket,
   not the whole part) before the long print.

5. **Delete an overhang.** Find one face that would have needed
   support. Chamfer, re-angle, or bridge it so Preview no longer
   wants support there. Screenshot or save the before/after 3MF.

6. **Design a boss and install hardware.** Model a boss for a
   heat-set insert the shop stocks (use the vendor hole chart).
   Print it in PLA or PETG. Install **one** insert with a mentor
   and a soldering iron — vertical, no mashed plastic volcano.
   Alternative if the shop has no inserts: a captured-nut pocket
   that actually holds a hex nut from spinning.

7. **Call print versus machine.** One paragraph: why this part is
   printed (or why you would switch it to aluminum / COTS). Mention
   load, wear, revision speed, and a material from the Operator
   ticket.

## Acceptance Criteria

- [ ] A named part exists in CAD with a stated layer orientation
      and a written strength reason.
- [ ] Bolt and mating clearances are on the model; a coupon was
      printed and measured (or a mentor watched the dry-fit).
- [ ] One overhang or bridge was redesigned so it slices without
      support (or with support only on a non-critical face).
- [ ] A boss for a heat-set insert (or a captured-nut pocket) was
      printed and the hardware installed without destroying the
      boss.
- [ ] The print-versus-machine paragraph names the part and a
      material.
- [ ] A mentor can open the CAD or 3MF without you driving the
      mouse.

## Resources

- [Bambu Wiki: Knowledge sharing](https://wiki.bambulab.com/en/knowledge-sharing)
- [Markforged: Design for FDM / composites](https://markforged.com/resources/learn/design-for-additive-manufacturing-plastics-composites)
- [CNC Kitchen: heat-set inserts](https://www.cnckitchen.com/blog/the-amazing-and-easy-way-to-put-threads-in-your-3d-prints)
- [Bambu Studio support settings](https://wiki.bambulab.com/en/software/bambu-studio/support)
- [CAD track](../../cad/)

## Notes

- A ten-minute coupon saves a ten-hour wrong hole. Print the
  interface first.
- Soldering irons are hot. Inserts that go in crooked are weaker
  than a captured nut. Ask for a second iron stand, not a finger.
- Next:
  [Troubleshooting Failed Prints](../troubleshooting/)
  — the part will still fail sometimes; Veteran work is naming
  why.
