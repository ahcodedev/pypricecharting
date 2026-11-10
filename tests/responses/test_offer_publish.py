import json
from datetime import date

from pypricecharting.responses import OfferPublishResponse
from pypricecharting.types import OfferStatus, Status
from tests.mocks.json import OFFER_PUBLISH_RESPONSE_JSON


def test_offer_publish_json_to_model():
    response = OfferPublishResponse.model_validate_json(json.dumps(OFFER_PUBLISH_RESPONSE_JSON))

    assert response.status is Status.SUCCESS
    assert response.offer_id == "vtdsww72uyslgooawzyyijsllm"
    assert response.offer_url == "/offer/vtdsww72uyslgooawzyyijsllm"
    assert response.offer_status is OfferStatus.AVAILABLE
    assert response.product_name == "EarthBound"
    assert response.console_name == "Super Nintendo"
    assert response.condition_string == "Normal wear"
    assert response.include_string == "Game only"
    assert response.has_pictures is False
    assert response.price == 2500
    assert response.cost_basis == 1000
    assert response.sku == "ABC-123"
    assert response.is_collection is False
    assert response.quantity == 2
    assert response.start_time == date(2017, 10, 31)


def test_offer_publish_model_to_json():
    response = OfferPublishResponse(
        status=Status.SUCCESS,
        offer_id="vtdsww72uyslgooawzyyijsllm",
        offer_url="/offer/vtdsww72uyslgooawzyyijsllm",
        offer_status=OfferStatus.AVAILABLE,
        product_name="EarthBound",
        console_name="Super Nintendo",
        condition_string="Normal wear",
        include_string="Game only",
        has_pictures=False,
        price=2500,
        cost_basis=1000,
        sku="ABC-123",
        is_collection=False,
        quantity=2,
        start_time=date(2017, 10, 31),
    )

    dumped = response.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFER_PUBLISH_RESPONSE_JSON
