# Routes

Every published route, one row per path pattern. `{sport}` is the sport slug (`basketball`, `tennis`, `esport`, `ice-hockey`, and the rest). Football match, player, and team routes have no slug: `/api/match/{id}`, not `/api/football/match/{id}`.

The comment is the summary published for that route. Where several sports share the path and the wording differs only by the sport name, the row keeps one comment.

Names after the path are query parameters. Omit one you are not using. `page` on search, team, and player lists starts at 0. `page` on `scheduled-tournaments` starts at 1.

A `200` body is the payload for that route. A `204` body is empty. The shapes that callers parse most often are in [README](README.md). Field lists are the other pages in this folder. Machine-readable parameters are in [openapi/](../openapi/).

## Event

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/event/newly-added` |  | List newly added events |
| `GET /api/match/{customId}/h2h` |  | Get head-to-head history |
| `GET /api/match/{eventId}/best-players/summary` |  | Get match best-player summary |
| `GET /api/match/{id}` |  | Get football match details |
| `GET /api/match/{id}/average-positions` |  | Get match average positions |
| `GET /api/match/{id}/best-players` |  | Get match best players |
| `GET /api/match/{id}/commentary` |  | Get match commentary |
| `GET /api/match/{id}/duel` |  | Get head-to-head summary |
| `GET /api/match/{id}/form` |  | Get match form analysis |
| `GET /api/match/{id}/goalkeeper/jersey/away` |  | Get away goalkeeper jersey |
| `GET /api/match/{id}/goalkeeper/jersey/home` |  | Get home goalkeeper jersey |
| `GET /api/match/{id}/graph` |  | Get match momentum graph |
| `GET /api/match/{id}/graph/sequence` |  | Get event graph sequence |
| `GET /api/match/{id}/incidents` |  | Get match incidents |
| `GET /api/match/{id}/lineups` |  | Get match lineups |
| `GET /api/match/{id}/meta` |  | Get event metadata |
| `GET /api/match/{id}/official-tweets` |  | Get event official tweets |
| `GET /api/match/{id}/provider/{providerId}/winning-odds` |  | Get match winning odds |
| `GET /api/match/{id}/shotmap` |  | Get match shot map |
| `GET /api/match/{id}/statistics` |  | Get match statistics |
| `GET /api/match/{id}/votes` |  | Get match votes |
| `GET /api/match/{id}/weather` |  | Get event weather |
| `GET /api/match/{id}/win-probability` |  | Get match win probability |
| `GET /api/matches/bottom/{day}/{month}/{year}` |  | Get bottom football matches by date |
| `GET /api/matches/live` |  | Get live football matches |
| `GET /api/matches/top/{day}/{month}/{year}` |  | Get top football matches by date |
| `GET /api/sport/event-count/{timezoneOffset}` |  | Count events for a timezone offset |
| `GET /api/trending/events/{country}` |  | List trending events |
| `GET /api/venue/{id}/events/{sport}/{span}/{page}` |  | Get venue events |
| `GET /api/{sport}/event/{customId}/h2h` |  | Get head-to-head events |
| `GET /api/{sport}/event/{customId}/h2h/events` |  | Get head-to-head history for an event |
| `GET /api/{sport}/event/{id}` |  | Get event |
| `GET /api/{sport}/event/{id}/comments` |  | Get event comments |
| `GET /api/{sport}/event/{id}/duel` |  | Get head-to-head summary |
| `GET /api/{sport}/event/{id}/form` |  | Get pregame form |
| `GET /api/{sport}/event/{id}/games` |  | Get event games |
| `GET /api/{sport}/event/{id}/graph` |  | Get event graph |
| `GET /api/{sport}/event/{id}/graph/sequence` |  | Get event graph sequence |
| `GET /api/{sport}/event/{id}/incidents` |  | Get event incidents |
| `GET /api/{sport}/event/{id}/lineups` |  | Get event lineups |
| `GET /api/{sport}/event/{id}/meta` |  | Get event metadata |
| `GET /api/{sport}/event/{id}/official-tweets` |  | Get event official tweets |
| `GET /api/{sport}/event/{id}/point-by-point` |  | Get point by point |
| `GET /api/{sport}/event/{id}/pregame-form` |  | Get pre-game form for an event |
| `GET /api/{sport}/event/{id}/provider/{providerId}/winning-odds` |  | Get match winning odds |
| `GET /api/{sport}/event/{id}/statistics` |  | Get event statistics |
| `GET /api/{sport}/event/{id}/tennis-power` |  | Get power |
| `GET /api/{sport}/event/{id}/votes` |  | Get event votes |
| `GET /api/{sport}/event/{id}/win-probability` |  | Get win probability |
| `GET /api/{sport}/events/live` |  | List live events |
| `GET /api/{sport}/events/{day}/{month}/{year}` |  | List events on a date |
| `GET /api/{sport}/match/{customId}/h2h` |  | Get head-to-head events |
| `GET /api/{sport}/match/{id}` |  | Get match details |
| `GET /api/{sport}/match/{id}/at-bats` |  | List at-bats |
| `GET /api/{sport}/match/{id}/atbat/{atBatId}/pitches` |  | Get at-bat pitches |
| `GET /api/{sport}/match/{id}/best-players` |  | Get match best players |
| `GET /api/{sport}/match/{id}/comments` |  | Get event comments |
| `GET /api/{sport}/match/{id}/duel` |  | Get head-to-head summary |
| `GET /api/{sport}/match/{id}/form` |  | Get match form analysis |
| `GET /api/{sport}/match/{id}/graph` |  | Get event graph |
| `GET /api/{sport}/match/{id}/graph/sequence` |  | Get event graph sequence |
| `GET /api/{sport}/match/{id}/incidents` |  | Get match incidents |
| `GET /api/{sport}/match/{id}/innings` |  | Get match innings |
| `GET /api/{sport}/match/{id}/lineups` |  | Get match lineups |
| `GET /api/{sport}/match/{id}/meta` |  | Get event metadata |
| `GET /api/{sport}/match/{id}/official-tweets` |  | Get event official tweets |
| `GET /api/{sport}/match/{id}/provider/{providerId}/winning-odds` |  | Get match winning odds |
| `GET /api/{sport}/match/{id}/series` |  | Get match series information |
| `GET /api/{sport}/match/{id}/statistics` |  | Get match statistics |
| `GET /api/{sport}/match/{id}/top-performers` |  | Get top performers |
| `GET /api/{sport}/match/{id}/umpires` |  | Get event umpires |
| `GET /api/{sport}/match/{id}/votes` |  | Get match votes |
| `GET /api/{sport}/match/{id}/weather` |  | Get event weather |
| `GET /api/{sport}/match/{id}/win-probability` |  | Get win probability |
| `GET /api/{sport}/matches/live` |  | Get live matches |
| `GET /api/{sport}/matches/{day}/{month}/{year}` |  | Get matches by date |
| `GET /api/{sport}/venue/{id}/events/{sport}/{span}/{page}` |  | Get venue events |

## Tournament

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/calendar/season/{seasonId}/{year}/days-with-events` |  | Get calendar days with events |
| `GET /api/category/{categoryId}/matches/{day}/{month}/{year}` |  | Get category scheduled events |
| `GET /api/category/{id}/event-count/{day}/{month}/{year}/{timezoneOffset}` |  | Get category unique tournament event count |
| `GET /api/category/{id}/events/{day}/{month}/{year}` |  | Get matches by category and date |
| `GET /api/group/tournament/{tournamentId}/season/{seasonId}/matches` |  | Get tournament season events |
| `GET /api/group/tournament/{tournamentId}/season/{seasonId}/standings/home` |  | Get group tournament home standings |
| `GET /api/group/tournament/{tournamentId}/season/{seasonId}/standings/total` |  | Get group tournament total standings |
| `GET /api/placeholder/tournament.png` |  | Get tournament placeholder image |
| `GET /api/placeholder/tournament.svg` |  | Get tournament placeholder image |
| `GET /api/rankings/unique-tournament/{tournamentId}/{weightClass}/{gender}` |  | Get division rankings |
| `GET /api/tournament/all/category/{id}` |  | Get tournaments by category |
| `GET /api/tournament/categories` |  | Get football tournament categories |
| `GET /api/tournament/categories/all` |  | List every sport category |
| `GET /api/tournament/categories/live` |  | List live sport categories |
| `GET /api/tournament/{tournamentId}` |  | Get league details |
| `GET /api/tournament/{tournamentId}/events/live/{page}` |  | List live events of a unique tournament |
| `GET /api/tournament/{tournamentId}/featured-events` |  | Get tournament featured events |
| `GET /api/tournament/{tournamentId}/meta` |  | Get tournament metadata |
| `GET /api/tournament/{tournamentId}/scheduled-events/{date}` |  | Get tournament events on date |
| `GET /api/tournament/{tournamentId}/schedules/{day}/{month}/{year}` |  | Get tournament events on date |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/best-players` |  | Get overall league top players |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/best-players/per-game` |  | Get per-game player leaders |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/best-teams` |  | Get overall league top teams |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/cuptrees` |  | Get league cup trees |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/groups` |  | Get league groups |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/info` |  | Get tournament season info |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/matches/last/{page}` |  | Get recent league matches |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/matches/next/{page}` |  | Get upcoming league matches |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/matches/round/{round}` |  | Get league events by round |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/matches/round/{round}/slug/{slug}` |  | Get league events by round and slug |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/power-rankings/round/{round}` |  | Get power rankings by round |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/power-rankings/rounds` |  | List power ranking rounds |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/rounds` |  | List league rounds |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/standings/away` |  | Get away league standings |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/standings/home` |  | Get home league standings |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/standings/total` |  | Get total league standings |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/statistics` | `limit`, `page`, `group`, `order`, `accumulation`, `minApps`, `fields`, `filters` | Get aggregated player statistics |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/statistics/info` |  | Get player statistics metadata |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/top-ratings/overall` |  | Get tournament top ratings |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/tow/rounds` |  | List team of the week rounds |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/venues` |  | Get tournament season venues |
| `GET /api/tournament/{tournamentId}/seasons` |  | Get league seasons |
| `GET /api/tournament/{tournamentId}/top-player-performance` | `orderBy` | Get tournament top player performance |
| `GET /api/tournament/{tournamentId}/winners` |  | Get tournament winners |
| `GET /api/tournaments/finished-upcoming/{date}` |  | List finished and upcoming tournaments |
| `GET /api/tournaments/live` |  | List live tournaments |
| `GET /api/{sport}/calendar/unique-tournament/{id}/{timezoneOffset}/months-with-events` |  | Get months with events |
| `GET /api/{sport}/calendar/{yearMonth}/{timezoneOffset}/{sport}/stages` |  | Get calendar sport stages |
| `GET /api/{sport}/category/{categoryId}/live-unique-tournaments` |  | Get live tournaments for category |
| `GET /api/{sport}/category/{id}/event-count/{day}/{month}/{year}/{timezoneOffset}` |  | Get category unique tournament event count |
| `GET /api/{sport}/category/{id}/events/{day}/{month}/{year}` |  | List category events on a date |
| `GET /api/{sport}/category/{id}/stages/all` |  | List every stage in a category |
| `GET /api/{sport}/category/{id}/unique-tournaments` |  | Get unique tournaments by category |
| `GET /api/{sport}/group/tournament/{tournamentId}/season/{seasonId}/matches` |  | Get group matches |
| `GET /api/{sport}/group/tournament/{tournamentId}/season/{seasonId}/standings/total` |  | Get group tournament total standings |
| `GET /api/{sport}/rankings/unique-tournament/{tournamentId}/summary` |  | Get rankings summary for a tournament |
| `GET /api/{sport}/stage/featured` |  | Get the featured stage |
| `GET /api/{sport}/stage/scheduled/{date}` |  | List scheduled stages |
| `GET /api/{sport}/stage/{id}/driver-performance` |  | Get driver performance |
| `GET /api/{sport}/stage/{id}/extended` |  | Get stage extended details |
| `GET /api/{sport}/stage/{id}/races/type/{type}` |  | List races by type |
| `GET /api/{sport}/stage/{id}/standings/competitor` |  | Get stage competitor standings |
| `GET /api/{sport}/stage/{id}/substages-with-rankings` |  | List substages with rankings |
| `GET /api/{sport}/stage/{stageId}` |  | Get a stage |
| `GET /api/{sport}/stage/{stageId}/substages` |  | Get stage substages |
| `GET /api/{sport}/tournament/all/category/{id}` |  | List tournaments in a category |
| `GET /api/{sport}/tournament/categories` |  | Get tournament categories |
| `GET /api/{sport}/tournament/categories/all` |  | List every sport category |
| `GET /api/{sport}/tournament/categories/live` |  | List live sport categories |
| `GET /api/{sport}/tournament/{tournamentId}` |  | Get tournament |
| `GET /api/{sport}/tournament/{tournamentId}/draft/{year}/pick-lottery-probability` |  | Get draft lottery probabilities |
| `GET /api/{sport}/tournament/{tournamentId}/draft/{year}/pick/{pick}` |  | Get one draft pick |
| `GET /api/{sport}/tournament/{tournamentId}/draft/{year}/prospect/{prospectId}` |  | Get one draft prospect |
| `GET /api/{sport}/tournament/{tournamentId}/events/live/{page}` |  | List live events of a unique tournament |
| `GET /api/{sport}/tournament/{tournamentId}/featured-events` |  | Get featured tournament events |
| `GET /api/{sport}/tournament/{tournamentId}/info` |  | Get tournament meta info |
| `GET /api/{sport}/tournament/{tournamentId}/scheduled-events/{date}` |  | Get tournament events on date |
| `GET /api/{sport}/tournament/{tournamentId}/schedules/{day}/{month}/{year}` |  | List tournament events on a date |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-players/overall` |  | Get top players overall |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-players/per-game` |  | Get top players per game statistics |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-players/per-game/overall` |  | Get top players per game overall |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-players/per-game/playoffs` |  | Get top players per game for playoffs |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-players/per-game/regularSeason` |  | Get top players per game for regular season |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-players/playoffs` |  | Get top players for playoffs |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-players/regularSeason` |  | Get top players for regular season |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-players/regularseason` |  | Get top players for regular season |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-players/types` |  | Get player statistics types |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-teams/overall` |  | Get top teams overall |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-teams/playoffs` |  | Get top teams for playoffs |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/best-teams/regularSeason` |  | Get top teams for regular season |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/champions` |  | List champions |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/cup-trees` |  | Get tournament bracket |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/cup-trees/old` |  | Get tournament draw (legacy format) |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/cuptrees` |  | Get structured cup tree |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/draft` |  | Get draft |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/events/last/{page}` |  | List previous season events |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/events/next/{page}` |  | List upcoming season events |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/events/round/{round}` |  | List events in a round |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/events/round/{round}/slug/{slug}` |  | List events in a round and slug |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/groups` |  | Get tournament groups |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/individual-awards` |  | List individual awards |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/info` |  | Get tournament season info |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/matches` |  | Get tournament season matches |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/matches/last/{page}` |  | List previous season events |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/matches/next/{page}` |  | List upcoming season events |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/matches/round/{round}` |  | List events in a round |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/matches/round/{round}/slug/{slug}` |  | List events in a round and slug |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/power-rankings/rounds` |  | Get tournament power ranking rounds |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/rounds` |  | List season rounds |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/shot-action-areas/event/overall` |  | Get shot action areas by event overall |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/shot-actions/areas/playoffs` |  | Get shot actions areas for playoffs |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/shot-actions/areas/regularSeason` |  | Get shot actions areas for regular season |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/standings/away` |  | Get away standings |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/standings/home` |  | Get home standings |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/standings/total` |  | Get total standings |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/statistics/info` |  | Get tournament statistics info |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/top-players` |  | Get tournament top players |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/top-ratings/overall` |  | Get tournament top ratings |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/top-teams/mainDraw` |  | Get tournament top teams main draw |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/venue/{venueId}/events/all/{page}` |  | Get tournament venue events |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/venues` |  | List season venues |
| `GET /api/{sport}/tournament/{tournamentId}/seasons` |  | List tournament seasons |
| `GET /api/{sport}/tournament/{tournamentId}/top-player-performance` | `orderBy` | Get tournament top player performance |
| `GET /api/{sport}/tournament/{tournamentId}/winners` |  | Get tournament winners |
| `GET /api/{sport}/tournaments/finished-upcoming/{date}` |  | List finished and upcoming tournaments |
| `GET /api/{sport}/tournaments/live` |  | List live tournaments |
| `GET /api/{sport}/unique-stage/{uniqueStageId}/season` |  | Get unique stage seasons |
| `GET /api/{sport}/unique-tournament/all/category/{id}` |  | Get tournaments by category |
| `GET /api/{sport}/unique-tournament/{tournamentId}` |  | Get tournament details |
| `GET /api/{sport}/unique-tournament/{tournamentId}/events/live/{page}` |  | List live events of a unique tournament |
| `GET /api/{sport}/unique-tournament/{tournamentId}/featured-events` |  | Get featured events for a tournament |
| `GET /api/{sport}/unique-tournament/{tournamentId}/main-events/last/{page}` |  | Get last main events for a tournament |
| `GET /api/{sport}/unique-tournament/{tournamentId}/main-events/next/{page}` |  | Get next main events for a tournament |
| `GET /api/{sport}/unique-tournament/{tournamentId}/schedules/{day}/{month}/{year}` |  | Get tournament schedule by date |
| `GET /api/{sport}/unique-tournament/{tournamentId}/schedules/{month}/{year}` |  | Get scheduled main events by month |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/cuptrees` |  | Get tournament cup trees |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/groups` |  | Get tournament groups |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/matches/last/{page}` |  | Get tournament last matches |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/matches/next/{page}` |  | Get league next matches |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/matches/round/{round}` |  | Get tournament matches by round |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/matches/round/{round}/slug/{slug}` |  | Get tournament matches by round with slug |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/rounds` |  | Get tournament rounds |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/standings/away` |  | Get tournament away standings |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/standings/home` |  | Get tournament home standings |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/standings/total` |  | Get tournament total standings |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/top-players-per-game/all/overall` |  | Get top players per game |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/top-players/overall` |  | Get top players overall |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/top-teams/overall` |  | Get top teams overall |
| `GET /api/{sport}/unique-tournament/{tournamentId}/seasons` |  | Get tournament seasons |
| `GET /api/{sport}/unique-tournament/{uniqueTournamentId}/tournament/{tournamentId}/mma-events/all` |  | Get all events for a tournament |

## Team

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/manager/{id}` |  | Get manager details |
| `GET /api/manager/{id}/history` |  | Get manager career history |
| `GET /api/manager/{id}/matches/next/{page}` |  | Get manager upcoming matches |
| `GET /api/manager/{id}/matches/previous/{page}` |  | Get manager previous matches |
| `GET /api/match/{id}/managers` |  | Get match managers |
| `GET /api/match/{id}/team/{teamId}/heatmap` |  | Get match team heatmap by ID |
| `GET /api/placeholder/manager.png` |  | Get manager placeholder image |
| `GET /api/placeholder/manager.svg` |  | Get manager placeholder image |
| `GET /api/placeholder/team.svg` |  | Get team placeholder image |
| `GET /api/rankings/team/{teamId}` |  | Get team rankings |
| `GET /api/referee/{id}` |  | Get referee details |
| `GET /api/referee/{id}/matches/next/{page}` |  | Get upcoming referee matches |
| `GET /api/referee/{id}/matches/previous/{page}` |  | Get previous referee matches |
| `GET /api/referee/{id}/statistics` |  | Get referee statistics |
| `GET /api/team-of-the-period/{periodId}` |  | Get team of the period |
| `GET /api/team/{id}` |  | Get team details |
| `GET /api/team/{id}/achievements` |  | Get team achievements |
| `GET /api/team/{id}/events/{month}/{year}` |  | List team events in a month |
| `GET /api/team/{id}/featured-event` |  | Get team featured event |
| `GET /api/team/{id}/featured-players` |  | Get team featured players |
| `GET /api/team/{id}/matches/near` |  | Get team near matches |
| `GET /api/team/{id}/matches/next/{page}` |  | Get upcoming team matches |
| `GET /api/team/{id}/matches/previous/{page}` |  | Get previous team matches |
| `GET /api/team/{id}/standings/seasons` |  | Get team standings seasons |
| `GET /api/team/{id}/statistics/seasons` |  | Get team statistics seasons |
| `GET /api/team/{id}/tournament/{tournamentId}/season/{seasonId}/best-players` |  | Get team top players overall |
| `GET /api/team/{id}/tournament/{tournamentId}/season/{seasonId}/ranks/overall` |  | Get team overall ranks |
| `GET /api/team/{id}/tournament/{tournamentId}/season/{seasonId}/statistics` |  | Get team overall statistics |
| `GET /api/team/{id}/tournaments` |  | Get team unique tournaments |
| `GET /api/team/{id}/transfers` |  | Get team transfer history |
| `GET /api/team/{id}/unique-tournaments/all` |  | Get all team tournaments |
| `GET /api/team/{teamId}/tournament/{tournamentId}/season/{seasonId}/goal-distributions` |  | Get team goal distributions |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/round/{roundId}/team-of-week` |  | Get team of the week |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/team-events/away` |  | Get league team away event totals |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/team-events/home` |  | Get league team home event totals |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/team-events/total` |  | Get league team events totals |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/team-of-the-period/periods/awarded` |  | List awarded team-of-the-period entries |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/team-of-the-season` |  | Get team of the season |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/team-of-the-week/periods` |  | List team-of-the-week periods |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/team-statistics/types` |  | Get team statistics types |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/team/{teamId}/performance` |  | Get team league performance graph |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/teams` |  | Get tournament season teams |
| `GET /api/{sport}/event/{id}/team-streaks` |  | Get fighter streaks for an event |
| `GET /api/{sport}/group/tournament/{tournamentId}/season/{seasonId}/team-events/total` |  | Get group tournament team events total |
| `GET /api/{sport}/manager/{id}` |  | Get manager |
| `GET /api/{sport}/manager/{id}/matches/previous/{page}` |  | List previous matches for a manager |
| `GET /api/{sport}/match/{id}/managers` |  | Get match managers |
| `GET /api/{sport}/match/{id}/team-streaks` |  | Get match team streaks |
| `GET /api/{sport}/match/{id}/team/{teamId}/shotmap` |  | Get team shot map |
| `GET /api/{sport}/stage/{id}/standings/team` |  | Get stage team standings |
| `GET /api/{sport}/team-of-the-period/{periodId}` |  | Get team of the period |
| `GET /api/{sport}/team/{id}` |  | Get team details |
| `GET /api/{sport}/team/{id}/career-statistics` |  | Get fighter career statistics |
| `GET /api/{sport}/team/{id}/driver/history` |  | Get rider history |
| `GET /api/{sport}/team/{id}/events/last/{page}` |  | Get last events for an fighter |
| `GET /api/{sport}/team/{id}/events/near` |  | Get team near matches |
| `GET /api/{sport}/team/{id}/events/next/{page}` |  | Get next events for an fighter |
| `GET /api/{sport}/team/{id}/events/previous/{page}` |  | Get previous team matches |
| `GET /api/{sport}/team/{id}/events/{month}/{year}` |  | List team events in a month |
| `GET /api/{sport}/team/{id}/featured-event` |  | Get featured event for a team |
| `GET /api/{sport}/team/{id}/matches/near` |  | List nearby events for a team |
| `GET /api/{sport}/team/{id}/matches/next/{page}` |  | List next events for a team |
| `GET /api/{sport}/team/{id}/matches/previous/{page}` |  | List previous events for a team |
| `GET /api/{sport}/team/{id}/performance` |  | Get team performance |
| `GET /api/{sport}/team/{id}/rankings` |  | Get team rankings |
| `GET /api/{sport}/team/{id}/recent-unique-tournaments` |  | Get team recent tournaments |
| `GET /api/{sport}/team/{id}/season/{seasonId}/best-result` |  | Get team season best result |
| `GET /api/{sport}/team/{id}/stage/season/{seasonId}/races` |  | Get team stage season races |
| `GET /api/{sport}/team/{id}/stage/seasons` |  | Get team stage seasons |
| `GET /api/{sport}/team/{id}/standings/seasons` |  | List standings seasons for a team |
| `GET /api/{sport}/team/{id}/statistics/seasons` |  | Get team statistics seasons |
| `GET /api/{sport}/team/{id}/tournament/{tournamentId}/season/{seasonId}/best-players/playoffs` |  | Get team top players for playoffs |
| `GET /api/{sport}/team/{id}/tournament/{tournamentId}/season/{seasonId}/best-players/regularSeason` |  | Get team top players for regular season |
| `GET /api/{sport}/team/{id}/tournament/{tournamentId}/season/{seasonId}/best-players/regularseason` |  | Get team top players for regular season |
| `GET /api/{sport}/team/{id}/tournament/{tournamentId}/season/{seasonId}/ranks/overall` |  | Get team overall ranks |
| `GET /api/{sport}/team/{id}/tournament/{tournamentId}/season/{seasonId}/ranks/playoffs` |  | Get team playoffs rankings |
| `GET /api/{sport}/team/{id}/tournament/{tournamentId}/season/{seasonId}/ranks/regularSeason` |  | Get team regular season rankings |
| `GET /api/{sport}/team/{id}/tournament/{tournamentId}/season/{seasonId}/statistics/playoffs` |  | Get team playoffs statistics |
| `GET /api/{sport}/team/{id}/tournament/{tournamentId}/season/{seasonId}/statistics/regularSeason` |  | Get team regular season statistics |
| `GET /api/{sport}/team/{id}/tournaments` |  | Get team tournaments |
| `GET /api/{sport}/team/{id}/tournaments/last` |  | Get team recent tournaments |
| `GET /api/{sport}/team/{id}/transfers` |  | Get team transfers |
| `GET /api/{sport}/team/{id}/unique-tournament/{tournamentId}/season/{seasonId}/top-players/overall` |  | Get team top players overall |
| `GET /api/{sport}/team/{id}/unique-tournaments` |  | List unique tournaments for a team |
| `GET /api/{sport}/team/{id}/unique-tournaments/all` |  | Get all team tournaments |
| `GET /api/{sport}/team/{id}/year-statistics/{year}` |  | Get team year statistics |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/team-events/away` |  | Get team events, away |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/team-events/home` |  | Get team events, home |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/team-events/total` |  | Get team events, total |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/team-of-the-period/periods/awarded` |  | List awarded team-of-the-period entries |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/team-of-the-period/periods/rated` |  | List rated team-of-the-period entries |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/team-of-the-season` |  | Get team of the season |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/team-of-the-week/periods` |  | List team-of-the-week periods |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/team-of-the-week/rounds` |  | Get tournament team of the week rounds |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/team-statistics/types` |  | Get team statistics types |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/teams` |  | Get tournament season teams |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/team-events/away` |  | Get team events away statistics |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/team-events/home` |  | Get team events home statistics |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/team-events/total` |  | Get team events total statistics |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/team-of-the-season` |  | Get team of the season |

## Player

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/match/{id}/player/jersey/away` |  | Get away player jersey |
| `GET /api/match/{id}/player/jersey/away-clean` |  | Get away player clean jersey |
| `GET /api/match/{id}/player/jersey/home` |  | Get home player jersey |
| `GET /api/match/{id}/player/jersey/home-clean` |  | Get home player clean jersey |
| `GET /api/match/{id}/player/{playerId}/goalkeeper-shotmap` |  | Get goalkeeper shotmap |
| `GET /api/match/{id}/player/{playerId}/heatmap` |  | Get match player heatmap |
| `GET /api/match/{id}/player/{playerId}/rating-breakdown` |  | Get match player rating breakdown |
| `GET /api/match/{id}/player/{playerId}/shotmap` |  | Get football match player shotmap |
| `GET /api/match/{id}/player/{playerId}/statistics` |  | Get player match statistics |
| `GET /api/match/{id}/players/featured` |  | Get match featured players |
| `GET /api/placeholder/player.png` |  | Get player placeholder image |
| `GET /api/placeholder/player.svg` |  | Get player placeholder image |
| `GET /api/player/trending` |  | Get trending players |
| `GET /api/player/{id}` |  | Get player details |
| `GET /api/player/{id}/attribute` |  | Get player attributes |
| `GET /api/player/{id}/characteristics` |  | Get player characteristics |
| `GET /api/player/{id}/matches/near` |  | Get player nearby matches |
| `GET /api/player/{id}/matches/previous/{page}` |  | Get player match history |
| `GET /api/player/{id}/penalty` |  | Get player penalty history |
| `GET /api/player/{id}/penalty-history/tournament/{tournamentId}/season/{seasonId}` |  | Get player penalty history by season |
| `GET /api/player/{id}/statistics/all` |  | Get all player statistics |
| `GET /api/player/{id}/statistics/match-type/{matchType}` |  | Get player statistics by match type |
| `GET /api/player/{id}/statistics/national` |  | Get player national team statistics |
| `GET /api/player/{id}/statistics/season` |  | Get player seasonal statistics |
| `GET /api/player/{id}/summary` |  | Get player last year summary |
| `GET /api/player/{id}/tournament/{tournamentId}/events/last/{page}` |  | Get player tournament last matches |
| `GET /api/player/{id}/tournament/{tournamentId}/season/{seasonId}/heatmap` |  | Get player season heatmap overall |
| `GET /api/player/{id}/tournament/{tournamentId}/season/{seasonId}/last-ratings` |  | Get player last ratings |
| `GET /api/player/{id}/tournament/{tournamentId}/season/{seasonId}/ratings` |  | Get player ratings |
| `GET /api/player/{id}/tournament/{tournamentId}/season/{seasonId}/statistics` |  | Get player overall statistics |
| `GET /api/player/{id}/transfer` |  | Get player transfer history |
| `GET /api/player/{id}/unique-tournaments` |  | Get player tournaments |
| `GET /api/team/{id}/players` |  | Get team squad |
| `GET /api/team/{id}/players/statistics/seasons` |  | Get team player statistics seasons |
| `GET /api/team/{id}/unique-tournament/{tournamentId}/season/{seasonId}/player-statistics/{type}` |  | Get team squad player statistics |
| `GET /api/tournament/{tournamentId}/player-news` |  | Get tournament player news |
| `GET /api/tournament/{tournamentId}/player-transfer-history/all/{page}` |  | Get tournament transfer history |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/player-of-the-season` |  | Get player of the season |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/player-of-the-season-race` |  | Get player of season race |
| `GET /api/tournament/{tournamentId}/season/{seasonId}/player-statistics/types` |  | Get player statistics info |
| `GET /api/{sport}/match/{id}/player/{playerId}/pitches/{kind}` |  | Get pitches for one player in an event |
| `GET /api/{sport}/match/{id}/player/{playerId}/shotmap` |  | Get player shot map |
| `GET /api/{sport}/match/{id}/player/{playerId}/statistics` |  | Get player match statistics |
| `GET /api/{sport}/player/{id}` |  | Get player details |
| `GET /api/{sport}/player/{id}/events/doubles/last/{page}` |  | List doubles results |
| `GET /api/{sport}/player/{id}/events/near` |  | List nearby events for a team |
| `GET /api/{sport}/player/{id}/events/next/{page}` |  | List next events for a team |
| `GET /api/{sport}/player/{id}/events/previous/{page}` |  | List previous events for a team |
| `GET /api/{sport}/player/{id}/events/singles/last/{page}` |  | List singles results |
| `GET /api/{sport}/player/{id}/events/{month}/{year}` |  | List team events in a month |
| `GET /api/{sport}/player/{id}/featured-event` |  | Get featured event for a team |
| `GET /api/{sport}/player/{id}/grand-slam/best-results` |  | Get grand-slam best results |
| `GET /api/{sport}/player/{id}/matches/near` |  | Get player near matches |
| `GET /api/{sport}/player/{id}/matches/previous/{page}` |  | Get previous player matches |
| `GET /api/{sport}/player/{id}/performance` |  | Get team performance |
| `GET /api/{sport}/player/{id}/rankings` |  | Get player rankings |
| `GET /api/{sport}/player/{id}/season/{seasonId}/best-result` |  | Get season best result |
| `GET /api/{sport}/player/{id}/season/{seasonId}/statistical-rankings/{phase}` |  | Get statistical rankings |
| `GET /api/{sport}/player/{id}/standings/seasons` |  | List standings seasons for a team |
| `GET /api/{sport}/player/{id}/statistics/season` |  | Get player statistics seasons |
| `GET /api/{sport}/player/{id}/statistics/seasons` |  | Get player statistics seasons |
| `GET /api/{sport}/player/{id}/tournament/{tournamentId}/events/last/{page}` |  | Get player tournament last matches |
| `GET /api/{sport}/player/{id}/tournament/{tournamentId}/season/{seasonId}/pitches/{kind}/{phase}` |  | Get a player's pitches in a season |
| `GET /api/{sport}/player/{id}/tournament/{tournamentId}/season/{seasonId}/ratings/regularSeason` |  | Get player regular season ratings |
| `GET /api/{sport}/player/{id}/tournament/{tournamentId}/season/{seasonId}/shot-actions/playoffs` |  | Get player shot actions for playoffs |
| `GET /api/{sport}/player/{id}/tournament/{tournamentId}/season/{seasonId}/shot-actions/regularSeason` |  | Get player shot actions for regular season |
| `GET /api/{sport}/player/{id}/tournament/{tournamentId}/season/{seasonId}/statistics/overall` |  | Get player overall statistics |
| `GET /api/{sport}/player/{id}/tournament/{tournamentId}/season/{seasonId}/statistics/playoffs` |  | Get player playoffs statistics |
| `GET /api/{sport}/player/{id}/tournament/{tournamentId}/season/{seasonId}/statistics/regularSeason` |  | Get player regular season statistics |
| `GET /api/{sport}/player/{id}/tournament/{tournamentId}/season/{seasonId}/statistics/regularseason` |  | Get player regular season statistics |
| `GET /api/{sport}/player/{id}/tournaments/last` |  | Get player recent tournaments |
| `GET /api/{sport}/player/{id}/transfers` |  | Get player transfer history |
| `GET /api/{sport}/player/{id}/unique-tournament/{tournamentId}/season/{seasonId}/statistics/overall` |  | Get player overall statistics |
| `GET /api/{sport}/player/{id}/unique-tournaments` |  | List unique tournaments for a team |
| `GET /api/{sport}/player/{id}/year-statistics/{year}` |  | Get year statistics |
| `GET /api/{sport}/players/trending` |  | List trending players |
| `GET /api/{sport}/team/{id}/player-statistics/seasons` |  | Get team player statistics seasons |
| `GET /api/{sport}/team/{id}/players` |  | Get team players |
| `GET /api/{sport}/team/{id}/players/statistics/seasons` |  | Get team player statistics seasons |
| `GET /api/{sport}/team/{id}/unique-tournament/{tournamentId}/season/{seasonId}/player-statistics/{type}` |  | Get team squad player statistics |
| `GET /api/{sport}/tournament/{tournamentId}/player-news` |  | Get tournament player news |
| `GET /api/{sport}/tournament/{tournamentId}/player-transfer-history/all/{page}` |  | Get tournament transfer history |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/player-of-the-season` |  | Get tournament player of the season |
| `GET /api/{sport}/tournament/{tournamentId}/season/{seasonId}/player-statistics/types` |  | Get player statistics info |
| `GET /api/{sport}/unique-tournament/{tournamentId}/season/{seasonId}/player-statistics/types` |  | Get player statistics types |

## Odds

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/match/{id}/odds` |  | Get match betting odds |
| `GET /api/match/{id}/odds/{providerId}/all` |  | Get all odds for event |
| `GET /api/match/{id}/odds/{providerId}/featured` |  | Get match featured odds |
| `GET /api/match/{id}/streaks` |  | Get team streaks |
| `GET /api/match/{id}/streaks/odds` |  | Get match streaks with odds |
| `GET /api/matches/odds/featured` |  | Get featured betting events |
| `GET /api/matches/odds/featured-by-popularity/{providerId}` |  | List featured events by popularity |
| `GET /api/matches/odds/{day}/{month}/{year}` |  | Get sport odds by date |
| `GET /api/odds/providers/{countryCode}/{regionCode}/{type}` |  | List odds providers for a country region |
| `GET /api/odds/providers/{countryCode}/{type}` |  | List odds providers for a country |
| `GET /api/odds/season/{seasonId}/provider/{providerId}/all` |  | Get all odds for a season |
| `GET /api/{sport}/event/{id}/odds` |  | Get event odds |
| `GET /api/{sport}/event/{id}/odds/{providerId}/all` |  | Get all odds for event |
| `GET /api/{sport}/event/{id}/odds/{providerId}/featured` |  | Get match featured odds |
| `GET /api/{sport}/event/{id}/streak` |  | Get match streaks |
| `GET /api/{sport}/event/{id}/streaks` |  | Get event streaks |
| `GET /api/{sport}/event/{id}/streaks/odds` |  | Get match streaks with odds |
| `GET /api/{sport}/events/odds/featured-by-popularity/{providerId}` |  | List featured events by popularity |
| `GET /api/{sport}/events/odds/featured-by-tiers/{providerId}` |  | Get featured events by tiers |
| `GET /api/{sport}/events/odds/featured/{providerId}` |  | Get featured events with odds |
| `GET /api/{sport}/events/odds/{day}/{month}/{year}` |  | Get events with odds |
| `GET /api/{sport}/match/{id}/odds` |  | Get match betting odds |
| `GET /api/{sport}/match/{id}/odds/{providerId}/all` |  | Get all odds for event |
| `GET /api/{sport}/match/{id}/odds/{providerId}/featured` |  | Get match featured odds |
| `GET /api/{sport}/match/{id}/streaks` |  | Get match streaks |
| `GET /api/{sport}/match/{id}/streaks/odds` |  | Get match streaks with odds |
| `GET /api/{sport}/matches/odds/featured-by-popularity/{providerId}` |  | List featured events by popularity |
| `GET /api/{sport}/matches/odds/featured-by-tiers/{providerId}` |  | Get featured betting events by tiers |
| `GET /api/{sport}/matches/odds/featured/{providerId}` |  | Get featured betting events |
| `GET /api/{sport}/matches/odds/{day}/{month}/{year}` |  | Get matches with odds by date |
| `GET /api/{sport}/stage/{id}/odds/provider/{providerId}/all` |  | Get stage odds (all) by provider |
| `GET /api/{sport}/stage/{id}/odds/provider/{providerId}/featured` |  | Get stage odds (featured) by provider |
| `GET /api/{sport}/team/{id}/odds/provider/{providerId}` |  | Get team odds |

## Search

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/search/all` | `q`, `sport`, `page` | Search all entities |
| `GET /api/search/suggestions/{entityType}` | `sport` | Get search suggestions |
| `GET /api/search/unique-tournaments` | `q`, `sport`, `page` | Search unique tournaments |
| `GET /api/search/{entityType}` | `q`, `sport`, `page` | Search by entity type |
| `GET /api/search/{term}` | `page` | Search football entities |
| `GET /api/{sport}/search/{term}` | `page` | Search entities |

## Media

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/category/{categoryId}/image` |  | Get category image |
| `GET /api/manager/{id}/image` |  | Get manager image |
| `GET /api/match/{id}/highlights` |  | Get match highlights |
| `GET /api/match/{id}/media/country/{country}` |  | Get event media summary |
| `GET /api/player/{id}/image` |  | Get player image |
| `GET /api/player/{id}/media` |  | Get player media |
| `GET /api/player/{id}/media/videos` |  | Get player media videos |
| `GET /api/referee/{id}/image` |  | Get referee image |
| `GET /api/team/{id}/image` |  | Get team logo |
| `GET /api/team/{id}/image/small` |  | Get team small logo |
| `GET /api/team/{id}/media` |  | Get team media |
| `GET /api/tournament/{tournamentId}/image` |  | Get tournament logo |
| `GET /api/tournament/{tournamentId}/image/dark` |  | Get league dark logo |
| `GET /api/tournament/{tournamentId}/media` |  | Get league media |
| `GET /api/tv/channel/{channId}/event/{id}` |  | Get match TV channel votes |
| `GET /api/tv/channel/{id}/schedule` |  | Get TV channel schedule |
| `GET /api/tv/country/all/event/{id}` |  | Get match TV countries |
| `GET /api/tv/country/{countryCode}/channels` |  | Get country TV channels |
| `GET /api/venue/{id}/image` |  | Get venue image |
| `GET /api/{sport}/category/{categoryId}/image` |  | Get category image |
| `GET /api/{sport}/character/{characterId}/image` |  | Get character image |
| `GET /api/{sport}/event/{id}/highlights` |  | Get event highlights |
| `GET /api/{sport}/event/{id}/media/country/{country}` |  | Get event media summary |
| `GET /api/{sport}/manager/{id}/image` |  | Get manager image |
| `GET /api/{sport}/map/{mapId}/image` |  | Get map image |
| `GET /api/{sport}/match/{id}/highlights` |  | Get event highlights |
| `GET /api/{sport}/match/{id}/media/country/{country}` |  | Get event media summary |
| `GET /api/{sport}/player/{id}/image` |  | Get player image |
| `GET /api/{sport}/player/{id}/media` |  | Get player media |
| `GET /api/{sport}/player/{id}/media/videos` |  | Get player media videos |
| `GET /api/{sport}/stage/{id}/highlights` |  | Get stage highlights |
| `GET /api/{sport}/stage/{id}/image` |  | Get a stage image |
| `GET /api/{sport}/team/{id}/image` |  | Get team image |
| `GET /api/{sport}/team/{id}/image/small` |  | Get team small logo |
| `GET /api/{sport}/team/{id}/media` |  | Get team media |
| `GET /api/{sport}/tournament/{tournamentId}/image` |  | Get tournament logo |
| `GET /api/{sport}/tournament/{tournamentId}/image/dark` |  | Get tournament dark logo |
| `GET /api/{sport}/tournament/{tournamentId}/media` |  | Get tournament media |
| `GET /api/{sport}/unique-stage/{id}/image` |  | Get a unique-stage image |
| `GET /api/{sport}/unique-tournament/{tournamentId}/image` |  | Get tournament logo |
| `GET /api/{sport}/unique-tournament/{tournamentId}/image/dark` |  | Get tournament dark logo |
| `GET /api/{sport}/unique-tournament/{tournamentId}/media` |  | Get tournament media |
| `GET /api/{sport}/venue/{id}/image` |  | Get venue image |

## Other

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/countries/all` |  | Get all countries |
| `GET /api/country/{code}/flag` |  | Get country flag (img API) |
| `GET /api/img/flag/{flag}` |  | Get country flag |
| `GET /api/main-events/{date}/extended` |  | List extended main events by date |
| `GET /api/placeholders/fighter-female.svg` |  | Get female fighter placeholder image |
| `GET /api/placeholders/fighter-male.svg` |  | Get male fighter placeholder image |
| `GET /api/rankings/fifa` |  | Get FIFA rankings |
| `GET /api/rankings/uefa/clubs` |  | Get UEFA clubs rankings |
| `GET /api/rankings/uefa/countries` |  | Get UEFA countries rankings |
| `GET /api/scheduled-tournaments/{day}/{month}/{year}/page/{page}` |  | Get football scheduled tournaments by date |
| `GET /api/transfer` | `page`, `sort` | List transfers |
| `GET /api/venue/{id}` |  | Get venue details |
| `GET /api/venue/{id}/near-events` |  | Get venue near events |
| `GET /api/{sport}/calendar/{day}/{month}/{year}/categories` |  | Get categories for a day |
| `GET /api/{sport}/calendar/{month}/{year}` |  | Get calendar overview |
| `GET /api/{sport}/calendar/{month}/{year}/categories` | `days` | Get categories for multiple days |
| `GET /api/{sport}/categories` |  | Get categories |
| `GET /api/{sport}/categories/all` |  | List every sport category |
| `GET /api/{sport}/categories/live` |  | List live sport categories |
| `GET /api/{sport}/game/{id}/bans` |  | Get game bans |
| `GET /api/{sport}/game/{id}/lineups` |  | Get game lineups |
| `GET /api/{sport}/game/{id}/rounds` |  | Get game rounds |
| `GET /api/{sport}/game/{id}/statistics` |  | Get game statistics |
| `GET /api/{sport}/main-events/{date}/extended` |  | List extended main events by date |
| `GET /api/{sport}/octogon.png` |  | Get octagon image |
| `GET /api/{sport}/rankings/atp` |  | Get ATP rankings |
| `GET /api/{sport}/rankings/atp/live` |  | Get live ATP rankings |
| `GET /api/{sport}/rankings/rugby-union` |  | Get Union rankings |
| `GET /api/{sport}/rankings/wta` |  | Get WTA rankings |
| `GET /api/{sport}/rankings/wta/live` |  | Get live WTA rankings |
| `GET /api/{sport}/scheduled-tournaments/{day}/{month}/{year}/page/{page}` |  | Get scheduled tournaments by date |
| `GET /api/{sport}/unique-stage/{id}/recent-stage-ids` |  | Get recent stage IDs |
| `GET /api/{sport}/venue/{id}` |  | Get venue details |
