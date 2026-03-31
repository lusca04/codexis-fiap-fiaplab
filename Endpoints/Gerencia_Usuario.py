from flask import Flask, Blueprint ,request, jsonify
from .Login import GerenciaLoginAtual
from datetime import datetime
import sqlite3

conn = sqlite3.connect("fiaplab.db",check_same_thread=False)
cursor = conn.cursor()

user_app = Blueprint("user",__name__)

Ocupacoes = ["ALUNO", "ADMINISTRADOR"]

@user_app.route("/Cadastro/", methods=["POST"])
def RegisterUsers():
    user_atual = GerenciaLoginAtual()
    if user_atual:
        Ocupacao = user_atual.get("Ocupacao") 
        if Ocupacao == "ADMINISTRADOR":
                return cadastraUsuario()
        else:
             return jsonify("Usúario não tem permissão")
    else:
           return cadastraUsuario() #cadastra primeiro acesso

@user_app.route("/Cadastro/", methods=["DELETE"])
def DeleteUsers():
    user_atual = GerenciaLoginAtual()
    if user_atual:
        Ocupacao = user_atual.get("Ocupacao") 
        if Ocupacao == "ADMINISTRADOR":
            try:
                    data = request.get_json()
                    Cpf = data.get("Cpf")
                    Email = data.get("Email")
                    Rm = data.get("Rm")
                    Dt_Nascimento = data.get("Dt_Nascimento")

                    cursor.execute("""
                    DELETE FROM Users
                    WHERE Cpf = ?
                    AND Email = ?
                    AND Rm = ?
                    AND Dt_Nascimento = ? 
                    """,(Cpf, Email, Rm, Dt_Nascimento))

                    conn.commit()

                    return  jsonify({"mensagem": "Operacao concluida com sucesso!"}), 200
            
            except sqlite3.IntegrityError as e:
                return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 409

            except Exception as e:
                return jsonify({"erro": f": {str(e)}"}), 500
        else:
            return jsonify("Usúario não tem permissão")
    else:
        return jsonify("Usúario não esta logado")
    
@user_app.route("/Cadastro/", methods=["GET"])
def GetUsers():
    try:
            usuarios = []
            user_atual = GerenciaLoginAtual()
            if user_atual:
                Ocupacao = user_atual.get("Ocupacao") 
                if Ocupacao == "ADMINISTRADOR":
                    cursor.execute("""
                    SELECT * FROM Users
                    """)

                    resultado = cursor.fetchall()

                    for resultados in resultado:
                        usuarios.append({
                            "Cpf": resultados[1],
                            "Nome": resultados[2],
                            "Email": resultados[3],
                            "Rm": resultados[4],
                            "Ocupacao": resultados[5],
                            "Dt_Nascimento": resultados[6],
                            "Curso": resultados[7],
                            "Periodo": resultados[8],
                            "Dt_Formacao_Esperado": resultados[9],
                            "Dt_Cpu": resultados [10],
                            "Ind_Ativo": resultados[11]
                        })
                else:
                    cursor.execute("""
                    SELECT Nome, Email, Curso FROM Users
                    WHERE Ocupacao = "ADMINISTRADOR"
                    """)

                    resultado = cursor.fetchall()

                    for resultados in resultado:
                        usuarios.append({
                        
                            "Nome": resultados[2],
                            "Email": resultados[3],
                            "Curso": resultados[7],
                        })

                    
                return jsonify(usuarios), 200
            else:
                return jsonify("Nenhuma conta logada"), 409
            
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500
  
@user_app.route("/Cadastro/", methods=["PUT"])
def UpdateUsers():
    user_atual = GerenciaLoginAtual()
    if user_atual:
        Ocupacao = user_atual.get("Ocupacao") 
        if Ocupacao == "ADMINISTRADOR":   
            try:
                    data = request.get_json()
                    Cpf = data.get("Cpf")
                    Rm = data.get("Rm")
                    Ind_ativo = data.get("Ind_ativo")

                    cursor.execute("""
                    UPDATE Users
                    SET Ind_Ativo = ?
                    WHERE Cpf = ?
                    AND Rm = ?
                    """,(Ind_ativo, Cpf, Rm))

                    conn.commit()

                    return  jsonify({"mensagem": "Status do usúario atualizado com sucesso!"}), 200
            
            except sqlite3.IntegrityError as e:
                return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 409

            except Exception as e:
                return jsonify({"erro": f": {str(e)}"}), 500
        else:
            return jsonify("Usúario não tem permissão"), 409
    else:
        return jsonify("Usúario não esta logado"),409
     
def cadastraUsuario():
    try:
        data = request.get_json()
        Cpf = data.get("Cpf")
        Nome = data.get("Nome")
        Email = data.get("Email")
        Rm = data.get("Rm")
        Ocupacao = data.get("Ocupacao").upper()
        Dt_Nascimento = data.get("Dt_Nascimento")
        Curso = data.get("Curso_Area")
        Periodo = data.get("Periodo")
        Dt_Formacao = data.get("Dt_formacao")
        Dt_Cpu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not all([Cpf, Nome, Email, Rm, Ocupacao, Dt_Nascimento]):
                    return jsonify({"erro": "Cpf, Nome, Email, Rm, Ocupacao e Data de Nascimento"
                    "são obrigatórios."}), 400
        
        if Ocupacao not in Ocupacoes:
            return jsonify({"erro": f"Ocupação inválida. Valores permitidos: {Ocupacoes}"}), 400
        
        cursor.execute("""
            Select Cpf, Nome, Email, Rm, Ocupacao, Dt_Nascimento, Curso, 
            Periodo, Dt_Formacao_Esperado, Dt_Cpu from Users
            where Cpf = ? 
            OR Rm = ?
            OR Nome = ?
            OR Email = ?
            Limit 1
            """, (Cpf, Rm, Nome, Email))

        resultado = cursor.fetchone()
        if resultado:
            usuario = {
                "Cpf": resultado[0],
                "Nome": resultado[1],
                "Email": resultado[2],
                "Rm": resultado[3],
                "Ocupacao": resultado[4],
                "Dt_Nascimento": resultado[5],
                "Curso": resultado[6],
                "Periodo": resultado[7],
                "Dt_Formacao_Esperado": resultado[8],
                "Dt_Cpu": resultado[9]
            } 
            return jsonify("Usúario ja cadastrado"), 409
        else:
            cursor.execute("""
                INSERT INTO Users 
                (Cpf, Nome, Email, Rm, Ocupacao, Dt_Nascimento, Curso, 
                Periodo, Dt_Formacao_Esperado, Dt_Cpu)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (Cpf, Nome, Email, Rm, Ocupacao, Dt_Nascimento, Curso, Periodo, Dt_Formacao, 
                Dt_Cpu))

            conn.commit()

            return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao cadastrar novo usuário: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500