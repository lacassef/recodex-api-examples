# Team

A **Team** is a club or national side. The model is shared across every sport, so it
carries fields that only apply to some of them — e.g. the salary‑cap fields
(`activeCap`, `capMaximum`, `capSpace`, `luxuryTaxThreshold`, `totalCap`) are mostly
relevant to North‑American leagues, while `subTeam1`/`subTeam2` describe doubles pairs
or affiliated squads. Like `Player`, a team object may be full (team endpoint) or
trimmed (inside an `Event`).

**Where you'll see it:** team endpoints, standings, squads, and as `homeTeam`/`awayTeam`
on every [Event](Event.md).

**Related models:** [Event](Event.md) · [Player](Player.md) · [Subteam](Subteam.md) ·
[Transfer](Transfer.md) · [Category](Category.md). Logos come from the team‑image
endpoint (`image/png`).

### Example (trimmed)

```json
{
  "id": 2685,
  "name": "Atalanta",
  "shortName": "Atalanta",
  "nameCode": "ATA",
  "national": false,
  "teamColors": { "primary": "#0000ff", "secondary": "#000000", "text": "#000000" },
  "country": { "alpha2": "IT", "name": "Italy" },
  "sport": { "id": 1, "name": "Football", "slug": "football" }
}
```

## Properties

- **activeCap** (`number`):
    - Represents the active salary cap for the team, which is the portion of the salary cap currently allocated to active players.

- **capMaximum** (`number`):
    - The maximum salary cap allowed for the team. This is the upper limit of the total salary expenditure that the team can have.

- **capSpace** (`number`):
    - Indicates the remaining salary cap space available to the team, calculated as the difference between the cap maximum and the active cap.

- **category** (`Category`):
    - Represents the category or division the team belongs to, such as a league, conference, or competition level.

- **country** (`Country`):
    - The country where the team is based or registered.

- **disabled** (`boolean`):
    - Flag indicating whether the team is currently disabled or inactive in the system.

- **fieldTranslations** (`FieldTranslations`):
    - Contains translations for various fields related to the team, allowing for internationalization and localization of team-related information.

- **foundationDateTimestamp** (`number`):
    - The timestamp representing the date when the team was founded.

- **fullName** (`string`):
    - The full legal or formal name of the team.

- **gender** (`string`):
    - Indicates the gender category of the team, such as male, female, or mixed.

- **id** (`number`):
    - A unique identifier for the team.

- **isRecent** (`boolean`):
    - A flag indicating whether the team has been recently active or updated.

- **luxuryTaxThreshold** (`number`):
    - Represents the luxury tax threshold for the team. Exceeding this amount may result in additional financial penalties.

- **manager** (`Manager`):
    - Represents the manager or head coach responsible for overseeing the team's operations and performance.

- **name** (`string`):
    - The official name of the team.

- **nameCode** (`string`):
    - A short code or abbreviation representing the team's name, often used in standings, fixtures, or scoreboards.

- **national** (`boolean`):
    - Indicates whether the team is a national team, representing a country rather than a club or regional entity.

- **parentTeam** (`Team`):
    - Refers to the parent team, if this team is a subsidiary or affiliate of another team.

- **playerTeamInfo** (`PlayerTeamInfo`):
    - Contains information about the team's players, such as roster details and player statistics.

- **primaryUniqueTournament** (`UniqueTournament`):
    - The primary tournament or competition in which the team participates.

- **ranking** (`number`):
    - The team's current ranking in its primary competition or league.

- **shortName** (`string`):
    - A shortened version of the team's name, typically used for brevity in UI elements or media.

- **signedPlayers** (`number`):
    - The number of players currently signed to the team.

- **slug** (`string`):
    - A URL-friendly identifier for the team.

- **sport** (`Sport`):
    - The sport that the team competes in, such as football, basketball, or cricket.

- **subTeam1** (`SubTeam`):
    - Represents the first affiliated sub-team, if any. This might be a junior team or a reserve squad.

- **subTeam2** (`SubTeam`):
    - Represents the second affiliated sub-team, if any.

- **teamColors** (`TeamColors`):
    - The official colors of the team.

- **teamRankings** (`array of TeamRankings`):
    - A list of rankings across various competitions or metrics, showing the team's performance relative to others.

- **totalCap** (`number`):
    - Represents the total salary cap, including all players, both active and inactive.

- **tournament** (`Tournament`):
    - Represents the tournament or league in which the team is currently participating.

- **type** (`number`):
    - Indicates the type of team, such as club, national, or regional.

- **userCount** (`number`):
    - The number of users or fans associated with or following the team.

- **venue** (`Venue`):
    - The home venue or stadium where the team plays its games.

- **wdlRecord** (`Record`):
    - The team's win-draw-loss record, providing a summary of their performance in recent matches or seasons.