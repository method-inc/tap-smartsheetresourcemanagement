from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("description", th.StringType),
    th.Property("guid", th.StringType),
    th.Property("name", th.StringType),
    th.Property("deleted_at", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("type", th.StringType),
).to_dict()