import os


class BaseConfig(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "xk@(!uj(68$86abj_93uowhgo-5sosju&_x%6j=^xm*=v2!9kc"
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = "slate"
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '5.0.0-alpha.14'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost:5432/blog"
