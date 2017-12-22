from flask import Flask, abort, request, flash, redirect, render_template, url_for
# from flask_bootstrap import Bootstrap

from db.db_helper import init
from model.user_object import UserObj
from persistence.user_dao import search_user, add_user, validate_user
from utils.parser import user_parser_json
from views.forms import LoginForm, RegistrationForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
Bootstrap(app)
init()


def exception_404():
    abort(404)

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


@app.route('/login/create:<login>,<password>', methods=['POST'])
def create_user(login, password):

    if not request.json or 'login' not in request.json:
        exception_404()

    user = UserObj(request.json['login'], request.json['password'])
    user.set_type("student")
    add_user(user)

    return "Adicionado com sucesso {}".format(user)


@app.route('/login/update:<login>,<password>', methods=['PUT'])
def update_user(login, password):
    if not login:
        exception_404()

    user_obj = search_user(login)
    user_obj.set_password(request.json['password'])
    # TODO metodo de atualizaçao do banco


@app.route('/login/delete:<login>', methods=['DELETE'])
def delete_user(login):
    if not login:
        exception_404()
    delete_user(login)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def homepage():
    return render_template("home/index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Você se cadastrou com sucesso! Agora só precisa acessar sua conta.')

        return redirect(url_for('login'))
    return render_template("auth/register.html", form=form, title="Register")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        if not validate_user(form.email.data, form.password.data):
            error = 'Dados inválidos. Por favor tente novamente.'
            return error
        else:
            return redirect(url_for('dashboard'))
    return render_template('auth/login.html', form=form, title="Login", error=error)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return ('usuário logado, parabéns')

@app.route('/logout')
def logout():
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run()
