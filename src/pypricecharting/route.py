from enum import Enum, unique

# Source: https://www.pricecharting.com/api-documentation


BASE_URL = "https://www.pricecharting.com"


@unique
class Prices(Enum):
    """PriceCharting Prices API Routes"""

    PRODUCT = "/api/product"
    PRODUCTS = "/api/products"


@unique
class MarketPlace(Enum):
    """PriceCharting MarketPlace API Routes"""

    OFFERS = "/api/offers"
    OFFER_PUBLISH = "/api/offer-publish"
    OFFER_DETAILS = "/api/offer-details"
    OFFER_FEEDBACK = "/api/offer-feedback"
    OFFER_SHIP = "/api/offer-ship"
    OFFER_END = "/api/offer-end"
    OFFER_REFUND = "/api/offer-refund"


@unique
class Route(Enum):
    """PriceCharting API Routes"""

    PRICES = Prices
    MARKETPLACE = MarketPlace
