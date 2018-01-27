from db.db_helper import get_session, Photo
from model.photo_object import PhotoObj


def add_photo(photo_obj):
    session = get_session()
    session = session()
    new_photo = Photo()
    new_photo.plant_id = photo_obj.get_plant_id()
    new_photo.url = photo_obj.get_url()
    new_photo.path = photo_obj.get_path

    session.add(new_photo)
    session.commit()
    session.refresh(new_photo)
    photo_id = new_photo.id
    session.close()
    return photo_id


def search_photo(name):
    path = "imagens/plants/" + name
    session = get_session()
    session = session()
    photo_query = session.query(Photo).filter(Photo.path == path).all()
    if len(photo_query) > 0:
        photo_query = photo_query[0]
    if photo_query:
        photo_obj = PhotoObj(name)
        photo_obj.set_plant_id(photo_query.plant_id)
        photo_obj.set_path(photo_query.path)
        photo_obj.set_url(photo_query.url)
        photo_obj.set_id(photo_query.id)
        session.close()
        return photo_obj
    else:
        session.close()
        return None


def delete_photo(name):
    path = "imagens/plants/" + name
    session = get_session()
    session = session()
    session.query(Photo).filter(Photo.path == path).delete()
    session.commit()
    session.close()