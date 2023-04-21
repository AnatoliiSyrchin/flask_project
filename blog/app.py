from flask import Flask

from blog.users.views import users_app
from blog.articles.views import articles_app


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
