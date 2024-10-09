"""Stream type classes for tap-smartsheetresourcemanagement."""

from __future__ import annotations

import sys
import typing as t
from urllib.parse import parse_qsl
from typing import TYPE_CHECKING, Any, Optional
from tap_smartsheetresourcemanagement.client import SmartsheetResourceManagementStream

# Schema imports
from .schemas.users import schema as users_schema
from .schemas.assignments import schema as assignments_schema
from .schemas.projects import schema as projects_schema
from .schemas.assignables import schema as assignables_schema
from .schemas.status_options import schema as status_options_schema
from .schemas.holidays import schema as holidays_schema
from .schemas.availabilities import schema as availabilities_schema
from .schemas.placeholder_resources import schema as placeholder_resources_schema
from .schemas.leave_types import schema as leave_types_schema

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

if TYPE_CHECKING:
    import requests
    from singer_sdk.helpers.types import Context

class UsersStream(SmartsheetResourceManagementStream):
    """Define custom stream."""
    name = "smartsheet_users"
    path = "/users"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema = users_schema

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
        
        params: dict = {}
        params["per_page"] = 100
        params["fields"] = "tags,custom_field_values"
        params["with_archived"] = True
        params["sort_order"] = "ascending"
        params["sort_field"] = "updated"
        
        if next_page_token:
            params.update(parse_qsl(next_page_token.query))
        
        return params
    
    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "user_id": record["id"]
        }

class AssignmentsStream(SmartsheetResourceManagementStream):
        
    name = "smartsheet_assignments"
    path = "/assignments"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema = assignments_schema
    
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
        
        params: dict = {}
        params["per_page"] = 100
        params["with_phases"] = True
        params["sort_order"] = "ascending"
        params["sort_field"] = "updated"
        params["from"] = self.config.get("start_date")
        params["to"] = self.config.get("end_date")
        
        if next_page_token:
            params.update(parse_qsl(next_page_token.query))
        
        return params
    
class ProjectsStream(SmartsheetResourceManagementStream):
    name = "smartsheet_projects"
    path = "/projects"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema = projects_schema
    
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
        
        params: dict = {}
        params["per_page"] = 100
        params["fields"] = "tags,custom_field_values"
        params["with_archived"] = True
        params["sort_order"] = "ascending"
        params["sort_field"] = "updated"
        
        if next_page_token:
            params.update(parse_qsl(next_page_token.query))
        
        return params
    
class AssignablesStream(SmartsheetResourceManagementStream):
    name = "smartsheet_assignables"
    path = "/assignables"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema = assignables_schema
    
class StatusOptionsStream(SmartsheetResourceManagementStream):
    name = "smartsheet_status_options"
    path = "/status_options"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema = status_options_schema
    
class HolidaysStream(SmartsheetResourceManagementStream):
    name = "smartsheet_holidays"
    path = "/holidays"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema = holidays_schema
    
class AvailabilitesStream(SmartsheetResourceManagementStream):
    name = "smartsheet_availabilities"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema = availabilities_schema
    parent_stream_type = UsersStream
    path = "/users/{user_id}/availabilities"
    ignore_parent_replication_keys = False
    
class PlaceholderResourcesStream(SmartsheetResourceManagementStream):
    name = "smartsheet_placeholder_resources"
    path = "/placeholder_resources"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema = placeholder_resources_schema
    
class LeaveTypesStream(SmartsheetResourceManagementStream):
    name = "smartsheet_leave_types"
    path = "/leave_types"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema = leave_types_schema