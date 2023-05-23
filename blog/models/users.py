from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship

from blog.models.datebase import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True, default="", server_default="")
    username = Column(String(256), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    first_name = Column(String(255), unique=False, nullable=False, default='', server_default='')
    last_name = Column(String(255), unique=False, nullable=False, default='', server_default='')
    _password = Column(Text, nullable=True)

    author = relationship('Author', uselist=False, back_populates='user')

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return check_password_hash(self._password, password)

    def __repr__(self):
        return f'User {self.username}'
    
    def __str__(self):
        return self.username
