from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("date", th.StringType),
    th.Property("name", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
).to_dict()