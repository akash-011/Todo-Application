import os


class Config(object):
    """
    Parent config class
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQL_ALCHEMY_URI = os.getenv('DATABASE_URL')
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'


class DevelopmentConfig(Config):

    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqllite:///test_todo.db'


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
