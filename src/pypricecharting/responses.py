from datetime import date

from pydantic import Field

from pypricecharting.models import Buyer, Offer, PriceChartingModel, ProductSummary
from pypricecharting.types import OfferStatus, Rating, Status


class ProductResponse(ProductSummary):
    """api/product response

    Prices are in pennies. Price keys mean different conditions for video games, cards and
    comics, noted below as video games / cards / comics.

    https://www.pricecharting.com/api-documentation#api-product
    """

    status: Status
    genre: str | None = None
    release_date: date | None = None
    upc: str | None = None
    asin: str | None = None  # Amazon ASIN
    epid: str | None = None  # eBay ePID
    tcg_id: str | None = None  # TCGplayer ID, trading cards only
    sales_volume: int | None = None  # yearly units sold

    loose_price: int | None = None  # item only / ungraded / ungraded
    cib_price: int | None = None  # box and manual / grade 7-7.5 / 4.0-4.5
    new_price: int | None = None  # new and sealed / grade 8-8.5 / 6.0-6.5
    graded_price: int | None = None  # graded by WATA or VGA / grade 9 / 8.0-8.5
    box_only_price: int | None = None  # box only / grade 9.5 / 9.2
    manual_only_price: int | None = None  # manual only / PSA 10 / 9.8
    bgs_10_price: int | None = None  # cards BGS 10 / comics 10.0
    condition_9_price: int | None = None  # cards grade 1 / comics 2.0
    condition_10_price: int | None = None  # cards grade 2 / comics 9.6
    condition_13_price: int | None = None  # cards grade 3 / comics 3.0
    condition_14_price: int | None = None  # cards grade 4 / comics 5.0
    condition_15_price: int | None = None  # cards grade 5 / comics 7.0
    condition_16_price: int | None = None  # cards grade 6 / comics 9.0
    condition_17_price: int | None = None  # cards CGC 10 / comics 9.4
    condition_18_price: int | None = None  # cards SGC 10
    condition_19_price: int | None = None  # cards CGC 10 Pristine
    condition_20_price: int | None = None  # cards BGS 10 Black
    condition_21_price: int | None = None  # cards TAG 10
    condition_22_price: int | None = None  # cards ACE 10

    gamestop_price: int | None = None  # GameStop pre-owned price
    retail_loose_buy: int | None = None
    retail_loose_sell: int | None = None
    retail_cib_buy: int | None = None
    retail_cib_sell: int | None = None
    retail_new_buy: int | None = None
    retail_new_sell: int | None = None


class ProductsResponse(PriceChartingModel):
    """api/products response

    https://www.pricecharting.com/api-documentation#api-products
    """

    status: Status
    products: list[ProductSummary] = Field(default_factory=list)


class OffersResponse(PriceChartingModel):
    """api/offers response

    https://www.pricecharting.com/api-documentation#offers
    """

    status: Status
    offers: list[Offer] = Field(default_factory=list)


class OfferDetailsResponse(PriceChartingModel):
    """api/offer-details response

    https://www.pricecharting.com/api-documentation#offer-details
    """

    status: Status
    buyer: Buyer | None = None
    buyer_left_feedback: bool | None = None
    seller_left_feedback: bool | None = None
    id: int | None = None  # PriceCharting product ID
    product_name: str | None = None
    console_name: str | None = None
    condition: str | None = None
    includes: str | None = None
    cost_basis: int | None = None
    price: int | None = None
    max_price: int | None = None
    min_price: int | None = None
    shipping_premium: int | None = None  # extra paid by the buyer for international shipping
    has_pictures: bool | None = None
    is_collection: bool | None = None
    is_ended: bool | None = None
    is_price_descending: bool | None = None  # reverse auction
    is_refunded: bool | None = None
    is_shipped: bool | None = None
    is_sold: bool | None = None
    offer_id: str | None = None
    offer_status: OfferStatus | None = None
    offer_url: str | None = None
    sku: str | None = None  # only returned to the seller
    tracking_number: str | None = None
    start_time: date | None = None
    sale_time: date | None = None
    shipped_time: date | None = None
    ended_time: date | None = None
    refunded_time: date | None = None


class OfferPublishResponse(PriceChartingModel):
    """api/offer-publish response

    https://www.pricecharting.com/api-documentation#offer-publish
    """

    status: Status
    offer_id: str | None = None
    offer_url: str | None = None
    offer_status: OfferStatus | None = None
    product_name: str | None = None
    console_name: str | None = None
    condition_string: str | None = None
    include_string: str | None = None
    has_pictures: bool | None = None
    price: int | None = None
    cost_basis: int | None = None
    sku: str | None = None
    is_collection: bool | None = None
    quantity: int | None = None
    start_time: date | None = None


class OfferFeedbackResponse(PriceChartingModel):
    """api/offer-feedback response

    https://www.pricecharting.com/api-documentation#offer-feedback
    """

    status: Status
    offer_id: str | None = None
    rating: Rating | None = None
    comment: str | None = None


class OfferShipResponse(PriceChartingModel):
    """api/offer-ship response

    https://www.pricecharting.com/api-documentation#offer-ship
    """

    status: Status
    offer_id: str | None = None
    is_shipped: bool | None = None
    shipped_time: date | None = None
    tracking_number: str | None = None


class OfferEndResponse(PriceChartingModel):
    """api/offer-end response

    https://www.pricecharting.com/api-documentation#offer-end
    """

    status: Status
    offer_id: str | None = None
    is_ended: bool | None = None
    ended_time: date | None = None


class OfferRefundResponse(PriceChartingModel):
    """api/offer-refund response

    https://www.pricecharting.com/api-documentation#offer-refund
    """

    status: Status
    offer_id: str | None = None
    is_refunded: bool | None = None
    refunded_time: date | None = None
