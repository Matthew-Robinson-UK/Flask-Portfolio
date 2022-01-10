import re
from flask import render_template, url_for, request, redirect, flash
import flask_login
from wtforms.fields import choices
from wtforms.widgets.core import SubmitInput
from blog import app, db
from blog import forms
from blog.models import Rating, User, Post, Comment
from blog.forms import OrderForm, RegistrationForm, LoginForm, CommentForm, RatingForm
from flask_login import login_user, logout_user, current_user


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
    
@app.route("/post/<int:post_id>", methods=['GET','Post'])
def post(post_id):
  post = Post.query.get_or_404(post_id)
  # possibly change form to more descriptive comment_form
  form = CommentForm()
  rating_form = RatingForm()
  # reference needed below
  if form.validate_on_submit():
    comment = Comment(comment=form.comment_box.data, post=post, user=current_user._get_current_object())
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('.post', post_id=post.id))
  if rating_form.is_submitted():
    if current_user.ratings == []:
      # https://python-adv-web-apps.readthedocs.io/en/latest/flask_db3.html
      rating = Rating(value = request.form['rating'], post=post, user=current_user._get_current_object())
      db.session.add(rating)
      db.session.commit()
      return redirect(url_for('.post', post_id=post.id))
    else:
      flash('You are only able to rate a post once ', 'danger')
      return redirect(url_for('.post', post_id=post.id))
  return render_template('post.html',title=post.title,post=post, form=form, rating_form=rating_form)

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


@app.route("/registered")
def registered():
  return render_template('registered.html', title='Thanks!')

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
