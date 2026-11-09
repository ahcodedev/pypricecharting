from datetime import date

import pytest
from httpx2 import Response

from pypricecharting.error import APIError
from pypricecharting.responses import OfferEndResponse, _parse
from pypricecharting.types import Status

OFFER_END_JSON = {
    "status": "success",
    "offer-id": "vtdsww72uyslgooawzyyijsllm",
    "is-ended": True,
    "ended-time": "2017-10-31",
}


def test_parse_success():
    response = _parse(Response(200, json=OFFER_END_JSON), OfferEndResponse)

    assert isinstance(response, OfferEndResponse)
    assert response.status is Status.SUCCESS
    assert response.offer_id == "vtdsww72uyslgooawzyyijsllm"
    assert response.is_ended is True
    assert response.ended_time == date(2017, 10, 31)


def test_parse_error_status_code():
    body = {"status": "error", "error-message": "No such offer"}

    with pytest.raises(APIError, match="404: No such offer") as exc_info:
        _parse(Response(404, json=body), OfferEndResponse)

    assert exc_info.value.message == "No such offer"
    assert exc_info.value.status_code == 404


def test_parse_error_status_with_success_code():
    body = {"status": "error", "error-message": "Offer already ended"}

    with pytest.raises(APIError, match="200: Offer already ended"):
        _parse(Response(200, json=body), OfferEndResponse)


def test_parse_error_without_message_uses_reason_phrase():
    with pytest.raises(APIError, match="400: Bad Request"):
        _parse(Response(400, json={"status": "error"}), OfferEndResponse)


def test_parse_non_json_response():
    with pytest.raises(APIError, match="502: Bad Gateway"):
        _parse(Response(502, text="<html>Bad Gateway</html>"), OfferEndResponse)
