import json
from datetime import date

from pypricecharting.responses import OfferShipResponse
from pypricecharting.types import Status
from tests.mocks.json import OFFER_SHIP_JSON


def test_offer_ship_json_to_model():
    response = OfferShipResponse.model_validate_json(json.dumps(OFFER_SHIP_JSON))

    assert response.status is Status.SUCCESS
    assert response.offer_id == "vtdsww72uyslgooawzyyijsllm"
    assert response.is_shipped is True
    assert response.shipped_time == date(2017, 10, 31)
    assert response.tracking_number == "901234567890000"


def test_offer_ship_model_to_json():
    response = OfferShipResponse(
        status=Status.SUCCESS,
        offer_id="vtdsww72uyslgooawzyyijsllm",
        is_shipped=True,
        shipped_time=date(2017, 10, 31),
        tracking_number="901234567890000",
    )

    dumped = response.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFER_SHIP_JSON
