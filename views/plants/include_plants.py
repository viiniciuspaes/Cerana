from flask import Blueprint, render_template, abort, redirect, url_for
from jinja2 import TemplateNotFound
from controllers.plant_controller import *
from .forms import IncludePlantForm
from model.plant_object import PlantObj
include_plants = Blueprint('include_plants', __name__,
                    template_folder='templates')

@include_plants.route('/plants/include_plants', methods=['GET', 'POST'])
def include_plant():
    erro = None
    form = IncludePlantForm()
    if form.validate_on_submit():
        plant = PlantObj(form.scientific_name.data, form.popular_name.data, form.family.data, form.kingdom.data, form.phylum.data, form.plant_description.data)
        criado = create_plant_register(plant)
        if criado:
            return redirect(url_for('plants.search_plants'))
    try:
        return render_template("plant/include_plantT.html", form=form,title = "CadastroPlanta")
    except TemplateNotFound:
        abort(404)

