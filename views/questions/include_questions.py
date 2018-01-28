from flask import Blueprint, render_template, abort, url_for, redirect
from flask_login import current_user, LoginManager
from jinja2 import TemplateNotFound
from controllers.question_controller import *
from controllers.tag_controler import *

from .forms import IncludeQuestionsForm
from model.question_object import QuestionObj
from model.tag_object import TagObj

include_questions = Blueprint('include_questions', __name__, 
                    template_folder='templates')


@include_questions.route('/questions/include_questions', methods=['GET', 'POST']) 
def include_question():
    form = IncludeQuestionsForm()
    if form.validate_on_submit():
        tag = TagObj(form.tag.data)
        tag_id = create_tag_tag_register(tag)
        user_id = int(current_user.id)
        question = QuestionObj(form.question.data, form.description.data, tag_id, user_id)
        criado = create_question(question)
        if criado:
            return redirect(url_for('questions.search_questions'))
    try:
        return render_template("questions/create_question.html", form=form,title = "CadastroQuestao")
    except TemplateNotFound:
        abort(404)
 