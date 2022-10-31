"""Functions to get trade data."""
import requests


def trade(trade_id=None):
    """Get a single trade from thetagang.com."""
    resp = requests.get(f"https://api.thetagang.com/trades/{trade_id}")
    print(resp.status_code)
    if resp.status_code == requests.codes.ok:
        return resp.json()["data"]["trade"]

    return None
