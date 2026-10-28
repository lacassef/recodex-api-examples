# Feeds and scoreboards

Filled calls are in [Examples](../guides/examples.md). The order of calls is in [Workflows](../guides/workflows.md).

## Feed endpoint

GET `/api/livescores/feed/{version}/{feed}`

Parameters:

- `version` (path, required)
- `feed` (path, required)

Response: `FeedResponse`

Feed names are in [Feed names](feed-patterns.md). When a named route exists, call that route.

## Common match list fields

Match list feeds commonly include these decoded fields:

- `sharedindexes_event_id` (`eventId`)
- `sharedindexes_match_start_utime` (scheduled start time)
- `home_name`, `away_name`
- `sharedindexes_home_current_result`, `sharedindexes_away_current_result`
- `sharedindexes_home_full_time_result`, `sharedindexes_away_full_time_result`
- `marked_as_live`
- `sharedindexes_home_red_card_count`, `sharedindexes_away_red_card_count`
- `sharedindexes_sport_id`
- `sharedindexes_tournament_name`
- `country_name`, `country_id`
- `tournament_id`
- `sharedindexes_tournament_stage_id`
- `tournament_template_id`

## Sport scoreboard

GET `/api/livescores/sports/{sportId}/scoreboard`

Parameters:

- `sportId` (path, required)
- `dayOffset` (query, omit for today)
- `lang` (query, omit for `en`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Sport refresh

GET `/api/livescores/sports/{sportId}/refresh`

Parameters:

- `sportId` (path, required)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Sport odds list

GET `/api/livescores/sports/{sportId}/odds`

Parameters:

- `sportId` (path, required)
- `dayOffset` (query, omit for today)
- `lang` (query, omit for `en`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Sport featured

GET `/api/livescores/sports/{sportId}/featured`

Parameters:

- `sportId` (path, required)
- `scope` (query, omit for `0`)
- `projectId` (query, omit for `2`)
- `lang` (query, omit for `en`)
- `group` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `FeedResponse`
