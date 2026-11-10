"""Shared JSON test data, in the API's kebab-case format."""

# Models

BUYER_JSON = {
    "buyer-email": "buyer@example.com",
    "shipping-name": "Jane Doe",
    "shipping-line1": "123 Main St",
    "shipping-line2": "Apt 4",
    "shipping-city": "Springfield",
    "shipping-state": "IL",
    "shipping-zip": "62701",
    "shipping-country": "US",
}


OFFER_JSON = {
    "offer-id": "smzksacsy5i2dsrddxsrlzsp6i",
    "offer-status": "sold",
    "offer-url": "/offer/smzksacsy5i2dsrddxsrlzsp6i",
    "id": 9307,
    "product-name": "M.C. Kids",
    "console-name": "NES",
    "condition-string": "Normal wear",
    "include-string": "Game only",
    "price": 1473,
    "is-available": False,
    "is-sold": True,
    "is-ended": True,
    "is-shipped": False,
    "sale-time": "2017-10-31",
    "shipped-time": "0001-01-01",
    "ended-time": "2017-10-31",
    "cert-id": "5672930123",
    "grade-co-id": 1,
}


PRODUCT_SUMMARY_JSON = {
    "id": "4801",
    "product-name": "Tactics Ogre",
    "console-name": "Playstation",
}


# Requests

OFFER_PUBLISH_REQUEST_JSON = {
    "product": "6910",
    "price-max": 2500,
    "price-min": 1500,
    "condition-id": "1",
    "cost-basis": 1000,
    "broken": "on",
    "sku": "ABC-123",
    "quantity": 2,
}

OFFERS_REQUEST_JSON = {
    "status": "sold",
    "buyer": "7cgdyu5ynzos3mxwhfh46xj3f4",
    "console": "G17",
    "condition-id": 1,
    "genre": "Football",
    "id": "6910",
    "seller": "3mxwhfh46xj3f47cgdyu5ynzos",
    "sort": "lowest-price",
}


# Responses

ERROR_JSON = {"status": "error", "error-message": "No such product"}

OFFERS_JSON = {
    "status": "success",
    "offers": [
        {"offer-id": "smzksacsy5i2dsrddxsrlzsp6i", "offer-status": "sold", "price": 1473},
        {"offer-id": "vtdsww72uyslgooawzyyijsllm", "offer-status": "available", "price": 2500},
    ],
}


OFFER_DETAILS_JSON = {
    "status": "success",
    "buyer": {
        "buyer-email": "buyer@example.com",
        "shipping-name": "Jane Doe",
        "shipping-line1": "123 Main St",
        "shipping-city": "Springfield",
        "shipping-state": "IL",
        "shipping-zip": "62701",
        "shipping-country": "US",
    },
    "buyer-left-feedback": False,
    "seller-left-feedback": True,
    "id": 9307,
    "product-name": "M.C. Kids",
    "console-name": "NES",
    "condition": "Normal wear",
    "includes": "Game only",
    "cost-basis": 500,
    "price": 1473,
    "max-price": 2000,
    "min-price": 1000,
    "shipping-premium": 0,
    "has-pictures": True,
    "is-collection": False,
    "is-ended": True,
    "is-price-descending": True,
    "is-refunded": False,
    "is-shipped": True,
    "is-sold": True,
    "offer-id": "smzksacsy5i2dsrddxsrlzsp6i",
    "offer-status": "sold",
    "offer-url": "/offer/smzksacsy5i2dsrddxsrlzsp6i",
    "sku": "ABC-123",
    "tracking-number": "901234567890000",
    "start-time": "2017-10-01",
    "sale-time": "2017-10-31",
    "shipped-time": "2017-11-01",
    "ended-time": "2017-10-31",
    "refunded-time": "0001-01-01",
}


OFFER_END_JSON = {
    "status": "success",
    "offer-id": "vtdsww72uyslgooawzyyijsllm",
    "is-ended": True,
    "ended-time": "2017-10-31",
}


OFFER_FEEDBACK_JSON = {
    "status": "success",
    "offer-id": "vtdsww72uyslgooawzyyijsllm",
    "rating": 2,
    "comment": "Great buyer",
}


OFFER_PUBLISH_RESPONSE_JSON = {
    "status": "success",
    "offer-id": "vtdsww72uyslgooawzyyijsllm",
    "offer-url": "/offer/vtdsww72uyslgooawzyyijsllm",
    "offer-status": "available",
    "product-name": "EarthBound",
    "console-name": "Super Nintendo",
    "condition-string": "Normal wear",
    "include-string": "Game only",
    "has-pictures": False,
    "price": 2500,
    "cost-basis": 1000,
    "sku": "ABC-123",
    "is-collection": False,
    "quantity": 2,
    "start-time": "2017-10-31",
}


OFFER_REFUND_JSON = {
    "status": "success",
    "offer-id": "vtdsww72uyslgooawzyyijsllm",
    "is-refunded": True,
    "refunded-time": "2017-10-31",
}


OFFER_SHIP_JSON = {
    "status": "success",
    "offer-id": "vtdsww72uyslgooawzyyijsllm",
    "is-shipped": True,
    "shipped-time": "2017-10-31",
    "tracking-number": "901234567890000",
}


PRODUCTS_JSON = {
    "status": "success",
    "products": [
        PRODUCT_SUMMARY_JSON,
        {"console-name": "GameBoy Advance", "id": "2611", "product-name": "Tactics Ogre"},
    ],
}


PRODUCT_BASIC_JSON = {
    "status": "success",
    "id": "6910",
    "product-name": "EarthBound",
    "console-name": "Super Nintendo",
    "loose-price": 17244,
    "cib-price": 42995,
    "new-price": 53000,
    "release-date": "1995-06-05",
}


PRODUCT_JSON = {
    "status": "success",
    "id": "6910",
    "product-name": "EarthBound",
    "console-name": "Super Nintendo",
    "release-date": "1995-06-05",
    "sales-volume": 120,
    "loose-price": 17244,
    "cib-price": 42995,
    "new-price": 53000,
    "bgs-10-price": 60000,
    "condition-9-price": 9000,
    "retail-loose-buy": 12000,
}
