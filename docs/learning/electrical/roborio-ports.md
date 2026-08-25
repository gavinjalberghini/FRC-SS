---
layout: electrical-lesson
title: roboRIO Ports & Communication Protocols
subtitle: CAN, I2C, SPI, RS-232, MXP, and the user/reset buttons — what each port does and when to use it.
permalink: /learning/electrical/roborio-ports/
role: lead
order: 9
size: 2
time: "1–2 hrs"
---

## Description

The roboRIO is the robot's main controller, and it has a lot of
specialty ports. A Level 3 technician understands every port — not just
the DIO and analog you used in
[Sensors & Signal Inputs](../sensors/) — so they can land an unusual
device and reason about a silent bus. This ticket is a tour of the
ports and the protocols they speak. You will stand over a real roboRIO
with the
[serial-bus and I/O pages](https://docs.wpilib.org/en/stable/docs/hardware/sensors/serial-buses.html)
open and point. Then you will research one real device per specialty
port so the names attach to hardware, not to a legend on a slide.

Protocols are just agreements about voltage, timing, and who is allowed
to talk. **CAN** is the robot's backbone: a two-wire differential pair
that survives the noise of motor leads better than a single-ended PWM
line. **I2C** is a two-wire addressable bus at **3.3 V** on the
roboRIO. **SPI** is faster, chip-select per device, often how an
onboard or navX-class gyro is hung. **RS-232** is old, slow, and
everywhere — ground, receive, transmit. Mix the voltages or swap CAN
high and low and the bus looks "dead" when the wire is fine. That is
why this ticket exists before you spend an hour in
[Status Lights](../status-lights-fault-codes/) staring at a red Comm
LED.

The robot stays in the safe state while you probe ports. You do not
hot-plug 12 V into a 3.3 V pin to "see if it enumerates."

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a
mentor accepts the criteria below.

## Prerequisites

- [The FRC Control System](../control-system/) and
  [Sensors & Signal Inputs](../sensors/) completed.
- A roboRIO you can stand over (robot in the safe state, or a spare
  on the bench) and a laptop for the research write-up.

## What you'll learn

- The communication protocols on the roboRIO and the pins each one
  uses.
- What the onboard buttons and the MXP expansion port do.
- A habit of researching one real-world use for each specialty port
  instead of memorizing an empty list.

## Tasks

1. **Open the I/O pages and the CAN page.** Keep
   [WPILib: Serial buses](https://docs.wpilib.org/en/stable/docs/hardware/sensors/serial-buses.html)
   (I2C, SPI, RS-232, MXP photographs) and
   [WPILib: Digital Inputs — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/digital-inputs-hardware.html)
   on the bench. Read
   [WPILib: CAN devices](https://docs.wpilib.org/en/stable/docs/software/can-devices/index.html)
   and
   [WPILib: CAN Wiring Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/can-wiring-basics.html).
   Skim the
   [NI roboRIO user manual](https://www.ni.com/docs/en-US/bundle/roborio-frc-2/page/manual.html)
   for the button and port photographs. You are matching silk-screen
   to protocol, not imaging a roboRIO.

2. **CAN, with your finger on the connector.** The CAN bus is the
   communications backbone. It daisy-chains the roboRIO to the PDH,
   motor controllers, and the pneumatics module.

   - **Yellow = HIGH, green = LOW.** Newer roboRIOs print the
     color names on the connector. Swapping them is a silent bus.
   - The bus must be **terminated at both ends** with 120 Ω. The
     roboRIO is one end. The PDH (or PDP) ships with a termination
     switch — you found it in
     [Power Distribution](../power-distribution/). If the PDH is
     in the middle of the chain, that switch is OFF and you owe a
     terminator at the real end.
   - CTRE's
     [CAN bus troubleshooting](https://v6.docs.ctr-electronics.com/en/stable/docs/troubleshooting/canbus-troubleshooting.html)
     is the page you will actually use at an event when LEDs go
     red. Read the termination and "jostle the harness" sections.

   On a scratch note: draw this robot's CAN chain in order, mark
   the two terminators, and write the color of each wire.

3. **Serial protocols, pin by pin.** Standing at the roboRIO, point
   at each port and say the pins out loud:

   - **I2C (Inter-Integrated Circuit)** — two shared wires, many
     devices, each with a unique address. Pins: ground, power
     (**3.3 V**), SCL (clock), SDA (data). The roboRIO is master;
     devices are slaves. Feeding I2C 5 V or 12 V is how you buy a
     new gyro.
   - **SPI (Serial Peripheral Interface)** — faster. Shared clock
     and data plus a **chip select** per device (up to four on
     the dedicated SPI). Signals: SCK, MOSI (master out / slave
     in), MISO (master in / slave out), CS. Onboard and navX-class
     gyros often live here.
   - **RS-232 (UART)** — basic, relatively slow, very common.
     Pins: ground, receive, transmit. Cross RX/TX if the device
     expects to talk to a PC.

   Write the pin list for each on the same note. You will need it
   for Task 5.

4. **MXP and the two buttons.**

   - **MXP (myRIO Expansion Port)** — the dense connector that
     accepts breakout boards (more DIO, more analog, more SPI/I2C).
     Screw holes hold the board so it does not lever out in
     defense.
   - **Reset button** — held for about 5 seconds, reboots the
     FPGA and processor. This is not an enable button and not a
     "make it drive" button.
   - **User button** — a general-purpose input readable in code.
     It is **not** debounced. Do not design a critical interlock
     that is only this button.

   Point at both buttons without hovering a metal tool across
   nearby pins.

5. **Research usage.** For **each** specialty port (CAN already
   has a job — pick a *specific* device on your robot; then I2C,
   SPI, RS-232, and MXP), find one real example of a team or a
   COTS device using it. Examples that count: a navX on SPI or
   I2C, a REV or CTRE gyro, a sensor that actually speaks RS-232,
   an MXP breakout. Write a short page (a dozen lines is enough)
   in your team's learning repo or a shared note:

   - port name
   - pin/voltage trap
   - the device you found
   - a link to the datasheet or vendor page

   Being able to point at a concrete use is the whole point. A
   list of acronyms is not.

6. **Hand the note and the write-up to a mentor.** Walk the
   roboRIO with them. If your team exported these tickets, link
   the write-up and move the issue to In Review.

## Acceptance Criteria

- [ ] You named every user-facing port on the roboRIO (CAN, I2C,
      SPI, RS-232, DIO, analog, PWM, MXP, USB, Ethernet, RSL) and
      the protocol or job it uses.
- [ ] You stated the wire/pin meaning for CAN (H/L + termination),
      I2C (3.3 V, SCL, SDA), SPI (SCK, MOSI, MISO, CS), and RS-232
      (GND, RX, TX).
- [ ] You explained what the reset button and the user button do
      — and what they are *not*.
- [ ] You researched and presented one real device for each
      specialty port (I2C, SPI, RS-232, MXP), with a link a mentor
      can open.
- [ ] Your CAN sketch of *this* robot marks both terminators.

## Resources

- [WPILib: roboRIO introduction](https://docs.wpilib.org/en/stable/docs/software/roborio-info/roborio-introduction.html)
- [WPILib: CAN devices](https://docs.wpilib.org/en/stable/docs/software/can-devices/index.html)
- [WPILib: CAN Wiring Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/can-wiring-basics.html)
- [WPILib: Serial buses (sensors)](https://docs.wpilib.org/en/stable/docs/hardware/sensors/serial-buses.html)
- [NI roboRIO User Manual](https://www.ni.com/docs/en-US/bundle/roborio-frc-2/page/manual.html)
- [CTRE: CAN bus troubleshooting](https://v6.docs.ctr-electronics.com/en/stable/docs/troubleshooting/canbus-troubleshooting.html)
- [WPILib: Hardware Component Overview](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-hardware.html)

## Notes

- I2C on the roboRIO is 3.3 V. "It is just I2C" is not permission
  to use a 5 V module without a level shifter the vendor documents.
- The next ticket,
  [Status Lights & Fault Codes](../status-lights-fault-codes/), is
  how these ports complain when they are unhappy: roboRIO LEDs,
  PDH, SPARK MAX, Talon FX, and the pneumatics module. Bring this
  I/O pages with you.
