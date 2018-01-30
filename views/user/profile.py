from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import current_user
from .forms import ProfileForm

from controllers.profile_controller import *

user = Blueprint('user', __name__,
                    template_folder='templates')


@user.route('/user/view_profile', methods=['GET', 'POST'])
def view_profile():
    form = ProfileForm()
    profile = profile_data(int(current_user.id))
    name = profile.name
    birth = profile.birth
    phone = profile.phone
    occupation = profile.occupation
    try:
        return render_template('user/profile-bootstrap.html', name = name, birth = birth, phone = phone, occupation = occupation)
    except TemplateNotFound:
        abort(404)


@user.route('/user/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    try:
        return render_template('user/edit-profile-bootstrap.html')
    except TemplateNotFound:
        abort(404)
