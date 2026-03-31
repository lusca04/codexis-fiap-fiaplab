from flask import Blueprint, request, jsonify
from api.Services.horario_service import *
from api.Repositories.login_repository import get_logged_user, is_admin

horario_app = Blueprint("horario", __name__)


@horario_app.route("/Horarios/", methods=["POST"])
def create():
    user = get_logged_user()

    if not is_admin(user):
        return jsonify({"erro": "Apenas admin"}), 403

    data = request.get_json()

    create_horario(data["Disponivel"], data["Horario"], user["Id_Usuario"])

    return jsonify({"mensagem": "Criado"}), 201


@horario_app.route("/Horarios/", methods=["GET"])
def list_all():
    return jsonify(get_horarios()), 200


@horario_app.route("/Horarios/", methods=["PUT"])
def update():
    data = request.get_json()

    if update_horario(data["Disponivel"], data["Horario"]):
        return jsonify({"mensagem": "Atualizado"}), 200

    return jsonify({"erro": "Nada atualizado"}), 404


@horario_app.route("/Horarios/", methods=["DELETE"])
def delete():
    user = get_logged_user()

    if not is_admin(user):
        return jsonify({"erro": "Apenas admin"}), 403

    data = request.get_json()

    if delete_horario(data["Horario"], user["Id_Usuario"]):
        return jsonify({"mensagem": "Removido"}), 200

    return jsonify({"erro": "Nada removido"}), 404