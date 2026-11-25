from marshmallow import Schema, fields, validate


class RegisterSchema(Schema):

    username = fields.String(
        required=True,
        validate=validate.Length(min=3, max=30)
    )

    email = fields.Email(required=True)

    password = fields.String(
        required=True,
        validate=validate.Length(min=8)
    )

    first_name = fields.String(required=True)

    last_name = fields.String(required=True)


class LoginSchema(Schema):

    email = fields.Email(required=True)

    password = fields.String(required=True)

    role = fields.String(
        load_default="viewer",
        validate=validate.OneOf([
            "admin",
            "manager",
            "technician",
            "viewer"
        ])
    )