import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never quess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    POSTS_PER_PAGE = 10
    '''
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    '''
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'gasht.examples@gmail.com'
    MAIL_PASSWORD = 'cfvsqkexibqgfhjkm'
    MAIL_DEFAULT_SENDER = 'flask@example.com'
    ADMINS = ['agashturi@gmail.com']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #CELERY_BROKER_URL = 'redis://localhost:6379/0'
    #CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    #CELERY_BROKER_URL = 'amqp://'
    #CELERY_RESULT_BACKEND = 'amqp'