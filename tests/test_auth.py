import logging
from urllib.parse import parse_qs

import pytest
from httpx2 import AsyncClient, Client, MockTransport, Request, Response
from pydantic import SecretStr

from pypricecharting import AsyncPriceCharting, PriceCharting
from pypricecharting._auth import _REDACT_FILTER, _RedactTokenFilter, _TokenAuth
from tests.mocks.mock_pricecharting import TOKEN

URL = "https://example.com/api/product"


def _capture(sent: list[Request]):
    def handler(request: Request) -> Response:
        sent.append(request)
        return Response(200)

    return MockTransport(handler)


def _client(sent: list[Request]) -> Client:
    return Client(auth=_TokenAuth(SecretStr(TOKEN)), transport=_capture(sent))


def _record(msg: str, *args: object) -> logging.LogRecord:
    return logging.LogRecord("httpx2", logging.INFO, __file__, 1, msg, args, None)


# _TokenAuth


def test_token_auth_does_not_expose_token():
    auth = _TokenAuth(SecretStr(TOKEN))
    assert TOKEN not in repr(vars(auth))


def test_get_adds_token_to_query():
    sent: list[Request] = []
    with _client(sent) as client:
        client.get(URL, params={"id": "1"})

    assert sent[0].url.params["t"] == TOKEN
    assert sent[0].url.params["id"] == "1"
    assert sent[0].content == b""


def test_get_replaces_existing_token():
    sent: list[Request] = []
    with _client(sent) as client:
        client.get(URL, params={"t": "other"})

    assert sent[0].url.params.get_list("t") == [TOKEN]


def test_post_adds_token_to_form_body():
    sent: list[Request] = []
    with _client(sent) as client:
        client.post(URL, data={"offer-id": "abc"})

    request = sent[0]
    assert parse_qs(request.content.decode()) == {"offer-id": ["abc"], "t": [TOKEN]}
    assert "t" not in request.url.params
    assert request.headers["Content-Type"] == "application/x-www-form-urlencoded"
    assert request.headers["Content-Length"] == str(len(request.content))


def test_post_without_body_sends_only_token():
    sent: list[Request] = []
    with _client(sent) as client:
        client.post(URL)

    request = sent[0]
    assert parse_qs(request.content.decode()) == {"t": [TOKEN]}
    assert request.headers["Content-Type"] == "application/x-www-form-urlencoded"
    assert request.headers["Content-Length"] == str(len(request.content))


def test_post_keeps_other_headers():
    sent: list[Request] = []
    with _client(sent) as client:
        client.post(URL, data={"offer-id": "abc"}, headers={"X-Test": "1"})

    assert sent[0].headers["X-Test"] == "1"


async def test_async_get_adds_token_to_query():
    sent: list[Request] = []
    auth = _TokenAuth(SecretStr(TOKEN))
    async with AsyncClient(auth=auth, transport=_capture(sent)) as client:
        await client.get(URL, params={"id": "1"})

    assert sent[0].url.params["t"] == TOKEN


async def test_async_post_adds_token_to_form_body():
    sent: list[Request] = []
    auth = _TokenAuth(SecretStr(TOKEN))
    async with AsyncClient(auth=auth, transport=_capture(sent)) as client:
        await client.post(URL, data={"offer-id": "abc"})

    assert parse_qs(sent[0].content.decode()) == {"offer-id": ["abc"], "t": [TOKEN]}


# _RedactTokenFilter


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        (f"{URL}?t={TOKEN}", f"{URL}?t=REDACTED"),
        (f"{URL}?id=1&t={TOKEN}", f"{URL}?id=1&t=REDACTED"),
        (f"{URL}?t={TOKEN}&id=1", f"{URL}?t=REDACTED&id=1"),
    ],
)
def test_filter_redacts_token(url, expected):
    record = _record('HTTP Request: %s %s "%s"', "GET", url, "HTTP/1.1 200 OK")

    assert _RedactTokenFilter().filter(record) is True
    assert record.getMessage() == f'HTTP Request: GET {expected} "HTTP/1.1 200 OK"'
    assert TOKEN not in record.getMessage()


def test_filter_leaves_other_messages_unchanged():
    record = _record("HTTP Request: %s %s", "GET", f"{URL}?id=1&type=t")

    assert _RedactTokenFilter().filter(record) is True
    assert record.msg == "HTTP Request: %s %s"
    assert record.args == ("GET", f"{URL}?id=1&type=t")


def test_filter_ignores_params_ending_in_t():
    record = _record(f"{URL}?format=json&cat=1")

    _RedactTokenFilter().filter(record)
    assert record.getMessage() == f"{URL}?format=json&cat=1"


def test_httpx2_request_log_is_redacted(caplog):
    sent: list[Request] = []
    with caplog.at_level(logging.INFO, logger="httpx2"):
        logging.getLogger("httpx2").addFilter(_REDACT_FILTER)
        with _client(sent) as client:
            client.get(URL, params={"id": "1"})

    assert "t=REDACTED" in caplog.text
    assert TOKEN not in caplog.text


# Client installation


def test_client_installs_filter_once():
    PriceCharting(TOKEN).close()
    PriceCharting(TOKEN).close()

    filters = logging.getLogger("httpx2").filters
    assert filters.count(_REDACT_FILTER) == 1


async def test_async_client_installs_filter_once():
    await AsyncPriceCharting(TOKEN).aclose()
    await AsyncPriceCharting(TOKEN).aclose()

    filters = logging.getLogger("httpx2").filters
    assert filters.count(_REDACT_FILTER) == 1
