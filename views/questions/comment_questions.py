from flask import Blueprint, render_template, abort, url_for, redirect
from flask_login import current_user, LoginManager
from jinja2 import TemplateNotFound
from controllers.question_controller import *
from controllers.tag_controler import *
from controllers.comment_controller import *

from .forms import IncludeQuestionsForm
from model.question_object import QuestionObj
from model.tag_object import TagObj
from model.comment_object import CommentObj

comment_questions = Blueprint('comment_questions', __name__, 
                    template_folder='templates')


@comment_questions.route('/questions/comment_questions', methods=['GET', 'POST']) 
def cemment_question():
    form = CommentQuestionsForm()
    if form.validate_on_submit():
        question = QuestionObj(form..data)
        question_id = get_question(question)
        user_id = int(current_user.id)
        comment = CommentObj(form.answer.data)
        criado = comment_post(comment, question)
        if criado:
            return redirect(url_for('questions.search_questions'))
    try:
        return render_template("questions/create_question.html", form=form,title = "CadastroQuestao")
    except TemplateNotFound:
        abort(404)
 