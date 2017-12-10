from flask import Flask, abort, request

from db.db_helper import init
from model.user_object import UserObj
from persistence.user_dao import search_user, add_user
from utils.parser import user_parser_json

app = Flask(__name__)
init()


def exception_404():
    abort(404)


@app.route('/login/open', methods=['GET'])
def get_user():

    # this method have to receive the user from the url
    # user = UserObj('vini', '123')  # only for test
    # add_user(user)
    user = search_user('vini')
    return user_parser_json(user)


@app.route('/login/create', methods=['POST'])
def create_user():

    if not request.json or 'login' not in request.json:
        exception_404()

    user = UserObj(request.json['login'], request.json['password'])
    user.set_type("student")
    add_user(user)

    return "Adicionado com sucesso {}".format(user)


@app.route('/login/update<string:login>', methods=['PUT'])
def update_user(login):
    if not login:
        exception_404()

    user_obj = search_user(login)
    user_obj.set_password(request.json['password'])
    # TODO metodo de atualizaçao do banco


@app.route('/login/delete<string:login>', methods=['DELETE'])
def delete_user(login):
    if not login:
        exception_404()
    delete_user(login)


if __name__ == '__main__':
    app.run()
