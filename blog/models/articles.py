from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Table
from sqlalchemy.orm import relationship
from blog.models.datebase import db
from blog.models.tags_articles import tag_article_association_table


#tag_article_association_table = Table(
#    'tag_article_association',
#    db.metadata,
#    Column('tag_id', Integer, ForeignKey('tags.id'), nullable=False),
#    Column('article_id', Integer, ForeignKey('articles.id'), nullable=False),
#)


class Article(db.Model):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=tag_article_association_table, back_populates='articles')

    def __str__(self):
        return self.title
