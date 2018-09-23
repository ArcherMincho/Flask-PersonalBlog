from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class RegistrationForm(Form):
    str1 = 'Usernames must be only letters, numbers, dots or underscores'
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), \
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, str1)])
    password = PasswordField('Password', validators=[DataRequired(), \
                                                     EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password again', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError('Invalid email.')


class PasswordResetForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    new_password = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Change my password now.')

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError("Email haven't been registered.")


class ChangePasswordForm(Form):
    password = PasswordField('New Password', validators=[DataRequired(), \
                                                         EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')


class ChangeEmailForm(Form):
    newemail = StringField('New Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Change my email address now.')

    def validate_newemail(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_password(self, field):
        print(current_user)
        if not current_user.verify_password(field.data):
            raise ValidationError('Wrong password.')
