from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

class ProfileForm(FlaskForm):
    """
    Form para perfil
    """
  