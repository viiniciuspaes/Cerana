from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from controllers.question_controller import *
from .forms import *
from flask import request


questions = Blueprint('questions', __name__,
                    template_folder='templates')

@questions.route('/search_questions', methods=['GET', 'POST'])
def search_questions():
    form = SearchQuestionsForm(csrf_enabled=False)
    if request.method == "POST":
        question = get_question(form.question.data)
        if question:
            return question.get_question()
        else:
            return "nao achou"
    return render_template("questions/pesquisa_pergunta.html", form=form)