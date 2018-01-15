from flask import Flask, abort, flash, redirect, render_template, url_for
from flask_bootstrap import Bootstrap

from db.db_helper import init
from model.user_object import UserObj
from persistence.user_dao import search_user, add_user
from utils.parser import user_parser_json
from views.forms import LoginForm, RegistrationForm

from controllers.user_controller import validate_login, validate_sing_up, get_user_logged
from views.user.profile import profile as profile_blueprint

from flask_login import LoginManager, login_user, logout_user

app = Flask(__name__)
app.register_blueprint(profile_blueprint)
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


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def homepage():
    return render_template("home/index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = UserObj(form.email.data, form.password.data)
        valida = validate_sing_up(user)
        if valida:
            flash('Você se cadastrou com sucesso!')
            return redirect(url_for('login'))
        else:
            flash('usuario ja cadastrado!')
    return render_template("auth/register.html", form=form, title="Register")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        valida = validate_login(form.email.data, form.password.data)
        if not valida:
            error = 'Dados inválidos. Por favor tente novamente.'
            return error
        else:
            login_user(valida[1])
            return redirect(url_for('dashboard'))
    return render_template('auth/login.html', form=form, title="Login", error=error)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('teste.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run()