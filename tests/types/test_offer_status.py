import pytest

from pypricecharting.types import OfferStatus


def test_offer_status_members():
    assert len(OfferStatus) == 5
    assert OfferStatus.AVAILABLE.value == "available"
    assert OfferStatus.SOLD.value == "sold"
    assert OfferStatus.ENDED.value == "ended"
    assert OfferStatus.PENDING.value == "pending"
    assert OfferStatus.COLLECTION.value == "collection"


def test_offer_status_lookup_by_value():
    for member in OfferStatus:
        assert OfferStatus(member.value) is member


def test_offer_status_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        OfferStatus("invalid")
