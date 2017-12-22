from db.db_helper import get_session, User
from model.user_object import UserObj


def add_user(user_obj):
    session = get_session()
    session = session()
    new_user = User()
    new_user.login = user_obj.get_login()
    new_user.password = user_obj.get_password()
    new_user.active = user_obj.get_state()
    new_user.user_type = user_obj.get_type()
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    user_id = new_user.id
    session.close()
    return user_id


def search_user(login):
    session = get_session()
    session = session()
    user_query = session.query(User).filter(User.login == login)
    user_query = user_query[0]
    user_obj = UserObj(user_query.login, user_query.password)
    user_obj.set_type(user_query.user_type)
    session.close()

    return user_obj


def validate_user(login, password):
    session = get_session()
    session = session()
    user_query = session.query.filter_by(User.login == login, User.password == password).first()
    if len(user_query) > 0:
        user_query = user_query[0]
        user_obj = UserObj(user_query.login, user_query.password)
        user_obj.set_type(user_query.user_type)
        session.close()
        return user_obj
    else:
        session.close()
        return None


def get_all_users():
    session = get_session()
    session = session()
    user_query = session.query(User).all()
    session.close()


def delete_user(login):
    session = get_session()
    session = session()
    session.query(User).filter(User.login == login).delete()
    session.commit()
    session.close()
