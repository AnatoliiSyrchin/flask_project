from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from blog.models import Article, Tag
from blog.forms.tag import CreateTagForm
from blog.models.datebase import db


tags_app = Blueprint("tags_app", __name__, url_prefix="/tags", static_folder='../static')


@tags_app.route("/", endpoint="list")
def tags_list():
    tags = Tag.query.all()
    return render_template("tags/list.html", tags=tags) 

@tags_app.route("/<int:tag_id>/", endpoint="details")
@login_required
def tag_details(tag_id: int):
    tag = Tag.query.filter_by(
        id=tag_id
        ).options(
            joinedload(Tag.articles)
        ).one_or_none()
    # tags = Tag.query.filter_by(id=article.id).one_ore_more()
    if not tag:
        raise NotFound(f"Tag #{tag_id} doesn't exist!")

    return render_template('tags/details.html', tag=tag)

@tags_app.route('/create', methods=['GET', 'POST'], endpoint='create')
@login_required
def create_tag():
    form = CreateTagForm(request.form)
    error = None

    if request.method == 'POST' and form.validate_on_submit():
        tag = Tag(name=form.name.data)
        db.session.add(tag)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new tag!")
            error = "Could not create tag!"
        else:
            return redirect(url_for("tags_app.details", tag_id=tag.id))

    return render_template('tags/create.html', form=form, error=error)
