# fiaplab/nucleo_funcional.py
# Módulo de gerenciamento de horários de atendimento

horarios = []  

def listar_horarios():
    print("\n Horários cadastrados:")
    if not horarios:
        print("Nenhum horário cadastrado.")
        return

    for h in horarios:
        status = "Disponível" if h["disponivel"] else "Ocupado"
        print(f"{h['horario']} — {status}")


def cadastrar_horario(admin, horario):
    for h in horarios:
        if h["horario"] == horario:
            print("Horário já existe.")
            return False

    horarios.append({
        "admin": admin,
        "horario": horario,
        "disponivel": True,
        "usuario": None
    })

    print(f"Horário {horario} cadastrado com sucesso.")
    return True

def reservar_horario(usuario, horario):
    for h in horarios:
        if h["horario"] == horario:
            if not h["disponivel"]:
                print("Horário já está ocupado.")
                return False

            h["disponivel"] = False
            h["usuario"] = usuario

            print(f"{usuario} reservou o horário {horario}.")
            return True

    print("Horário não encontrado.")
    return False

def cancelar_reserva(usuario, horario):
    for h in horarios:
        if h["horario"] == horario and h["usuario"] == usuario:
            h["disponivel"] = True
            h["usuario"] = None

            print("Reserva cancelada com sucesso.")
            return True
        
    print("Reserva não encontrada.")
    return False    