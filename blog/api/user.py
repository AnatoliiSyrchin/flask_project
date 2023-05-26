from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.schemas import UserSchema
from blog.models.datebase import db
from blog.models import User


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }