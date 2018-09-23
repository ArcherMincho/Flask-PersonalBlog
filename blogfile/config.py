import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'qing.blog'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qq.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = 874850627
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'archer996.'
    FLASKY_MAIL_SUBJECT_PREFIX = '[BLOG of ECHO]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <a874850627@qq.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'a874850627@qq.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 2
    FLASKY_FOLLOWERS_PER_PAGE = 2
    FLASKY_COMMENTS_PER_PAGE = 2

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:qing1234.@localhost:3306/blog'
    SQLALCHEMY_COMMIT_ON_TEAMDOWN = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
