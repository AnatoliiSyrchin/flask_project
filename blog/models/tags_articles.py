from sqlalchemy import Column, Integer, ForeignKey, Table
from blog.models.datebase import db
#from blog.models.articles import Article

tag_article_association_table = Table(
    'tag_article_association',
    db.metadata,
    Column('tag_id', Integer, ForeignKey('tags.id'), nullable=False),
    Column('article_id', Integer, ForeignKey('articles.id'), nullable=False),
)


