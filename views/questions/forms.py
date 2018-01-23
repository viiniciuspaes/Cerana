from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class IncludeQuestionForm(FlaskForm):
    """
    Form para cadastrar pergunta.
    """
    question = StringField('Pergunta', validators=[DataRequired()])
    description = StringField('Descrição', validators=[DataRequired()])
    submit = SubmitField('Enviar Pergunta')
