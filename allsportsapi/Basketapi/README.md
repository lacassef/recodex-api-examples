# Basketball Examples

Examples for the [Basketball API (basketapi1)](https://rapidapi.com/fluis.lacasse/api/basketapi1/)
focused on **shot data**: plotting a shotmap, building a shot‑density heatmap, and
classifying shots into court zones.

| File | What it does |
|------|--------------|
| [`basketball-shotmap.py`](basketball-shotmap.py) | Draws a half‑court with Matplotlib, plots made/missed/saved shots, and renders a shot‑density heatmap on the same court coordinates (NumPy). |
| [`PlayerShotActionAreas.md`](PlayerShotActionAreas.md) | Explains how to classify a shot's `(x, y)` into a named court zone (corner three, top of the key, paint, …). |

---

## Endpoints

| Data | Endpoint |
|------|----------|
| Team shotmap (match) | `GET /api/basketball/match/{id}/team/{teamId}/shotmap` |
| Player shotmap (match) | `GET /api/basketball/match/{id}/player/{playerId}/shotmap` |
| Player shot‑action areas (season) | `GET /api/basketball/player/{id}/tournament/{tournamentId}/season/{seasonId}/shot-actions/{regularSeason\|playoffs}` |
| Tournament shot‑action areas (season) | `GET /api/basketball/tournament/{tournamentId}/season/{seasonId}/shot-actions/areas/{regularSeason\|playoffs}` |

Host: `basketapi1.p.rapidapi.com` (or `allsportsapi2.p.rapidapi.com` with the bundle path).

---

## Shot data shape

Both routes return `{ "shotmap": [ ... ] }`. Pass that array to `plot_shotmap()`. `shots_from_body()` reads it for you. A `204` is an empty body.

The team route aggregates every attempt at one spot:

```json
{ "x": -233, "y": -2, "made": 1, "missed": 1, "saved": 0 }
```

| Field | Meaning |
|-------|---------|
| `x` | Horizontal position. `0` is the basket; negative = left, positive = right. |
| `y` | Distance from the basket toward half‑court. Slightly negative means just behind the rim. |
| `made` / `missed` / `saved` | How many attempts at that spot ended that way. |

The player route is one attempt per item, not those counts:

```json
{ "x": -40, "y": 8, "type": 1, "typeName": "made", "isHome": false, "id": 19548784, "period": "2Q" }
```

`type` `1` and `typeName` `"made"` are a made shot. `type` `0` and `"missed"` are a miss. There is no `made` / `missed` / `saved` on this object.

### Coordinate system

The example uses a hoop‑centred court:

- **Origin `(0, 0)` is the basket.** The backboard is drawn at `y = -7.5`.
- `x` runs roughly **‑250 … 250**.
- `y` grows from the basket toward half‑court. The axis in the example is **‑50 … 470**, so the hoop and shots with a small negative `y` stay on the chart.
- The three‑point arc sits at radius ≈ **238** (`x² + y² >= 56644`). Corner threes are `x <= -219` and `y < 89`, or `x >= 219` and `y < 89`.

These same thresholds drive the zone classification in
[`PlayerShotActionAreas.md`](PlayerShotActionAreas.md). `TOP_MIDDLE` is the middle of the arc. `CENTER_MIDDLE` is the middle of the paint. They are different zones.

---

## Running the Python example

```bash
pip install matplotlib numpy
python basketball-shotmap.py
```

`basketball-shotmap.py` ships with sample team shots and two views:

1. **Shotmap** — made shots in green, missed in red, saved in blue, over a half‑court. A spot with more than one outcome draws each marker.
2. **Heatmap** — a 2‑D histogram on the same court axes (`x` −250…250, `y` −50…470), with the court drawn on top. Team cells are weighted by `made + missed + saved`.

```python
import os, requests

headers = {
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": "basketapi1.p.rapidapi.com",
}
url = "https://basketapi1.p.rapidapi.com/api/basketball/match/{id}/team/{teamId}/shotmap"
res = requests.get(url, headers=headers, timeout=15)
shots = [] if res.status_code == 204 else shots_from_body(res.json())
plot_shotmap(shots)
```

The player route uses the same functions. `shots_from_body` reads `shotmap` from the 200 body.

---

## Classifying shots into zones

See [`PlayerShotActionAreas.md`](PlayerShotActionAreas.md) for the full algorithm. In
short: check the corner‑three regions first, then use the distance from the basket to
separate two‑pointers from three‑pointers, then split each band left/centre/right. This
turns raw `(x, y)` coordinates into human‑readable zones (e.g. *top‑left outside*,
*centre middle*, *bottom right*) for aggregations and labelled charts.

---

## Notes & best practices

- **Keep your API key server‑side** — never embed it in client code (see the
  [root README](../README.md) and [FAQ](../FAQ.md)).
- Cache finished‑match shotmaps; they don't change after the game ends.
- Season "shot‑action areas" endpoints are pre‑aggregated by zone — handy when you want
  shooting splits without computing them yourself.
