---
layout: electrical-lesson
title: Motors & Motor Controllers
subtitle: Brushed vs. brushless motors, CAN vs. PWM control, and wiring controllers from the PDH to the motor.
permalink: /learning/electrical/motors-controllers/
role: veteran
order: 6
size: 2
time: "1–2 hrs"
---

## Description

Motors are how the robot does work. A motor controller is a fast switch
that turns battery current into a commanded voltage (or current) at the
motor. The roboRIO does not drive a CIM or a NEO directly — it asks a
controller, and the controller handles the power.

Two physics distinctions matter more than brand names.

**Brushed vs. brushless.** A brushed motor (CIM, BAG, 775-class) uses
physical brushes and a commutator to reverse current in the spinning
windings. Two fat wires, simple. A brushless motor (NEO, Kraken, Falcon)
moves that switching into electronics: the controller commutates stator
coils around a magnet rotor. More efficient and more power per pound;
also more ways to wire it wrong. Many modern controllers can run either
type, but they must be **told**. A SPARK MAX defaults to brushless —
cyan or magenta idle LED. Hold the mode button to switch to brushed
(blue or yellow). Putting 12 V of "brushed" thinking into a brushless
motor, or the other way around, is how you let the smoke out.

**CAN vs. PWM.** PWM is one signal wire per controller and no useful
feedback. CAN is a daisy-chained pair (yellow = high, green = low) that
carries commands **and** current, temperature, faults, and sensor data.
Each device needs a unique CAN ID. Competitive robots run almost
everything on CAN. A bus only works if it is one chain with termination
at both ends — you found the PDH terminator in
[Power Distribution](../power-distribution/).

Wiring a controller is a polarity problem dressed as a connector
problem. **Power input** is `V+ / V−` (or the red/black pigtail that is
*not* marked `M+ / M−`). That pair goes to a high-current PDH channel
behind a correctly sized breaker. **Motor output** is `M+ / M−` and goes
to the motor, red-to-red / black-to-black (or the motor's documented
colors). Landing battery voltage on the motor terminals is a classic,
expensive mistake. Confirm the controller LED matches the motor type
**before** anyone enables.

The robot stays in the safe state until a mentor is watching the first
power-on. Blocks under the drive. Hands off the mechanism.

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a mentor
accepts the criteria below.

## Prerequisites

- [Power Distribution](../power-distribution/) and
  [Wiring Craftsmanship](../wiring-craftsmanship/) completed (you
  already have a tug-tested power run and a passing ferrule).
- A spare controller and motor, or a robot mechanism a mentor will let
  you land. Battery off until the walkthrough is done.

## What you'll learn

- The difference between brushed and brushless, in terms of who does
  the commutating.
- Common FRC motors and the controllers that drive them.
- When CAN is worth the extra wire (almost always) and what PWM still
  does.
- How to wire power in, motor out, and CAN without swapping V and M.

## Tasks

1. **Watch the two machines.** Watch
   [How does an electric motor work? (DC / brushed)](https://www.youtube.com/watch?v=GQatiB-JHdI)
   (The Engineering Mindset) and
   [Brushless DC motor — how it works](https://www.youtube.com/watch?v=bCEiOnuODac)
   (Learn Engineering). Write four sentences: *A brush commutates
   by …*, *A brushless controller commutates by …*, *I can tell this
   motor is brushed because …*, *I can tell this motor is brushless
   because …*. Keep the note — a mentor will ask.

2. **Read the vendor pages for the hardware you actually have.** You
   do not need every controller on earth. You need the ones on this
   robot:

   - REV:
     [SPARK MAX overview](https://docs.revrobotics.com/brushless/spark-max/overview),
     [operating modes](https://docs.revrobotics.com/brushless/spark-max/operating-modes),
     and
     [status LED patterns](https://docs.revrobotics.com/brushless/spark-max/status-led).
   - CTRE:
     [Phoenix 6 hardware reference](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
     and the
     [Talon FX page](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/talonfx/index.html)
     (Falcon / Kraken have the controller in the motor).
   - WPILib:
     [Using CAN devices](https://docs.wpilib.org/en/stable/docs/software/can-devices/index.html)
     and the SPARK MAX mode note in
     [Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html).

   Fill this table for *your* robot, not a catalog:

   | Controller | Vendor | Motor it drives here | Brushed or brushless? | CAN, PWM, or both? |
   | --- | --- | --- | --- | --- |
   | SPARK MAX / SPARK Flex | REV | | | |
   | Talon FX (integrated) | CTRE | | | |
   | Talon SRX / Victor SPX (if present) | CTRE | | | |

3. **Read the LED before you apply power.** With the controller
   powered only if a mentor is present and the robot is on blocks:
   name the idle color and what it means (SPARK MAX: cyan/magenta =
   brushless, blue/yellow = brushed; brake vs. coast is the other
   axis). If the color does not match the motor sitting next to it,
   fix the mode *before* anyone enables. Hold-to-swap on a SPARK MAX
   is about 3–4 seconds — the wiring doc walks it.

4. **Land the three connections, in order.** Battery still
   disconnected until a mentor checks polarity. Then:

   1. **Power in** to `V+ / V−` from a high-current PDH channel
      behind a correctly sized breaker (typically 40 A, never above
      the wire or the
      [game manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)).
      Red to V+, black to V−. Tug. Whisker check.
   2. **Motor out** to the motor leads, matching colors, using Wago
      221 or the team's equivalent. Confirm you did **not** put
      battery voltage on `M+ / M−`.
   3. **CAN** in and out, yellow to high, green to low, daisy-chained
      toward the next device. Unique ID is a programmer/lead job —
      do not clone an ID "to see if it works."

   **Double-check that the red power wire goes to V+, never M+.**
   Swapping power and motor terminals is the classic, damaging
   mistake this ticket exists to prevent.

5. **Power on only for a LED and polarity check.** Safe state first
   (blocks, announce, mentor watching). Main breaker on. Confirm the
   controller LED matches Task 3. Do **not** enable drive unless a
   mentor and a programmer are running a known-safe Test-mode bump.
   If something smells or the LED is a fault color, breaker off,
   battery off, then look — you will use the full LED charts in
   [Status Lights](../status-lights-fault-codes/).

6. **Hand it in.** A mentor looks at V vs. M, CAN colors, labels,
   strain relief, and the LED. If your team exported these tickets,
   attach a photo of the landed controller and move the issue to
   In Review.

## Acceptance Criteria

- [ ] You stated, for a motor on the table, whether it is brushed or
      brushless and what mode its controller needs, in your own
      words (not "the sticker says NEO").
- [ ] You explained one real trade-off between CAN and PWM (feedback
      and wiring count vs. simplicity).
- [ ] You wired a motor controller end to end — power in on V+/V−,
      motor out on M+/M−, CAN yellow/green — with correct polarity
      and tug-tested joints. A mentor verified you did not land 12 V
      on the motor terminals.
- [ ] The controller status LED indicated the correct motor type
      before anyone enabled.
- [ ] The run is labeled and strain-relieved to the
      [Wiring Craftsmanship](../wiring-craftsmanship/) standard.

## Resources

- [CTRE Phoenix 6 hardware reference](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
- [CTRE Talon FX hardware](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/talonfx/index.html)
- [REV SPARK MAX overview](https://docs.revrobotics.com/brushless/spark-max/overview)
- [REV SPARK MAX operating modes](https://docs.revrobotics.com/brushless/spark-max/operating-modes)
- [REV SPARK MAX status LEDs](https://docs.revrobotics.com/brushless/spark-max/status-led)
- [WPILib: CAN devices](https://docs.wpilib.org/en/stable/docs/software/can-devices/index.html)
- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
- [How a DC motor works (YouTube)](https://www.youtube.com/watch?v=GQatiB-JHdI)
- [How a brushless motor works (YouTube)](https://www.youtube.com/watch?v=bCEiOnuODac)
- [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)

## Notes

- Integrated controllers (Talon FX in a Kraken/Falcon) still have a
  power pair and a CAN pair. There is no separate "motor output"
  because the motor is the can. Do not invent one.
- Duplicate CAN IDs make two devices lie in turns. Never "just
  match the ID on the other side."
- The next ticket ([Sensors & Signal Inputs](../sensors/)) is the
  other half of useful motion: limit switches, encoders, gyros, and
  the rule that signal wire does not ride next to motor-power wire.
