# Best practices

Send the parameters the operation lists in the OpenAPI. The rest of this page is what to leave out.

## Omit the usual values

Do not send a parameter whose omitted value is already the one you want.

- Omit `langId` for the default language. Omit `userCountryId` for the default country.
- Omit `publisherId` and `campaign` when you do not have them.
- Omit `timezone` when you do not need a zone. When you send one, use an IANA name.
- Omit `showOdds` when you do not want odds.
- Omit `promoteNational` to leave national teams unpromoted.
- Omit `appType` on play-by-play for the default.
- Omit `lastUpdateId` for a full response. Send the previous `lastUpdateId` when you are polling.
- Omit `isPreview` on news for the full list.

Send the parameter when you want a different value. Do not send an empty value.

## One id, from the previous response

Take the id from the list you just received and send the name the next operation uses. Do not send `competitorId` to a route that lists `competitor` or `competitorIds`.

Refresh a list with `lastUpdateId`. Send `competitionsLimit` on the first call, and the cursor on the refresh.

`roundKey` `0` is a real round. Send it when that is the round you want.

## Dates

Send the locale short pattern, such as `30/09/2026` for `langId` `31` or `10`. Do not send a timestamp.

## Paging

Pass `paging.nextPage` or `paging.previousPage` through as `paging`. Do not rebuild that string.

## Images

Use the `imageVersion` from the entity. The flag and the trophy have no version. Prefer the light competition routes for the logo in a list.

## What you do not send

No request body. No account cookie. No token. Image routes are `GET` and return `image/png`.
