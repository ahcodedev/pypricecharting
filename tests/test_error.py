import pytest

from pypricecharting.error import APIError, PriceChartingError


def test_api_error_attributes():
    error = APIError("No such product", 404)
    assert error.message == "No such product"
    assert error.status_code == 404


def test_api_error_str():
    assert str(APIError("No such product", 404)) == "404: No such product"


def test_api_error_is_pricecharting_error():
    assert issubclass(APIError, PriceChartingError)
    assert not issubclass(APIError, ValueError)


def test_api_error_caught_as_pricecharting_error():
    with pytest.raises(PriceChartingError, match="500: Internal error"):
        raise APIError("Internal error", 500)
