from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from controllers.question_controller import *

questions = Blueprint('questions', __name__,
                    template_folder='templates')
'''
@questions.route('/questions', methods=['GET', 'POST'])
def homepage():
    try:
        return render_template("/questions/Pergunta.html")
    except TemplateNotFound:
        abort(404)
'''

@questions.route('/questions/include_questions', methods=['GET', 'POST'])
def include_question():
    erro = None
    form = IncludeQuestionForm()
    if request.method == "POST":
        create_question(form.question.data, form.description.data)
        return render_template('/questions/search_pergunta.html')
