from flask import Flask, Blueprint, request, jsonify
from datetime import datetime
from .Login import GerenciaLoginAtual
import sqlite3

conn = sqlite3.connect("fiaplab.db",check_same_thread=False)
cursor = conn.cursor()

horario_app = Blueprint("horario",__name__)

#adm cadastra hora
@horario_app.route("/Horarios/", methods=["POST"])
def RegisterHorario():
    user_atual = GerenciaLoginAtual()
    if user_atual:
        Ocupacao = user_atual.get("Ocupacao") 
        if Ocupacao == "ADMINISTRADOR":
            try:
                    data = request.get_json()
                    Disponivel = data.get("Disponivel")
                    Horario = data.get("Horario")


                    cursor.execute("""
                    INSERT INTO Horarios
                    (Disponivel, Horario,Id_user)
                    values(?,?,?)
                    """,(Disponivel, Horario, user_atual.get("Id_Usuario")))

                    conn.commit()
                    return jsonify({"mensagem": "Horario cadastrado com sucesso"})
            except sqlite3.IntegrityError as e:
                return jsonify({"erro": f"Erro ao cadastrar horario em base: {str(e)}"}), 409

            except Exception as e:
                return jsonify({"erro": f": {str(e)}"}), 500
        else:
            return jsonify({"mensagem":"alunos nao tem permissao par cadastrar horario"}), 409
    else:
        return jsonify({"mensagem":"Logue com uma conta de administrador para adicionar um horario"}), 409
    
#todos veem as horas e de qual adm e se esta disponivel ou nao
@horario_app.route("/Horarios/", methods=["GET"])
def GetHorarios():
    try:
        horarios = []
        cursor.execute("""
        SELECT C1.Disponivel , C1.Horario, C1.Id, C2.Nome, C2.Email FROM Horarios C1
        INNER JOIN Users C2
        ON C1.Id_user = C2.Id_Usuario 
        WHERE C2.Ocupacao = "ADMINISTRADOR"
        """)
        resultado = cursor.fetchall()
        for resultados in resultado:
            horarios.append({
                "Disponivel": resultados[0],
                "Horario": resultados[1],
                "Id": resultados[2],
                "Nome": resultados[3],
                "Email": resultados[4],
            })
        return jsonify(horarios),200
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao consultar horarios: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500

#aluno ou adm mudam a disponibilidade daquele horario
@horario_app.route("/Horarios/", methods=["PUT"])
def UpdateHorarios():
    user_atual = GerenciaLoginAtual()
    if user_atual:
        Ocupacao = user_atual.get("Ocupacao") 
        if Ocupacao == "ADMINISTRADOR":
            try:
                data = request.get_json()
                Disponivel = data.get("Disponivel")
                Horario = data.get("Horario")

                cursor.execute("""
                UPDATE Horarios 
                SET Disponivel = ?
                WHERE Id_user = ? 
                AND Horario = ?
                """,(Disponivel,user_atual.get("Id_Usuario"),Horario))

                conn.commit()
                return jsonify({"mensagem":"Horario atualizado com sucesso"}),200
            except sqlite3.IntegrityError as e:
                return jsonify({"erro": f"Erro ao atualizar horario em base: {str(e)}"}), 409

            except Exception as e:
                return jsonify({"erro": f": {str(e)}"}), 500
        else:
                data = request.get_json()
                Disponivel = data.get("Disponivel")
                Horario = data.get("Horario")
                Id = data.get("Id")

                cursor.execute("""
                UPDATE Horarios 
                SET Disponivel = ?
                ,Id_user_relacionado = ?
                WHERE Id = ? 
                AND Horario = ?
                AND Disponivel = 1
                """,(Disponivel,user_atual.get("Id_Usuario"),Id,Horario))

                conn.commit()
                return jsonify({"mensagem":"Horario atualizado com sucesso"}),200
    else:
        return jsonify({"mensagem":"Logue com uma conta de administrador para remover um horario"}), 409
    
#adm deleta hora
@horario_app.route("/Horarios/", methods=["DELETE"])
def DeletHorarios():
    user_atual = GerenciaLoginAtual()
    if user_atual:
        Ocupacao = user_atual.get("Ocupacao") 
        if Ocupacao == "ADMINISTRADOR":
            try:
                data = request.get_json()
                Horario = data.get("Horario")

                cursor.execute("""
                DELETE FROM Horarios WHERE
                Id_user = ? 
                AND Horario = ?
                """,(user_atual.get("Id_Usuario"),Horario))

                conn.commit()
                return jsonify({"mensagem":"Horario deletado com sucesso"}),200
            except sqlite3.IntegrityError as e:
                return jsonify({"erro": f"Erro ao deletar horario em base: {str(e)}"}), 409

            except Exception as e:
                return jsonify({"erro": f": {str(e)}"}), 500
        else:
            return jsonify({"mensagem":"alunos nao tem permissao par deletar horario"}), 409
    else:
        return jsonify({"mensagem":"Logue com uma conta de administrador para remover um horario"}), 409