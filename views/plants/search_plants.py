from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from controllers.plant_controller import *
plants = Blueprint('plants', __name__,
                    template_folder='templates')

@plants.route('search_plant', methods=['GET', 'POST'])
def include_plants():
    erro = None
    form = IncludePlantForm()
    if request.method == "POST":
        get_plant(form.scientific_name.data)
        return render_template("/plants/search_plant.html")
