from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class IncludePlantForm(FlaskForm):
    """
    Form para cadastrar planta.
    """
    scientific_name = StringField('Nome Científico', validators=[DataRequired()])
    common_name = StringField('Nome Comum', validators=[DataRequired()])
    family = StringField('Família', validators=[DataRequired()])
    kingdom	= StringField('Reino', validators=[DataRequired()])
    phylum = StringField('Filo', validators=[DataRequired()])
    #photograph =
    plant_description = StringField('Descrição', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Planta')

class SearchPlantForm(FlaskForm):
    """
    Form para pesquisar planta.
    """
    scientific_name = StringField('Nome Científico da Planta', validators=[DataRequired()])
    submit = SubmitField('Pesquisar Planta')