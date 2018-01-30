from flask import Blueprint, render_template, abort, url_for, redirect
from flask_login import current_user, LoginManager
from jinja2 import TemplateNotFound
from controllers.question_controller import *
from controllers.tag_controler import *
from controllers.comment_controller import *

from .forms import CommentQuestionsForm, SearchQuestionsForm
from model.question_object import QuestionObj
from model.tag_object import TagObj
from model.comment_object import CommentObj

comment_questions = Blueprint('comment_questions', __name__, 
                    template_folder='templates')


@comment_questions.route('/questions/comment_questions', methods=['GET', 'POST']) 
def comment_question():
    formC = CommentQuestionsForm(csrf_enabled=False)
    if formC.validate_on_submit():
        question = get_question(formC.question.data)
        #comment_obj.set_user_id(current_user.id)
        question_id = question.get_question_id()
        #comment_obj.set_question_id(question_id)
        user_id = int(current_user.id)
        #comment_obj.set_user_id(current_user.id)
        answer = CommentObj(formC.answer.data, question_id, user_id)
        criado = comment_post(answer)
        pergunta = question.get_question()
        resposta = criado.get_answer()
        if criado:
             return render_template('result_answer.html', formC=formC, resposta = resposta, pergunta = pergunta )
        else:
            return "Não encontrado"
    return render_template("questions/pesquisa_pergunta.html", form=form)
 