# Event

An **Event** is a single match, game or fixture — the central object of the API.
Almost everything else (lineups, statistics, incidents, odds, votes) is attached to
an event by its `id`. One event references both teams, its tournament and season, a
status, a clock and a score, plus optional sport‑specific blocks (cricket toss,
American‑football yardage, combat‑sports weight class, and so on).

**Where you'll see it:** schedule/live endpoints return arrays of events; match‑detail
endpoints return a single event or objects keyed to its `id`.

**Related models:** [Team](Team.md) · [Player](Player.md) · [Tournament](Tournament.md) ·
[Incidents](Incidents.md) · [EventStatistics](EventStatistics.md). For reading the
match clock and interpreting `status`, see the [FAQ](../FAQ.md).

### Example (trimmed)

```json
{
  "id": 12436870,
  "slug": "atalanta-sturm-graz",
  "startTimestamp": 1727861400,
  "homeTeam": { "id": 2685, "name": "Atalanta", "shortName": "Atalanta" },
  "awayTeam": { "id": 2832, "name": "Sturm Graz", "shortName": "Sturm Graz" },
  "homeScore": { "current": 5, "period1": 2, "period2": 3 },
  "awayScore": { "current": 0, "period1": 0, "period2": 0 },
  "status": { "code": 100, "description": "Ended", "type": "finished" },
  "lastPeriod": "period2",
  "winnerCode": 1,
  "tournament": { "id": 7, "name": "UEFA Champions League" }
}
```

> ℹ️ Sport‑specific fields (e.g. `currentBatsmanId`, `tossDecision`, `yardDistance`,
> `weightClass`, `fightDiscipline`) are populated only for the relevant sport and are
> `null` everywhere else.

## Properties

- **aggregatedWinnerCode** (`number`):
    - Represents the code of the team or player who is the aggregated winner of the event.

- **attendance** (`number`):
    - Indicates the number of people attending the event.

- **awayRedCards** (`number`):
    - Tracks the number of red cards issued to the away team during the event.

- **awayScore** (`Score`):
    - Holds the score of the away team.

- **awayTeam** (`Team`):
    - Represents the away team participating in the event.

- **awayTeamRanking** (`number`):
    - Indicates the ranking of the away team at the time of the event.

- **awayTeamSeasonHistoricalForm** (`TeamSeasonForm`):
    - Stores the historical form of the away team during the season.

- **awayTeamSeed** (`string`):
    - Refers to the seed assigned to the away team in the event.

- **bestOf** (`number`):
    - Represents the "best of" format for the event, such as best of 3, 5, etc.

- **bet365ExcludedCountryCodes** (`array of string`):
    - Contains a list of country codes where bet365 services are excluded for the event.

- **changes** (`EventChanges`):
    - Tracks changes made to the event.

- **childEvents** (`array of number`):
    - Holds the list of child event IDs associated with this event.

- **coverage** (`number`):
    - Indicates the extent of coverage provided for the event.

- **cricketBallProperties** (`array of string`):
    - Stores properties of the cricket ball used in the event, such as color, type, etc.

- **crowdsourcingDataDisplayEnabled** (`boolean`):
    - Flag to indicate if crowdsourcing data display is enabled for the event.

- **crowdsourcingEnabled** (`boolean`):
    - Flag to indicate if crowdsourcing is enabled for the event.

- **cupMatchesInRound** (`number`):
    - Number of cup matches in the current round of the event.

- **currentBatsmanId** (`number`):
    - The ID of the current batsman in a cricket event.

- **currentBattingTeamId** (`number`):
    - The ID of the current batting team in a cricket event.

- **currentBowlerId** (`number`):
    - The ID of the current bowler in a cricket event.

- **currentPeriodStartTimestamp** (`number`):
    - Timestamp representing the start time of the current period in the event.

- **customId** (`string`):
    - A custom identifier for the event.

- **defaultPeriodCount** (`number`):
    - Number of default periods (e.g., halves, quarters) in the event.

- **defaultPeriodLength** (`number`):
    - Length of each default period in the event.

- **deletedAtTimestamp** (`number`):
    - Timestamp indicating when the event was deleted, if applicable.

- **detailId** (`number`):
    - An identifier for additional details related to the event.

- **endTimestamp** (`number`):
    - Timestamp marking the end time of the event.

- **eventEditor** (`EventEditor`):
    - The editor responsible for making changes to the event.

- **eventEditorName** (`string`):
    - Name of the event editor.

- **eventType** (`string`):
    - Describes the type of event, e.g., match, tournament, etc.

- **fanRatingEvent** (`boolean`):
    - Indicates whether fan ratings are enabled for the event.

- **fightDiscipline** (`string`):
    - Specifies the discipline (e.g., boxing, MMA) of the fight in the event.

- **fightState** (`string`):
    - Represents the current state of the fight, such as ongoing, ended, etc.

- **fightType** (`string`):
    - Type of fight in the event, such as a title fight, exhibition, etc.

- **finalResultOnly** (`boolean`):
    - Indicates whether only the final result is considered in the event.

- **finalRound** (`number`):
    - Specifies the final round number in the event.

- **firstToServe** (`number`):
    - Indicates the ID of the team or player who serves first in a match.

- **gameAdvantageTeamId** (`number`):
    - ID of the team that has the advantage in the game.

- **gender** (`string`):
    - Indicates the gender category of the event participants (e.g., male, female, mixed).

- **groundType** (`string`):
    - Describes the type of ground or playing surface for the event.

- **hasBet365LiveStream** (`boolean`):
    - Indicates whether the event is available for live streaming on bet365.

- **hasEventPlayerHeatMap** (`boolean`):
    - Indicates whether a player heat map is available for the event.

- **hasEventPlayerStatistics** (`boolean`):
    - Indicates whether player statistics are available for the event.

- **hasGlobalHighlights** (`boolean`):
    - Indicates whether global highlights are available for the event.

- **hasXg** (`boolean`):
    - Indicates whether Expected Goals (xG) statistics are available for the event.

- **hide** (`boolean`):
    - Flag to indicate whether the event should be hidden.

- **homeRedCards** (`number`):
    - Tracks the number of red cards issued to the home team during the event.

- **homeScore** (`Score`):
    - Holds the score of the home team.

- **homeTeam** (`Team`):
    - Represents the home team participating in the event.

- **homeTeamRanking** (`number`):
    - Indicates the ranking of the home team at the time of the event.

- **homeTeamSeasonHistoricalForm** (`TeamSeasonForm`):
    - Stores the historical form of the home team during the season.

- **homeTeamSeed** (`string`):
    - Refers to the seed assigned to the home team in the event.

- **id** (`number`):
    - The unique identifier for the event.

- **isAwarded** (`boolean`):
    - Indicates whether the event has been awarded a particular status or result.

- **isEditor** (`boolean`):
    - Indicates whether the event is in editor mode.

- **isRecent** (`boolean`):
    - Flag to indicate if the event is recent or upcoming.

- **lastPeriod** (`string`):
    - Represents the last period played in the event.

- **manOfMatch** (`Player`):
    - The player awarded "Man of the Match" in the event.

- **mute** (`boolean`):
    - Flag to mute notifications or alerts for the event.

- **note** (`string`):
    - Additional notes or remarks related to the event.

- **parentEventId** (`number`):
    - ID of the parent event, if this event is a child event.

- **periods** (`object`):
    - Maps period names to their corresponding values or details.

- **previousLegEventId** (`number`):
    - ID of the previous leg of the event, if applicable.

- **referee** (`Referee`):
    - Represents the referee officiating the event.

- **refereeName** (`string`):
    - Name of the referee officiating the event.

- **roundInfo** (`Round`):
    - Information about the round or stage of the event.

- **season** (`Season`):
    - Represents the season in which the event is taking place.

- **seasonStatisticsType** (`string`):
    - Indicates the type of statistics used for the season.

- **showTotoPromo** (`boolean`):
    - Indicates whether a "Toto Promo" should be shown for the event.

- **slug** (`string`):
    - A URL-friendly identifier for the event.

- **startTimestamp** (`number`):
    - Timestamp indicating the start time of the event.

- **status** (`Status`):
    - Current status of the event, such as scheduled, ongoing, completed.

- **statusReason** (`string`):
    - Reason for the current status of the event.

- **time** (`Time`):
    - Represents the time-related details of the event.

- **tossDecision** (`string`):
    - The decision made by the toss-winning team (e.g., bat, bowl) in a cricket event.

- **tossWin** (`string`):
    - The team that won the toss in a cricket event.

- **tournament** (`Tournament`):
    - The tournament to which the event belongs.

- **tvUmpireName** (`string`):
    - Name of the TV umpire in a cricket event.

- **typeList** (`HashSet<EventType>`):
    - Set of event types associated with the event.

- **umpire1Name** (`string`):
    - Name of the first on-field umpire in a cricket event.

- **umpire2Name** (`string`):
    - Name of the second on-field umpire in a cricket event.

- **venue** (`Venue`):
    - Venue where the event is being held.

- **weightClass** (`string`):
    - Weight class of the participants in a combat sports event.

- **winType** (`string`):
    - Describes the type of win (e.g., knockout, points) in the event.

- **winnerCode** (`number`):
    - Code representing the winner of the event.

- **yardDistance** (`AmericanFootballDownDistance`):
    - Represents the yard distance in an American football event related to the down distance.