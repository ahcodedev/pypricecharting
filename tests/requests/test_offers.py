import json

import pytest
from pydantic import ValidationError

from pypricecharting.requests import OffersRequestParams, OffersSort, OffersStatus
from pypricecharting.types import Console, Genre
from tests.mocks.json import OFFERS_REQUEST_JSON


def test_offers_status_members():
    assert len(OffersStatus) == 4
    assert OffersStatus.AVAILABLE == "available"
    assert OffersStatus.SOLD == "sold"
    assert OffersStatus.ENDED == "ended"
    assert OffersStatus.COLLECTION == "collection"


def test_offers_status_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        OffersStatus("pending")


def test_offers_sort_members():
    assert len(OffersSort) == 3
    assert OffersSort.NAME == "name"
    assert OffersSort.STARTS == "starts"
    assert OffersSort.LOWEST_PRICE == "lowest-price"


def test_offers_sort_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        OffersSort("price")


def test_offers_json_to_model():
    request = OffersRequestParams.model_validate_json(json.dumps(OFFERS_REQUEST_JSON))

    assert request.status is OffersStatus.SOLD
    assert request.buyer == "7cgdyu5ynzos3mxwhfh46xj3f4"
    assert request.console is Console.NES
    assert request.condition_id == 1
    assert request.genre is Genre.FOOTBALL
    assert request.id == "6910"
    assert request.seller == "3mxwhfh46xj3f47cgdyu5ynzos"
    assert request.sort is OffersSort.LOWEST_PRICE


def test_offers_model_to_json():
    request = OffersRequestParams(
        status=OffersStatus.SOLD,
        buyer="7cgdyu5ynzos3mxwhfh46xj3f4",
        console=Console.NES,
        condition_id=1,
        genre=Genre.FOOTBALL,
        id="6910",
        seller="3mxwhfh46xj3f47cgdyu5ynzos",
        sort=OffersSort.LOWEST_PRICE,
    )

    dumped = request.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFERS_REQUEST_JSON


def test_offers_only_status_is_required():
    request = OffersRequestParams(status=OffersStatus.AVAILABLE)

    assert request.model_dump(mode="json", by_alias=True, exclude_none=True) == {
        "status": "available"
    }


def test_offers_requires_status():
    with pytest.raises(ValidationError, match="status"):
        OffersRequestParams.model_validate({})


def test_offers_rejects_unknown_status():
    with pytest.raises(ValidationError, match="status"):
        OffersRequestParams.model_validate({"status": "pending"})
