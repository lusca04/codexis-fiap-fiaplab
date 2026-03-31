from datetime import datetime
from api.Repositories import usuario_repository

def login_user(cpf, rm):
    user = usuario_repository.find_user_by_cpf_rm(cpf, rm)

    if not user:
        return None

    return {
        "Id_Usuario": user[0],
        "Nome": user[2],
        "Ocupacao": user[5]
    }


def create_user(data):
    if usuario_repository.user_exists(data["Cpf"], data["Email"], data["Rm"]):
        return False

    rowcount = usuario_repository.insert_user((
        data["Cpf"],
        data["Nome"],
        data["Email"],
        data["Rm"],
        data["Ocupacao"].upper(),
        data["Dt_Nascimento"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    return rowcount > 0


def get_all_users():
    return usuario_repository.list_users()