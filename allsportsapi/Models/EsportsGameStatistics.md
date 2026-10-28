# EsportsGameStatistics (Esports)

**EsportsGameStatistics** holds one team's stats for a single game/map of a MOBA‑style
esports match (the fields map to *League of Legends*‑type objectives): kills, gold
earned, structures destroyed (towers, inhibitors, barracks), neutral objectives
(dragons by element, Baron Nashor, Rift Herald), `firstBlood` and champion `bans`. One
match is made of several games; each game has a home and an away statistics object —
see [EsportsGameStatisticsResponse](EsportsGameStatisticsResponse.md).

**Where you'll see it:** esports match‑statistics endpoints.

**Related models:** [EsportsGameStatisticsResponse](EsportsGameStatisticsResponse.md) ·
[Event](Event.md).

## Properties

- **bans** (`array of ESportCharacter`):
    - A list of characters that were banned during the match, representing the characters that teams chose to prohibit from being played.

- **barracksDestroyed** (`number`):
    - The number of enemy barracks (structures) that were destroyed by this team.

- **barracksRemaining** (`number`):
    - The number of barracks that remain intact for this team by the end of the match.

- **chemtechDrakeKills** (`number`):
    - The number of Chemtech Drakes (a type of dragon) that this team killed during the match.

- **cloudDrakeKills** (`number`):
    - The number of Cloud Drakes killed by this team during the match.

- **dragonKills** (`number`):
    - The total number of dragons of all types that this team killed during the match.

- **elderDrakeKills** (`number`):
    - The number of Elder Drakes (a powerful dragon) that this team killed during the match.

- **firstBlood** (`boolean`):
    - A flag indicating whether this team achieved the first blood (the first kill) in the match.

- **goldEarned** (`number`):
    - The total amount of gold earned by this team throughout the match.

- **heraldKilled** (`boolean`):
    - A flag indicating whether this team killed the Rift Herald (a powerful neutral monster) during the match.

- **hextechDrakeKills** (`number`):
    - The number of Hextech Drakes killed by this team during the match.

- **infernalDrakeKills** (`number`):
    - The number of Infernal Drakes killed by this team during the match.

- **inhibitorKills** (`number`):
    - The number of enemy inhibitors (key structures) that this team destroyed during the match.

- **kills** (`number`):
    - The total number of kills achieved by this team during the match.

- **mountainDrakeKills** (`number`):
    - The number of Mountain Drakes killed by this team during the match.

- **nashorKills** (`number`):
    - The number of Baron Nashor kills achieved by this team during the match.

- **oceanDrakeKills** (`number`):
    - The number of Ocean Drakes killed by this team during the match.

- **towerKills** (`number`):
    - The total number of towers (defensive structures) that this team destroyed during the match.

- **towersDestroyed** (`number`):
    - The number of enemy towers that were destroyed by this team.

- **towersRemaining** (`number`):
    - The number of towers that remain standing for this team by the end of the match.