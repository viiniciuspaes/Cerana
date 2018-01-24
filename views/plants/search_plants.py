from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from controllers.plant_controller import *
plants = Blueprint('plants', __name__,
                    template_folder='templates')

@plants.route('/search_plants', methods=['GET', 'POST'])
def search_plants():
    erro = None
    form = SearchPlantForm()
    if request.method == "POST":
        plant = PlantObj(get_plant(form.scientific_name.data))
        return render_template("pesquisa.html")
