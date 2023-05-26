from combojsonapi.utils import Relationship
from marshmallow_jsonapi import Schema, fields


class UserSchema(Schema):
    class Meta:
        type_ = "user"
        self_view = "user_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "user_list"

    id = fields.Integer(as_string=True)
    first_name = fields.String(allow_none=False, required=True)
    last_name = fields.String(allow_none=False, required=True)
    username = fields.String(allow_none=False, required=True)
    email = fields.Email(allow_none=False, required=True)
    is_staff = fields.Boolean(allow_none=False, required=True)

    author = Relationship(
        nested="AuthorSchema",
        attribute="author",
        related_view="author_detail",
        related_view_kwargs={"id": "<id>"},
        schema="AuthorSchema",
        type_="author",
        many=False,
    )