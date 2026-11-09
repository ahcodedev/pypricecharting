import json
from datetime import date

from pypricecharting.responses import OfferRefundResponse
from pypricecharting.types import Status

OFFER_REFUND_JSON = {
    "status": "success",
    "offer-id": "vtdsww72uyslgooawzyyijsllm",
    "is-refunded": True,
    "refunded-time": "2017-10-31",
}


def test_offer_refund_json_to_model():
    response = OfferRefundResponse.model_validate_json(json.dumps(OFFER_REFUND_JSON))

    assert response.status is Status.SUCCESS
    assert response.offer_id == "vtdsww72uyslgooawzyyijsllm"
    assert response.is_refunded is True
    assert response.refunded_time == date(2017, 10, 31)


def test_offer_refund_model_to_json():
    response = OfferRefundResponse(
        status=Status.SUCCESS,
        offer_id="vtdsww72uyslgooawzyyijsllm",
        is_refunded=True,
        refunded_time=date(2017, 10, 31),
    )

    dumped = response.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFER_REFUND_JSON
