import pypricecharting
from pypricecharting import error, models, requests, responses, types
from pypricecharting.asyncpricecharting import AsyncPriceCharting
from pypricecharting.pricecharting import PriceCharting


def test_all_names_are_importable():
    for name in pypricecharting.__all__:
        assert hasattr(pypricecharting, name), name


def test_all_has_no_duplicates():
    assert len(pypricecharting.__all__) == len(set(pypricecharting.__all__))


def test_exports_clients():
    assert pypricecharting.PriceCharting is PriceCharting
    assert pypricecharting.AsyncPriceCharting is AsyncPriceCharting


def test_exports_errors():
    assert pypricecharting.PriceChartingError is error.PriceChartingError
    assert pypricecharting.ParameterError is error.ParameterError
    assert pypricecharting.APIError is error.APIError


def test_exports_public_classes_from_modules():
    for module in (models, requests, responses, types):
        public = [
            name
            for name, value in vars(module).items()
            if isinstance(value, type)
            and value.__module__ == module.__name__
            and not name.startswith("_")
        ]
        for name in public:
            assert name in pypricecharting.__all__, f"{module.__name__}.{name} is not exported"
