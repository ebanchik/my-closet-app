# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '2t0RRAGGyVuJZ7fzwYrFcavgJptKzqCo'  # Change this to a strong, random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
csrf.init_app(app)

from app import models  # noqa: F401
from app import routes  # noqa: F401
