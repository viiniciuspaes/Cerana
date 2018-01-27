class TagObj:
    def __init__(self, name):
        self.tag_name = name
        self.tag_id = None

    def get_tag_name(self):
        return self.tag_name

    def set_tag_name(self, name):
        self.tag_name = name

    def get_tag_id(self):
        return self.tag_id

    def set_tag_id(self, id):
        self.tag_id = id
