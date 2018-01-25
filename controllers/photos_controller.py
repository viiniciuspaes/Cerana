from persistence.photo_dao import search_photo, add_photo


def save_photo(photo_object):
    if not search_photo(photo_object.get_name()):
        add_photo(photo_object)
    else:
        return None
