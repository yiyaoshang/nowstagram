# -*- encoding=utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')
app.secret_key = 'newcoder'
db = SQLAlchemy(app)
login_manager = LoginManager(app)


from nowstagram import models,views