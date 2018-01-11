from persistence.user_dao import search_user, add_user, delete_user


def get_user(login):
    return search_user(login)


def validate_sing_up(user):
    user_result = search_user(user.get_login())
    if user_result:
        return None
    else:
        add_user(user)
        return user


def validate_login(user, password):
    user_to_login = search_user(user)
    if user_to_login and password == user_to_login.get_password():
        return user_to_login
    else:
        return None


def exists(user):
    return True if search_user(user.get_login()) else False


def verify_password(user):
    pass


def encrypt_password(user):
    pass


def erase_user(user):
    delete_user(user.get_login())


def update_user(user):
    pass

