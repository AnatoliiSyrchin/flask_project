from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship


class ArticleSchema(Schema):
    class Meta:
        type_ = "article"
        self_view = "article_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "article_list"
        
    id = fields.Integer(as_string=True)
    title = fields.String(allow_none=False, required=True)
    text = fields.String(allow_none=False, required=True)
    created_at = fields.DateTime(allow_none=True)
    updated_at = fields.DateTime(allow_none=True)

author = Relationship(
    nested="AuthorSchema",
    attribute="author",
    related_view="author_detail",
    related_view_kwargs={"id": "<id>"},
    schema="AuthorSchema",
    type_="author",
    many=False,
)
tags = Relationship(
    nested="TagSchema",
    attribute="tags",
    related_view="tag_detail",
    related_view_kwargs={"id": "<id>"},
    schema="TagSchema",
    type_="tag",
)