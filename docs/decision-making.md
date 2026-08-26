---
layout: page
title: Decision-Making Guide
eyebrow: How we decide
subtitle: From the whole-robot call down to the bracket on the bench — and what jumps the line.
permalink: /decision-making/
---

This guide is the **authoritative reference** for how robot design and build
decisions get made on the team. The principle is simple: decisions are made as
close to the work as possible, and only escalate when they need to. Once a
decision is made through this process, **everyone is expected to respect it** —
see the [Team Contract]({{ '/contract/' | relative_url }}). Who sits in the
chairs is in [How We Staff Leadership]({{ '/staffing-leadership/' | relative_url }}).
What each tier owns day to day is on the
[Org Chart]({{ '/org-chart/' | relative_url }}).

## The cascade

A season is a stack of decisions, not one meeting.

1. **Robot-level** calls set the machine and the season priorities.
2. Those calls become **module constraints** — envelopes, motor counts, interfaces.
3. **Veterans** decide how to implement inside the task they were given.
4. A few things are **out of band**. They skip the stack and use a special
   process.

If you do not know which layer you are in, you are probably about to make
someone else's decision. Stop and ask.

| Kind of call | Who decides | What it looks like |
| --- | --- | --- |
| **Robot-level** | Student leads vote; adults have final say | Drivetrain type, scoring strategy, which mechanisms exist |
| **Module constraint** | Leads shape it from the robot-level call | Height, weight share, motor budget, how two subsystems meet |
| **Inside the task** | The Veteran who owns the task | Bracket layout, print orientation, cable path, command structure |
| **Out of band** | Special process — often adults first | Safety, money, locked priorities, one-way cuts, people, inspection |

## Robot-level decisions

These are the calls that define the robot and the season. They are
**one-way enough** that the leadership table has to make them, and adults
have to live with them.

Examples:

- Swerve or a tank-style drive.
- One scoring mechanism or two. Climb or no climb.
- Where the weight and motor budget go — elevator vs intake vs shooter.
- Practice robot or a parts-in-a-box spare.
- Must / should / won't feature list after kickoff.

These go through the **formal process** below. A Veteran does not change
them at the bench because a cooler idea showed up on Thursday.

## Module constraints — the handshake

Once the robot-level call is made, it **flows down**. Leads turn it into
constraints the people doing the work can actually use. That is work-shaping:
size the task, name the interface, leave the implementation to the Veteran.

Examples of a handshake, not a new robot decision:

- The elevator may go to *this* height and weigh *this* much, because the
  robot envelope and the drivetrain already spent their share.
- The intake must present a game piece at *this* pose, because that is what
  the chosen shooter eats.
- Electrical gets *n* motor channels and *this* bump-stop on current, because
  the PDH and the brownout margin are already spoken for.
- Software gets one coprocessor and a cycle-time target, because the auto
  plan assumed that.

Leads write these down. Veterans work inside them. If a constraint is wrong
or impossible, that is an escalation — not a quiet rewrite at the mill.

## Inside the task — Veterans decide

If the decision **lives inside the task you were given**, you make it.
Veterans are the workhorse. Relative autonomy is the point.

Examples that should *not* become a leadership meeting:

- Bolt pattern and gusset shape, as long as the tube stays in the CAD
  envelope and the load path still makes sense.
- Print orientation, infill, and which Bambu is running tonight.
- How this cable run gets from the PDH to that motor, given the run plan.
- Command structure and naming for a subsystem you own, given the repo
  conventions.
- Which length of hex shaft to order, if it fits the locked design.
- Wording on a scout-sheet question you were asked to draft.

Document what you decided and why. Flag anything that **touches another
person's task** before it becomes their surprise. If you are about to blow
a constraint — weight, interface, motor count, schedule — that is no longer
inside the task. Take it to your Lead.

People on the core path do not own these calls yet. They propose, they
shadow, they do not unilaterally change the part.

## Out of band — special process

Some calls are not "inside the task" and not "the next leadership standup."
They jump the line.

| Out-of-band trigger | What you do | Who owns the call |
| --- | --- | --- |
| **Safety** — unsafe act, injury, missing PPE, a tool you were not signed off on | Stop the work. Find a mentor. | Adults. Not a vote. |
| **Unbudgeted money** — a part, a trip, a tool that is not in the plan | Do not buy it. Take it to a Lead and a mentor. | Adults, with the business Lead in the room |
| **Locked priority** — changing a must/should/won't after it was set | Do not start the new thing. Formal process. | Leads vote; adults final say |
| **One-way door** — cutting a unique tube, deleting a mechanism, sending the Impact essay | Pause. Name the door. Formal process if it cannot be undone cheaply. | Leads + adults |
| **Breaks another trade's constraint** — your "small" change starves their motor, their height, their time | Stop. Both Leads, same conversation. | The two Leads; escalate if they disagree |
| **Inspection / rules risk** — bumpers, weight, pneumatics, a mechanism that might be illegal | Do not ship hope. Mentor + relevant Lead. | Adults on legality; Leads on the design response |
| **People** — eligibility, pulling a chair, conflict that is not about a part | Not a shop-floor vote. | Adults, using the [Team Contract]({{ '/contract/' | relative_url }}) |
| **Event strategy that is not the pick list** — last-minute alliance or a play that dumps the scout sheet | Name that you are off-book. | Drive/strategy Leads + mentors, before the alliance captain walks to the station |

Out of band is not "ask everyone." It is "use the *right* process instead of
the convenient one."

## Four walks through the stack

**Kickoff, Saturday.** The room wants swerve because it is swerve. That is a
robot-level call: drivetrain type, motor budget, weight, and what every
other module will sit on. Leads convene, argue from the game, vote. Adults
have final say. The elevator Lead does not get a private swerve veto on
Sunday because CAD is hard.

**Week 3, the mill.** A Veteran is building the elevator and wants a fourth
stage. It would make the intake handshake easier. It also blows the weight
share the robot-level call already spent. That is **not** inside the task.
The Veteran takes it to the Lead. If the Lead thinks the robot-level
priority should move, it goes formal. If not, the fourth stage does not
get cut.

**Thursday night, a motor dies.** Replacing it with the same part is inside
the task. Changing the gearbox so the cycle time no longer matches the auto
plan is a constraint break — software and strategy are now in the room.
Both Leads, same night. Do not "just try it on the practice robot" and
forget to tell anyone.

**District event, alliance selection.** The pick list is a robot-level
strategy artifact. Crossing it off-book because a friend asked is out of
band. The strategy Lead and a mentor name the deviation *before* someone
walks to the station. After the handshake, the team lives with it.

**Anytime, the grinder.** No glasses. This is not a design debate. Work
stops. A mentor handles it. There is no Student Leadership Team agenda
item for PPE.

## Making a formal decision

When a decision is robot-level, contested, locked-priority, or cannot be
resolved at the layers above, it goes through this process, in order:

1. **The student leads convene and vote.** The
   [Student Leadership Team]({{ '/org-chart/' | relative_url }}) — the Leads,
   who serve as co-captains — discusses the options and votes.
2. **The adults have the final say.** The team is student-driven, but mentors
   hold final authority. The leads' vote informs that call; it does not
   override it.
3. **The head teacher breaks a tie.** If the adults cannot reach agreement,
   the **head teacher** makes the final decision.

Safety, eligibility, and unbudgeted money do **not** wait for a lead vote.
Those start with adults.

<div class="callout">
  <div class="callout-icon">🗳️</div>
  <p><strong>In short:</strong> robot-level calls set the machine → leads turn them into module constraints → Veterans decide inside the task → anything that is safety, money, a locked priority, a one-way door, or a people issue jumps to a special process. Formal votes: student leads, then adults, then the head teacher on an adult tie.</p>
</div>

## Respecting the outcome

- It is the **responsibility of every member** — student and mentor alike —
  to respect and support decisions made through this process, **even when they
  argued for something else**.
- Raise concerns through your Lead *before* a decision is made. Once it is
  made, get behind it so the team can move.
- Re-opening a call because you lost the argument is not a new fact. A new
  fact (it does not fit, it is illegal, it is unsafe, the part does not exist)
  is an escalation.
- This expectation is part of the [Team Contract]({{ '/contract/' | relative_url }}).
