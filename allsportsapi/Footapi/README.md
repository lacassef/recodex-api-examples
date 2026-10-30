# Football / Soccer Examples

Self‑contained, browser‑ready visualizations built on the
[Football API (footapi7)](https://rapidapi.com/fluis.lacasse/api/footapi7/). Each file
ships with **sample data** so you can open it directly, and shows how to swap in **live
data** from the API.

| File | What it does |
|------|--------------|
| [`football_shotmap.html`](football_shotmap.html) | Renders a match or player **shotmap** on the attacking third: every shot placed from `draw`, sized by xG (when available), colored by outcome, with a line to the block or the goal line. Includes an API loader. |
| [`football_heatmap.html`](football_heatmap.html) | Renders a positional **heatmap** (D3.js) over a pitch image, with live radius/opacity controls and an API loader for player, team, and season heatmaps. |
| [`soccer_field.png`](soccer_field.png) | Pitch background used by the heatmap. |

---

## Shotmap

### Endpoints

| Data | Endpoint |
|------|----------|
| Whole‑match shotmap | `GET /api/match/{id}/shotmap` |
| Single player's shots | `GET /api/match/{id}/player/{playerId}/shotmap` |
| One goalkeeper's shots | `GET /api/match/{id}/player/{playerId}/goalkeeper-shotmap` |

Host: `footapi7.p.rapidapi.com` (or `allsportsapi2.p.rapidapi.com` with the bundle path).

The match and the player shotmap routes return `{ "shotmap": [ ... ] }`. A `204` is an empty body: the route is valid and this match has no shots. Do not parse JSON. The goalkeeper route is a separate body for that goalkeeper.

### Response shape (per shot)

Each entry in `shotmap[]` describes one shot:

| Field | Meaning |
|-------|---------|
| `player` | The shooter ([Player](../Models/Player.md), trimmed). |
| `isHome` | `true` = home team, `false` = away. |
| `shotType` | Outcome: `goal`, `save`, `post`, `miss`, `block`. |
| `goalType` | On a goal: `regular`, `penalty`, or `own`. Absent otherwise. |
| `situation` | Build‑up, with hyphens: `regular`, `assisted`, `set-piece`, `corner`, `fast-break`, `free-kick`, `penalty`. |
| `bodyPart` | `left-foot`, `right-foot`, `head`, `other`. |
| `playerCoordinates` | Where the shot was taken: `{x, y, z}`. |
| `goalMouthCoordinates` | Where it met the goal: `{x, y, z}`. `x` is usually `0`. `y` runs across the goal, 0–100 (right‑to‑left from the shooter's view). `z` is the height, 0–100. |
| `goalMouthLocation` | A label for that point, such as `low-left`, `low-centre`, `high`, `close-left`. |
| `blockCoordinates` | `{x, y, z}` where a save or a block stopped the shot. Absent on a goal or a clean miss. |
| `draw` | Points already laid out for the attacking‑third graphic. See below. |
| `xg`, `xgot` | Expected Goals and Expected Goals on Target (present when the match has xG coverage). |
| `time`, `addedTime` | Minute of the shot. |
| `incidentType` | `shot`. |
| `goalkeeper` | The goalkeeper, on some shots. |

### Coordinates

Plot `draw`, not a fresh conversion of `playerCoordinates`.

The graphic is the attacking third. `x` runs 0–100 across the pitch. `y` is `0` on the goal line and grows to about 35. The goal is at the top.

| `draw` point | Meaning |
|--------------|---------|
| `start` | The shot. `start.x` = `playerCoordinates.y`. `start.y` = `playerCoordinates.x`. |
| `block` | Present when the shot is saved or blocked. `block.x` = `blockCoordinates.y`. `block.y` = `blockCoordinates.x`. |
| `end` | The goal line, so `end.y` is `0`. `end.x` = `100 - goalMouthCoordinates.y`. |
| `goal` | A separate picture of the goal mouth. `goal.x` matches `end.x`. `goal.y` = `100 - goalMouthCoordinates.z` (about 0–100). Do not plot `goal` on the 35‑deep pitch. |

Place the marker at `start`. Draw the line to `block` when that point exists, otherwise to `end`. In pixels, with the pitch box at `PITCH_X = 100` and `PITCH_Y = 35`:

```text
left = draw.start.x / 100 * width
top  = draw.start.y / 35  * height
```

Marker size follows `xg` when present (and uses a fixed default size when `xg` is absent). Color follows `shotType` (green = goal, amber = save, red = post, grey = block, white = miss).

If `draw` is missing, build the same points by swapping axes: start is `{x: playerCoordinates.y, y: playerCoordinates.x}`, block is the same swap of `blockCoordinates`, and end is `{x: 100 - goalMouthCoordinates.y, y: 0}`.

### Try it with live data

1. Open `football_shotmap.html` in a browser — it renders the bundled sample immediately.
2. Paste your **RapidAPI key**, a **Match ID** (e.g. `14015387`), and optionally a **Player ID**, then click **Load Shots**.
3. On any error it falls back to the sample data (and tells you in the status line).

> Find a Match ID from any schedule/live endpoint (`event.id`).

---

## Heatmap

### Endpoints

| Data | Endpoint |
|------|----------|
| Player positions in a match | `GET /api/match/{id}/player/{playerId}/heatmap` |
| Team positions in a match | `GET /api/match/{id}/team/{teamId}/heatmap` |
| Player positions across a season | `GET /api/player/{id}/tournament/{tournamentId}/season/{seasonId}/heatmap` |

The three bodies are different. `x` and `y` are 0–100 on the full pitch in every case. Check `hasEventPlayerHeatMap` on the event before requesting a player or team map.

| Route | 200 body |
|-------|----------|
| Player, one match | `{ "heatmap": [ { "x", "y" } ] }` |
| Team, one match | `{ "playerPoints": [ { "x", "y" } ], "goalkeeperPoints": [ { "x", "y" } ] }` |
| Player, one season | `{ "points": [ { "x", "y", "count" } ], "matches": 0, "events": [ ] }` |

A team map is both arrays together. `playerPoints` and `goalkeeperPoints` have no `count`: each point is one visit, and `x` can be fractional. A season map already sets `count` (how many times the player was at that `x`, `y`). `matches` is an integer. `events` is the list of matches behind the map. Sum `count` when the same `x`, `y` appears more than once. Do not drop `count` and recount the rows.

### How the demo works

`football_heatmap.html` uses **D3.js v6**. `pointsFromPayload()` accepts a bare `{x, y}` list or any of the three bodies above, and `setHeatmapData(body)` binds and renders the circles. The script:

1. Reads `count` when the point has one, otherwise treats the point as one visit, then sums visits that share `x` and `y`.
2. Draws one circle per location over [`soccer_field.png`](soccer_field.png). Both axes are 0–100. SVG `y` grows downward, so the pitch is flipped: `cx = x/100 * width`, `cy = height − y/100 * height`.
3. Lets you tune **radius** and **opacity** with the sliders, or load live data for any of the three heatmap routes.

To use live data in your own code, fetch one of the heatmap endpoints from your backend and pass the 200 body to `setHeatmapData(body)` (or `pointsFromPayload(body)`). A `204` means that match has no map.

---

## Notes & best practices

- **Keep your API key server‑side.** These HTML files prompt for a key only so you can
  experiment locally — in production, proxy the request through your backend (see the
  [root README](../README.md) and [FAQ](../FAQ.md)).
- Shotmaps/heatmaps are available only for matches with that coverage — check the event
  flags (`hasEventPlayerHeatMap`, `hasXg`) on the [Event](../Models/Event.md) first.
- Cache match shotmaps/heatmaps once a match has finished; they no longer change.
