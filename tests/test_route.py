import pytest

from pypricecharting.route import MarketPlace, Prices, Route

# Source: https://www.pricecharting.com/api-documentation


def test_prices_route():
    assert len(Prices) == 2
    assert Prices.PRODUCT.value == "/api/product"
    assert Prices.PRODUCTS.value == "/api/products"


def test_prices_lookup_by_value():
    for member in Prices:
        assert Prices(member.value) is member


def test_prices_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Prices("Invalid Route")


def test_marketplace_route():
    assert len(MarketPlace) == 7
    assert MarketPlace.OFFERS.value == "/api/offers"
    assert MarketPlace.OFFER_PUBLISH.value == "/api/offer-publish"
    assert MarketPlace.OFFER_DETAILS.value == "/api/offer-details"
    assert MarketPlace.OFFER_FEEDBACK.value == "/api/offer-feedback"
    assert MarketPlace.OFFER_SHIP.value == "/api/offer-ship"
    assert MarketPlace.OFFER_END.value == "/api/offer-end"


def test_marketplace_lookup_by_value():
    for member in MarketPlace:
        assert MarketPlace(member.value) is member


def test_marketplace_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        MarketPlace("Invalid Route")


def test_route_routes():
    assert len(Route) == 2
    assert Route.MARKETPLACE.value is MarketPlace
    assert Route.PRICES.value is Prices


def test_genre_lookup_by_value():
    for member in Route:
        assert Route(member.value) is member


def test_route_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Route("Invalid Route")
