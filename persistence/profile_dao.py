from db.db_helper import get_session, Profile
from model.profile_object import ProfileObj


def add_profile(profile):
    session = get_session()
    session = session()
    new_profile = Profile()
    new_profile.name = profile.get_name()
    new_profile.birth = profile.get_birth()
    new_profile.city = profile.get_city()
    new_profile.level = profile.get_level()
    new_profile.occupation = profile.get_occupation()
    new_profile.telephone = profile.get_phone()
    new_profile.specialty = profile.get_specialty()
    session.add(new_profile)
    session.commit()
    session.refresh(new_profile)
    profile_id = new_profile.id
    session.close()
    return profile_id


def search_profile(name):
    session = get_session()
    session = session()
    profile_query = session.query(Profile).filter(Profile.login == name)
    profile_query = profile_query[0]
    profile_obj = ProfileObj(profile_query.name, profile_query.specialty)
    # TODO the rest of the attributes need to be returned as well
    profile_obj.set_id(profile_query.id)
    session.close()

    return profile_obj


def get_all_profiles():
    session = get_session()
    session = session()
    profile_query = session.query(Profile).all()
    session.close()

    return profile_query


def delete_profile(name):
    session = get_session()
    session = session()
    session.query(Profile).filter(Profile.name == name).delete()
    session.commit()
    session.close()
