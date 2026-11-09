import pytest

from pypricecharting.types import State


def test_state_members():
    assert len(State) == 1
    assert State.ON.value == "on"


def test_state_lookup_by_value():
    assert State("on") is State.ON


def test_state_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        State("off")
