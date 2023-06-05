import os

from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv('FLASK_ENV' or 'production')
DEBUG = ENV == 'development'


SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True

FLASK_ADMIN_SWATCH = "slate"

OPENAPI_URL_PREFIX = '/api/swagger'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.1.6'
