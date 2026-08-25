---
layout: electrical-lesson
title: Sensors & Signal Inputs
subtitle: Limit switches, encoders, gyros, and rangefinders — by function and by how they talk to the roboRIO.
permalink: /learning/electrical/sensors/
role: veteran
order: 7
size: 2
time: "1–2 hrs"
---

## Description

Sensors let the robot perceive its environment and its own mechanisms. A
robot that knows where its arm is, how far it has driven, or which way
it is facing can score faster — and stop before it bends a shaft. This
ticket categorizes sensors two ways: by **what they measure** and by
**how they communicate** with the roboRIO. Function drives design.
Protocol drives wiring.

You already know the power tree
([Power Distribution](../power-distribution/)) and you can make a joint
that survives a tug
([Wiring Craftsmanship](../wiring-craftsmanship/)). Sensors fail in
quieter ways: a 5 V device fed from 12 V, a limit switch that flexes
and double-hits, a signal wire that picked up the PWM hash from a
motor lead running next to it. The habit is the same as power —
correct voltage, correct port, strain relief, then a mentor tug — plus
one new rule: **signal and motor-power wiring do not share a bundle**.

Many brushless controllers already include an encoder. Position over
CAN is "free" once the motor is on the bus. You still need discrete
sensors for end-of-travel, heading, and distance. You will wire a
limit switch to a DIO port and an analog sensor to an analog input on
a real roboRIO or a breakout. You will not write Java here; you will
know which three pins you just used so a programmer is not guessing.

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a
mentor accepts the criteria below.

## Prerequisites

- [The FRC Control System](../control-system/) and
  [Wiring Craftsmanship](../wiring-craftsmanship/) completed.
- [Motors & Motor Controllers](../motors-controllers/) completed so
  you know why motor-power wire is noisy.
- A roboRIO (or a robot in the safe state) and at least one
  mechanical limit switch plus one analog sensor (potentiometer,
  analog pressure sensor, or similar).

## What you'll learn

- Common sensor types grouped by what they measure.
- The three communication buckets — analog, digital, serial — and
  which roboRIO pins each one uses.
- How to wire and mount a sensor so the reading is the mechanism, not
  the flex in the bracket.

## Tasks

1. **Read the hardware overview, then one protocol page.** Read
   [WPILib: Sensor Overview — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/sensor-overview-hardware.html)
   and
   [WPILib: Digital Inputs — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/digital-inputs-hardware.html).
   Skim
   [WPILib: Sensor Overview — Software](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/sensors/index.html)
   only far enough to see that each hardware class has a matching
   software class. Open
   [WPILib: Analog Inputs — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/analog-inputs-hardware.html)
   and keep them on the bench (both pages show the S / V / ground pin
   layout). You will tour every specialty port in
   [roboRIO Ports](../roborio-ports/); today you need DIO and analog.

2. **Sort sensors by function.** On a scratch note, write one
   sentence each for the groups below, then walk a robot or parts
   drawer and write the *actual part name* your team uses in that
   group (or "we do not have one"):

   - **Proximity / limit** — presence or end-of-travel. Mechanical
     switches, magnetic, inductive, photoelectric.
   - **Distance** — ultrasonic, triangulating rangefinder, LIDAR.
   - **Shaft rotation** — **encoders** (count rotation / position)
     and **potentiometers** (absolute angle over a limited range).
   - **Acceleration** — accelerometers.
   - **Heading / rotation rate** — gyros. A heading gyro is how
     swerve and autonomous know "which way is forward."

   Built-in motor encoders count as the shaft-rotation row. Say so.

3. **Sort the same sensors by protocol.** For each part you named,
   write **analog**, **digital (DIO)**, or **serial** (CAN, I2C,
   SPI, RS-232):

   - **Analog input** — a voltage proportional to the reading
     (potentiometer, analog pressure sensor). Three pins: signal,
     power, ground. Respect the sensor's voltage.
   - **Digital input (DIO)** — on/off (limit switches) and
     pulse trains (quadrature encoders). The roboRIO DIO rail is
     **5 V**. A simple switch goes between **signal and ground**;
     the port's pull-up makes an open switch read high and a
     closed switch read low. A powered three-wire sensor uses
     signal, 5 V, and ground.
   - **Serial bus** — richer devices (navX on SPI or I2C, many
     gyros, CAN sensors). Ports and addresses are the next ticket.

   Analog and DIO are simple to support. Serial is more capable and
   more ways to get the wiring wrong.

4. **Wire a limit switch to DIO.** Robot in the safe state. Using
   the DIO hardware page:

   - Pick an unused DIO (0–9 on the roboRIO).
   - Two-wire switch: one side to **S**, the other to **ground**.
     Do not jumper 5 V to ground.
   - Strain-relieve at the switch body and at the roboRIO. Mount
     the switch so the mechanism hits the lever, not so the
     bracket flexes and chatters.
   - Label both ends with the DIO number and the mechanism
     ("elevator top", not "switch 2").

   Tug both ends. Ask a programmer (or a mentor with a laptop) to
   confirm the DIO changes state when you press the lever. You do
   not write the code.

5. **Wire an analog sensor.** Same standard: matching voltage
   (many analog sensors are 5 V; some specialty parts are 3.3 V —
   **read the datasheet**, do not assume), signal to analog **S**,
   power to **V**, ground to ground. Route the signal cable **away
   from** the motor-power run you built in the last ticket. If the
   only path is next to a motor lead, say so to a mentor — that is
   a design problem, not a zip-tie problem.

6. **Explain the noise rule.** Tell a mentor, in two sentences,
   why a limit-switch cable should not be tie-wrapped to a 40 A
   motor lead for three feet. The short version: changing current
   in the fat wire induces voltage in the skinny one, and the
   roboRIO will believe it.

7. **Hand it in.** A mentor presses the limit switch and looks at
   both landings. If your team exported these tickets, attach a
   labeled photo of the DIO and analog runs and move the issue to
   In Review.

## Acceptance Criteria

- [ ] You matched at least three real sensors (on the robot or in
      the drawer) to what they measure.
- [ ] For each of those three, you stated analog, digital, or
      serial, and which roboRIO resource it uses.
- [ ] A limit switch is wired to a DIO (signal and ground for a
      two-wire switch), labeled, strain-relieved, and changes
      state when pressed.
- [ ] An analog sensor is wired to an analog input at the correct
      voltage, labeled, and routed off the motor-power bundle.
- [ ] You explained, in your own words, why signal and power
      wiring are routed separately.

## Resources

- [WPILib: Sensor Overview — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/sensor-overview-hardware.html)
- [WPILib: Sensor Overview — Software](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/sensors/index.html)
- [WPILib: Digital Inputs — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/digital-inputs-hardware.html)
- [WPILib: Analog Inputs — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/analog-inputs-hardware.html)
- [WPILib: Encoders — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/encoders-hardware.html)
- [WPILib: Gyroscopes — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/gyros-hardware.html)
- [WPILib: Serial buses](https://docs.wpilib.org/en/stable/docs/hardware/sensors/serial-buses.html)
- [WPILib: Wiring Best Practices](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-best-practices.html)

## Notes

- Many DIO and I2C devices are unhappy at 12 V and some are unhappy
  at 5 V. The pin can supply 5 V or 3.3 V depending on the port.
  Read the device page before you land power.
- A limit switch that "works on the bench" and chatters on the
  robot is usually a floppy mount, not a bad switch.
- The next ticket,
  [Pneumatics 2: Purpose & Construction](../pneumatics-construction/),
  puts the identification from
  [Pneumatics 1](../pneumatics-identification/) onto a board you
  can inspect. After that, [roboRIO Ports](../roborio-ports/)
  finishes the serial-bus half of this ticket.
