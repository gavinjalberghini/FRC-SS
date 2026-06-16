---
layout: electrical-lesson
title: Wiring Craftsmanship
subtitle: Wire gauge, crimping, ferrules, connectors, labeling, and strain relief — wiring that survives a season.
permalink: /learning/electrical/wiring-craftsmanship/
role: veteran
order: 5
size: 2
time: "2–3 hrs"
---

## Overview

Good wiring is the difference between a robot that runs all season and one that
dies mysteriously between matches. Level 2 is where you stop just identifying
parts and start *building* to a standard. This lesson covers the craft: choosing
wire, making solid connections, and managing wire so it survives the abuse of a
competition.

## Prerequisites

- [Electrical Safety](../electrical-safety/).
- [The FRC Control System](../control-system/) and [Power Distribution](../power-distribution/).

## What you'll learn

- How to choose wire gauge for a given current.
- How to strip, crimp, and ferrule wire so connections don't fail.
- Connector types and when to use each.
- Labeling, color conventions, and strain relief.

## Unit 1 — Wire gauge

Thicker wire (lower AWG number) carries more current with less voltage drop and
heat. Typical FRC choices:

- **6 AWG** — battery and main power leads.
- **10–12 AWG** — motor and high-current motor-controller leads.
- **18 AWG** — roboRIO, radio, and other low-current devices.
- **22 AWG** — CAN bus data wires.

Always match the wire to the breaker/fuse protecting it and to the current
limits in the game manual.

## Unit 2 — Making connections

- **Strip cleanly.** Use the correct gauge slot so you don't nick strands. Nicked
  strands break and add resistance.
- **Crimp, don't just twist.** A proper crimp on a terminal lug or connector is
  gas-tight and mechanically strong. Tug-test every crimp.
- **Ferrules** on stranded wire give a clean, solid insert into lever/spring
  terminals (PDH, roboRIO, PH). Use the right ferrule size and crimp tool.
- **Verify insertion.** Many connectors (Wago 221, PDH terminals) have an
  inspection window — confirm copper is seated past the metal.

## Unit 3 — Connectors

- **Anderson SB50** — battery connection.
- **Wago 221 lever connectors** — fast, reliable inline splices for motor power.
- **PDH lever/spring terminals** — branch power.
- **Weidmuller / spring terminals** on the roboRIO — push-button release.
- **CAN connectors / daisy chain** — covered in the CAN lesson.

## Unit 4 — Labeling & strain relief

- **Color convention:** red = positive, black = negative; CAN uses yellow (high)
  and green (low).
- **Label both ends** of every wire with its device/channel.
- **Strain relief:** secure wire near each connector so motion and vibration pull
  on the tie, not the joint. Leave a small service loop — never pull a connection
  tight.
- **Route away from moving parts** (belts, chains, sharp edges); shield wires
  that pass through metal.

## Steps & acceptance criteria

- [ ] Select correct wire gauge for the battery lead, a motor, and the roboRIO.
- [ ] Make a clean strip, a tug-tested crimp, and a properly ferruled wire end.
- [ ] Wire one motor controller from the PDH to the motor with correct polarity,
      labeling, and strain relief.
- [ ] Explain your team's color and labeling convention.

## Resources

- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
- [WPILib: Wiring Best Practices](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/robot-preemptive-troubleshooting.html)

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — document your team's standard wire colors, gauge-per-subsystem chart, label format, and preferred crimp tools/connectors here.</p>
</div>
