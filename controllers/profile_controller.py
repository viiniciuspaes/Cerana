from persistence.question_dao import get_all_questions
from persistence.user_dao import search_user


def load_user_data(login):
    user = search_user(login)
    return user if user else None


def load_user_questions():
    questions = get_all_questions()
    return questions if questions else None
