from db.db_helper import get_session, Question, User
from model.question_object import QuestionObj


def add_question(question_obj):
    session = get_session()
    session = session()
    new_question = Question()
    new_question.user_id = int(User.get_id())
    new_question.tag_id = question_obj.get_tag_id()
    new_question.question = question_obj.get_question()
    new_question.description = question_obj.get_description()
    session.add(new_question)
    session.commit()
    session.refresh(new_question)
    question_id = new_question
    session.close()
    return question_id


def search_question(question):
    session = get_session()
    session = session()
    question_query = session.query(Question).filter(Question.question == question).all()
    if len(question_query) > 0:
        question_query = question_query[0]
    if question_query:
        question_obj = QuestionObj(question_query.question)
        question_obj.set_description(question_query.description)
        session.close()
        return question_obj
    else:
        session.close()
        return None


def get_all_questions():
    session = get_session()
    session = session()
    question_query = session.query(Question).all()
    session.close()
    return question_query


def get_all_questions_from_user(user):
    session = get_session()
    session = session()
    questions = session.query(Question).filter(Question.id_user == user.get_id()).all()
    return questions


def delete_question(question):
    session = get_session()
    session = session()
    session.query(Question).filter(Question.question == question).delete()
    session.commit()
    session.close()
