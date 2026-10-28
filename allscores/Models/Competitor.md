# Competitor

A **Competitor** is a team or another side in a list.

**Where you'll see it:** top competitors, competitor details, and `competitors` on a [ScoresList](ScoresList.md) or a [Search](Search.md).

**Related models:** [Athlete](Athlete.md), [Transfer](Transfer.md), [Competition](Competition.md), [Related](Related.md).

`id` is `competitorId` on details, current games, and squads. Recent form, standings, brackets, and trends call it `competitor`. Fixtures, results, and custom scores call a list `competitorIds`. Other lists call it `competitors`.

The top list names `color`. Details name `colors`. Squads are grouped under `squads` by position. This page does not name the keys inside a squad group.

### Example

This object shows keys the top list and the details route name. It is not a captured team. No example response in the guides pins a competitor id on this object, so `id` is omitted here.

```json
{
  "hasSquad": true,
  "hasTransfers": true,
  "hasTrophies": true,
  "hasHighlights": true
}
```

## Properties

- **id** (`number`):
    - Competitor id. Read it from the list you open next.

- **name** (`string`):
    - Display name.

- **longName** (`string`):
    - Long name on the top list.

- **symbolicName** (`string`):
    - Short name.

- **countryId** (`number`):
    - Country id.

- **sportId** (`number`):
    - Sport id.

- **imageVersion** (`number`):
    - Version for a competitor image. See [Image](Image.md).

- **mainCompetitionId** (`number`):
    - The competition this side is mainly in.

- **color** (`value`):
    - Color on the top list. The description does not pick a JSON type.

- **colors** (`value`):
    - Colors on the details route.

- **hasSquad** (`boolean`):
    - A squad is available.

- **hasTransfers** (`boolean`):
    - Transfers are available.

- **hasTrophies** (`boolean`):
    - Trophies are available on the details route.

- **hasHighlights** (`boolean`):
    - Highlights are available on the details route.

- **squads** (`array`):
    - Roster groups by position on the squads route.

- **recentGames** (`array`):
    - Recent matches on the home and away sides of [HeadToHead](HeadToHead.md).
