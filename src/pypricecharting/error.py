class PriceChartingError(Exception):
    """Base class for all PriceCharting errors"""


class ParameterError(PriceChartingError, ValueError):
    """Raised when an API method is called with invalid parameters

    Raised before any request is sent.
    """


class APIError(PriceChartingError):
    """Raised when the API returns an error response

    Attributes:
        message: The API's `error-message`, or the HTTP reason phrase if it has none.
        status_code: The HTTP status code of the response.

    """

    def __init__(self, message: str, status_code: int):
        """Store the API error message and HTTP status code."""
        super().__init__(f"{status_code}: {message}")
        self.message = message
        self.status_code = status_code
