import os
from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from controllers.plant_controller import *
from .forms import IncludePlantForm
from model.plant_object import PlantObj
include_plants = Blueprint('include_plants', __name__,
                    template_folder='templates')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_ROOT = APP_ROOT[:-13]

@include_plants.route('/plants/include_plants', methods=['GET', 'POST'])
def include_plant():
    print("TESTE" + APP_ROOT)
    form = IncludePlantForm()
    target = os.path.join(APP_ROOT,"imagens/banco_planta/" )
    image_names = os.listdir("././imagens/banco_planta")
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)
    
    if form.validate_on_submit():
        plant = PlantObj(form.scientific_name.data, form.popular_name.data, form.family.data, form.kingdom.data, form.phylum.data, form.description.data)
        criado = create_plant_register(plant)
        if criado:
            return redirect(url_for('plants.search_plants'))
    try:
        return render_template("plant/include_plantT.html", form=form,title = "CadastroPlanta")
    except TemplateNotFound:
        abort(404)