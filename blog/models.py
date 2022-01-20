from datetime import datetime
from sqlalchemy import UniqueConstraint
from blog import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  title = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)
  description = db.Column(db.String(250), nullable=False)
  image_file = db.Column(db.String(40), nullable=False, default='default.jpg')
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  comments = db.relationship('Comment', backref='post')
  ratings = db.relationship('Rating', backref='post')

  def __repr__(self):
    return f"Post('{self.date}', '{self.title}', '{self.content}')"


class Comment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  comment = db.Column(db.Text, nullable=False)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

  def __repr__(self):
    return f"Comment('{self.date}', '{self.comment}', '{self.author_id}')"

class Rating(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  value = db.Column(db.Integer(), nullable=False)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
  # Unique constraint to allow a user to rate a each post only once
  # taken from SQLAlchemy 1.4 documentation 19 - 01 - 2022
  # accessed 20 - 01 -21
  # https://docs.sqlalchemy.org/en/14/core/constraints.html#sqlalchemy.schema.PrimaryKeyConstraint
  __table_args__ = (UniqueConstraint('author_id','post_id', name='_user_post_rating'),)
  # end of referenced code
  def __repr__(self):
    return f"Rating('{self.date}', '{self.value}', '{self.author_id}')"


class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20))
  email = db.Column(db.String(120), unique=True, nullable=False)
  hashed_password=db.Column(db.String(128), unique=True, nullable=False)
  post = db.relationship('Post', backref='user', lazy=True)
  comments = db.relationship('Comment', backref='user')
  ratings = db.relationship('Rating', backref='user')
  linkedin = db.Column(db.String(120))
  is_admin=db.Column(db.Boolean,nullable=False,default=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

#adated from Grinberg(2014, 2018)
  @property
  def password(self):
    raise AttributeError('Password is not readable.')

  @password.setter
  def password(self,password):
    self.hashed_password=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.hashed_password,password)


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))