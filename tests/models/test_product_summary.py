import json

from pypricecharting.models import ProductSummary

PRODUCT_SUMMARY_JSON = {
    "id": "4801",
    "product-name": "Tactics Ogre",
    "console-name": "Playstation",
}


def test_product_summary_json_to_model():
    summary = ProductSummary.model_validate_json(json.dumps(PRODUCT_SUMMARY_JSON))

    assert summary.id == "4801"
    assert summary.product_name == "Tactics Ogre"
    assert summary.console_name == "Playstation"


def test_product_summary_model_to_json():
    summary = ProductSummary(id="4801", product_name="Tactics Ogre", console_name="Playstation")

    dumped = summary.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == PRODUCT_SUMMARY_JSON


def test_product_summary_defaults_to_none():
    summary = ProductSummary()

    assert summary.id is None
    assert summary.product_name is None
    assert summary.console_name is None
