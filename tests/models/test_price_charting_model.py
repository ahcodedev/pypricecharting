import pytest

from pypricecharting.models import PriceChartingModel, to_kebab


class Example(PriceChartingModel):
    console_name: str
    bgs_10_price: int


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("id", "id"),
        ("console_name", "console-name"),
        ("bgs_10_price", "bgs-10-price"),
        ("shipping_line1", "shipping-line1"),
    ],
)
def test_to_kebab(name, expected):
    assert to_kebab(name) == expected


def test_model_validates_by_alias():
    model = Example.model_validate({"console-name": "NES", "bgs-10-price": 100})

    assert model.console_name == "NES"
    assert model.bgs_10_price == 100


def test_model_validates_by_name():
    model = Example(console_name="NES", bgs_10_price=100)

    assert model.console_name == "NES"
    assert model.bgs_10_price == 100


def test_model_dumps_by_alias():
    model = Example(console_name="NES", bgs_10_price=100)

    assert model.model_dump(by_alias=True) == {"console-name": "NES", "bgs-10-price": 100}
