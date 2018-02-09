from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from controllers.plant_controller import *
from .forms import *
from flask import request
import os


plants = Blueprint('plants', __name__,
                    template_folder='templates')

@plants.route('/search_plants', methods=['GET', 'POST'])
def search_plants(result=None):
    form = SearchPlantForm(csrf_enabled=False)
    image_names = os.listdir("././imagens/banco_planta")
    #print(image_names)
    if request.method == "POST":
        plant = get_plant(form.scientific_name.data)
        if plant:
            nome_c = plant.scientific_name
            nome_comum = plant.popular_name
            reino = plant.kingdom
            descricao = plant.description
            filo = plant.phylum
            familia = plant.family
            destino = plant.photodir
            return render_template('result_plant.html', filo = filo, familia = familia, nome_c = nome_c, nome_comum = nome_comum, reino = reino, descricao = descricao, destino = destino)
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
    return render_template("pesquisa.html", form=form,image_names=image_names)