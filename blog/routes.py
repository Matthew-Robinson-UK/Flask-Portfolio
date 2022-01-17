from flask import render_template, url_for, request, redirect, flash, session
import flask_login
from wtforms.widgets.core import SubmitInput
from blog import app, db
from blog.models import Rating, User, Post, Comment
from blog.forms import OrderForm, RegistrationForm, LoginForm, CommentForm, RatingForm
from flask_login import login_user, logout_user, current_user
from sqlalchemy.sql import func


@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST']) 
def home():
  order_form=OrderForm()
  posts=Post.query.all()
  if request.method == 'POST':
    order=request.form['sort']
    if order == 'date_desc':
      posts=Post.query.order_by(Post.date.desc()).all()
      return render_template('home.html', posts=posts, order_form=order_form)
    elif order == 'date_asc':
      posts=Post.query.order_by(Post.date.asc()).all()
      return render_template('home.html', posts=posts, order_form=order_form)
  return render_template('home.html', posts=posts, order_form=order_form)

@app.route("/contact") 
def contact():
  user_email = User.query.filter_by(email='robinson.matthew2@gmail.com').first()
  user_linkedin = User.query.filter_by(linkedin='https://www.linkedin.com/in/matthew-lee-robinson/').first()
  return render_template('contact.html', title='Contact', user_email = user_email, user_linkedin = user_linkedin)

@app.route("/disclaimer") 
def disclaimer():
  return render_template('disclaimer.html', title='Disclaimer')

@app.route("/privacy_policy") 
def privacy_policy():
  return render_template('privacy_policy.html', title='Privacy Policy')
    
@app.route("/post/<int:post_id>", methods=['GET','Post'])
def post(post_id):
  post = Post.query.get_or_404(post_id)
  form = CommentForm()
  rating_form = RatingForm()
  # Query containing an outerjoin to be able to combine ratings and post tables to allow average of indivdual posts to be read.
  # taken from Stack Overflow post by Carl 23 - 05 - 2018
  # accessed 10 - 01 - 2022
  # https://stackoverflow.com/questions/50477793/flask-sqlalchemy-outerjoin-with-three-tables
  ratings = db.session.query(Post.id, db.func.avg(Rating.value)).outerjoin(Rating, Post.id == Rating.post_id).group_by(Post.id).all()
  # end of referenced code.
  for p in ratings:
    if post_id == p[0]:
      try:
          avg_rating = round(p[1], 1)
      except:
          avg_rating = 0

  if form.validate_on_submit():
    # Storing the user of a comment by retrieving it from the current_user 
    # taken from werkzeug documents by Pallet Projects 2007
    # accessed 02 - 01 - 2022
    # https://werkzeug.palletsprojects.com/en/2.0.x/local/
    comment = Comment(comment=form.comment_box.data, post=post, user=current_user._get_current_object())
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('.post', post_id=post.id))
  if rating_form.is_submitted():
    rating = Rating(value = request.form['rating'], post=post, user=current_user._get_current_object())
    # end of referenced code.
    db.session.add(rating)
    db.session.commit()
    return redirect(url_for('.post', post_id=post.id))
  return render_template('post.html',title=post.title,post=post, form=form, rating_form=rating_form, avg_rating=avg_rating)

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful!', 'success')
    flask_login.login_user(user)
    flash('You\'ve successfully logged in,'+' '+ current_user.username +'!', 'success')
    return redirect(url_for('home'))   
  if form.is_submitted() and current_user.is_anonymous:
    flash('Sorry, there is a problem with your registration', 'danger')
  return render_template('register.html',title='Register',form=form)


@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('You\'ve successfully logged in,'+' '+ current_user.username +'!', 'success')
      return redirect(url_for('home'))
    return redirect(url_for('error'))
  return render_template('login.html',title='Login', form=form)


@app.route("/logout")
def logout():
  logout_user()
  flash('You\'re now logged out. Thanks for your visit!', 'success')
  return redirect(url_for('home'))

@app.route("/error") 
def error():
    return render_template('error.html', title='Login Error')
