import json

from pypricecharting.responses import ErrorResponse
from pypricecharting.types import Status
from tests.mocks.json import ERROR_JSON


def test_error_json_to_model():
    response = ErrorResponse.model_validate_json(json.dumps(ERROR_JSON))

    assert response.status is Status.ERROR
    assert response.error_message == "No such product"


def test_error_model_to_json():
    response = ErrorResponse(status=Status.ERROR, error_message="No such product")

    dumped = response.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == ERROR_JSON


def test_error_message_defaults_to_none():
    response = ErrorResponse.model_validate_json('{"status": "error"}')

    assert response.error_message is None
