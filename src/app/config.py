import os


BASEDIR = os.path.abspath(os.getcwd())

class Config():
    DEBUG = False
    DATE_FORMAT = '%Y-%m-%d'


class ProductionConfig(Config):
    SERVER_NAME = '127.0.0.1:5000'
    PREFERRED_URL_SCHEME = 'https'
    ENV = 'production'
    DEBUG = False


class DevelopmentConfig(Config):
    SERVER_NAME = 'localhost:5000'
    PREFERRED_URL_SCHEME = 'http'
    ENV = 'development'
    DEBUG = True
