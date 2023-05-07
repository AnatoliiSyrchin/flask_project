from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from blog.models import Article, User, Author
from blog.forms.article import CreateArticleForm
from blog.models.datebase import db

articles_app = Blueprint("articles_app", __name__, url_prefix="/articles", static_folder='../static')


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

@articles_app.route('/create', methods=['GET', 'POST'], endpoint='create')
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    user = User.query.filter_by(id=current_user.id).one_or_none()

    error = None

    if request.method == 'POST' and form.validate_on_submit():
        if not user.author:
            author = Author(user_id=user.id)
            db.session.add(author)
            db.session.commit()
            print('author created')
        article = Article(title=form.title.data, text=form.text.data, author_id=user.author.id)
        db.session.add(article)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles_app.details", article_id=article.id))

    return render_template('articles/create.html', form=form, error=error)
