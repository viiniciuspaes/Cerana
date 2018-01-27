from flask import Flask, abort, flash, redirect, render_template, url_for, request, Blueprint
from flask_bootstrap import Bootstrap
from flask_uploads import IMAGES, UploadSet, configure_uploads

from controllers.photos_controller import save_photo
from controllers.plant_controller import create_plant_register
from db.db_helper import init
from model.photo_object import PhotoObj
from model.plant_object import PlantObj
from model.user_object import UserObj


from controllers.user_controller import validate_login, validate_sing_up, get_user_logged
from utils.parser import text_to_json, user_parser_json
from views.auth.forms import RegistrationForm, LoginForm

from views.user.profile import user as view_profile_blueprint
from views.auth.home_auth import auth as auth_blueprint
from views.home.homepage import  home as home_blueprint
from views.plants.search_plants import plants as plants_blueprint
from views.questions.search_questions import questions as questions_blueprint
from views.plants.include_plants import include_plants as include_plants_blueprint
from views.questions.include_questions import create_questions as create_questions_blueprint


from flask_login import LoginManager, login_user, logout_user

app = Flask(__name__)
app.register_blueprint(view_profile_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(questions_blueprint)
app.register_blueprint(plants_blueprint)
app.register_blueprint(include_plants_blueprint)
app.register_blueprint(create_questions_blueprint)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['UPLOADED_PHOTOS_DEST'] = 'imagens/plants'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)

DEBUG_MODE = False
init(drop_tables=DEBUG_MODE)


def exception_404():
    abort(404)


@login_manager.user_loader
def load_user(id):
    return get_user_logged(id)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def homepage():
    return render_template("home/index-bootstrap.html")


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
    return render_template("auth/register-bootstrap.html", form=form, title="Register")


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
    return render_template('auth/login-bootstrap.html', form=form, title="Login", error=error)


@app.route('/login/mobile', methods=['GET', 'POST'])
def login_mobile():
    receive = request.get_json()
    if receive:
        valida = validate_login(receive["login"], receive["password"])
        if not valida:
            error = 'Dados inválidos. Por favor tente novamente.'
            return text_to_json(error)
        else:
            login_user(valida[1])
            return user_parser_json(valida[0])


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('pesquisa.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_test():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        plant_obj = PlantObj("example", 'example_popular')
        plant_id = create_plant_register(plant_obj)
        photo_obj = PhotoObj(filename)
        photo_obj.set_plant_id(plant_id)
        save_photo(photo_obj)
        return filename
    return 'So para testes'


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    login_manager.init_app(app)
    app.run()
