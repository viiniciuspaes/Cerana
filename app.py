from flask import Flask, jsonify, abort, request

from utils.parser import user_parser_json
from model.user_model import User

app = Flask(__name__)


def exception_404():
    abort(404)


@app.route('/login/open', methods=['GET'])
def get_user():
    user = User('vini', '123')
    return user_parser_json(user)


@app.route('/login/create', methods=['POST'])
def create_user():

    if not request.json or 'login' not in request.json:
        exception_404()

    user = User(request.json['login'], request.json['password'])

    return "Adicionado com sucesso {}".format(user)


@app.route('/login/update<string:login>', methods=['PUT'])
def update_user(login):
    if not login:
        exception_404()

    #TODO metodo de busca do banco com task_id
    user = User('a', 'b') #usando as paradas do banco
    user.set_login(request.json['login'])
    user.set_password(request.json['password'])
    # TODO metodo de atualizaçao do banco


@app.route('/login/delete<string:login>', methods=['DELETE'])
def delete_user(login):
    if not login:
        exception_404()
    # TODO metodo de busca do banco com task_id
    user = User('a', 'b')  # usando as paradas do banco
    # TODO metodo de adeletar do banco


if __name__ == '__main__':
    app.run()
