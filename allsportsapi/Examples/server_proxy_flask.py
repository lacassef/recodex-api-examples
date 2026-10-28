"""
Server-side proxy (Python / Flask) that keeps your RapidAPI key SECRET.

Your front-end calls THIS server (no key), and the server adds the auth headers
and forwards the request to AllSportsAPI. The key never reaches the browser.
Works for JSON endpoints AND binary image endpoints (it passes bytes through).

Run:
    export RAPIDAPI_KEY="your_key_here"
    pip install flask requests
    python server_proxy_flask.py

Then from the browser, drop the headers entirely and call your proxy:
    fetch('http://localhost:3000/api/matches/live').then(r => r.json())
    <img src="http://localhost:3000/api/player/3041/image" />
"""

import os

import requests
from flask import Flask, Response, request

HOST = os.environ.get("RAPIDAPI_HOST", "footapi7.p.rapidapi.com")
API_KEY = os.environ.get("RAPIDAPI_KEY")
PORT = int(os.environ.get("PORT", 3000))

if not API_KEY:
    raise SystemExit("Set RAPIDAPI_KEY in your environment first.")

app = Flask(__name__)


@app.route("/api/<path:subpath>")
def proxy(subpath):
    """Forward /api/<subpath> (with query string) to AllSportsAPI."""
    target = f"https://{HOST}/api/{subpath}"
    headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": HOST}

    api_res = requests.get(
        target, headers=headers, params=request.args, timeout=15
    )

    # Mirror the status and content type (JSON or an image).
    response = Response(
        api_res.content,
        status=api_res.status_code,
        content_type=api_res.headers.get("Content-Type", "application/json"),
    )
    # CORS for local front-end development — restrict the origin in production!
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    app.run(port=PORT)
