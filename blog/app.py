from flask import Flask

from blog.users.views import users_app
from blog.articles.views import articles_app
from blog.models.datebase import db
from blog.auth.view import auth_app, login_manager


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "abcdefg123456"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth_app)
