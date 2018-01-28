from db.db_helper import get_session, Tag
from model.tag_object import TagObj

def add_tag(tag_obj):
    session = get_session()
    session = session()
    new_tag = Tag()
    new_tag.name = tag_obj.get_tag_name()
    session.add(new_tag)
    session.commit()
    session.refresh(new_tag)
    tag_id = new_tag
    session.close()
    return tag_id.id

def search_tag(tag):
    session = get_session()
    session = session()
    tag_query = session.query(Tag).filter(Tag.name == tag).all()
    if tag_query:
        tag_query = tag_query[0]
        tag_obj = TagObj(tag_query.name)
        tag_obj.set_tag_id(tag_query.id)
        session.close()
        return tag_obj
    else:
        session.close()
        return None


def id_tag(tag):
    tag_id = search_tag(tag)
    if tag_id:
        return tag_id.get_tag_id()
    else:
        tag_obj = TagObj(tag)
        return add_tag(tag_obj)