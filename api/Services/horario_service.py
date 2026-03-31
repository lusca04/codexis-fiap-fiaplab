from api.Repositories import horario_repository

def create_horario(disponivel, horario, user_id):
    return horario_repository.insert_horario(disponivel, horario, user_id)


def get_horarios():
    return horario_repository.list_horarios()


def update_horario(disponivel, horario):
    return horario_repository.update_horario(disponivel, horario)


def delete_horario(horario, user_id):
    return horario_repository.delete_horario(horario, user_id)