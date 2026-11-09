import logging
import re
from collections.abc import Generator
from urllib.parse import urlencode

from httpx2 import Auth, Request, Response
from pydantic import SecretStr

_TOKEN_PARAM = re.compile(r"([?&]t=)[^&\s\"']+")


class _TokenAuth(Auth):
    """Add the PriceCharting token as `t` in the query string (GET) or form body (POST)."""

    requires_request_body = True

    def __init__(self, token: SecretStr):
        self._token = token

    def auth_flow(self, request: Request) -> Generator[Request, Response]:
        """Attach the token to the outgoing request."""
        token = self._token.get_secret_value()

        if request.method == "GET":
            request.url = request.url.copy_set_param("t", token)
            yield request
            return

        param = urlencode({"t": token}).encode()
        body = request.content + b"&" + param if request.content else param
        headers = request.headers.copy()
        headers.pop("Content-Length", None)  # forces httpx2 to recalculate length
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        yield Request(
            request.method,
            request.url,
            headers=headers,
            content=body,
            extensions=request.extensions,
        )


class _RedactTokenFilter(logging.Filter):
    """Replace the `t` query parameter in httpx2 log records with `REDACTED`."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Redact the token in place and always let the record through."""
        message = record.getMessage()
        redacted = _TOKEN_PARAM.sub(r"\1REDACTED", message)
        if redacted != message:
            record.msg = redacted
            record.args = None
        return True


_REDACT_FILTER = _RedactTokenFilter()
