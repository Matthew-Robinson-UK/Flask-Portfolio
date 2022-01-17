from os import error
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.fields import SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp, Email
from blog.models import User

class RegistrationForm(FlaskForm):
  username = StringField('First name',validators=[DataRequired(), Regexp('^[a-zA-Z0-9]{1,20}$',message='Your first name contains invalid characters or is over 20 characters long.')])
  # Email validators
  # taken from WTFroms documentation by WTForms 2008
  # accessed 20 - 12 - 2021
  # https://wtforms.readthedocs.io/en/2.3.x/validators/
  email = StringField('Email',validators=[DataRequired(),Email(message='Invalid email. Please check.', granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
  # end of referenced code.
  password = PasswordField('Password',validators=[DataRequired(),Regexp('^[a-zA-Z0-9]{1,20}$',message='Your password contain invalid characters or is over 20 characters long.'),EqualTo('confirm_password', message='Passwords do not match. Please try again.')])
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
    comment_box = TextAreaField('Write a comment.', validators=[DataRequired()])
    submit = SubmitField('Comment')
# code used for a star emoji
# taken from iemoji website 2010
# accessed 05 - 01 - 2022
# http://www.iemoji.com/view/emoji/586/animals-nature/white-medium-star
class RatingForm(FlaskForm):
  rating = SelectField(u'Select a rating', coerce=int, choices=[('1', u"\u2B50"), ('2', u"\u2B50"u"\u2B50"), ('3', u"\u2B50"u"\u2B50"u"\u2B50"), ('4', u"\u2B50"u"\u2B50"u"\u2B50"u"\u2B50"), ('5', u"\u2B50"u"\u2B50"u"\u2B50"u"\u2B50"u"\u2B50")],validators=[DataRequired()])
  submit = SubmitField('Rating')
# end of referenced code.
class OrderForm(FlaskForm):
  sort = SelectField(u'Select an order', choices=[('date_asc','Ascending'), ('date_desc', 'Descending')], validators=[DataRequired()])
  submit = SubmitField('sort')
