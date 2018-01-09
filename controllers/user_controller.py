from persistence.user_dao import search_user, add_user


def validate_sing_up(user):
    user_result = search_user(user.get_login())
    if user_result:
        return None
    else:
        add_user(user)


def validate_login(user):
    user_to_login = search_user(user.get_login())
    if user_to_login:
        return None
    else:
        return user_to_login


def exists(user):
    return True if search_user(user.get_login()) else False


def verify_password(user):
    pass


def encrypt_password(user):
    pass


def delete_user(user):
    pass

def update_user(user):
    pass

