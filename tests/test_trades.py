"""Test the trade functions."""
import responses
from unittest.mock import patch

from thetagang import trades


@responses.activate
def test_trade_valid():
    """Test retrieving a valid trade."""
    trade_id = "86be322e-e7c7-44dc-a589-f8e0ac4ecf3a"
    expected = {"data": {"trade": {"guid": trade_id}}}
    responses.add(
        responses.GET,
        f"https://api.thetagang.com/trades/{trade_id}",
        json=expected,
        status=200,
    )
    result = trades.trade(trade_id)
    assert isinstance(result, dict)


@responses.activate
def test_trade_invalid():
    """Test retrieving an invalid trade."""
    trade_id = "this-would-never-exist"
    responses.add(
        responses.GET,
        f"https://api.thetagang.com/trades/{trade_id}",
        status=404,
    )
    result = trades.trade(trade_id)
    assert result is None
