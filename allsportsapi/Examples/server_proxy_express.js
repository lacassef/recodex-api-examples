/**
 * Server-side proxy (Node / Express) that keeps your RapidAPI key SECRET.
 *
 * Your front-end calls THIS server (no key), and the server adds the auth headers
 * and forwards the request to AllSportsAPI. The key never reaches the browser.
 * Works for JSON endpoints AND binary image endpoints (it streams bytes through).
 *
 * Run (Node 18+, which has a global fetch):
 *     export RAPIDAPI_KEY="your_key_here"
 *     npm install express
 *     node server_proxy_express.js
 *
 * Then from the browser, drop the headers entirely and call your proxy:
 *     fetch('http://localhost:3000/api/matches/live').then(r => r.json())
 *     <img src="http://localhost:3000/api/player/3041/image" />
 */

const express = require('express');

const HOST = process.env.RAPIDAPI_HOST || 'footapi7.p.rapidapi.com';
const API_KEY = process.env.RAPIDAPI_KEY;
const PORT = process.env.PORT || 3000;

if (!API_KEY) {
  console.error('Set RAPIDAPI_KEY in your environment first.');
  process.exit(1);
}

const app = express();

// Forward every /api/* path (query string included) to AllSportsAPI.
app.get('/api/*', async (req, res) => {
  const target = `https://${HOST}${req.originalUrl}`;
  try {
    const apiRes = await fetch(target, {
      headers: { 'X-RapidAPI-Key': API_KEY, 'X-RapidAPI-Host': HOST },
    });

    // Mirror the status and content type (JSON or an image).
    res.status(apiRes.status);
    const contentType = apiRes.headers.get('content-type');
    if (contentType) res.set('content-type', contentType);

    // CORS for local front-end development — restrict the origin in production!
    res.set('Access-Control-Allow-Origin', '*');

    if (apiRes.status === 204) return res.end();

    const buffer = Buffer.from(await apiRes.arrayBuffer());
    res.send(buffer);
  } catch (err) {
    console.error('API request failed:', err);
    res.status(502).json({ error: 'API request failed' });
  }
});

app.listen(PORT, () => {
  console.log(`Proxy listening on http://localhost:${PORT} → ${HOST}`);
});
