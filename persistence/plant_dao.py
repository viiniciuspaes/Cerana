from db.db_helper import get_session, Plant
from model.plant_object import PlantObj


def add_plant(plant_obj):
    session = get_session()
    session = session()
    new_plant = Plant()
    new_plant.scientific_name = plant_obj.get_scientific_name()
    new_plant.popular_name = plant_obj.get_popular_name()
    new_plant.family = plant_obj.get_family()
    new_plant.kingdom = plant_obj.get_kingdom()
    new_plant.phylum = plant_obj.get_phylum()
    new_plant.description = plant_obj.get_description()
    session.add(new_plant)
    session.commit()
    session.refresh(new_plant)
    plant_id = new_plant.id
    session.close()
    return plant_id


def search_plant(scientific_name):
    session = get_session()
    session = session()
    plant_query = session.query(Plant).filter(Plant.scientific_name == scientific_name)
    plant_query = plant_query[0]
    plant_obj = PlantObj(plant_query.scrientific_name, plant_query.popular_name)
    # TODO the rest of the attributes need to be returned as well
    plant_obj.set_plant_id(plant_query.id)
    session.close()

    return plant_obj


def get_all_plants():
    session = get_session()
    session = session()
    plant_query = session.query(Plant).all()
    session.close()

    return plant_query


def delete_plant(scientific_name):
    session = get_session()
    session = session()
    session.query(Plant).filter(Plant.scientific_name == scientific_name).delete()
    session.commit()
    session.close()
