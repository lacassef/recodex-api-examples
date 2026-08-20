# Contributing

This repository is the public docs and examples hub for Recodex sports APIs. Useful contributions are extra examples, clearer docs, and OpenAPI fixes.

## Examples

Add a pair of files under `allsportsapi/Examples/` (Python and Node when both apply):

1. Read the key from `RAPIDAPI_KEY`. Never hard-code secrets.
2. Send `X-RapidAPI-Key` and `X-RapidAPI-Host`.
3. Handle `200`, `204`, `429`, and `5xx` the same way as `quickstart.py`.
4. Link the new files from `allsportsapi/Examples/README.md` and the root `README.md`.

Sport-specific demos belong in `allsportsapi/Footapi/`, `Basketapi/`, or `Tennisapi/`.

## Docs and OpenAPI

- Keep the category → unique tournament → season → event tree consistent with `allsportsapi/README.md`.
- If you change a path or schema, update the matching file in `allsportsapi/openapi/`.
- Prefer small, copy-paste snippets over new dependencies.

## Questions

- Bugs in examples or docs: open an [issue](https://github.com/lacassef/recodex-api-examples/issues).
- How do I call endpoint X: use [Discussions](https://github.com/lacassef/recodex-api-examples/discussions).
- Keys, quotas, and billing: RapidAPI dashboard for the API you subscribed to.

## Listing this repo (maintainers)

The GitHub URL to paste on every marketplace page:

`https://github.com/lacassef/recodex-api-examples`

Suggested one-liner:

```text
OpenAPI specs and Python/JavaScript examples (live scores, fixtures, standings, odds, shotmaps):
https://github.com/lacassef/recodex-api-examples
```

Paste it in:

- RapidAPI → each API (AllSportsAPI, FootAPI, TennisAPI, …) → About / Website / long description
- [API.market AllSportsAPI](https://api.market/store/recodex/allsportsapi)

Social preview (GitHub has no API for this): repo **Settings → Social preview → Upload** → `.github/social-preview.png`.
