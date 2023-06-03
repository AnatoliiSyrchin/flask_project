import os
from flask import Flask
from flask_migrate import Migrate

from blog.users.views import users_app
from blog.articles.views import articles_app
from blog.authors.views import authors_app
from blog.tags.views import tags_app
from blog.models.datebase import db
from blog.auth.views import auth_app, login_manager
from blog.admin.views import admin_app
from blog.api import init_api


def create_app() -> Flask:

    app = Flask(__name__)

    cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
    app.config.from_object(f"blog.config.{cfg_name}")
    
    register_extensions(app)
    register_blueprints(app)
    
    return app

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    admin_app.init_app(app)
    api = init_api(app)
    migrate = Migrate(app, db, compare_type=True)

def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(tags_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(authors_app)