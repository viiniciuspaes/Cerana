from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from .forms import ProfileForm


user = Blueprint('user', __name__,
                    template_folder='templates')


@user.route('/user/view_profile', methods=['GET', 'POST'])
def view_profile():
    form = ProfileForm()
    try:
        return render_template('user/profile-bootstrap.html')
    except TemplateNotFound:
        abort(404)


@user.route('/user/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    try:
        return render_template('user/edit-profile-bootstrap.html')
    except TemplateNotFound:
        abort(404)
