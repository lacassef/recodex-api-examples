# Athlete

An **Athlete** is one person.

**Where you'll see it:** athlete details, top athletes, athlete games, and the athletes list on [Search](Search.md).

**Related models:** [Career](Career.md), [Competitor](Competitor.md), [Competition](Competition.md).

Details, games, career, and trophy stats call the id `athleteId`. Next game, chart events, news, and outrights call a list `athletes`. On details, `athleteId` is one id or several separated by commas. `817` and `45579` are the ids in the [examples](../guides/examples.md).

Without `fullDetails`, details name age, position, club, and nationality. `fullDetails=true` adds jersey, contract, injury, `shortBio`, `highlightStats`, `lastMatches`, transfers, trophies, and `careerStats`. The top list names `clubId` and `imageVersion` instead of `club`.

`nextGame` is the object on athlete-next-game when a game is scheduled. The description names start time, status, competition, venue, and the home and away competitors on that object. This page does not turn those words into keys.

`chartEvents` is the plotted-events object. The description names zones, penalty totals, and events with pitch position. This page does not name keys inside that object.

### Example (details, without fullDetails)

Values other than the request id are not shown. `817` is the athlete id you send. The response field that carries it is `id` on a list. Details do not rename it.

```json
{
  "id": 817
}
```

## Properties

- **id** (`number`):
    - Athlete id on a list or on search.

- **age** (`value`):
    - Age on details and on the top list.

- **position** (`value`):
    - Position on details and on the top list.

- **club** (`value`):
    - Club on details when `fullDetails` is omitted.

- **clubId** (`number`):
    - Club id on the top list.

- **nationality** (`value`):
    - Nationality on details and on the top list.

- **imageVersion** (`number`):
    - Version on the top list. `48583` with version `3` is the athlete image in the examples.

- **jersey** (`value`):
    - Added when `fullDetails=true`.

- **contract** (`value`):
    - Added when `fullDetails=true`.

- **injury** (`value`):
    - Added when `fullDetails=true`.

- **shortBio** (`string`):
    - Added when `fullDetails=true`.

- **highlightStats** (`value`):
    - Added when `fullDetails=true`.

- **lastMatches** (`array`):
    - Added when `fullDetails=true`.

- **transfers** (`array`):
    - Added when `fullDetails=true`.

- **trophies** (`array`):
    - Added when `fullDetails=true`.

- **careerStats** (`value`):
    - Added when `fullDetails=true`.

- **nextGame** (`object`):
    - The next scheduled game on athlete-next-game.

- **chartEvents** (`object`):
    - Plotted shots and goals on athlete chart events.

- **played** (`value`):
    - On one entry of athlete games.

- **hasStats** (`boolean`):
    - That entry has stats.

- **athleteStats** (`value`):
    - Stats on that entry.

- **relatedCompetitor** (`object`):
    - The competitor that entry is tied to.
