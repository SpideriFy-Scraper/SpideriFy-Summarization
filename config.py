from dotenv import dotenv_values
config = dotenv_values(".summarization.env")

class Config(object):
    """Base config, uses staging Database Server."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config["SECRET_KEY"]

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    DEVELOPMENT = True
    TESTING = True
    PROPAGATE_EXCEPTIONS = True

