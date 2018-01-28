from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class IncludeQuestionsForm(FlaskForm):
    """
    Form para cadastrar pergunta.
    """
    question = StringField('Pergunta', validators=[DataRequired()])
    description = StringField('Descrição', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Enviar Pergunta')

class SearchQuestionsForm(FlaskForm):
    """
    Form para pesquisar pergunta.
    """
    question = StringField('Digite a Pergunta', validators=[DataRequired()])
    submit = SubmitField('Pesquisar')
    
class CommentQuestionsForm(FlaskForm):
    """
    Form para comentar pergunta
    """
    answer = StringField('Digite a Pergunta', validators=[DataRequired()])
    submit = SubmitField('Enviar')
