from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = '86a13d29b940a84c8c8a067871c226da70397817097eaf3b' 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c21105215:211052152Australia@csmysql.cs.cf.ac.uk:3306/c21105215_c21105215_flask_blog'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes

from flask_admin import Admin
from blog.views import AdminView
from blog.models import User, Post
admin = Admin(app,name='Admin panel',template_mode='bootstrap3')
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Post, db.session))

