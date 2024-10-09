from singer_sdk import typing as th

schema = th.PropertiesList(
        th.Property("last_login_time", th.DateTimeType),
        th.Property("billrate", th.NumberType),
        th.Property("id", th.IntegerType),
        th.Property("first_name", th.StringType),
        th.Property("last_name", th.StringType),
        th.Property("account_owner", th.BooleanType),
        th.Property("archived", th.BooleanType),
        th.Property("billability_target", th.NumberType),
        th.Property("billable", th.BooleanType),
        th.Property("created_at", th.DateTimeType),
        th.Property("deleted", th.BooleanType),
        th.Property("deleted_at", th.DateTimeType),
        th.Property("discipline", th.StringType),
        th.Property("display_name", th.StringType),
        th.Property("email", th.StringType),
        th.Property("employee_number", th.StringType),
        th.Property("guid", th.StringType),
        th.Property("hire_date", th.StringType),
        th.Property("invitation_pending", th.BooleanType),
        th.Property("license_type", th.StringType),
        th.Property("location", th.StringType),
        th.Property("location_id", th.IntegerType),
        th.Property("mobile_phone", th.StringType),
        th.Property("office_phone", th.StringType),
        th.Property("role", th.StringType),
        th.Property("termination_date", th.StringType),
        th.Property("type", th.StringType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("user_settings", th.IntegerType),
        th.Property("user_type_id", th.IntegerType),
        th.Property("thumbnail", th.StringType),
        th.Property("has_login", th.BooleanType),
        th.Property("login_type", th.StringType),
        th.Property("archived_at", th.DateTimeType),
        th.Property("tags", th.ObjectType(
            th.Property("paging", th.ObjectType(
                th.Property("self", th.StringType),
                th.Property("next", th.StringType),
                th.Property("previous", th.StringType),
                th.Property("page", th.IntegerType),
                th.Property("per_page", th.IntegerType)
            )),
            th.Property("data", th.ArrayType(th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("value", th.StringType)
            )))
        )),
        th.Property("custom_field_values", th.ObjectType(
            th.Property("paging", th.ObjectType(
                th.Property("self", th.StringType),
                th.Property("next", th.StringType),
                th.Property("previous", th.StringType),
                th.Property("page", th.IntegerType),
                th.Property("per_page", th.IntegerType)
            )),
            th.Property("data", th.ArrayType(th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("custom_field_name", th.StringType),
                th.Property("custom_field_id", th.IntegerType),
                th.Property("value", th.StringType),
                th.Property("created_at", th.DateTimeType),
                th.Property("updated_at", th.DateTimeType)
            )))
        ))
    ).to_dict()