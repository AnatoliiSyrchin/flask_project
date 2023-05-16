from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from blog.models.datebase import db
from blog.models.tags_articles import tag_article_association_table



class Tag(db.Model):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)

    articles = relationship('Article', secondary=tag_article_association_table, back_populates='tags')

