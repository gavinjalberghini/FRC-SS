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

## Description

Good wiring is the difference between a robot that runs all season and one
that dies mysteriously between matches. Level 2 is where you stop just
identifying parts and start *building* to a standard. This ticket is the
craft: choosing copper that can carry the current, making a joint that is
gas-tight, and dressing wire so vibration and defense pull on a zip-tie,
not on a ferrule.

The physics is the same as [Electrical Safety](../electrical-safety/).
Thicker wire (a **lower** AWG number) has more cross-section, less
resistance, less `I²R` heat, and less voltage drop at the far end. A
nicked strand is a smaller wire pretending to be the size you stripped.
A loose crimp is a resistor that only shows up when the robot hits the
wall. The breaker you picked in
[Power Distribution](../power-distribution/) protects the wire
*downstream* of it — so the wire, the breaker, and the game manual have
to agree. The **manual wins**.

You will strip, crimp, and ferrule on practice wire, then tug-test every
joint. A ferrule that slides off in your fingers is not a ferrule. You
will also wire one motor-controller power run on a practice board or
spare robot (battery still disconnected until a mentor says otherwise)
with polarity, labels, and strain relief. You are not configuring CAN
IDs or spinning a motor yet — that is
[Motors & Motor Controllers](../motors-controllers/).

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a mentor
accepts the criteria below.

## Prerequisites

- [Electrical Safety](../electrical-safety/) completed.
- [The FRC Control System](../control-system/) and
  [Power Distribution](../power-distribution/) completed.
- A crimper that matches the terminals (ferrule crimper for ferrules,
  lug crimper for lugs — pliers are not a crimper), practice wire, and
  a mentor who will fail a pretty-but-weak crimp.

## What you'll learn

- How to choose wire gauge for a given current, and why AWG numbers
  run backwards.
- How to strip, crimp, and ferrule so the joint survives a tug test.
- Which connector belongs where (SB50, Wago 221, PDH levers, roboRIO
  spring terminals).
- Labeling, color convention, and strain relief that lasts a district
  event.

## Tasks

1. **Read the official craft, not a forum thread.** Read
   [WPILib: Wiring Best Practices](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-best-practices.html)
   and the connector / ferrule / tug-test notes in
   [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
   (the Weidmuller / ferrule section and the Wago lever section). Skim
   [WPILib: Preemptive Troubleshooting](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/preemptive-troubleshooting.html)
   through battery connections and "tug on every wire." Write three
   habits on a scratch note: *strain relief is …*, *a tug test is …*,
   and *whiskers are …*.

2. **Choose gauge on purpose.** Typical FRC starting points — always
   checked against the current
   [game manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system):

   - **6 AWG** (or larger copper) — battery and main power leads.
   - **10–12 AWG** — motor and high-current motor-controller leads.
   - **18 AWG** — roboRIO, radio, and other low-current devices
     (confirm the manual's minimum for that circuit).
   - **22 AWG** — CAN bus data wires (yellow = high, green = low).

   On the scratch note, pick a gauge for (a) the battery lead, (b) a
   drivetrain motor, and (c) the roboRIO feed, and write the breaker
   that would sit upstream of each. If you want more current than the
   wire can carry, you change the wire — you do not swap in a bigger
   breaker.

3. **Strip without nicking.** On practice wire (not the robot), strip
   three ends: one 10–12 AWG, one 18 AWG, one 22 AWG. Use the correct
   gauge slot. Inspect under good light: if you cut or flattened
   strands, cut that end off and do it again. Nicked strands break
   after a weekend of vibration and add resistance now.

4. **Crimp a terminal and a ferrule; tug both.** Using the matching
   tool (hex or square crimp for ferrules — a pair of dikes is not a
   crimp tool):

   - Crimp one ring or fork lug onto practice 10–12 AWG. The
     insulation should be held by the insulation barrel if the lug
     has one; copper should not be visible as a handful of strays.
   - Crimp one ferrule onto practice 18 AWG (the size of ferrule
     that matches the wire — a loose ferrule is a decorative
     sleeve). Ferrules exist so stranded wire enters a lever or
     spring terminal as one piece instead of as whiskers.
   - **Tug test** each joint as if you meant it. If the wire slides
     out, or the ferrule stays in your fingers, scrap it and redo.
     Keep the passing ferrule. That physical part is the artifact.

   WPILib's wiring page shows a ferrule going into a roboRIO
   terminal. Copy that standard, not a YouTube "twist and tape."

5. **Know the connectors by job.** On the practice board or robot
   (battery still off), point at and name:

   - **Anderson SB50** — battery connection. Contacts fully seated.
   - **Wago 221 lever connectors** — common inline splice for motor
     power. Lever open, wire in, lever down, tug, look for whiskers.
   - **PDH lever / spring terminals** — branch power. Many have an
     inspection window: copper should sit past the metal.
   - **roboRIO Weidmuller / spring terminals** — press the button,
     insert, release, tug. A ferrule here is how you stop splay.
   - CAN daisy-chain — you will land CAN in the next ticket; today
     just find the yellow/green pair.

6. **Wire one controller power run to spec.** On a spare board or a
   robot in the safe state, land **power only** for one motor
   controller: PDH high-current channel → correct breaker → V+ / V−
   (red to V+, black to V− — never M+ / M−). Leave the motor leads
   disconnected or clearly tagged if a mentor wants them on. Then:

   - **Color:** red = positive, black = negative.
   - **Label both ends** with device and PDH channel.
   - **Strain relief:** a tie near each connector so a yank loads
     the tie, not the joint. Leave a small service loop. Never pull
     a connection taut.
   - **Route** away from belts, chain, and sharp chassis edges.

   You will finish motor-side and CAN in
   [Motors & Motor Controllers](../motors-controllers/).

7. **Show the work.** A mentor tugs your ferrule and looks at the
   labeled power run. If your team exported these tickets, photo the
   ferrule next to a ruler or the labeled run and move the issue to
   In Review.

## Acceptance Criteria

- [ ] You selected a legal wire gauge for the battery lead, a motor
      run, and the roboRIO, and you named the breaker/fuse that
      protects each. You said the game manual wins.
- [ ] A practice strip has no nicked strands.
- [ ] A crimped ferrule (and a lug, if the shop uses them) passed a
      mentor tug test. The ferrule did not slide off.
- [ ] One motor-controller **power** run is landed on the correct
      PDH terminals with correct polarity, both-end labels, and
      strain relief. A mentor tugged the wires and looked for
      whiskers.
- [ ] You explained the team's color and labeling convention out
      loud (red/black, CAN yellow/green, labels on both ends).

## Resources

- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
- [WPILib: Wiring Best Practices](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-best-practices.html)
- [WPILib: Preemptive Troubleshooting](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/preemptive-troubleshooting.html)
- [WPILib: CAN Wiring Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/can-wiring-basics.html)
- [REV PDH overview](https://docs.revrobotics.com/ion-control/pdh/overview)
- [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)

## Notes

- `git status` before `git add` has an electrical twin: look at the
  joint before you close the lever. Whiskers and half-inserted
  ferrules are how robots brown out on Einstein.
- Do not tin the end of a wire and then stuff it in a Wago or
  spring terminal. Solder creeps; the joint loosens.
- The next ticket ([Motors & Motor Controllers](../motors-controllers/))
  is the rest of that run: motor output, CAN vs. PWM, brushed vs.
  brushless, and the classic "I landed 12 V on M+" mistake.
