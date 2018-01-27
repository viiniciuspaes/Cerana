from persistence.tag_dao import add_tag, search_tag
from model.tag_object import TagObj

def create_tag_tag_register(tag):
    tag_result = search_tag(tag.get_nome())
    if tag_result:
        return None
    else:
        add_tag(tag)
        return tag


def get_tag(tag):
    return search_tag(tag)