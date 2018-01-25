class PhotoObj:
    def __init__(self, name):
        self.id = None
        self.plant_id = None
        self.url = None
        self.name = name
        self.path = "imagens/plants/" + self.name

    def get_id(self):
        return self.id

    def get_plant_id(self):
        return self.plant_id

    def get_url(self):
        return self.url

    def get_path(self):
        return self.path

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_plant_id(self, plant_id):
        self.plant_id = plant_id

    def set_url(self, url):
        self.url = url

    def set_path(self, name):
        self.path = "imagens/plants/" + name
