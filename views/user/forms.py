from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

class ProfileForm(FlaskForm):
    """
    Form para perfil
    """
    name = StringField('Nome Usuario')
    birth = StringField('Data de nascimento')
    email = StringField('Email')
    occupation = StringField('Graduação')
    phone = StringField('Telefone')