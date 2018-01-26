from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from controllers.plant_controller import *
from .forms import *
from flask import request


plants = Blueprint('plants', __name__,
                    template_folder='templates')

@plants.route('/search_plants', methods=['GET', 'POST'])
def search_plants(result=None):
    form = SearchPlantForm(csrf_enabled=False)
    if request.method == "POST":
        plant = get_plant(form.scientific_name.data)
        if plant:
            filo = plant.phylum
            familia = plant.family
            return filo, familia
            #result = plant(request.args['family'])
            #return render_template('pesquisa.html', result=result)
            #''' 
        #<form method="post"> 
            #<p><plant.scientific_name> 
+
            #<p><input type=submit value=Login> 
        #</form> 
   #''' 
        else:
            return "Não achou!"
    return render_template("pesquisa.html", form=form)