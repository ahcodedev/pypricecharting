import json

import pytest
from pydantic import ValidationError

from pypricecharting.responses import OfferFeedbackResponse
from pypricecharting.types import Rating, Status

OFFER_FEEDBACK_JSON = {
    "status": "success",
    "offer-id": "vtdsww72uyslgooawzyyijsllm",
    "rating": 2,
    "comment": "Great buyer",
}


def test_offer_feedback_json_to_model():
    response = OfferFeedbackResponse.model_validate_json(json.dumps(OFFER_FEEDBACK_JSON))

    assert response.status is Status.SUCCESS
    assert response.offer_id == "vtdsww72uyslgooawzyyijsllm"
    assert response.rating is Rating.GREAT
    assert response.comment == "Great buyer"


def test_offer_feedback_model_to_json():
    response = OfferFeedbackResponse(
        status=Status.SUCCESS,
        offer_id="vtdsww72uyslgooawzyyijsllm",
        rating=Rating.GREAT,
        comment="Great buyer",
    )

    dumped = response.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFER_FEEDBACK_JSON


def test_offer_feedback_unknown_rating_raises():
    with pytest.raises(ValidationError, match="rating"):
        OfferFeedbackResponse.model_validate({"status": "success", "rating": 3})
