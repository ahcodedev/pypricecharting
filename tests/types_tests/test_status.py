import pytest

from pypricecharting.types.status import Status


def test_status():
    assert len(Status) == 2
    assert Status.SUCCESS.value == "success"
    assert Status.ERROR.value == "error"


def test_status_lookup_by_id():
    for member in Status:
        assert Status(member.value) is member


def test_status_unknown_id_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Status("invalid")
