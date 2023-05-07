from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import Author


authors_app = Blueprint("authors_app", __name__, url_prefix="/authors", static_folder='../static')


@authors_app.route("/", endpoint="list")
def users_list():
    authors = Author.query.all()
    return render_template("authors/list.html", authors=authors)


@authors_app.route("/<int:author_id>/", endpoint="details")
@login_required
def author_details(author_id: int):
    author = Author.query.filter_by(id=author_id).one_or_none()
    
    if author is None:
        raise NotFound(f"User #{author_id} doesn't exist!")
    

    return render_template('authors/details.html', author_id=author_id, author=author)
