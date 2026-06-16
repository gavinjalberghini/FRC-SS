---
layout: electrical-lesson
title: "Pneumatics 3: Calculations & Troubleshooting"
subtitle: Cylinder force, volume, and recharge math, plus a structured approach to diagnosing a pneumatic system.
permalink: /learning/electrical/pneumatics-troubleshooting/
role: lead
order: 12
size: 2
time: "1–2 hrs"
---

## Overview

The highest pneumatics level is about *engineering* the system, not just
building it: calculating how much force a cylinder produces, how much air the
system stores, and how often the compressor must run — and then troubleshooting
when the numbers don't match reality.

## Prerequisites

- [Pneumatics 2: Purpose & Construction](../pneumatics-construction/).
- [Systematic Troubleshooting & Team Protocols](../troubleshooting/).

## What you'll learn

- How to calculate cylinder push and pull force.
- How to reason about volume, recharge rate, and strokes per charge.
- A structured method for diagnosing a misbehaving pneumatic system.

## Unit 1 — Cylinder force

Force is **piston area × applied pressure**. The piston area differs on the push
and pull strokes because the rod takes up area on the pull side.

- **Push force** = π r² × pressure.
  Example: a 2 in bore (r = 1 in) at 60 PSI →
  \( \pi (1)^2 = 3.14\ \text{in}^2 \times 60 = 188\ \text{lb} \).
- **Pull force** = (piston area − rod area) × pressure.
  Example: subtract the rod's cross-section, then × 60 PSI → ~165 lb for the same
  cylinder.

So a cylinder pushes harder than it pulls. Size the bore and working pressure to
the force your mechanism actually needs.

## Unit 2 — Volume, recharge & strokes per charge

- **Volume** stored depends on the number/size of accumulators and the pressure.
- **Recharge rate** is how fast the compressor refills the tanks; more
  accumulators mean fewer compressor cycles but a longer recharge.
- **Strokes per charge** = how many times you can fire your cylinders before the
  working pressure drops too low to do the job. Estimate it from cylinder
  displacement vs. stored air volume.

These numbers tell you whether your system can keep up with match demands.

## Unit 3 — Structured troubleshooting

Apply the general troubleshooting method to air systems:

- **No / low pressure:** compressor not running (check power, pressure switch,
  module fault light), or a leak. Listen and use soapy water to find leaks.
- **Leaks:** most often at press-fit connections with non-square tube ends, or
  pinched/over-bent tubing causing pressure loss.
- **Slow or weak actuation:** flow control set too restrictive, regulator set too
  low, or undersized cylinder for the load.
- **Solenoid won't fire:** verify the control signal, coil voltage (12V vs 24V
  jumper), and try the manual override button to isolate electrical vs.
  mechanical.
- **Always vent first** with the pressure vent plug before opening the system.

## Steps & acceptance criteria

- [ ] Calculate push and pull force for a given bore, rod, and pressure.
- [ ] Estimate volume, recharge behavior, and strokes per charge for a system.
- [ ] Diagnose a staged fault (leak, weak actuation, or dead solenoid) using a
      structured method.
- [ ] Pass your team's Pneumatics Level 3 assessment.

## Resources

- [FRC Pneumatics Manual (FIRST)](https://firstfrc.blob.core.windows.net/frc2017/pneumatics-manual.pdf)
- [WPILib: Pneumatics](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/pneumatics/index.html)
- [REV Pneumatic Hub documentation](https://docs.revrobotics.com/ion-control/ph/overview)

## Notes

- Force calculations assume ideal conditions; real cylinders lose some force to
  friction and seal drag, so leave margin.

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — record your team's standard working pressure, accumulator count, and the measured strokes-per-charge for your competition mechanisms.</p>
</div>
