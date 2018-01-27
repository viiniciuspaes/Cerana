from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

user = Blueprint('user', __name__,
                    template_folder='templates')


@user.route('/user/view_profile', methods=['GET', 'POST'])
def view_profile():
    try:
        return render_template('user/profile-bootstrap.html')
    except TemplateNotFound:
        abort(404)

'''
@profile.route('/profile/edit_profile', methods=['GET', 'POST'])
def update_profile():
    try:
        return render_template('user/edit_profile.html')
    except TemplateNotFound:
        abort(404)
'''