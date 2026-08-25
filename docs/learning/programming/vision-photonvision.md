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

## Description

Vision is how the robot sees field elements and AprilTags so it
can aim, align, and localize. On this curriculum that usually
means **PhotonVision** on a coprocessor (Raspberry Pi, Orange
Pi, or similar) plus cameras (Arducam, OV9281, a Limelight
running its own stack). The programming lead owns whether those
boxes boot, have unique IPs, and publish a pipeline the roboRIO
can trust — not whether a freshman "might look at vision later."

You just practiced reading other teams' architecture in
[Researching Robot Code](../researching-robot-code/). This
ticket is a hardware-and-config lab that those repos assume
already works. The last ticket,
[Code Review & Build-Season Leadership](../code-review-leadership/),
is people and process; a camera with a duplicate IP will waste
more of that process than a sloppy PR comment.

The easy mistakes are almost all **order and network**: two
coprocessors on `10.TE.AM.11`, importing settings before you
isolate the device, flashing a bad microSD and blaming
PhotonVision, putting the camera in a bumper hole that sees
only carpet. Wiring and imaging are lead work because they
fail silently until Thursday.

You will read the official PhotonVision docs, flash or walk
through flashing an image, and either configure a pipeline on
real hardware or write a complete procedure as if you did —
a mentor decides which, based on whether cameras are on the
shelf. Preserve the copy-settings sequence below; it is the
part teams get wrong. Notes go in `frc-learning/vision/`.
This site does not track SD cards.

## Prerequisites

- [FRC Hardware & Firmware](../frc-hardware/) — you know the
  robot network exists and the radio is not "the internet."
- [Code a Robot](../code-a-robot/) — you have deployed *some*
  robot code. PhotonLib on a robot you have never enabled is
  extra chaos.
- [Researching Robot Code](../researching-robot-code/)
  recommended so you have seen how another team named cameras
  and subscribed to targets.
- A mentor, a coprocessor, a camera, and a spare microSD if
  the team is actually imaging. Ethernet to a switch, not a
  prayer.

## What you'll learn

- How multiple cameras get data and power through a switch,
  and why static IPs must be unique.
- How to flash a PhotonVision image and what to do when the
  card is the problem.
- How to create a pipeline from scratch, and how to **copy**
  settings between cameras without an IP fight.

## Coprocessor networking

When a robot needs more than one camera, route them through a
network switch so each coprocessor gets **data** on the robot
LAN and **power** (PoE or a dedicated 5 V / 12 V feed — follow
the hardware you have). Plan a labeled path from each camera
to the switch. Assign each coprocessor a **distinct static
IP**. Two devices that share an IP will make the config UI
lie to you: you will save settings to the wrong box, or to
neither.

Read
[PhotonVision: Networking](https://docs.photonvision.org/en/latest/docs/quick-start/networking.html)
before you plug in the second Pi. WPILib's vision overview is
[Vision Processing](https://docs.wpilib.org/en/stable/docs/software/vision-processing/index.html)
if you need the roboRIO-side picture.

Typical FRC robot IPs live under `10.TE.AM.xx` (team 1234 →
`10.12.34.xx`). The roboRIO is usually `.2`. Cameras and Pis
need unused addresses the radio's DHCP will not stomp. Write
the map down in `vision/ip-map.md` *before* you image the
third device.

## Imaging a coprocessor

Download a PhotonVision image that **matches the coprocessor**
from
[PhotonVision releases](https://github.com/PhotonVision/photonvision/releases).
The wrong board image will boot into nothing useful.

Flash the image following the
[Quick Installation Guide](https://docs.photonvision.org/en/latest/docs/quick-start/quick-install.html)
(Raspberry Pi Imager for Pi / Orange Pi images).
[BalenaEtcher](https://etcher.balena.io/) still works on a
`.img` / `.img.xz` if that is what you have.

If a flash fails or the card will not mount, try a **different
microSD card**. Cards fail often. Do not re-download the image
four times before you swap the card.

After first boot, complete networking so you can reach the
web UI. Official quick start:
[PhotonVision documentation](https://docs.photonvision.org/en/latest/).

## Configuring a pipeline

AprilTag localization versus a colored-object pipeline are
different jobs. Start with the docs for what you actually
need:

- [AprilTag introduction](https://docs.photonvision.org/en/latest/docs/apriltag/apriltag-intro.html)
- [PhotonLib vendordep](https://docs.photonvision.org/en/latest/docs/programming/photonlib/adding-vendordep.html)
  — how robot code subscribes, once the UI works

### New camera, from scratch

Follow the networking guide, open the UI at the device's IP
(or the default the docs list for a fresh image), name the
camera after the **direction it faces** (`front`, `elevator`,
not `Camera1`), and create the pipeline there. Save. Power-
cycle once and confirm the UI still comes up at the static
IP you intended.

### Copying an existing camera's settings (order matters)

A misordered import is the most common reason a camera "will
not take" a configuration. Do it in this order:

1. Open the camera you want to copy **from** and **export
   all settings**.
2. Unplug every coprocessor from the switch **except** the
   one you are configuring (so there is no IP conflict).
3. Browse to the new camera (a brand-new device is reachable
   at its default address; an existing one at its assigned
   IP) and **import all settings**.
4. Rename the camera to the direction it faces, set its
   static IP, and set its name.
5. Reconnect the coprocessors you unplugged.
6. Set the static IP for the coprocessor (if that is a
   separate step from the camera name) and confirm the
   roboRIO's static IP is still what you think it is.
7. Power-cycle the robot, then reach the camera's config
   page at its **new** IP to verify. Imported settings can
   overwrite IPs — always re-check.

Write a checklist in `vision/copy-settings.md` that is this
sequence in your own words, with the IPs you actually used
(or the IPs you *would* use, if this was a dry run).

## Tasks

1. **Read the official docs.** Read PhotonVision
   [home / quick start](https://docs.photonvision.org/en/latest/),
   [networking](https://docs.photonvision.org/en/latest/docs/quick-start/networking.html),
   [Quick Installation Guide](https://docs.photonvision.org/en/latest/docs/quick-start/quick-install.html),
   and the
   [AprilTag intro](https://docs.photonvision.org/en/latest/docs/apriltag/apriltag-intro.html).
   Skim
   [PhotonLib vendordep](https://docs.photonvision.org/en/latest/docs/programming/photonlib/adding-vendordep.html)
   so you know what robot code needs later. In
   `vision/README.md`, write the difference between a
   coprocessor pipeline and PhotonLib on the roboRIO.

2. **Draw the network.** In `vision/ip-map.md`, list every
   vision device the team has or wants: hostname, MAC if you
   have it, static IP, switch port or PoE injector, facing
   direction. Include the roboRIO and the radio. If a device
   does not exist yet, put `TBD` and the IP you reserve.

3. **Image or watch an image.** Download the correct
   PhotonVision release asset. Flash a card with Raspberry Pi
   Imager or BalenaEtcher as the quick-install page specifies.
   Boot the coprocessor.
   Reach the UI. Screenshot the version page into
   `vision/screenshots/`. If hardware is unavailable, write
   `vision/imaging-dry-run.md` with the exact release URL you
   would download, the board name, and the flash steps — a
   mentor must agree this counts.

4. **Configure a pipeline.** On hardware: create a pipeline
   (AprilTag if you have tags in the shop, or a reflective /
   colored pipeline if that is what you have). Name the
   camera by direction. Save, power-cycle, reopen at the
   static IP. Screenshot the pipeline page. In software
   notes, write the pipeline index you would put in PhotonLib.

5. **Practice the copy sequence.** If you have a second
   device, copy settings using the ordered steps above. If
   you have only one, walk a mentor through the sequence
   using `vision/copy-settings.md` and have them initial the
   file. Do not skip step 2 (isolate the target device).

6. **Robot-code pointer.** Add three sentences on how you
   would add the PhotonVision vendordep and subscribe to
   `PhotonCamera` / AprilTag pose — cite the PhotonLib page.
   You do not have to merge vision into competition `main`
   for this ticket.

7. **Open a pull request** with `vision/` and the screenshots.
   Demonstrate the UI (or the dry-run packet) to a mentor.

## Acceptance Criteria

- [ ] `vision/README.md` explains pipeline (coprocessor) versus
      PhotonLib (roboRIO).
- [ ] `vision/ip-map.md` lists intended IPs for every vision
      device plus roboRIO/radio, with no duplicates.
- [ ] You flashed a PhotonVision image and opened the UI, **or**
      a mentor signed a dry-run doc that names the exact
      release and board.
- [ ] A pipeline exists (screenshot) or the dry-run names
      which pipeline type you would create first and why.
- [ ] `vision/copy-settings.md` is the seven-step copy
      sequence in your own words, with IPs. A mentor agrees
      you would isolate devices before import.
- [ ] Notes cite the PhotonLib vendordep page for how code
      would subscribe.
- [ ] A pull request is open or was merged after review.

## Resources

- [PhotonVision documentation](https://docs.photonvision.org/en/latest/)
- [PhotonVision: networking](https://docs.photonvision.org/en/latest/docs/quick-start/networking.html)
- [PhotonVision: Quick Installation Guide](https://docs.photonvision.org/en/latest/docs/quick-start/quick-install.html)
- [PhotonVision: AprilTag intro](https://docs.photonvision.org/en/latest/docs/apriltag/apriltag-intro.html)
- [PhotonVision: adding the vendordep](https://docs.photonvision.org/en/latest/docs/programming/photonlib/adding-vendordep.html)
- [PhotonVision releases](https://github.com/PhotonVision/photonvision/releases)
- [BalenaEtcher](https://etcher.balena.io/)
- [WPILib: Vision processing](https://docs.wpilib.org/en/stable/docs/software/vision-processing/index.html)
- [Limelight docs](https://docs.limelightvision.io/) — if the
  team also runs Limelights; do not mix their IP plan with
  PhotonVision's by accident

## Notes

- Step **order** matters when copying settings. A misordered
  import is the usual reason a camera will not take a
  configuration.
- Always confirm static IPs after imaging and after import.
  Imported settings overwrite them.
- A camera that sees the ceiling will produce confident,
  useless tags. Mounting is a programming-lead problem when
  the score depends on it.
- Next, and last: [Code Review & Build-Season Leadership](../code-review-leadership/).
  Vision that only you can reboot is not leadership.
