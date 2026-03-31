from flask import Blueprint, request, jsonify
from api.Services.usuario_service import create_user, get_all_users
from api.Repositories.login_repository import get_logged_user, is_admin

user_app = Blueprint("user", __name__)

@user_app.route("/Cadastro/", methods=["POST"])
def register():
    user = get_logged_user()

    if user and not is_admin(user):
        return jsonify({"erro": "Sem permissão"}), 403

    if create_user(request.get_json()):
        return jsonify({"mensagem": "Usuário criado"}), 201

    return jsonify({"erro": "Usuário já existe"}), 409


@user_app.route("/Cadastro/", methods=["GET"])
def list_users():
    if not get_logged_user():
        return jsonify({"erro": "Não autenticado"}), 401

    return jsonify(get_all_users()), 200