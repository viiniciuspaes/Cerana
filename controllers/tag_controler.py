from persistence.tag_dao import add_tag, search_tag
from model.tag_object import TagObj


def create_tag_tag_register(tag):
    tag_result = search_tag(tag.get_tag_name())
    if tag_result:
        return tag_result.get_tag_id()
    else:
        tag_id = add_tag(tag)
        return tag_id


def get_tag(tag):
    return search_tag(tag)