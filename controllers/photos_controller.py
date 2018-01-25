from persistence.photo_dao import search_photo, add_photo


def save_photo(photo_object):
    if not search_photo(photo_object.get_name()):
        add_photo(photo_object)
    else:
        return None


def request_photo_path(file_name):
    photo = search_photo(file_name)
    return photo if photo else None
