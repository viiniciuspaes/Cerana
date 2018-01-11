from persistence.question_dao import get_all_questions_from_user
from persistence.user_dao import search_user


def load_user_data(user):
    user = search_user(user.get_login())
    return user if user else None


def load_user_questions(user):
    questions = get_all_questions_from_user(user)
    return questions if questions else None


def list_all_questions_from_user(user):
    return get_all_questions_from_user(user)
