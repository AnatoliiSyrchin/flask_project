import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "xk@(!uj(68$86abj_93uowhgo-5sosju&_x%6j=^xm*=v2!9kc"

class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"

class TestingConfig(BaseConfig):
    TESTING = True