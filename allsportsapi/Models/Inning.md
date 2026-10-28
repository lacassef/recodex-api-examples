# Inning (Cricket)

An **Inning** captures one innings of a cricket match: the batting and bowling line‑ups,
the running score and wickets, overs bowled, all the extras (byes, leg‑byes, wides,
no‑balls, penalties) and the batting partnerships. Limited‑overs matches have two
innings; multi‑day formats can have up to four.

**Where you'll see it:** cricket match‑detail / scorecard endpoints.

**Related models:** [Batsman](Batsman.md) · [Team](Team.md) · [Player](Player.md) ·
[Event](Event.md).

## Properties

- **battingLine** (`array of Batsman`):
    - A list of batsmen who are part of the batting lineup for the inning.

- **battingTeam** (`Team`):
    - The team that is batting during this inning.

- **bowlingLine** (`array of Bowler`):
    - A list of bowlers who are part of the bowling lineup for the inning.

- **bowlingTeam** (`Team`):
    - The team that is bowling during this inning.

- **bye** (`number`):
    - The total number of bye runs (runs scored without the batsman hitting the ball) accrued during this inning.

- **currentBatsman** (`Player`):
    - The batsman currently at the crease.

- **currentBowler** (`Player`):
    - The bowler currently delivering overs.

- **extra** (`number`):
    - The total number of extra runs given during this inning, which includes wides, no balls, byes, and leg byes.

- **id** (`number`):
    - A unique identifier for this specific inning within a match.

- **isInningDeclare** (`number`):
    - Indicates whether the inning was declared, typically in longer formats of the game where a team might declare their inning to strategically advance the game.

- **legBye** (`number`):
    - The total number of leg bye runs (runs scored when the ball hits the batsman's body but not the bat) accrued during this inning.

- **noBall** (`number`):
    - The total number of no balls (illegal deliveries) bowled during this inning.

- **number** (`number`):
    - The sequential number of the inning within the match.

- **overs** (`number`):
    - The total number of overs bowled during this inning.

- **partnerships** (`array of Partnership`):
    - A list of batting partnerships during the inning.

- **penalty** (`number`):
    - The total number of penalty runs awarded during the inning, which are typically added due to breaches of conduct or rules by the opposing team.

- **score** (`number`):
    - The total number of runs scored by the batting team during this inning.

- **superOver** (`number`):
    - Indicates whether this inning includes a super over, used in certain formats of the game to decide the match in the event of a tie.

- **wickets** (`number`):
    - The total number of wickets lost by the batting team during this inning.

- **wide** (`number`):
    - The total number of wide balls (illegal deliveries too wide or high to be hit) bowled during this inning.