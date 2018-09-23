from flask_wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField, \
    SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User


class EditProfileForm(Form):
    str1 = 'Usernames must be only letters, numbers, dots or underscores'
    username = StringField('Username', validators=[DataRequired(), \
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, str1)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def validate_username(self, field):
        if field.data != current_user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class EditProfileAdminForm(Form):
    role = SelectField('Role', coerce=int)
    str1 = 'Usernames must be only letters, numbers, dots or underscores'
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), \
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, str1)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(Form):
    body = PageDownField('Write down your mind here.', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_body(self, field):
        if current_user is None:
            raise ValidationError('please login first.')


class CommentForm(Form):
    body = StringField('Write down your comment here', validators=[DataRequired()])
    submit = SubmitField('Submit')
