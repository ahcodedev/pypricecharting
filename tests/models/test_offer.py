import json
from datetime import date

import pytest
from pydantic import ValidationError

from pypricecharting.models import Offer
from pypricecharting.types import OfferStatus

OFFER_JSON = {
    "offer-id": "smzksacsy5i2dsrddxsrlzsp6i",
    "offer-status": "sold",
    "offer-url": "/offer/smzksacsy5i2dsrddxsrlzsp6i",
    "id": 9307,
    "product-name": "M.C. Kids",
    "console-name": "NES",
    "condition-string": "Normal wear",
    "include-string": "Game only",
    "price": 1473,
    "is-available": False,
    "is-sold": True,
    "is-ended": True,
    "is-shipped": False,
    "sale-time": "2017-10-31",
    "shipped-time": "0001-01-01",
    "ended-time": "2017-10-31",
    "cert-id": "5672930123",
    "grade-co-id": 1,
}


def test_offer_json_to_model():
    offer = Offer.model_validate_json(json.dumps(OFFER_JSON))

    assert offer.offer_id == "smzksacsy5i2dsrddxsrlzsp6i"
    assert offer.offer_status is OfferStatus.SOLD
    assert offer.offer_url == "/offer/smzksacsy5i2dsrddxsrlzsp6i"
    assert offer.id == 9307
    assert offer.product_name == "M.C. Kids"
    assert offer.console_name == "NES"
    assert offer.condition_string == "Normal wear"
    assert offer.include_string == "Game only"
    assert offer.price == 1473
    assert offer.is_available is False
    assert offer.is_sold is True
    assert offer.is_ended is True
    assert offer.is_shipped is False
    assert offer.sale_time == date(2017, 10, 31)
    assert offer.shipped_time == date(1, 1, 1)
    assert offer.ended_time == date(2017, 10, 31)
    assert offer.cert_id == "5672930123"
    assert offer.grade_co_id == 1


def test_offer_model_to_json():
    offer = Offer(
        offer_id="smzksacsy5i2dsrddxsrlzsp6i",
        offer_status=OfferStatus.SOLD,
        offer_url="/offer/smzksacsy5i2dsrddxsrlzsp6i",
        id=9307,
        product_name="M.C. Kids",
        console_name="NES",
        condition_string="Normal wear",
        include_string="Game only",
        price=1473,
        is_available=False,
        is_sold=True,
        is_ended=True,
        is_shipped=False,
        sale_time=date(2017, 10, 31),
        shipped_time=date(1, 1, 1),
        ended_time=date(2017, 10, 31),
        cert_id="5672930123",
        grade_co_id=1,
    )

    dumped = offer.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFER_JSON


def test_offer_unknown_status_raises():
    with pytest.raises(ValidationError, match="offer-status"):
        Offer.model_validate({"offer-status": "invalid"})
