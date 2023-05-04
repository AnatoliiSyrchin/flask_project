from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import User, Article

articles_app = Blueprint("articles_app", __name__, url_prefix="/articles", static_folder='../static')

# ARTICLES = {
#     1: {
#         'title': 'Flask',
#         'text': 'Flask article text ____________\
#             Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
#             sed do eiusmod tempor incididunt ut labore et dolore magna\
#             aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
#             ullamco laboris nisi ut aliquip ex ea commodo consequat.',
#         'author_id': 1
#     },
#     2: {
#         'title': 'Django',
#         'text': 'Django article text ____________\
#             Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
#             sed do eiusmod tempor incididunt ut labore et dolore magna\
#             aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
#             ullamco laboris nisi ut aliquip ex ea commodo consequat.',
#         'author_id': 2
#     },
#     3: {
#         'title': 'JSON:API',
#         'text': 'JSON:API article text ____________\
#             Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
#             sed do eiusmod tempor incididunt ut labore et dolore magna\
#             aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
#             ullamco laboris nisi ut aliquip ex ea commodo consequat.',
#         'author_id': 3
#     },
# }


@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles) 


@articles_app.route("/<int:article_id>/", endpoint="details")
@login_required
def article_details(article_id: int):
    article = Article.query.filter_by(id=article_id).one_or_none()
    if not article:
        raise NotFound(f"Article #{article_id} doesn't exist!")

    return render_template('articles/details.html', article=article)
