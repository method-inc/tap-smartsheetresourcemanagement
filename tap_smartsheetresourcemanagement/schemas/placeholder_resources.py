from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("title", th.StringType),
    th.Property("user_type_id", th.IntegerType),
    th.Property("guid", th.StringType),
    th.Property("role", th.StringType),
    th.Property("discipline", th.StringType),
    th.Property("location", th.StringType),
    th.Property("displayName", th.StringType),
    th.Property("type", th.StringType),
    th.Property("thumbnail", th.StringType),
    th.Property("abbreviation", th.StringType),
    th.Property("color", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("billrate", th.NumberType),
).to_dict()