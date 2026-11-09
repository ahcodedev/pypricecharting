import pytest

from pypricecharting.types import Rating


def test_rating_members():
    assert len(Rating) == 5
    assert Rating.GREAT.value == 2
    assert Rating.GOOD.value == 1
    assert Rating.OK.value == 0
    assert Rating.BAD.value == -1
    assert Rating.AWFUL.value == -2


def test_rating_lookup_by_value():
    for member in Rating:
        assert Rating(member.value) is member


def test_rating_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Rating(3)
