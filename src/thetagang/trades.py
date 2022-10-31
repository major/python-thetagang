"""Functions to get trade data."""
from __future__ import annotations

import requests


def trade(trade_id: str = "") -> dict[str, str]:
    """Get a single trade from thetagang.com."""
    resp = requests.get(f"https://api.thetagang.com/trades/{trade_id}")
    print(resp.status_code)
    if resp.status_code != requests.codes.ok:
        raise requests.exceptions.HTTPError("Unable to retrieve trade")

    return dict(resp.json()["data"]["trade"])
