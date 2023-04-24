from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import User

articles_app = Blueprint("articles_app", __name__, url_prefix="/articles", static_folder='../static')

ARTICLES = {
    1: {
        'title': 'Flask',
        'text': 'Flask article text ____________\
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'author_id': 1
    },
    2: {
        'title': 'Django',
        'text': 'Django article text ____________\
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'author_id': 2
    },
    3: {
        'title': 'JSON:API',
        'text': 'JSON:API article text ____________\
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'author_id': 3
    },
}


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES) 


@articles_app.route("/<int:article_id>/", endpoint="details")
@login_required
def article_details(article_id: int):
    try:
        article = ARTICLES[article_id]
    except KeyError:
        raise NotFound(f"Article #{article_id} doesn't exist!")

    users = User.query.all()
    user = User.query.filter_by(id=article['author_id']).one_or_none()

    return render_template(
        'articles/details.html',
        article_title=article['title'],
        article_text=article['text'],
        article_author_id=user.id if user else None,
        article_author_name=user.username if user else None,
    )
