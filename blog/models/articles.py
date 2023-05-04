from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from blog.models.datebase import db


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    Text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    author = relationship('Author', back_populates='aritcle')