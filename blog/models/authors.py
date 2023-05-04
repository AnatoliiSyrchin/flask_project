from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from blog.models.datebase import db


class Author(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship('User', back_populates='author')
    article = relationship('Article', back_populates='author')