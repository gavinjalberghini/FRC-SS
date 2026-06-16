---
layout: lesson
title: Vision & PhotonVision
subtitle: Image coprocessors, wire cameras, and configure vision pipelines.
permalink: /learning/programming/vision-photonvision/
role: lead
order: 16
size: 2
time: "1–2 hrs"
---

## Overview

Vision lets the robot see field elements and AprilTags to aim, align, and
localize. We use **PhotonVision** running on coprocessors (such as a Raspberry Pi)
with cameras like Arducams and Limelights. This lesson covers wiring, imaging a
coprocessor, and configuring pipelines — including how to copy settings between
cameras.

## Prerequisites

- [FRC Hardware & Firmware](../frc-hardware/) and [Code a Robot](../code-a-robot/).

## What you'll learn

- How to wire multiple cameras/coprocessors through a network switch.
- How to flash a PhotonVision image onto a coprocessor.
- How to set up a pipeline and reuse settings across cameras.

## Coprocessor networking

When a robot needs multiple cameras, route them through a network switch so each
coprocessor gets both **data** (to the robot network) and **power**. Plan your
wiring so every camera has a clear, labeled path back to the switch, and assign
each coprocessor a distinct static IP (multiple devices sharing an IP will confuse
the configuration tools).

## Imaging a coprocessor

- [ ] Download the PhotonVision image that matches your coprocessor from the
      [PhotonVision releases](https://github.com/PhotonVision/photonvision/releases).
- [ ] Flash the image to a microSD card with [BalenaEtcher](https://etcher.balena.io/).
- [ ] If a flash fails or the card won't mount, try a different microSD card —
      cards fail surprisingly often.

## Configuring a pipeline

- [ ] **New camera, from scratch:** follow the [PhotonVision networking guide](https://docs.photonvision.org/en/latest/docs/quick-start/networking.html)
      and create the pipeline directly.
- [ ] **Copying an existing camera's settings** (order matters):
  1. Open the camera you want to copy *from* and **export all settings**.
  2. Unplug every coprocessor from the switch *except* the one you're configuring
     (so there's no IP conflict).
  3. Browse to the new camera (a brand-new device is reachable at its default
     address; an existing one at its assigned IP) and **import all settings**.
  4. Rename the camera to the direction it faces, set its static IP, and set its
     name.
  5. Reconnect the coprocessors you unplugged.
  6. Set the static IP for the coprocessor and confirm the roboRIO's static IP.
  7. Power-cycle the robot, then reach the camera's config page at its IP to verify.

## Resources

- [PhotonVision documentation](https://docs.photonvision.org/en/latest/)
- [PhotonVision: networking](https://docs.photonvision.org/en/latest/docs/quick-start/networking.html)
- [BalenaEtcher](https://etcher.balena.io/)
- [WPILib: AprilTag & vision](https://docs.wpilib.org/en/stable/docs/software/vision-processing/index.html)

## Notes

- Step **order** matters when copying settings — a misordered import is the most
  common reason a camera "won't take" a configuration.
- Always confirm static IPs after imaging; imported settings can overwrite them.
