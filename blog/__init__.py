from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = '86a13d29b940a84c8c8a067871c226da70397817097eaf3b' 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes