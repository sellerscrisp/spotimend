from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length

# from spotimend.utils.api.spotify_handler import SpotifyHandler

# spotify = SpotifyHandler()


class UserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    # confirm_password = PasswordField(
    #     'Confirm Password',
    #     validators=[DataRequired()]
    # )
    email = StringField('Email', validators=[InputRequired()])


class DeleteForm(FlaskForm):
    """Delete form – intentionally left blank."""
