from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from controllers.question_controller import *
from controllers.tag_controler import *

from .forms import IncludeQuestionsForm
from model.question_object import QuestionObj

create_questions = Blueprint('create_questions', __name__,
                    template_folder='templates')

@create_questions.route('/questions/create_questions', methods=['GET', 'POST'])
def include_question():
    form = IncludeQuestionsForm()
    if form.validate_on_submit():
        tag_id = search_tag(form.tag.data)
        question = QuestionObj(form.question.data, form.description.data, tag_id)
        criado = create_question(question)
        if criado:
            return redirect(url_for('plants.search_plants'))
    try:
        return render_template("questions/create_question.html", form=form,title = "CadastroQuestao")
    except TemplateNotFound:
        abort(404)
