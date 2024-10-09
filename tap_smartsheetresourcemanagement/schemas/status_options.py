from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("label", th.StringType),
    th.Property("color", th.StringType),
    th.Property("stage", th.StringType),
    th.Property("order", th.NumberType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("deleted_at", th.DateTimeType),
).to_dict()