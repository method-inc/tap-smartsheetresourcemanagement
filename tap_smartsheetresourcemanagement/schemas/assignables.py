from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("description", th.StringType),
    th.Property("guid", th.StringType),
    th.Property("name", th.StringType),
    th.Property("deleted_at", th.DateTimeType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("type", th.StringType),
    th.Property("starts_at", th.StringType),
    th.Property("ends_at", th.StringType),
    th.Property("parent_id", th.IntegerType),
    th.Property("project_code", th.StringType),
    th.Property("secureurl", th.StringType),
    th.Property("secureurl_expiration", th.StringType),
    th.Property("timeentry_lockout", th.IntegerType),
    th.Property("settings", th.IntegerType),
    th.Property("project_state_id", th.IntegerType),
    th.Property("thumbnail", th.StringType),
    th.Property("owner_id", th.IntegerType),
    th.Property("owner_name", th.StringType),
    th.Property("client", th.StringType),
    th.Property("phase_name", th.StringType)
).to_dict()

# Example:
# {
#     'id': 123456,
#     'description': 'Lorem ipsum dolor sit amet',
#     'guid': 'a1b2c3d4e5f6',
#     'name': 'Fake Vacation',
#     'deleted_at': '2021-06-16T14:56:16Z',
#     'created_at': '2021-06-16T14:56:16Z',
#     'updated_at': '2021-06-16T14:56:16Z',
#     'type': 'LeaveType',
#     'starts_at': '2021-06-16T14:56:16Z',
#     'ends_at': '2021-06-16T14:56:16Z',
#     'parent_id': 789012,
#     'project_code': 'ABC123',
#     'secureurl': 'https://example.com',
#     'secureurl_expiration': '2021-06-16T14:56:16Z',
#     'timeentry_lockout': -1,
#     'settings': 0,
#     'project_state_id': 345678,
#     'thumbnail': 'https://example.com/thumbnail.jpg',
#     'owner_id': 901234,
#     'owner_name': 'John Doe',
#     'client': 'ACME Corp',
#     'phase_name': 'Phase 1'
# }
