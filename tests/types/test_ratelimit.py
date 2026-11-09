import datetime

import pytest

from pypricecharting.types import RateLimit


def test_ratelimit_members():
    assert len(RateLimit) == 3
    assert RateLimit.API.value == datetime.timedelta(seconds=1)
    assert RateLimit.CSV.value == datetime.timedelta(minutes=10)
    assert RateLimit.OFFERS_POLLING.value == datetime.timedelta(minutes=5)


def test_ratelimit_raises_for_invalid_value():
    with pytest.raises(ValueError, match="is not a valid"):
        RateLimit(datetime.timedelta(seconds=5))
