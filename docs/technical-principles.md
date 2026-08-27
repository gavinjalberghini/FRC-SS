---
layout: page
title: Technical Principles
eyebrow: How each trade works
subtitle: Declarative takes for Programming, Mechanical, and Electrical — the rules we choose on purpose.
permalink: /technical-principles/
---

These are **principles**, not tickets. A ticket teaches a skill. A principle
is a choice this team already made, so a Veteran does not have to re-argue
it at the bench every Thursday. They sit next to
[how we staff chairs]({{ '/staffing-leadership/' | relative_url }}) and
[how we decide]({{ '/decision-making/' | relative_url }}). The
[Learning Hub]({{ '/learning/' | relative_url }}) is where you practice the
craft that makes them real.

We start with three trades. CAD, printing, strategy, drive, and business
will get the same treatment when we have takes worth writing down.

If a principle and a one-off idea fight, the principle wins unless it goes
through the formal decision process. That is the point.

## Programming (Software)

This trade is **Software** on the [org chart]({{ '/org-chart/' | relative_url }}).
The Learning Hub track is [Programming]({{ '/learning/programming/' | relative_url }}).

### We use Git. That is not optional.

Git is how this team shares code. It is the industry standard for a reason:
more than one person can work on the same robot without overwriting each
other, and we can see *what* changed, *when*, and *why*. USB sticks,
"final_final_v3", and a laptop that only one senior can unlock are not a
version-control strategy.

What that looks like:

- The robot repo lives on GitHub. If it is not in Git, it is not on the
  robot.
- Every programmer can clone, branch, commit, and open a pull request.
  That is the [Git]({{ '/learning/programming/git/' | relative_url }}) and
  [GitHub]({{ '/learning/programming/github/' | relative_url }}) tickets,
  not a senior-only ritual.
- "I will merge it later" is how event-day mystery bugs are born.

### We freeze the codebase for events.

We take explicit steps to keep software from becoming the failure mode at
a competition. **Major feature work stops before we leave for an event.**
For the duration of that event we do not rewrite the architecture, land a
new subsystem, or "just try a different auto framework."

What we *will* do at an event: tune a constant, disable a broken command,
revert a known-good release, fix a crash that appeared on the field. What
we will not do: invent a climber in the hotel Friday night.

Why:

- Driver practice is a test of *this* code, not of the code you wish you
  had written.
- A mid-event rewrite burns the one thing you cannot buy back: trust that
  the robot will do tomorrow what it did today.
- This is a [one-way door]({{ '/decision-making/' | relative_url }}) dressed
  up as a late-night favor. It goes through the Lead and a mentor, or it
  does not happen.

Tag a **release** before you bag the robot. That tag is the thing you
revert to when Thursday's "tiny fix" is not tiny.

### We lean into Git the way a shop leans into a mill — with a process.

Pull requests, branches, named releases, and automatic lint/style checks
are not bureaucracy. They are how a volunteer team gets industry practice
without a full-time release engineer.

What that looks like:

- Work happens on a **branch**. `main` is what we would put on the field
  tonight.
- Changes land through a **pull request**. Someone who did not write the
  code looks at it. "Looks good" on 800 lines is not a review; see
  [Code Review & Build-Season Leadership]({{ '/learning/programming/code-review-leadership/' | relative_url }}).
- **Lint and style** run on the PR, not in a senior's head after merge.
  Format is not taste. It is a constraint, like a motor count.
- **Releases** are named and recoverable. "Whatever was on the stick" is
  not a release.

## Mechanical

The Learning Hub track is [Mechanical]({{ '/learning/mechanical/' | relative_url }}).

### We standardize tools and parts.

A shop with five hex-key standards and three kinds of "almost 1/2-inch
tube" is a shop that loses Thursday nights to a missing bit. We pick a
fastener family, a tube size, a handful of bearing and shaft standards,
and we stay there unless a module constraint forces a one-off.

What that looks like:

- The same hex, the same rivet gun, the same bumper fasteners, labeled
  and put back.
- A parts library a Veteran can shop from without inventing a new
  bolt length.
- Custom is allowed. *Mystery* custom — a one-off that only fits a
  tap nobody else owns — is not.

Standardization is how the next freshman can repair what you built after
you graduate.

### We start with COTS and fall back to custom.

Commercial off-the-shelf first. Wheels, gearboxes, elevator blocks,
intakes that already exist. Custom fabrication is the fallback when COTS
cannot meet the handshake — height, weight, interface — not the default
because machining is fun.

That forces a better question: *can we spend our hours on integration
and driver practice instead of making a part that REV or WCP already
ships?* A custom tube that saves two ounces and costs two weeks is
usually a bad trade. A custom plate that lets two COTS gearboxes share
a shaft can be a good one.

COTS-first is not "we never make anything." It is "we do not make a
thing until we can say why the catalog failed."

### We bring backups for the parts that end a night if they break.

Major mechanisms get a spare, a kit of wear parts, or a documented swap
path *before* the first event. An elevator that only exists once is a
single point of failure with a pit-crew audience.

What that looks like:

- A second intake, or the plates and belts to rebuild one in an hour.
- Spare gearboxes, chains, and the exact fasteners the standard uses.
- A written "if this breaks" card in the pit, not a senior's memory.

If we cannot spare it, we design so we can **repair** it with what is in
the box. That is a module constraint, not a hope.

## Electrical

The Learning Hub track is [Electrical]({{ '/learning/electrical/' | relative_url }}).

### Cable routing, weight, and wire type are decided at the start.

Harnesses that get "figured out at integrate" become rats' nests, extra
pounds on the wrong side of the robot, and a brownout that only happens
in eliminations. Routing, gauge, connector family, and service loops are
**module constraints**, same as motor count. They get a handshake when
the mechanism is still in CAD, not after the elevator is already welded
shut.

What that looks like:

- A run plan: battery → PDH → this motor, this gauge, this path, this
  strain-relief point.
- Weight of copper and connectors in the budget *before* someone asks
  for a fourth stage.
- Service loops and disconnects where a pit repair will actually happen.
- "We'll zip-tie it later" is how you fail a tug test in the queue.

If a mechanical change starves a run or a gauge, that is a
[constraint break]({{ '/decision-making/' | relative_url }}). Both Leads,
same night.

### We have a standard for "this harness will survive the event."

Pretty wiring that fails a tug is not done. We check robustness on
purpose: **tug tests** on every crimp and ferrule, **multimeter**
readings for continuity and polarity before we apply power, and the
other tools the ticket names — insulation, strain relief, labels, no
whiskers. See
[Wiring Craftsmanship]({{ '/learning/electrical/wiring-craftsmanship/' | relative_url }})
and
[WPILib's preemptive troubleshooting](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/preemptive-troubleshooting.html).

What that looks like:

- A Veteran does not "trust the crimp." They tug it. If the ferrule
  slides, it is not a ferrule.
- Polarity and continuity get a meter *before* the SB50 goes on.
- A written pass/fail for the harness — not "it looked fine" — before
  the robot is bagged or loaded.

The standard exists so two people can disagree about a joint without
inventing a new argument. The joint either meets it or it gets redone.

<div class="callout">
  <div class="callout-icon">🔧</div>
  <p><strong>In short:</strong> Programming ships through Git and freezes for events. Mechanical standardizes, starts with COTS, and brings a spare. Electrical decides the harness up front and proves it with a tug and a meter. More trades later.</p>
</div>
