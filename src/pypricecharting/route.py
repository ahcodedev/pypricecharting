from enum import StrEnum, unique

# Source: https://www.pricecharting.com/api-documentation


BASE_URL = "https://www.pricecharting.com"
"""Default API base URL."""


class Route:
    """PriceCharting API routes, grouped by API"""

    @unique
    class Prices(StrEnum):
        """PriceCharting Prices API Routes"""

        PRODUCT = "/api/product"
        PRODUCTS = "/api/products"

    @unique
    class Marketplace(StrEnum):
        """PriceCharting Marketplace API Routes"""

        OFFERS = "/api/offers"
        OFFER_PUBLISH = "/api/offer-publish"
        OFFER_DETAILS = "/api/offer-details"
        OFFER_FEEDBACK = "/api/offer-feedback"
        OFFER_SHIP = "/api/offer-ship"
        OFFER_END = "/api/offer-end"
        OFFER_REFUND = "/api/offer-refund"
