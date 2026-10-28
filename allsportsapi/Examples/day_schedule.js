/**
 * Matches for one competition-sized day.
 *
 * 1. Page through scheduled-tournaments (page starts at 1) until hasNextPage is false.
 * 2. Keep competitions whose timezoneEventCount for TZ_OFFSET is greater than 0.
 * 3. Load that competition's matches. The id is tournament.uniqueTournament.id.
 *
 * Football, cricket, tennis, and esports use scheduled-events/{YYYY-MM-DD}.
 * Esports has that form only. Other team sports use
 * /api/{sport}/tournament/{id}/schedules/{day}/{month}/{year}.
 *
 * Run (Node 18+):
 *     export RAPIDAPI_KEY="your_key_here"
 *     node day_schedule.js
 *
 *     DAY=29 MONTH=9 YEAR=2026 TZ_OFFSET=0 node day_schedule.js
 *     RAPIDAPI_HOST=volleyballapi.p.rapidapi.com SPORT_PREFIX=/volleyball node day_schedule.js
 */

const HOST = process.env.RAPIDAPI_HOST || 'footapi7.p.rapidapi.com';
const API_KEY = process.env.RAPIDAPI_KEY;
const SPORT_PREFIX = process.env.SPORT_PREFIX || '';
const DAY = Number(process.env.DAY || 29);
const MONTH = Number(process.env.MONTH || 9);
const YEAR = Number(process.env.YEAR || 2026);
const TZ_OFFSET = process.env.TZ_OFFSET || '0';

async function get(path) {
  if (!API_KEY) {
    console.error('Set RAPIDAPI_KEY in your environment first.');
    process.exit(1);
  }
  const headers = { 'X-RapidAPI-Key': API_KEY, 'X-RapidAPI-Host': HOST };
  const res = await fetch(`https://${HOST}${path}`, { headers });
  if (res.status === 204) return null;
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${path}`);
  return res.json();
}

async function* scheduledTournaments() {
  let page = 1;
  for (;;) {
    const data = await get(
      `/api${SPORT_PREFIX}/scheduled-tournaments/${DAY}/${MONTH}/${YEAR}/page/${page}`,
    );
    if (!data) return;
    for (const row of data.scheduled ?? []) yield row;
    if (!data.hasNextPage) return;
    page += 1;
  }
}

// Esports publishes the ISO date form only. Football, cricket, and tennis publish both.
const ISO_DATE = new Set(['', '/cricket', '/esport', '/tennis']);

async function eventsFor(uniqueTournamentId) {
  const iso = `${String(YEAR).padStart(4, '0')}-${String(MONTH).padStart(2, '0')}-${String(DAY).padStart(2, '0')}`;
  const path = ISO_DATE.has(SPORT_PREFIX)
    ? `/api${SPORT_PREFIX}/tournament/${uniqueTournamentId}/scheduled-events/${iso}`
    : `/api${SPORT_PREFIX}/tournament/${uniqueTournamentId}/schedules/${DAY}/${MONTH}/${YEAR}`;
  const data = (await get(path)) ?? {};
  return data.events ?? [];
}

async function main() {
  let kept = 0;
  for await (const row of scheduledTournaments()) {
    const counts = row.timezoneEventCount ?? {};
    if (Number(counts[TZ_OFFSET] || 0) <= 0) continue;
    const tournament = row.tournament ?? {};
    const unique = tournament.uniqueTournament ?? {};
    if (unique.id == null) continue;
    const events = await eventsFor(unique.id);
    kept += 1;
    console.log(`\n${unique.name || tournament.name} (${events.length} events)`);
    for (const ev of events) {
      const home = ev.homeTeam?.name ?? '?';
      const away = ev.awayTeam?.name ?? '?';
      const status = ev.status?.description ?? '';
      console.log(`  ${ev.id}  ${home} vs ${away}  ${status}`);
    }
  }
  console.log(`\n${kept} competitions for offset ${TZ_OFFSET}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
