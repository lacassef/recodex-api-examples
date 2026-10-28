# UniqueStage

A **UniqueStage** represents a stage of a competition — for example a round, phase or
leg within a larger event structure. It is most relevant to sports organised in stages
(such as motorsport) and carries its own identity, name and branding colors.

**Where you'll see it:** stage‑based competitions and their season/standings endpoints.

**Related models:** [Category](Category.md) · [UniqueTournament](UniqueTournament.md) ·
[Tournament](Tournament.md).

## Properties

- **category** (`Category`):
    - The category or division to which the stage belongs, such as a particular round or level within a tournament.

- **id** (`number`):
    - A unique identifier for the stage.

- **name** (`string`):
    - The official name of the stage. This could refer to the stage's round name, like "Quarterfinals" or "Group Stage".

- **primaryColorHex** (`string`):
    - The primary color of the stage, represented as a hexadecimal color code. This color may be used for branding, visual representation, or theming specific to this stage.

- **secondaryColorHex** (`string`):
    - The secondary color of the stage, also represented as a hexadecimal color code. This complements the primary color in the stage's visual identity.

- **slug** (`string`):
    - A URL-friendly identifier for the stage, often used in web applications for routing or identifying the stage in a readable manner.