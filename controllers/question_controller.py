from model.comment_object import CommentObj
from model.question_object import QuestionObj
from persistence.comment_dao import get_all_comments_from_question
from persistence.question_dao import search_question


def exists(question_name):
    exist = search_question(question_name)
    return True if exist else False


def n_comment(question_name):
    questions = get_all_comments_from_question(question_name)
    return len(questions)


def get_all_comments(question_name):
    comments = get_all_comments_from_question(question_name)
    comments_list = []
    for comment_query in comments:
        comments_obj = CommentObj()
        comments_obj.set_answer(comment_query.answer)
        comments_obj.set_likes(comment_query.likes)
        comments_obj.set_mark(comment_query.mark)
        comments_obj.set_question_id(comment_query.id_question)
        comments_obj.set_user_id(comment_query.id_user)
        comments_obj.set_comment_id(comment_query.id)
        comments_list.append(comments_obj)
    return comments_list
