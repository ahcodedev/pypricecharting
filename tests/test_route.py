import pytest

from pypricecharting.route import Route

# Source: https://www.pricecharting.com/api-documentation


def test_prices_route():
    assert len(Route.Prices) == 2
    assert Route.Prices.PRODUCT == "/api/product"
    assert Route.Prices.PRODUCTS == "/api/products"


def test_prices_lookup_by_value():
    for member in Route.Prices:
        assert Route.Prices(member) is member


def test_prices_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Route.Prices("Invalid Route")


def test_marketplace_route():
    assert len(Route.Marketplace) == 7
    assert Route.Marketplace.OFFERS == "/api/offers"
    assert Route.Marketplace.OFFER_PUBLISH == "/api/offer-publish"
    assert Route.Marketplace.OFFER_DETAILS == "/api/offer-details"
    assert Route.Marketplace.OFFER_FEEDBACK == "/api/offer-feedback"
    assert Route.Marketplace.OFFER_SHIP == "/api/offer-ship"
    assert Route.Marketplace.OFFER_REFUND == "/api/offer-refund"
    assert Route.Marketplace.OFFER_END == "/api/offer-end"


def test_marketplace_lookup_by_value():
    for member in Route.Marketplace:
        assert Route.Marketplace(member) is member


def test_marketplace_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Route.Marketplace("Invalid Route")
