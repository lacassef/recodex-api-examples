# FeedResponse

A **FeedResponse** is one normalized feed. `records` is the list. Each record's `fields` holds the decoded names. A value is a string, or an array when the feed stored a list.

**Where you'll see it:** `/feed/{version}/{feed}`, the sport scoreboard, refresh, odds, and featured routes, and the match and tournament feeds that return `FeedResponse`.

**Related models:** [ReqResponse](ReqResponse.md) uses the same record. The id you carry next is `sharedindexes_event_id`.

### Example (one scoreboard row)

Ids in this example belong to the example. `08W6fzLP` is an event id from the [examples](../guides/examples.md).

```json
{
  "version": "2",
  "feed": "f_1_0_2_en_1",
  "header": {},
  "records": [
    {
      "fields": {
        "sharedindexes_event_id": "08W6fzLP",
        "sharedindexes_sport_id": "1",
        "home_name": "Home",
        "away_name": "Away",
        "sharedindexes_home_current_result": "1",
        "sharedindexes_away_current_result": "0",
        "country_id": "98",
        "tournament_template_id": "COuk57Ci"
      }
    }
  ]
}
```

A row can omit a field. Other feeds add other keys under `fields`. Match-detail feeds use the same envelope and their own field names.

## Properties

- **version** (`string`):
    - The feed version, such as `2`.

- **feed** (`string`):
    - The feed name that produced this body.

- **header** (`object`):
    - Decoded header fields. Keys are dynamic.

- **records** (`array of FeedRecord`):
    - One entry per row.

- **records[].fields** (`object`):
    - Decoded field names. Values are strings or arrays of strings.

## Scoreboard fields

These names show up on a match list. They are keys inside `fields`, not siblings of `records`.

- **sharedindexes_event_id** (`string`):
    - The `eventId` for match routes.

- **sharedindexes_match_start_utime** (`string`):
    - Scheduled start time.

- **home_name** (`string`), **away_name** (`string`):
    - The two side names.

- **sharedindexes_home_current_result** (`string`), **sharedindexes_away_current_result** (`string`):
    - The current score.

- **sharedindexes_home_full_time_result** (`string`), **sharedindexes_away_full_time_result** (`string`):
    - The full-time score.

- **marked_as_live** (`string`):
    - Whether the row is live.

- **sharedindexes_home_red_card_count** (`string`), **sharedindexes_away_red_card_count** (`string`):
    - Red-card counts.

- **sharedindexes_sport_id** (`string`):
    - The sport id. See [Sport ids](../reference/sport-ids.md).

- **sharedindexes_tournament_name** (`string`):
    - The competition name on the row.

- **country_name** (`string`), **country_id** (`string`):
    - The country on the row.

- **tournament_id** (`string`):
    - `tournamentId` on tournament routes.

- **sharedindexes_tournament_stage_id** (`string`):
    - `stageId` on tournament routes.

- **tournament_template_id** (`string`):
    - `templateId` for matches, fixtures, and results.
