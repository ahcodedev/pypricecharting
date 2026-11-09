import json
from datetime import date

from pypricecharting.responses import OfferEndResponse
from pypricecharting.types import Status

OFFER_END_JSON = {
    "status": "success",
    "offer-id": "vtdsww72uyslgooawzyyijsllm",
    "is-ended": True,
    "ended-time": "2017-10-31",
}


def test_offer_end_json_to_model():
    response = OfferEndResponse.model_validate_json(json.dumps(OFFER_END_JSON))

    assert response.status is Status.SUCCESS
    assert response.offer_id == "vtdsww72uyslgooawzyyijsllm"
    assert response.is_ended is True
    assert response.ended_time == date(2017, 10, 31)


def test_offer_end_model_to_json():
    response = OfferEndResponse(
        status=Status.SUCCESS,
        offer_id="vtdsww72uyslgooawzyyijsllm",
        is_ended=True,
        ended_time=date(2017, 10, 31),
    )

    dumped = response.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFER_END_JSON
