from flask import Blueprint, request, jsonify
from api.Services.usuario_service import login_user
from api.Repositories.login_repository import save_logged_user, get_logged_user, remove_logged_user

login_app = Blueprint("login", __name__)


@login_app.route("/Login/", methods=["POST"])
def login():
    if get_logged_user():
        return jsonify({"mensagem": "Já logado"}), 200

    data = request.get_json()

    user = login_user(data.get("Cpf"), data.get("Rm"))

    if not user:
        return jsonify({"erro": "Usuário inválido"}), 404

    save_logged_user(user)

    return jsonify({"mensagem": f"Bem-vindo {user['Nome']}"}), 200


@login_app.route("/Sign_Out/", methods=["POST"])
def logout():
    remove_logged_user()
    return jsonify({"mensagem": "Logout realizado"}), 200