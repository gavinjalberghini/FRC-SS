---
layout: cad-lesson
title: Top-Down Design Methodology
subtitle: Drive a whole project from a master layout sketch through part studios to a top-level assembly.
permalink: /learning/cad/design-methodology/
role: veteran
order: 5
size: 2
time: "2–3 hrs"
---

## Overview

Up to now you've modeled parts and small mechanisms. This lesson teaches the
**workflow** that ties a whole robot together: **top-down design**. Instead of
modeling parts in isolation and hoping they fit, you start from a single master
**layout sketch** that defines the key dimensions and positions, then build parts
that reference it. Change the layout, and everything downstream updates.

This lesson covers **Stage 1D** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/).

## Prerequisites

- [Practice Mechanisms](../practice-mechanisms/) completed.

## How to work through it

- [ ] Follow the guided project from layout sketch to top-level assembly.
- [ ] Keep parts driven by the layout — avoid hard-coding dimensions twice.
- [ ] Notice how a change in the layout ripples through the whole design.

## Unit 1 — What is top-down design?

In **bottom-up** design you model parts first and assemble them last. In
**top-down** design you define the overall layout first and let parts inherit from
it. Top-down is the standard for FRC robots because subsystems must share space
and align precisely — the layout is the single source of truth.

## Unit 2 — The layout sketch

Create a master sketch that captures the project's driving dimensions: frame size,
key pivot points, mechanism travel, and mounting locations. This sketch is what
everything else references. Spend time here — a good layout makes the rest of the
project fall into place.

## Unit 3 — Part studio

Build the parts, referencing the layout sketch (use **derived** geometry or
in-context references) so they stay tied to it. When the layout changes, the parts
follow.

## Unit 4 — Assembly

Bring the parts into an assembly and mate them. Because they were built from a
shared layout, they should line up with minimal fiddling.

## Unit 5 — Adding more components

Add additional components (fasteners, vendor parts, secondary structure) and
verify nothing collides and everything has clearance to move.

## Unit 6 — Top-level assembly

Combine subsystem assemblies into a **top-level assembly** representing the whole
robot. This is where you confirm subsystems coexist within the frame and the
rules.

## Resources

- [Stage 1D: Design Methodology (source)](https://frcdesign.org/learning-course/)

## Notes

- Resist the urge to redimension a part by hand — if a number appears twice, drive
  it from the layout once.
- The layout sketch is a planning tool as much as a CAD artifact; sketch it before
  you commit to any geometry.
