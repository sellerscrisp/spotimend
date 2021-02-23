import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "postgresql:///spotimend"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql:///spotimend'


class TestingConfig(Config):
    TESTING = True


config_settings = {
    'production': ProductionConfig,
    'staging': StagingConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
