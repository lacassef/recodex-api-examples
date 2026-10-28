# CategoriesResponse

Categories for one sport, grouped into sections. `sections[].categories[].id` is the `categoryId` you send on tournament and participant routes.

**Where you'll see it:** `/sports/{sportId}/categories`.

**Related models:** [TournamentResolveResponse](TournamentResolveResponse.md).

### Example

`98` is the category id from the [examples](../guides/examples.md).

```json
{
  "sportId": 1,
  "path": "football",
  "sections": [
    {
      "name": "Section",
      "url": "football",
      "categories": [
        { "id": 98, "name": "Category", "url": "football/england", "sportId": 1 }
      ]
    }
  ]
}
```

## Properties

- **sportId** (`number`):
    - The sport you asked for.

- **path** (`string`):
    - The path this catalog was built for.

- **sections** (`array of CategorySection`):
    - Groups of categories.

- **sections[].name** (`string`):
    - The section label.

- **sections[].url** (`string`):
    - The section path.

- **sections[].categories** (`array of CategoryItem`):
    - The categories in that section.

- **categories[].id** (`number`):
    - `categoryId`.

- **categories[].name** (`string`):
    - The category label.

- **categories[].url** (`string`):
    - The category path.

- **categories[].sportId** (`number`):
    - The sport id on that category.
