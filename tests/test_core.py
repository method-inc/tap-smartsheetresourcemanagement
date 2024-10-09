"""Tests standard tap features using the built-in SDK tests library."""

import datetime, os

from singer_sdk.testing import get_tap_test_class

from tap_smartsheetresourcemanagement.tap import TapSmartsheetResourceManagement

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "auth_token": os.getenv("SSRM_AUTH_TOKEN"),
}


# Run standard built-in tap tests from the SDK:
TestTapSmartsheetResourceManagement = get_tap_test_class(
    tap_class=TapSmartsheetResourceManagement,
    config=SAMPLE_CONFIG,
)


# TODO: Create additional tests as appropriate for your tap.
