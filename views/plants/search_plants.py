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
            nome_c = plant.scientific_name
            nome_comum = plant.popular_name
            reino = plant.kingdom
            descricao = plant.description
            filo = plant.phylum
            familia = plant.family
            return render_template('result_plant.html', filo = filo, familia = familia, nome_c = nome_c, nome_comum = nome_comum, reino = reino, descricao = descricao )
            #result = plant(request.args['family'])
            #return render_template('pesquisa.html', result=result)
            #'''
        #<form method="post">
            #<p><plant.scientific_name>
            #<p><input type=submit value=Login>
        #</form>
   #'''
        else:
            return "Não achou!"
    return render_template("pesquisa.html", form=form)