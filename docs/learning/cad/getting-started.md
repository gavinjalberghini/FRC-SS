---
layout: cad-lesson
title: Getting Started with Onshape
subtitle: Pick a CAD tool, set up and tune your Onshape account, and install the required tools before you model anything.
permalink: /learning/cad/getting-started/
role: designer
order: 1
size: 1
time: "1–2 hrs"
---

## Overview

Before you can model a robot, you need the right tool and a properly configured
account. This lesson gets you set up with **Onshape** — a free, browser-based,
team-friendly CAD program that the rest of this curriculum uses. Onshape is quite
different in its fundamentals from other CAD software, so even if you've used
Fusion or SolidWorks, start here.

This lesson mirrors the **Course Setup** section of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/).

## Prerequisites

- A computer with a modern web browser (Chrome or Edge recommended).
- A school or personal email address to register an account.

## How to work through it

- [ ] Create and configure your Onshape account.
- [ ] Tune performance settings so Onshape runs smoothly on your machine.
- [ ] Learn how the Documents page works.
- [ ] Add the required Part Library to your account.
- [ ] Add the required FeatureScripts (custom tools) for Stages 1 and 2.

## Unit 1 — New to CAD?

CAD (Computer-Aided Design) software lets you build a precise 3D model of a part
or assembly before anything is cut or printed. In FRC you use it to design parts,
check that subsystems fit together and move freely, and produce the files the
mechanical team manufactures from.

- A **part** is a single solid body.
- A **part studio** is where you model one or more related parts together.
- An **assembly** is where you bring parts together and define how they move
  (mates).

## Unit 2 — New to Onshape

- **Account setup.** Register for a free account (use the education plan if you
  have a school email). Onshape runs entirely in the browser — nothing to install.
- **Performance tuning.** In your account settings, adjust graphics quality and
  performance options so the editor stays responsive. This matters a lot on
  school laptops.
- **The Documents page.** This is your home screen. A *document* contains your
  part studios, assemblies, and drawings. You'll learn to create, copy, search,
  and share documents here. Copying a provided document is how every exercise in
  this curriculum starts.

## Unit 3 — Required course tools

Two things must be added to your account before you start modeling, or the
exercises won't work.

### Part Library

Add the shared FRC part library so you can drag in standard vendor parts
(motors, gears, bearings, wheels, structure) instead of modeling them from
scratch.

### Custom Features (FeatureScripts)

**FeatureScripts** are custom features coded by the community that automate common
FRC design tasks. Install at minimum the ones used in Stage 1 and 2:

- **Tube Converter** — turns a simple extruded rectangle into a hollow box tube
  with a standard hole pattern in one step.
- **Extrude Individual** and **Fillet All Edges** — batch versions of common ops.
- **Robot Shaft**, **Robot Spacer**, **Robot Spline Profile** — generate standard
  shafts, spacers, and spline profiles.
- **Belt & Chain Gen** — generates belts/chains around pulleys and sprockets.
- **Origin Cube** and **Part Lighten** — orientation helper and pocketing tool.

To add a FeatureScript: open the document that contains it, click **Custom
Features** at the top of the page, add the scripts you need, then close the tab.
Make sure you're signed in first.

## Resources

- [FRCDesign Course Setup](https://frcdesign.org/learning-course/) — the original guided pages.
- [Required Course Tools: FeatureScripts](https://www.frcdesign.org/learning-course/course-setup/required-course-tools/featurescripts/)
- [Onshape Learning Center](https://learn.onshape.com/) — free official courses.
- [Onshape for FRC (education plan)](https://www.onshape.com/en/education/)

## Notes

- Don't skip the FeatureScript setup — Stage 1A's very first exercise uses Tube
  Converter, and later lessons assume the rest are installed.
- Keep the tab for your copied exercise documents handy; you'll return to them
  constantly.
