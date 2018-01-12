from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/profile')
def show():
    try:
        return render_template('user.html')
    except TemplateNotFound:
        abort(404)