---
layout: electrical-lesson
title: Electrical Safety
subtitle: Battery handling, fusing, avoiding shorts, and the safe-state habits that protect people and hardware.
permalink: /learning/electrical/electrical-safety/
role: technician
order: 1
size: 1
time: "30–60 min"
---

## Overview

Everything the electrical team does starts with safety. A 12-volt FRC battery
can deliver hundreds of amps into a short circuit — enough to melt tools, burn
skin, and start fires. This lesson covers the habits that keep people and
hardware safe before you ever pick up a crimper. You cannot earn any other
certification level until you have demonstrated these habits.

## Prerequisites

- None. This is the first lesson for every electrical team member.

## What you'll learn

- How to handle, charge, and store FRC batteries safely.
- Why fusing and circuit breakers matter, and how a short circuit behaves.
- How to put the robot in a known safe state before working on it.
- The personal protective equipment (PPE) and shop habits we expect.

## Unit 1 — The battery is always live

The FRC battery is a 12V sealed lead-acid (SLA) battery. Unlike a wall outlet,
it has no "off switch" — it is energized the moment it exists.

- **Never let the two terminals touch metal at the same time.** A wrench laid
  across both terminals becomes a heating element instantly.
- **Cover terminals** with the connector or a terminal cover whenever the
  battery is not on a robot.
- **Lift with care.** Batteries are ~12 lbs (5.4 kg). Carry by the strap, not
  the wires.
- **Inspect before use.** A cracked case, bulging sides, or leaking acid means
  the battery is retired immediately — tell a mentor.

## Unit 2 — Shorts, fuses, and breakers

A *short circuit* is an unintended low-resistance path between + and −. Because
the battery will push huge current through it, every robot has protection:

- The **120A main breaker** is the master cutoff between the battery and the
  rest of the robot. Flipping it off de-energizes the whole robot.
- **Branch breakers** (e.g. 40A) on the Power Distribution Hub/Panel protect
  each motor controller channel.
- **Fuses** protect low-current devices like the roboRIO and radio.

A breaker or fuse is sized to trip *before* the wire downstream of it overheats.
That is why you never upsize a breaker beyond what the wire and rules allow.

## Unit 3 — The safe state

Before working on robot wiring, put it in a known safe state:

- [ ] **Disconnect the battery** at the Anderson connector — don't just flip the
      main breaker.
- [ ] **Vent any stored pneumatic pressure** with the pressure vent plug (you'll
      learn this in the pneumatics lessons).
- [ ] **Put the robot on blocks** so the wheels are off the ground before any
      power test.
- [ ] **Announce** to nearby people before reconnecting power or enabling.

## Steps & acceptance criteria

- [ ] Demonstrate safe battery carry, terminal protection, and storage.
- [ ] Explain what a short circuit is and how the main breaker, branch breakers,
      and fuses protect against it.
- [ ] Put a robot into a fully safe state (battery disconnected, pressure
      vented, on blocks) without prompting.
- [ ] State the shop's eye-protection and PPE rules.

## Resources

- [FRC Game Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system) — the authoritative source for legal fusing and wiring.
- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html) — note the repeated polarity-check warnings.

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — document your team's specific shop safety rules here: required PPE, battery charging area procedures, who is allowed to connect power, and your fire-extinguisher locations.</p>
</div>
