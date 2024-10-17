"""REST client handling, including SmartsheetResourceManagementStream base class."""

from __future__ import annotations

import logging
import sys
import os
from typing import TYPE_CHECKING, Any, Iterable
from urllib.parse import parse_qsl

from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseHATEOASPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

if TYPE_CHECKING:
    import requests
    from singer_sdk.helpers.types import Context


# TODO: Delete this is if not using json files for schema definition
# SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"
API_VERSION = "v1"

IS_INCREMENTAL = os.getenv("IS_INCREMENTAL", "False").lower() == "true"

logging.basicConfig(level=logging.INFO)

class MyPaginator(BaseHATEOASPaginator):
    def get_next_url(self, response):
        data = response.json()
        if "paging" in data:
            return data["paging"]["next"]

class SmartsheetResourceManagementStream(RESTStream):
    """SmartsheetResourceManagement stream class."""

    # Update this value if necessary or override `parse_response`.
    records_jsonpath = "$.data[*]"
    replication_key = "updated_at"
    primary_keys = ["id"]
    
    # Update this value if necessary or override `get_new_paginator`.
    # next_page_token_jsonpath = "$.paging.next"  

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return f"https://api.rm.smartsheet.com/api/{API_VERSION}"

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="auth",
            value=self.config.get("auth_token", ""),
            location="header",
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")  # noqa: ERA001
        return headers

    def get_new_paginator(self) -> BaseHATEOASPaginator:
        """Create a new pagination helper instance.

        If the source API can make use of the `next_page_token_jsonpath`
        attribute, or it contains a `X-Next-Page` header in the response
        then you can remove this method.

        If you need custom pagination that uses page numbers, "next" links, or
        other approaches, please read the guide: https://sdk.meltano.com/en/v0.25.0/guides/pagination-classes.html.

        Returns:
            A pagination helper instance.
        """
        
        return MyPaginator()

    def get_url_params(
        self,
        context: Context | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        logging.info(f"Starting timestamp: {self.get_starting_timestamp(context)}")
        # assert False, "This is a test"

        params: dict = {}
        params["per_page"] = 100
        
        if next_page_token:
            params.update(parse_qsl(next_page_token.query))
        
        return params
    

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """

        records = extract_jsonpath(self.records_jsonpath, input=response.json())
        yield from records            
    
    def post_process(
        self,
        row: dict,
        context: Context | None = None,  # noqa: ARG002
    ) -> dict | None:
        """As needed, append or transform raw data to match expected structure.

        Args:
            row: An individual record from the stream.
            context: The stream context.

        Returns:
            The updated record dictionary, or ``None`` to skip the record.
        """
        if not self.replication_key:
            logging.info("Replication key is not set. Returning row.")
            return row
        else:
            logging.info(f"Replication key is set to: {self.replication_key}")
        
        
        if self.get_starting_timestamp(self.context) is None:
            logging.warning("Starting timestamp is None in post_process")
            starting_timestamp = self.config.get("start_date").isoformat()
        else:
            starting_timestamp = self.get_starting_timestamp(self.context)
            logging.info(f"Starting timestamp: {starting_timestamp}")
        
        row_id = row.get('id')
        row_updated_at = row.get(self.replication_key)
        assert row_updated_at is not None, "Row updated_at is None in post_process"
        
        if row_updated_at <= starting_timestamp.isoformat() and IS_INCREMENTAL:
            return None
        
        logging.debug(f"Row id: {row_id}\n")
        logging.debug(f"Row updated_at: {row_updated_at}\n")
        
        # Emit the state after processing each record (or batch)
        self.state = self._increment_stream_state(row)
        self.last_id = row_id
        return row