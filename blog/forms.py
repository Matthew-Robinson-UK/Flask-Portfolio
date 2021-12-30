from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp, Email
from blog.models import User

class RegistrationForm(FlaskForm):
  username = StringField('First name',validators=[DataRequired()])
  email = StringField('Email',validators=[DataRequired(),Email(message='Please check your email is correct and try again', granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
  password = PasswordField('Password',validators=[DataRequired(),Regexp('^[a-zA-Z0-9]{1,20}$',message='Your password should be up to 20 characters long, containing letters and numbers only.'),EqualTo('confirm_password', message='Passwords do not match. Please try again.')])
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
