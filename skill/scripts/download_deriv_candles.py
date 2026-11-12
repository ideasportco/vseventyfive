#!/usr/bin/env python3
"""Download historical candles from Deriv's public WebSocket API for research.

This script only requests candle history; it does not place or manage trades.
Verify the current API endpoint, app ID requirements, symbol name, and data-use
terms before use. Never put account credentials in this file.
"""
import argparse
import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import websockets
except ImportError:
    sys.exit("Install dependency: python -m pip install websockets")

DEFAULT_URL = "wss://ws.derivws.com/websockets/v3?app_id=1089"

async def fetch(url: str, symbol: str, count: int, granularity: int):
    async with websockets.connect(url, open_timeout=20, close_timeout=5) as ws:
        request = {
            "ticks_history": symbol,
            "adjust_start_time": 1,
            "count": count,
            "end": "latest",
            "granularity": granularity,
            "style": "candles",
        }
        await ws.send(json.dumps(request))
        response = json.loads(await ws.recv())
        if response.get("error"):
            raise RuntimeError(response["error"].get("message", "Unknown API error"))
        candles = response.get("candles")
        if not isinstance(candles, list):
            raise RuntimeError(f"Unexpected response: {response.keys()}")
        return candles

async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbol", default="R_75", help="Deriv API symbol; confirm current V75 symbol")
    parser.add_argument("--count", type=int, default=5000)
    parser.add_argument("--granularity", type=int, default=300, help="Candle seconds; 300 = M5")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--out", default="v75_m5_candles.json")
    args = parser.parse_args()
    if not (1 <= args.count <= 5000):
        parser.error("--count must be between 1 and 5000")
    if args.granularity <= 0:
        parser.error("--granularity must be positive")
    try:
        candles = await fetch(args.url, args.symbol, args.count, args.granularity)
    except Exception as exc:
        sys.exit(f"Candle request failed: {exc}")
    result = {
        "source": "Deriv public WebSocket candle-history request",
        "symbol": args.symbol,
        "granularity_seconds": args.granularity,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "count": len(candles),
        "limitations": [
            "Historical prices are not proof of executable quotes or fills.",
            "Check symbol mapping, API terms, timestamps, missing intervals, and feed changes.",
            "This script does not submit orders.",
        ],
        "candles": candles,
    }
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {len(candles)} candles to {args.out}")

if __name__ == "__main__":
    asyncio.run(main())
