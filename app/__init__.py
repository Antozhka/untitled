from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
#from celery import Celery
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'Пожалуйста, войдите, чтобы открыть эту страницу.'
mail = Mail(app)
bootstrap = Bootstrap(app)

#celery = Celery(app.name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
#celery.conf.update(app.config)

from . import routes, models