# Bracket

A **Bracket** is one knockout draw.

**Where you'll see it:** the brackets route. Send `competition`, or `competitor` for one side's draw.

**Related models:** [Competition](Competition.md). The body also includes the competitions and bookmakers the draw references.

This page does not name the keys inside `stages`.

## Properties

- **name** (`string`):
    - Bracket name.

- **title** (`string`):
    - Title.

- **competitionId** (`number`):
    - Competition the draw belongs to.

- **stages** (`array`):
    - Stages in the draw.

- **knockoutTitle** (`string`):
    - Knockout title.
