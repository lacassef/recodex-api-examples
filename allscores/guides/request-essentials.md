# Parameters

Each parameter name is the one in the [OpenAPI](../openapi/allscores_openapi.yaml). Send only the ones the operation lists. Required, type, and example are in the spec.

Lists are comma-separated. `131,132` is two competitor ids.

## Shared on JSON routes

Most JSON routes take these. Play-by-play does not. `/paging` takes `publisherId`, `campaign`, and `userCountryId`, and does not take `langId` or `timezone`.

| Parameter | What to send |
| --- | --- |
| `langId` | Language id from the [language table](../reference/enums.md). Omit for the default language. |
| `timezone` | IANA name. Example: `Africa/Maputo`. |
| `publisherId` | Publisher id. Omit when you do not have one. |
| `campaign` | Campaign. Omit when you do not have one. |
| `userCountryId` | Country id. Omit for the default country. |

## The name depends on the route

Sport numbers are in the [sport list](../reference/sport-ids.md).

| You have | Send it as |
| --- | --- |
| Sport, on countries | `sportId` |
| Sport, on trends and top athletes | `sportType` |
| Sport, on the other routes that filter by sport | `sport` |
| One competition, on details, standings, brackets, stats, trends, and best odds | `competition` |
| One competition, on athlete details, athlete games, and trophy stats | `competitionId` |
| Athlete details also accepts | `competition` |
| Several competitions | `competitions` |
| One competitor, on details, current games, and squads | `competitorId` |
| One competitor, on recent form, standings, brackets, and trends | `competitor` |
| Several competitors, on fixtures, results, and custom scores | `competitorIds` |
| Several competitors, on the other list routes | `competitors` |
| One game, on details, head to head, lineups, point by point, proposition, and teaser | `gameId` |
| One game, on pre-game stats | `game` |
| One game, on play-by-play | `sportifiergameid`, plus `fixtureid` when you have the provider fixture key |
| Several games, or one game on a route that asks for a list | `games` |
| Home, away, and competition, and no game id | `matchupId` as `homeId-awayId-competitionId` |
| One athlete, on details, games, career, and trophy stats | `athleteId` |
| Athlete details accepts several ids in that same parameter | `817` or `817,45579` |
| Several athletes, on next game, chart events, news, outrights, and related entities | `athletes` |

`athleteId` is a string on athlete details and an integer on the other athlete routes.

## Dates

`startDate`, `endDate`, and `date` are the locale short pattern. The patterns and an example are in [Languages and enums](../reference/enums.md).

## Score filters

These narrow a scores list. A route takes one only when that operation lists it.

| Parameter | What it does |
| --- | --- |
| `countries` | Comma-separated country ids. |
| `favoriteCompetitions` | Comma-separated competition ids. |
| `competitionsLimit` | Cap on competitions. |
| `withLive` | Include live games. |
| `withSuggested` | Include suggested games. |
| `blackListGames` | Comma-separated game ids to leave out. |
| `topBookmaker` | Bookmaker id. Omit when no bookmaker is selected. |
| `feedBy` | Feed selector. |
| `onlyOnTv` | Keep games that are on TV. |
| `roundKey` | Round key. `0` is a round. |
| `games` | Comma-separated game ids. |
| `relation` | `or` or `and`. |
| `showOdds` | Include odds. Omit when you do not want odds. |
| `context` | `1` home, `2` my scores, `3` competition page, `4` team page. |
| `numberOfGames` | How many games to return. |
| `onlyMajorGames` | Keep major games. |
| `onlyLiveGames` | Keep live games. |
| `withTop` | Include the top-games block. |
| `includeTopBettingOpportunity` | Include the top betting opportunity. Example: `1`. |
| `matchupId` | Matchup key on the routes that list it. |

## Polling and paging

`lastUpdateId` is the cursor from the previous response. Omit it for a full response.

`paging` on `/paging` is required. It is `paging.nextPage` or `paging.previousPage` from fixtures or results. Send that string unchanged.

## Play-by-play

`lang` is the numeric language id. `appType` is optional. Omit `appType` for the default. `fixtureid` is the provider fixture key. `sportifiergameid` is the game id. `isLive`, `IsFinished`, and `onlyPreview` are optional. The parameter `IsFinished` keeps that capitalization.
