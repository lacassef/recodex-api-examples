# Batsman (Cricket)

A **Batsman** is one batting line in a cricket [Inning](Inning.md): the runs scored,
balls faced, boundaries (`s4`) and sixes (`s6`), and — if dismissed — how the wicket
fell (`wicketTypeName`, the bowler and/or fielder involved) and the fall‑of‑wicket
context (`fowOver`, `fowScore`).

**Where you'll see it:** the `battingLine` of an [Inning](Inning.md).

**Related models:** [Inning](Inning.md) · [Player](Player.md).

## Properties

- **balls** (`number`):
    - The number of balls faced by the batsman during their innings.

- **fowOver** (`number`):
    - The over number during which the batsman was dismissed, part of the "Fall of Wicket" (FOW) statistics.

- **fowScore** (`number`):
    - The total score at the time of the batsman's dismissal, also part of the "Fall of Wicket" statistics.

- **player** (`Player`):
    - The player who is the batsman.

- **playerName** (`string`):
    - The name of the player, providing a textual identifier for the batsman.

- **s4** (`number`):
    - The number of boundaries (four runs) hit by the batsman.

- **s6** (`number`):
    - The number of sixes (six runs) hit by the batsman.

- **score** (`number`):
    - The total number of runs scored by the batsman.

- **wicketBowler** (`Player`):
    - The bowler responsible for the dismissal of the batsman, if the wicket was taken by a bowler.

- **wicketBowlerName** (`string`):
    - The name of the bowler who took the batsman's wicket, providing a textual identifier for the bowler.

- **wicketCatch** (`Player`):
    - The fielder who caught the ball if the batsman was dismissed by a catch.

- **wicketCatchName** (`string`):
    - The name of the fielder who caught the batsman out, providing a textual identifier for the fielder.

- **wicketTypeId** (`number`):
    - An identifier for the type of dismissal (e.g., caught, bowled, run out). This helps in categorizing the manner of the wicket.

- **wicketTypeName** (`string`):
    - A descriptive name of the type of wicket, providing details about how the batsman was dismissed (e.g., "Caught", "Bowled").