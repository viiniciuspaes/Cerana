from flask import Flask, abort, flash, redirect, render_template, url_for, request, Blueprint, send_from_directory

from flask_bootstrap import Bootstrap
from flask_uploads import IMAGES, UploadSet, configure_uploads

from controllers.photos_controller import save_photo
from controllers.plant_controller import create_plant_register
from db.db_helper import init
from model.photo_object import PhotoObj
from model.plant_object import PlantObj
from model.user_object import UserObj

import os

from controllers.plant_controller import *
from views.plants.forms import *
from flask import request

from controllers.user_controller import validate_login, validate_sing_up, get_user_logged
from utils.parser import text_to_json, user_parser_json
from views.auth.forms import RegistrationForm, LoginForm

from views.user.profile import user as view_profile_blueprint
from views.auth.home_auth import auth as auth_blueprint
from views.home.homepage import  home as home_blueprint
from views.plants.search_plants import plants as plants_blueprint
from views.questions.search_questions import questions as questions_blueprint
from views.plants.include_plants import include_plants as include_plants_blueprint
from views.questions.include_questions import include_questions as include_questions_blueprint 
from views.questions.comment_questions import comment_questions as comment_questions_blueprint 

from flask_login import LoginManager, login_user, logout_user, login_fresh

app = Flask(__name__)
app.register_blueprint(view_profile_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(questions_blueprint)
app.register_blueprint(plants_blueprint)
app.register_blueprint(include_plants_blueprint)
app.register_blueprint(include_questions_blueprint) 
app.register_blueprint(comment_questions_blueprint) 

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['UPLOADED_PHOTOS_DEST'] = 'imagens/plants'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

Bootstrap(app)
login_manager = LoginManager()

DEBUG_MODE = False
init(drop_tables=DEBUG_MODE)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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

@app.route('/upload', methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT,"imagens/banco_planta/" )
    form = SearchPlantForm(csrf_enabled=False)
    image_names = os.listdir("././imagens/banco_planta")
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)


    plant = get_plant(form.scientific_name.data)
    if plant:
        nome_c = plant.scientific_name
        nome_comum = plant.popular_name
        reino = plant.kingdom
        descricao = plant.description
        filo = plant.phylum
        familia = plant.family
        return render_template('result_plant.html', filo = filo, familia = familia, nome_c = nome_c, nome_comum = nome_comum, reino = reino, descricao = descricao )
    return render_template("pesquisa.html", form=form,image_names=image_names)


        
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("imagens/banco_planta/", filename)
    





@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    login_manager.init_app(app)
    app.run()
