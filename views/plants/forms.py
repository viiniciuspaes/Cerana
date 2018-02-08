from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class IncludePlantForm(FlaskForm):
    """
    Form para cadastrar planta.
    """
    scientific_name = StringField('Nome Científico', validators=[DataRequired()])
    popular_name = StringField('Nome Comum', validators=[DataRequired()])
    family = StringField('Família', validators=[DataRequired()])
    kingdom = StringField('Reino', validators=[DataRequired()])
    phylum = StringField('Filo', validators=[DataRequired()])
    foto = SubmitField('Enviar foto')
    description = StringField('Descrição', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class SearchPlantForm(FlaskForm):
    """
    Form para pesquisar planta.
    """
    scientific_name = StringField('Nome Científico da Planta', validators=[DataRequired()])
    submit = SubmitField('Pesquisar Planta')