import json

import pytest
from pydantic import ValidationError

from pypricecharting.requests import OfferPublishRequestParams
from pypricecharting.types import State
from tests.mocks.json import OFFER_PUBLISH_REQUEST_JSON


def test_offer_publish_json_to_model():
    request = OfferPublishRequestParams.model_validate_json(json.dumps(OFFER_PUBLISH_REQUEST_JSON))

    assert request.product == "6910"
    assert request.price_max == 2500
    assert request.price_min == 1500
    assert request.condition_id == 1
    assert request.cost_basis == 1000
    assert request.broken is State.ON
    assert request.sku == "ABC-123"
    assert request.quantity == 2
    assert request.upc is None


def test_offer_publish_model_to_json():
    request = OfferPublishRequestParams(
        product="6910",
        price_max=2500,
        price_min=1500,
        condition_id=1,
        cost_basis=1000,
        broken=State.ON,
        sku="ABC-123",
        quantity=2,
    )

    dumped = request.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFER_PUBLISH_REQUEST_JSON


def test_offer_publish_model_raises():
    with pytest.raises(ValidationError, match="One of product, upc, asin, epid, or offer_id"):
        OfferPublishRequestParams(price_max=2500, condition_id=1)


def test_offer_publish_add_to_collection():
    request = OfferPublishRequestParams(
        product="6910", price_max=2500, condition_id=1, add_to_collection=State.ON
    )

    dumped = request.model_dump(mode="json", by_alias=True, exclude_none=True)

    assert dumped["add-to-collection"] == "on"


def test_offer_publish_add_to_collection_rejects_other_values():
    with pytest.raises(ValidationError, match="add-to-collection"):
        OfferPublishRequestParams.model_validate(
            {"product": "6910", "price-max": 2500, "condition-id": 1, "add-to-collection": "yes"}
        )
