class PlantObj:
    def __init__(self, cientifc_name, popular_name,family=None,kingdom=None,phylum=None,description=None, photodir=None):
        self.plant_id = None
        self.scientific_name = cientifc_name
        self.popular_name = popular_name
        self.family = family
        self.kingdom = kingdom
        self.phylum = phylum
        self.description = description
        self.photodir = photodir
    
    def get_photodir(self):
        return self.photodir
    
    def set_photodir(self, photo_dir):
        self.photodir=photo_dir

    def get_plant_id(self):
        return self.plant_id

    def get_scientific_name(self):
        return self.scientific_name

    def get_popular_name(self):
        return self.popular_name

    def get_family(self):
        return self.family

    def get_kingdom(self):
        return self.kingdom

    def get_phylum(self):
        return self.phylum

    def get_description(self):
        return self.description

    def set_scientific_name(self, name):
        self.scientific_name = name

    def set_popular_name(self, name):
        self.popular_name =  name

    def set_family(self, family):
        self.family = family

    def set_phylum(self, phylum):
        self.phylum = phylum

    def set_description(self, description):
        self.description = description

    def set_plant_id(self, id):
        self.plant_id = id

    def set_kingdom(self, kingdom):
        self.kingdom = kingdom
