from sqlalchemy import Column, Integer, String, Boolean
from blog.models.datebase import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True)
    email = db.Column(String(255), nullable=False, default="", server_default="")
    username = db.Column(String(256), unique=True, nullable=False)
    password = db.Column(String(256), unique=True, nullable=False)
    is_staff = db.Column(Boolean, nullable=False, default=False)


    def __repr__(self):
        return f'User {self.username}'
