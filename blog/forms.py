from os import error
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp, Email
from blog.models import Comment, User

class RegistrationForm(FlaskForm):
  username = StringField('First name',validators=[DataRequired()])
  # https://wtforms.readthedocs.io/en/2.3.x/validators/
  email = StringField('Email',validators=[DataRequired(),Email(message='Invalid email. Please check.', granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
  # password must must be displayed as shown however password must also be betwenn 1 - 20 characters, error message is not accurate enough.
  password = PasswordField('Password',validators=[DataRequired(),Regexp('^[a-zA-Z0-9]{1,20}$',message='Your password contain invalid characters.'),EqualTo('confirm_password', message='Passwords do not match. Please try again.')])
  confirm_password = PasswordField('Confirm Password',validators=[DataRequired()])
  submit = SubmitField('Register')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('Email already exists. Please choose a different one.')



class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')

class CommentForm(FlaskForm):
  # reference needed below
    comment_box = TextAreaField('Write a comment.', validators=[DataRequired()])
    submit = SubmitField('Comment')