import os

from mlflow.tracking.request_header.abstract_request_header_provider import (
    RequestHeaderProvider,
)


class CloudflareRequestHeaderProvider(RequestHeaderProvider):
    """RequestHeaderProvider provided through plugin system"""

    def in_context(self):
        return True

    def request_headers(self):
        request_headers = {}
        if os.getenv("CF_ACCESS_TOKEN") is not None:
            request_headers["cf-access-token"] = os.getenv("CF_ACCESS_TOKEN")
        else:
            request_headers["cf-access-client-id"] = os.getenv("CF_ACCESS_CLIENT_ID")
            request_headers["cf-access-client-secret"] = os.getenv("CF_ACCESS_CLIENT_SECRET")
        return request_headers
