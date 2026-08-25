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

## Description

CAD (computer-aided design) is how an FRC team turns an idea into something a
shop can cut, print, and assemble. You build a precise 3D model first, check
that parts fit and move, then export drawings or cut files. The rest of this
curriculum uses **Onshape**: a browser-based CAD tool with a free education
plan, live collaboration, and a large FRC parts library.

Onshape is not a thinner SolidWorks or Fusion. Three ideas are different
enough that skipping this ticket will hurt later:

- A **document** is the project container. Inside it you keep **part studios**
  (where you model one or more related solids), **assemblies** (where you
  insert those parts and define motion with **mates**), and drawings.
- A **part** is a single solid body. Several parts can live in one studio and
  reference each other. That is how FRC teams model a plate against the tubes
  it bolts to, instead of guessing hole locations.
- **FeatureScripts** are community-written tools that show up in the toolbar
  like native features. Tube Converter, Robot Shaft, and Belt & Chain Gen are
  not optional extras — Stage 1A's first tube exercise uses them.

This ticket is **Course Setup** from the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/). That
course is the lab. This ticket teaches the ideas, then sends you to the exact
FRCDesign pages to create the account, tune the browser, and install the
tools. Do not skip Course Setup even if you have used another CAD package.

This site does not track whether you finished. Your Onshape documents live in
**your** account. Mentors review a share link or a screenshot, the same way
programming mentors review a pull request. If your team exported these tickets
into its own GitHub, close this issue there once a mentor accepts the
criteria below.

## Prerequisites

- A computer with a modern web browser. Chrome or Edge is recommended;
  Onshape's hardware acceleration is most reliable on Chromium.
- A school or personal email address you can receive mail at. A school
  address is required for the free
  [Onshape Education plan](https://www.onshape.com/en/education/).
- You do not need any CAD software installed. Onshape runs in the browser.

## What you'll learn

- What CAD is for on an FRC team, and what a part, a part studio, and an
  assembly each do.
- How to create an Onshape Education account, put a name and photo on it, and
  set inches as the default unit.
- How the Documents page works, and why every later ticket starts by
  **copying** a provided FRCDesign document into your account.
- How to install FRCDesignApp (the part library) and the named FeatureScripts
  Stage 1 and Stage 2 expect.

## Tasks

1. **Learn how the FRCDesign site works.** Open the
   [Website Feature Guide](https://frcdesign.org/feature-guide/). Note the
   green document buttons, the slideshow arrows, and the next/previous arrows
   at the bottom of each lesson. Those arrows — not this playbook — walk you
   through the exercises. Skim
   [New to CAD](https://frcdesign.org/learning-course/course-setup/new-to-cad/)
   even if you have used Fusion or SolidWorks. Write two sentences in a
   scratch note (you will paste them into the mentor note at the end):
   *A part studio is …* and *An assembly is …*.

2. **Create the Education account.** Follow
   [Account Setup](https://frcdesign.org/learning-course/course-setup/new-to-onshape/account-setup/)
   and register at
   [Onshape for Education](https://www.onshape.com/en/education/). Choose
   **Create EDU ACCOUNT**. Sign up as a student in grade school, enter your
   school, and use "Robotics" as the reason. Confirm the verification email,
   set a password, and finish the first-run prompts. Set:

   - default units to **inch**
   - a profile photo (or a consistent avatar mentors can recognize)
   - a display name you will answer to in the shop

   If your team already has an Educator classroom, ask a mentor to invite you
   **after** this ticket. Learning work still happens in documents you own.

3. **Tune performance.** School laptops choke Onshape when graphics
   acceleration is off. Follow
   [Performance Tuning](https://frcdesign.org/learning-course/course-setup/new-to-onshape/performance-tuning/).
   Use Chrome or Edge, turn on "Use graphics acceleration when available,"
   and run Onshape's browser compatibility check from that page. If the
   editor still stutters, try the ANGLE-backend steps on the same page.

4. **Learn the Documents page.** Follow
   [Documents Page](https://frcdesign.org/learning-course/course-setup/new-to-onshape/documents-page/).
   Create one empty document named `CAD Learning — YourName` so you know
   where copies will land. Open it, look at the tab bar, and notice you can
   add a Part Studio or an Assembly. Optionally complete
   [Navigating a Document](https://learn.onshape.com/courses/navigating-a-document)
   on the official Learning Center (about 30 minutes). You are not modeling
   a robot yet.

5. **Install the part library.** Follow
   [Part Library](https://frcdesign.org/learning-course/course-setup/required-course-tools/part-library/).
   Open the FRCDesignApp listing in the Onshape App Store, subscribe, and
   choose **Get for Free**. Reload any open documents. FRCDesignApp is the
   inserter; **FRCDesignLib** is the catalog of motors, gears, bearings,
   swerve modules, and fasteners you will drag into assemblies starting in
   Stage 1A Section 3. If the inserter is missing, clear the site cache and
   re-authorize the app, as that page describes.

6. **Install the named FeatureScripts.** Sign in first. Then follow
   [Custom Features](https://frcdesign.org/learning-course/course-setup/required-course-tools/featurescripts/)
   exactly. Open each linked document, click **Custom Features** at the top,
   add the scripts listed, and close the tab:

   - From Julia's Featurescripts: **Tube Converter**, **Extrude Individual**,
     **Fillet All Edges**
   - From Alex's Featurescripts: **Robot Shaft**, **Robot Spacer**,
     **Robot Spline Profile**
   - **Belt & Chain Gen** from its own document
   - **Origin Cube** from its own document
   - **Part Lighten** from 2471's Featurescripts (open the Lightening Gen
     folder after you click Add custom features)

   Confirm they appear in the custom-features dropdown of a part studio in
   `CAD Learning — YourName`. If a script shows a blue "update linked
   document" icon later, follow
   [Featurescript Help](https://frcdesign.org/resources/featurescript-help/).

7. **Hand it to a mentor.** Share `CAD Learning — YourName` (Onshape
   **Share**, mentor email or a view link) or export a screenshot of the
   FeatureScripts dropdown with the scripts from Task 6 visible. If your
   team exported these tickets, paste the link on this issue and move it to
   In Review. Include the two sentences from Task 1.

## Acceptance Criteria

- [ ] You can explain, in two sentences of your own words, the difference
      between a part studio and an assembly.
- [ ] An Onshape Education account exists with a non-default profile photo,
      a real display name, and inch units.
- [ ] FRCDesignApp / FRCDesignLib is installed and visible after a reload.
- [ ] Tube Converter, Extrude Individual, Fillet All Edges, Robot Shaft,
      Robot Spacer, Robot Spline Profile, Belt & Chain Gen, Origin Cube, and
      Part Lighten appear in your custom-features dropdown.
- [ ] A document you own named something like `CAD Learning — YourName`
      exists, and a mentor has a share link or a screenshot of that toolbar.
- [ ] A short written note (the two sentences from Task 1) is included with
      the share.

## Resources

- [FRCDesign Learning Course](https://frcdesign.org/learning-course/)
- [FRCDesign Website Feature Guide](https://frcdesign.org/feature-guide/)
- [New to CAD](https://frcdesign.org/learning-course/course-setup/new-to-cad/)
- [Account Setup](https://frcdesign.org/learning-course/course-setup/new-to-onshape/account-setup/)
- [Performance Tuning](https://frcdesign.org/learning-course/course-setup/new-to-onshape/performance-tuning/)
- [Documents Page](https://frcdesign.org/learning-course/course-setup/new-to-onshape/documents-page/)
- [Part Library / FRCDesignApp](https://frcdesign.org/learning-course/course-setup/required-course-tools/part-library/)
- [Required FeatureScripts](https://frcdesign.org/learning-course/course-setup/required-course-tools/featurescripts/)
- [Featurescript Help](https://frcdesign.org/resources/featurescript-help/)
- [Onshape Education plan](https://www.onshape.com/en/education/)
- [Onshape Learning Center](https://learn.onshape.com/)
- [Navigating a Document (Onshape)](https://learn.onshape.com/courses/navigating-a-document)
- [CAD Basics learning pathway](https://learn.onshape.com/learn/learning-path/introduction-to-cad)

## Notes

- Do not skip FeatureScript setup. Stage 1A Exercise 1 uses Tube Converter
  on the first tube you make. Later tickets assume Robot Shaft, Belt & Chain
  Gen, Origin Cube, and Part Lighten are already on your toolbar.
- Education subscriptions expire. Renew under Account → Subscriptions when
  Onshape warns you, or you will lose private documents mid-season.
- This playbook does not replace FRCDesign. When a later ticket says "do
  Exercise 3," it means on the FRCDesign page, in the document you copied
  into your account.
- The next ticket ([Onshape Fundamentals](../onshape-fundamentals/)) is
  Stage 1A: copy the provided document, then sketch, extrude, and assemble
  through every listed exercise.
