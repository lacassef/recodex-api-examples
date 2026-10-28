# OpenAPI specifications

OpenAPI 3.0 descriptions of every route. Import one into Swagger UI, Postman, Insomnia, or a client generator.

The `servers` entry is `https://{host}`. Set `host` to the marketplace host you subscribed to, and send that same value in `X-RapidAPI-Host`. The default host is the All Sports bundle.

These files list paths, parameters, and the response status. The JSON fields inside a `200` body are described in [Models](../Models/). A `200` schema of "JSON object" means the body is the payload for that route (`events`, `event`, `standings`, and so on). Extra fields may be present.

`204` means the route exists and there is no data for those parameters. The body is empty.

## Which file

| File | Use it when |
|------|-------------|
| `allsports_simplified_openapi.yaml` | You want one file for every sport and your tool has a size limit. Shared segments are enums. 353 paths. |
| `allsports_openapi.yaml` | You want every concrete path written out. 1978 paths. |
| `{sport}_openapi.yaml` | You are building one sport. |

Path counts move when routes are added. The simplified file is the one to import into a marketplace that rejects a very large document.

## Files

| File | Paths |
|------|------:|
| `allsports_openapi.yaml` | 1978 |
| `allsports_simplified_openapi.yaml` | 353 |
| `football_openapi.yaml` | 205 |
| `basketball_openapi.yaml` | 172 |
| `tennis_openapi.yaml` | 131 |
| `american_football_openapi.yaml` | 118 |
| `ice_hockey_openapi.yaml` | 116 |
| `table_tennis_openapi.yaml` | 110 |
| `baseball_openapi.yaml` | 110 |
| `handball_openapi.yaml` | 106 |
| `aussie_rules_openapi.yaml` | 104 |
| `bandy_openapi.yaml` | 104 |
| `beach_volley_openapi.yaml` | 104 |
| `floorball_openapi.yaml` | 104 |
| `futsal_openapi.yaml` | 104 |
| `minifootball_openapi.yaml` | 104 |
| `waterpolo_openapi.yaml` | 104 |
| `cricket_openapi.yaml` | 102 |
| `padel_openapi.yaml` | 101 |
| `esports_openapi.yaml` | 97 |
| `badminton_openapi.yaml` | 95 |
| `darts_openapi.yaml` | 95 |
| `snooker_openapi.yaml` | 95 |
| `rugby_openapi.yaml` | 95 |
| `volleyball_openapi.yaml` | 94 |
| `mma_openapi.yaml` | 77 |
| `cycling_openapi.yaml` | 66 |
| `motorsport_openapi.yaml` | 65 |

`esports_openapi.yaml` documents the public prefix `/api/esport`.

Football paths have no sport slug. Every other file includes the shared routes (search, flags, TV, odds providers) plus that sport's own routes.
