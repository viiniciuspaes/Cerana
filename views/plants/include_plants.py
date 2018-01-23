from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from controllers.plant_controller import *
plants = Blueprint('include_plants', __name__,
                    template_folder='templates')

@plants.route('/plants/include_plant', methods=['GET', 'POST'])
def include_plant():
    erro = None
    form = IncludePlantForm()
    if request.method == "POST":
        create_plant_register(form.scientific_name.data, form.common_name.data, form.family.data, form.kingdom.data, form.phylum.data, form.plant_description.data)
        return render_template("/plants/search_plant.html")
