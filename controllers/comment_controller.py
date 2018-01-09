from persistence.comment_dao import search_comment, add_comment


def like_comment(comment_obj):
    pass


def comment_post(comment_obj, question_obj):
    comment = search_comment(comment_obj.get_answer())
    if comment:
        return False
    else:
        comment_id = add_comment(comment_obj, question_obj)
        return comment_id


def delete_comment(comment_obj):
    delete_comment(comment_obj.get_answer())


def order_comments():
    pass


def report_comment():
    pass
