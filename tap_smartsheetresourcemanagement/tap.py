"""SmartsheetResourceManagement tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_smartsheetresourcemanagement import streams

class TapSmartsheetResourceManagement(Tap):
    """SmartsheetResourceManagement tap class."""

    name = "tap-smartsheetresourcemanagement"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.SmartsheetResourceManagementStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.UsersStream(self),
            streams.AssignmentsStream(self),
            streams.ProjectsStream(self),
            streams.AssignablesStream(self),
            streams.StatusOptionsStream(self),
            streams.HolidaysStream(self),
            streams.AvailabilitesStream(self),
            streams.PlaceholderResourcesStream(self),
            streams.LeaveTypesStream(self),
        ]

if __name__ == "__main__":
    TapSmartsheetResourceManagement.cli()
