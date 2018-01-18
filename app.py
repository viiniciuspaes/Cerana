from flask import Flask, abort, flash, redirect, render_template, url_for
from flask_bootstrap import Bootstrap

from db.db_helper import init
from model.user_object import UserObj
from persistence.user_dao import search_user, add_user
from utils.parser import user_parser_json

from controllers.user_controller import validate_login, validate_sing_up, get_user_logged

from views.user.profile import profile as profile_blueprint
from views.auth.home_auth import auth as auth_blueprint
from views.home.homepage import home as home_blueprint

from flask_login import LoginManager, login_user, logout_user

app = Flask(__name__)
app.register_blueprint(profile_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(home_blueprint)
app.config['SECRET_KEY'] = 'you-will-never-guess'

Bootstrap(app)

lm = LoginManager()
lm.init_app(app)

init()


def exception_404():
    abort(404)


@lm.user_loader
def load_user(id):
    return get_user_logged(id)


@app.route('/login/open:<login>,<password>', methods=['GET'])
def get_user(login, password):

    # this method have to receive the user from the url
    user_add = UserObj(login, password)  # only for test
    add_user(user_add)
    user = search_user(login)
    # user = validate_user(login, password)
    if user:
        return user_parser_json(user)
    else:
        return "usuario nao cadastrado"


if __name__ == '__main__':
    app.run()