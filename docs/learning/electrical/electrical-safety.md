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

## Description

Everything the electrical team does starts with safety. A 12-volt FRC battery
is not a wall outlet. It has no off switch. The terminals are live the moment
the battery exists. A healthy Kit-of-Parts sealed lead-acid pack can briefly
push well over 180 A, and a dead short can arc at several hundred amps —
enough to melt a wrench laid across both posts, burn skin, and start a fire.

That is physics, not a scare story. Current is voltage divided by resistance
(`I = V / R`). A short circuit is an unintended path whose resistance is
almost zero, so the current explodes. The heat in that path is `I²R`. The
wrench, the battery tab, and the first few inches of cable become the heating
element. A breaker or fuse exists to open the circuit *before* the wire
downstream of it overheats. That is why you never upsize a breaker past what
the wire can carry, and why the **current game manual wins** on every fuse,
breaker, and wire-gauge question. When this ticket and the manual disagree,
the manual is the rule.

You cannot earn any later electrical ticket until a mentor has watched you
put a robot into a known safe state. This first ticket exists so every later
one — identifying the control system, distributing power, building pneumatics,
crimping, diagnosing lights — happens on a robot that is not trying to move
or dump stored air into your hands.

This site does not track whether you finished. If your team exported these
tickets into its own GitHub, close this issue there once a mentor accepts the
criteria below.

## Prerequisites

- None. This is the first lesson for every electrical team member.
- Access to a shop battery, a robot or spare control board, and a mentor who
  can watch a safe-state demonstration.

## What you'll learn

- Why an FRC battery is always live, and how to carry, cover, charge, and
  store it so the terminals cannot short.
- What a short circuit actually is, and how the 120 A main breaker, branch
  breakers, and fuses are supposed to lose so the wire does not.
- The four-step **safe state** you will use before every later ticket:
  battery disconnected, pressure vented, robot on blocks, announce before
  power comes back.

## Tasks

1. **Read the physics of the pack.** Open
   [WPILib: Robot Battery Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/robot-battery.html)
   and read through the warnings about a battery that is always on. Write
   three sentences in a scratch note you will keep (you will reuse it when
   you label a board in the next ticket): *A short circuit is …*, *A wrench
   across both terminals is dangerous because …*, and *A breaker is sized
   to protect …*.

2. **Watch how a breaker saves the wire.** Watch
   [Circuit Breaker Basics — how do they work?](https://www.youtube.com/watch?v=VGj32euYZ2c)
   (The Engineering Mindset, about 8 minutes). Then skim the current
   [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
   power-distribution section (R6xx in recent manuals; the
   [2026 Game Manual PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
   is the current season's copy).
   Find the rules that set the 120 A main breaker, the 6 AWG (or larger)
   main leads, and the 10 A protection on the roboRIO. Write the rule
   numbers on the same scratch note. If a mentor, a vendor page, or this
   ticket ever disagrees with those rules, the manual wins.

3. **Handle a real battery.** With a mentor present, pick up a shop
   battery by the **strap**, not the wires. Confirm the Anderson SB50
   (or equivalent SB) housing fully covers both contacts. Inspect the
   case: cracked plastic, a bulging side, or leaking acid means the pack
   is retired — tell a mentor, do not put it on a robot. Put the battery
   back on the charging shelf the way your shop stores them (terminals
   covered, vents unobstructed). WPILib's battery page and game-manual
   charging rules (connector type, charge rate) are the references if
   your shop procedure is fuzzy.

4. **Learn the safe state.** Before anyone works on robot wiring, the
   robot is put in a known safe state:

   - **Disconnect the battery** at the Anderson connector. Flipping the
     120 A main breaker is not enough — a breaker can be bumped back on,
     and some work still wants the pack physically off the robot.
   - **Vent any stored pneumatic pressure** with the pressure vent plug.
     You will name that part in
     [Pneumatics 1](../pneumatics-identification/); you only need to
     find it and open it here. Listen until the hiss stops. Gauges
     should fall to zero.
   - **Put the robot on blocks** so the wheels cannot drive the chassis
     across the floor if someone enables it later.
   - **Announce** to everyone nearby before you reconnect power or ask
     a programmer to enable.

   Walk a robot or spare board through those four steps once with a
   mentor talking, then once with you talking.

5. **Demonstrate, unprompted.** Put the same robot into a fully safe
   state without the mentor cueing the next step. State the shop's
   eye-protection and PPE rules out loud (glasses in the shop, no
   dangling jewelry around rotating tools, know where the fire
   extinguisher is). If your shop has a written electrical sign-off
   sheet, this is the demonstration that goes on it.

6. **Hand the evidence to a mentor.** Show the scratch note from Tasks
   1–2 and repeat the safe-state demo if they missed it. If your team
   exported these tickets, paste a one-line note ("safe-state demo
   signed by …") on this issue and move it to In Review.

## Acceptance Criteria

- [ ] You can explain, in your own words, why the battery is always live
      and why a wrench across both terminals melts.
- [ ] You carried a battery by the strap, confirmed the terminals were
      covered, and identified at least one retired-pack symptom (crack,
      bulge, or leak).
- [ ] You stated which device the 120 A main breaker, a 40 A branch
      breaker, and a 10 A roboRIO fuse each protect, and you named the
      game-manual rules that size them. You said out loud that the
      manual wins over this ticket.
- [ ] A mentor watched you put a robot into a fully safe state without
      prompting: battery disconnected at the Anderson, pneumatics
      vented, robot on blocks, and a verbal announce-before-power habit.
- [ ] You stated the shop's eye-protection and PPE rules.

## Resources

- [WPILib: Robot Battery Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/robot-battery.html)
- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
  — read the polarity-check warnings; do not wire anything yet
- [WPILib: Hardware Component Overview](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-hardware.html)
- [FRC Competition Manual (resource library)](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
- [2026 Game Manual PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
  — Power Distribution (section 8.6) and Pneumatic System (section 8.8)
- [Circuit Breaker Basics (YouTube, The Engineering Mindset)](https://www.youtube.com/watch?v=VGj32euYZ2c)

## Notes

- Cover terminals whenever the battery is not on a robot. Work on one
  polarity at a time. Keep SB contacts fully seated in the housing —
  a half-inserted contact is a bare conductor waiting for a tool.
- Batteries are about 12 lb (5.4 kg). Carry by the strap. The leads are
  not a handle; yanking them loosens lugs and is how pits get a surprise
  short later.
- The main breaker is both protection *and* the robot's on/off switch.
  It is not a substitute for unplugging the pack when you have your
  hands in the wiring.
- The next ticket ([The FRC Control System](../control-system/)) is
  identification: you will point at every core device on a real robot
  or spare board and trace power and signal. You do that on a robot
  that is already in the safe state you just demonstrated.
