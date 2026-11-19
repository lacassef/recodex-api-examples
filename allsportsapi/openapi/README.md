# OpenAPI specifications

OpenAPI 3.0 descriptions of every route. Import one into Swagger UI, Postman, Insomnia, or a client generator.

Each file's `servers` URL is the RapidAPI host for that product. Send the same value in `X-RapidAPI-Host`. The All Sports bundle host is `allsportsapi2.p.rapidapi.com`. Single-sport hosts are in the [guide](../README.md). A sport with no separate listing uses the bundle host.

These files list paths, parameters, and the response status. The JSON fields inside a `200` body are described in [Models](../Models/). A `200` schema of "JSON object" means the body is the payload for that route (`events`, `event`, `standings`, and so on). Extra fields may be present.

`204` means the route exists and there is no data for those parameters. The body is empty.

## Which file

| File | Use it when |
|------|-------------|
| `allsports_simplified_openapi.yaml` | You want one file for every sport and your tool has a size limit. Shared segments are enums. 365 paths. |
| `allsports_openapi.yaml` | You want every concrete path written out. 1954 paths. |
| `{sport}_openapi.yaml` | You are building one sport. |

Path counts move when routes are added. The simplified file is the one to import into a marketplace that rejects a very large document.

## Files

| File | Paths |
|------|------:|
| `allsports_openapi.yaml` | 1954 |
| `allsports_simplified_openapi.yaml` | 365 |
| `football_openapi.yaml` | 203 |
| `basketball_openapi.yaml` | 171 |
| `tennis_openapi.yaml` | 130 |
| `american_football_openapi.yaml` | 117 |
| `ice_hockey_openapi.yaml` | 115 |
| `table_tennis_openapi.yaml` | 109 |
| `baseball_openapi.yaml` | 109 |
| `handball_openapi.yaml` | 105 |
| `aussie_rules_openapi.yaml` | 103 |
| `bandy_openapi.yaml` | 103 |
| `beach_volley_openapi.yaml` | 103 |
| `floorball_openapi.yaml` | 103 |
| `futsal_openapi.yaml` | 103 |
| `minifootball_openapi.yaml` | 103 |
| `waterpolo_openapi.yaml` | 103 |
| `cricket_openapi.yaml` | 101 |
| `padel_openapi.yaml` | 100 |
| `esports_openapi.yaml` | 96 |
| `badminton_openapi.yaml` | 94 |
| `darts_openapi.yaml` | 94 |
| `snooker_openapi.yaml` | 94 |
| `rugby_openapi.yaml` | 94 |
| `volleyball_openapi.yaml` | 93 |
| `mma_openapi.yaml` | 77 |
| `cycling_openapi.yaml` | 66 |
| `motorsport_openapi.yaml` | 65 |

`esports_openapi.yaml` documents the public prefix `/api/esport`.

Football paths have no sport slug. Every other file includes the shared routes (search, flags, TV, odds providers) plus that sport's own routes.
