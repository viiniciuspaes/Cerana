from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from controllers.plant_controller import *
from .forms import *
from flask import request


plants = Blueprint('plants', __name__,
                    template_folder='templates')

@plants.route('/search_plants', methods=['GET', 'POST'])
def search_plants():
    form = SearchPlantForm(csrf_enabled=False)
    if request.method == "POST":
        plant = get_plant(form.scientific_name.data)
        if plant:
            return '''
        <form method="post">
            <p><plant.scientific_name>
            <p><input type=submit value=Login>
        </form>
    '''
        else:
            return "Não achou!"
    return render_template("pesquisa.html", form=form)