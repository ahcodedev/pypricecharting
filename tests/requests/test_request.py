import json

import pytest
from pydantic import ValidationError

from pypricecharting.requests import OfferPublishRequest
from pypricecharting.types import State

OFFER_PUBLISH_JSON = {
    "product": "6910",
    "price-max": 2500,
    "price-min": 1500,
    "condition-id": "1",
    "cost-basis": 1000,
    "broken": "on",
    "sku": "ABC-123",
    "quantity": 2,
}


def test_offer_publish_json_to_model():
    request = OfferPublishRequest.model_validate_json(json.dumps(OFFER_PUBLISH_JSON))

    assert request.product == "6910"
    assert request.price_max == 2500
    assert request.price_min == 1500
    assert request.condition_id == "1"
    assert request.cost_basis == 1000
    assert request.broken is State.ON
    assert request.sku == "ABC-123"
    assert request.quantity == 2
    assert request.upc is None


def test_offer_publish_model_to_json():
    request = OfferPublishRequest(
        product="6910",
        price_max=2500,
        price_min=1500,
        condition_id="1",
        cost_basis=1000,
        broken=State.ON,
        sku="ABC-123",
        quantity=2,
    )

    dumped = request.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFER_PUBLISH_JSON


def test_offer_publish_model_raises():
    with pytest.raises(ValidationError, match="One of product, upc, asin, epid, or offer_id"):
        OfferPublishRequest(price_max=2500, condition_id="1")
