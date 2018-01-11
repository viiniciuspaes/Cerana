from persistence.plant_dao import add_plant, delete_plant, search_plant


def create_plant_register(plant):
    plant_result = search_plant(plant.get_scientific_name())
    if plant_result:
        return None
    else:
        add_plant(plant)
        return plant


def exists(plant):
    return True if search_plant(plant.get_scientific_name()) else False


def erase_plant(plant):
    delete_plant(plant.get_scientific_name())


def update_plant(user):
    pass


def get_plant(scientific_name):
    return search_plant(scientific_name)
