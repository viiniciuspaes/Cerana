from flask import jsonify


def user_parser_json(user):
    user = [
        {
            'id': user.get_id(),
            'login': user.get_login(),
            'password': user.get_password(),
            'active': user.get_state()
        },
    ]

    return jsonify({'user': user})
