from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("user_id", th.IntegerType),
    th.Property("day0", th.NumberType),
    th.Property("day1", th.NumberType),
    th.Property("day2", th.NumberType),
    th.Property("day3", th.NumberType),
    th.Property("day4", th.NumberType),
    th.Property("day5", th.NumberType),
    th.Property("day6", th.NumberType),
    th.Property("starts_at", th.StringType),
    th.Property("ends_at", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
).to_dict()
