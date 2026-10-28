# Routes

Every published LivescoresAPI route, one row per path. A `*` after a query name means that parameter is required. Omit an optional one you are not using.

A `200` body is the payload for that route. A `204` body is empty: do not parse it as JSON. Image routes return `image/png` or `image/avif`. The report HTML route returns HTML. The objects callers parse are in [README](README.md). Machine-readable parameters are in [openapi/](../openapi/).

## banners

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/banners` |  | Get banners |

## content

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/content/media` |  | Get content media |

## feed

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/feed/{version}/{feed}` |  | Get feed data |

## graphql

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/graphql` | _hash* | Get persisted query data |

## images

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/images/ott/*` |  | Get media image |
| `GET /api/livescores/images/static/*` |  | Get static asset image |

## matches

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/matches/{eventId}/box-score` | version | Get match box score |
| `GET /api/livescores/matches/{eventId}/box-score/names` | version | Get match box score names |
| `GET /api/livescores/matches/{eventId}/commentary` | version | Get match commentary |
| `GET /api/livescores/matches/{eventId}/commentary-only` | version | Get match commentary only |
| `GET /api/livescores/matches/{eventId}/detail-config` | version | Get match detail config |
| `GET /api/livescores/matches/{eventId}/h2h` | version | Get match head-to-head |
| `GET /api/livescores/matches/{eventId}/hashes` | version | Get match hash feed |
| `GET /api/livescores/matches/{eventId}/highlights` | version | Get current tennis game |
| `GET /api/livescores/matches/{eventId}/highlights/videos` | version | Get match highlight videos |
| `GET /api/livescores/matches/{eventId}/lineups` | projectId | Get match lineups |
| `GET /api/livescores/matches/{eventId}/lineups/updates` | projectId, providerId | Get match lineup updates |
| `GET /api/livescores/matches/{eventId}/missing-players` | projectId | Get missing players |
| `GET /api/livescores/matches/{eventId}/missing-players/updates` | providerId | Get missing player updates |
| `GET /api/livescores/matches/{eventId}/momentum` | projectId | Get match momentum |
| `GET /api/livescores/matches/{eventId}/momentum/stats` | providerId | Get match momentum stats |
| `GET /api/livescores/matches/{eventId}/momentum/updates` |  | Get match momentum updates |
| `GET /api/livescores/matches/{eventId}/news` | version | Get match news |
| `GET /api/livescores/matches/{eventId}/news-layout` | layoutTypeId, projectId | Get match news layout |
| `GET /api/livescores/matches/{eventId}/odds-detail` | version | Get match odds detail |
| `GET /api/livescores/matches/{eventId}/overview` | tab, version | Get match tournament table |
| `GET /api/livescores/matches/{eventId}/participants/{participantId}/detail` | version | Get match participant supplementary detail |
| `GET /api/livescores/matches/{eventId}/player-statistics` | projectId | Get match player statistics |
| `GET /api/livescores/matches/{eventId}/player-statistics/detail` | providerId | Get match player statistics detail |
| `GET /api/livescores/matches/{eventId}/player-statistics/updates` | providerId | Get match player statistics updates |
| `GET /api/livescores/matches/{eventId}/point-by-point` | version | Get match point-by-point |
| `GET /api/livescores/matches/{eventId}/report` | version | Get match report |
| `GET /api/livescores/matches/{eventId}/report/html` | version | Get match report (HTML) |
| `GET /api/livescores/matches/{eventId}/stage` | projectId | Get match summary odds form |
| `GET /api/livescores/matches/{eventId}/stats` | version | Get match stats |
| `GET /api/livescores/matches/{eventId}/timeline` | version | Get match live table |
| `GET /api/livescores/matches/{eventId}/top-scorers` | version | Get match top scorers |
| `GET /api/livescores/matches/{eventId}/tv/long` | version | Get match vertical summary |
| `GET /api/livescores/matches/{eventId}/tv/short` | version | Get match horizontal summary |

## navigation

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/navigation/{sportId}/{countryId}` |  | Get navigation by sport/country |

## news

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/news` | sportId*, sectionId, categoryId, version | Get news list |
| `GET /api/livescores/news/articles/{articleId}` |  | Get news article |
| `GET /api/livescores/news/entities/{entityTypeId}/{entityId}` | layoutTypeId, page, perPage, projectId | Get entity news list |

## odds

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/odds` | _hash* | Get odds data |

## participants

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/participants/{participantId}/events` | projectTypeId, projectId, version | Get participant events |
| `GET /api/livescores/participants/{participantId}/events/{eventId}/detail` | projectTypeId, version | Get participant event detail |
| `GET /api/livescores/participants/{participantId}/last-matches` | scope, version | Get participant last matches |
| `GET /api/livescores/participants/{participantId}/matches` | sportId*, categoryId*, lang, version | Get participant matches |
| `GET /api/livescores/participants/{participantId}/news` | version | Get participant news |
| `GET /api/livescores/participants/{participantId}/squad` | path, slug | Get participant squad |
| `GET /api/livescores/participants/{participantId}/transfers` | tab, page, version | Get participant transfers |

## players

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/players/{playerId}/injuries` | path, slug | Get player injuries |
| `GET /api/livescores/players/{playerId}/match-record` | path, slug | Get player match record |
| `GET /api/livescores/players/{playerId}/profile` | projectId, version | Get player profile |
| `GET /api/livescores/players/{playerId}/tournaments-won` | path, slug | Get player tournaments won |

## rankings

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/rankings/resolve` | path, sport, slug | Resolve ranking id |
| `GET /api/livescores/rankings/{rankingId}` | tab, variant, version | Get rankings |
| `GET /api/livescores/rankings/{sport}/{slug}/id` |  | Resolve ranking id by slug |

## remote-stats

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/remote-stats` |  | Get remote stats |

## req

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/req/{req}` |  | Get navigation data |

## search

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/search` | q* | Search entities |

## sports

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/sports/{sportId}/categories` | path | Get sport categories |
| `GET /api/livescores/sports/{sportId}/categories/{categoryId}/tournaments` | projectId, lang, flag, group, version | Get category tournament list |
| `GET /api/livescores/sports/{sportId}/featured` | scope, projectId, lang, group, version | Get sport featured list |
| `GET /api/livescores/sports/{sportId}/odds` | dayOffset, lang, version | Get sport odds list |
| `GET /api/livescores/sports/{sportId}/refresh` | version | Get sport refresh updates |
| `GET /api/livescores/sports/{sportId}/scoreboard` | dayOffset, lang, version | Get sport scoreboard |
| `GET /api/livescores/sports/{sportId}/season-calendar` | projectId | Get season calendar |

## system

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/system/status` | scope, version | Get system status |

## top-search

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/top-search` |  | Top search suggestions |

## tournaments

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/tournaments/archive` | path, sport, country, slug | Get tournament archive |
| `GET /api/livescores/tournaments/resolve` | path, sport, country, slug | Resolve tournament metadata |
| `GET /api/livescores/tournaments/{sportId}/{categoryId}/{templateId}/fixtures` | round*, page, lang, version | Get tournament fixtures |
| `GET /api/livescores/tournaments/{sportId}/{categoryId}/{templateId}/matches` | lang, version | Get tournament matches |
| `GET /api/livescores/tournaments/{sportId}/{categoryId}/{templateId}/results` | segment, projectId, lang, page, group, version | Get tournament results |
| `GET /api/livescores/tournaments/{tournamentId}/draw/{stageId}` | groupId, version | Get tournament draw |
| `GET /api/livescores/tournaments/{tournamentId}/list/{stageId}` | version | Get tournament list |
| `GET /api/livescores/tournaments/{tournamentId}/overview/{stageId}` | tab, version | Get tournament overview |
| `GET /api/livescores/tournaments/{tournamentId}/seasons/{stageId}` | projectId | Get tournament seasons |
| `GET /api/livescores/tournaments/{tournamentId}/tables/{stageId}` | version | Get tournament table |
| `GET /api/livescores/tournaments/{tournamentId}/top-scorers/{stageId}` | version | Get tournament top scorers |

## updates

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/livescores/updates` | sportId*, scope, version | Get updates |
| `GET /api/livescores/updates/counts` | projectId, version | Get update counts |
| `GET /api/livescores/updates/list` | sportId*, projectId, version | Get updates list |
