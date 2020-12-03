import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Upload configuration
    UPLOAD_FOLDER = '/app/uploads'
    ALLOWED_EXTENSIONS = {'blend'}

    # Mail configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    #flask admin theme
    FLASK_ADMIN_SWATCH = 'slate'

    LANGUAGES = ['en']

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

class DevelopmentConfig(Config):
    SECRET_KEY = "n378adfncvxz9z"

config = {
'development': DevelopmentConfig,
'testing': DevelopmentConfig,
'production': DevelopmentConfig
}
