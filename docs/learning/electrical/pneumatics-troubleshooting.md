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

## Description

The highest pneumatics level is about *engineering* the system, not
just building it. You already named every part
([Pneumatics 1](../pneumatics-identification/)) and assembled a
leak-free board ([Pneumatics 2](../pneumatics-construction/)). Now you
calculate how much force a cylinder produces, how much air the tanks
store, and how often the compressor must run — then you troubleshoot
when the numbers do not match the robot in front of you.

The physics is one line: **force = pressure × area**. A 2-inch-bore
cylinder at 60 PSI is not "a medium cylinder." It is about 188 lbf on
the push side, less on the pull side because the rod steals area.
Stored energy lives in the high-side tanks at up to **120 PSI**
(current manuals — check). Work happens after the regulator, commonly
at **60 PSI**. The game manual sets both numbers and the legal parts
list. The FIRST pneumatics PDF teaches the circuit. If they disagree,
the **game manual wins**.

Troubleshooting air uses the same five steps as
[Systematic Troubleshooting](../troubleshooting/): isolate the
subsystem, read the PH/PCM lights, start at the cylinder, check every
input (power, signal, **air**), walk up to a known-good item. The
extra rule you already own: **vent first**. A pressurized fitting is
a spring.

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a
mentor accepts the criteria below.

## Prerequisites

- [Pneumatics 2: Purpose & Construction](../pneumatics-construction/)
  completed (you have built and demoed a board).
- [Systematic Troubleshooting & Team Protocols](../troubleshooting/)
  completed (five-step hunt and verbal protocol).
- A calculator, a tape measure or calipers, and a board or robot you
  can diagnose. A mentor to stage a leak, a weak cylinder, or a dead
  solenoid.

## What you'll learn

- How to calculate cylinder push and pull force from bore, rod, and
  working pressure.
- How to reason about stored volume, recharge rate, and strokes per
  charge.
- How to apply the electrical troubleshooting method to air without
  skipping the vent.

## Tasks

1. **Re-read the rules, then the teaching PDF.** Open the current
   [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
   Pneumatic System section
   ([2026 PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf),
   section 8.8) and write today's stored-pressure cap and
   working-pressure requirement on the calculation sheet. Then skim
   [FIRST Pneumatics Manual](https://www.firstinspires.org/hubfs/web/program/frc/resources/pneumatics-manual.pdf)
   for the high-side / working-side diagram and the leak-test
   procedure. Vendor pages if you need module lights:
   [REV PH overview](https://docs.revrobotics.com/ion-control/ph/overview)
   and
   [PH status LEDs](https://docs.revrobotics.com/ion-control/ph/status-led).
   Software-side context only:
   [WPILib: Pneumatics APIs](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/pneumatics/index.html).

2. **Calculate push and pull force.** Force is piston area times
   applied **working** pressure (the number on the regulator gauge,
   not the tank gauge).

   - Piston area = π r², where r is half the **bore**.
   - **Push force** = piston area × pressure.
     Example (keep this one on the sheet): 2 in bore, so r = 1 in,
     area = π × 1² ≈ 3.14 in². At 60 PSI:
     3.14 × 60 ≈ **188 lbf**.
   - **Pull force** = (piston area − rod area) × pressure.
     Rod area is π times (rod radius)². Subtract that from 3.14 in²,
     then multiply by 60 PSI. A typical rod on that cylinder lands
     around **165 lbf**. The cylinder **pushes harder than it
     pulls**.

   Now do it for a cylinder on *this* robot or practice board:
   measure or read bore and rod, read the regulator, compute push
   and pull. Write the units (lbf). If the mechanism needs more
   force than that, you change bore or working pressure (within the
   manual) — you do not "turn the regulator past 60 because the
   hatch was sticky."

3. **Estimate volume, recharge, and strokes per charge.** On the
   same sheet:

   - **Stored volume** depends on the number and size of
     accumulators and the stored pressure (high side, ≤ 120 PSI
     unless the current manual says otherwise). More tanks store
     more air.
   - **Recharge rate** is how fast the compressor can put that
     air back. Compressor flow is limited by the manual (about
     1.1 CFM class in recent seasons — read the current R8xx
     compressor rule). More tanks means **fewer** compressor
     cycles during a match and a **longer** fill from empty.
   - **Cylinder displacement** per stroke ≈ piston area × stroke
     (push and pull each use a volume; they are not equal if the
     rod takes space).
   - **Strokes per charge** ≈ (usable stored air on the working
     side) / (air used per cycle). "Usable" is the air you can
     spend before working pressure falls below what the
     mechanism needs — not the air down to 0 PSI.

   These numbers tell you whether the system can keep up with
   match demand. If the hatch fires twelve times a match and you
   have three strokes of stored air, you have a design problem,
   not a "the compressor is weak" problem.

4. **Leave margin.** Real cylinders lose force to friction and
   seal drag. Real fittings leak a little. Real regulators droop
   under flow. If the mechanism needs 180 lbf, a 188 lbf
   calculation is not "done." Write a 20% margin on the sheet and
   say whether the chosen bore still clears it.

5. **Apply the five-step hunt to air.** Vent first if you will
   open anything. Then, with a mentor-staged fault (leak, weak
   actuation, or a solenoid that will not fire):

   1. Isolate: "pneumatics / this cylinder."
   2. Read PH/PCM status, compressor LED, solenoid channel LED.
   3. Start at the cylinder. Programmer checks that the code is
      actually commanding that channel.
   4. Check every input: working pressure on the gauge, tube
      seating, coil voltage (12 V vs 24 V jumper), CAN, PDH
      channel for the module, square-cut ends.
   5. Walk up to a known-good item (the other solenoid still
      fires; the high-side gauge is fine; only this tube hisses).

   Use this symptom list — it is a start, not a substitute for
   the hunt:

   - **No / low pressure:** compressor not running (power,
     pressure switch, module fault light) or a leak. Listen,
     then soapy water.
   - **Leaks:** most often press-fit connections with
     non-square tube, or pinched / over-bent tubing that acts
     like an orifice.
   - **Slow or weak actuation:** flow control too tight,
     regulator too low, or the math from Task 2 says the
     cylinder was never going to move this load.
   - **Solenoid will not fire:** control signal, coil voltage,
     then the **manual override** button to isolate electrical
     vs. mechanical (you practiced that in Pneumatics 2).
   - **Always vent** with the pressure vent plug before you
     pull a fitting.

6. **Write the diagnosis.** One paragraph: what you saw on the
   lights and gauges, the known-good item, the actual fault, and
   the force numbers that say whether the system was sized to
   succeed. If your team has a Pneumatics Level 3 sheet, this
   paragraph plus the calculation sheet *is* that assessment.

7. **Hand it in.** A mentor reads the math (they should be able
   to reproduce the 188 lbf example and your robot's numbers)
   and watches the staged diagnosis. If your team exported these
   tickets, attach the calculation sheet and move the issue to
   In Review.

## Acceptance Criteria

- [ ] You calculated push and pull force for a given bore, rod,
      and working pressure, including the 2 in / 60 PSI example
      (~188 lbf push) and one real cylinder on the team.
- [ ] You estimated stored volume, recharge behavior, and strokes
      per charge well enough to say whether the system can survive
      a match, and you stated the current manual's pressure caps.
- [ ] You diagnosed a staged fault (leak, weak actuation, or dead
      solenoid) with the five-step method, starting from lights
      and ending at a known-good item. You vented before opening
      the system.
- [ ] You used the solenoid manual override to separate
      electrical from mechanical when the fault was a dead
      valve.
- [ ] A mentor signed the team's Pneumatics Level 3 assessment,
      or the equivalent review of the calculation sheet plus the
      staged hunt.

## Resources

- [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
- [2026 Game Manual PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
  — section 8.8 Pneumatic System
- [FIRST Pneumatics Manual](https://www.firstinspires.org/hubfs/web/program/frc/resources/pneumatics-manual.pdf)
- [WPILib: Pneumatics](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/pneumatics/index.html)
- [WPILib: Wiring Pneumatics — REV PH](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-pneumatics-ph.html)
- [REV Pneumatic Hub overview](https://docs.revrobotics.com/ion-control/ph/overview)
- [REV PH status LEDs](https://docs.revrobotics.com/ion-control/ph/status-led)
- [WPILib: Status Light Quick Reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html)

## Notes

- Force calculations assume ideal conditions. Seals drag. Leave
  margin. Do not regulate above the manual to paper over a small
  bore.
- This is the last electrical ticket. A lead technician can put
  a robot in a safe state, name every device, land a tug-tested
  joint, read a status LED, walk a fault tree, and say whether
  a cylinder was ever going to lift the mechanism. That is the
  whole ladder, in order: safety → identify → power → pneumatics
  ID → craftsmanship → motors → sensors → build pneumatics →
  ports → lights → troubleshooting → this math.
