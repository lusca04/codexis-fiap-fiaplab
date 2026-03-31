from flask import Flask, Blueprint, request, jsonify
from datetime import datetime
import sqlite3, json, os

conn = sqlite3.connect("fiaplab.db",check_same_thread=False)
cursor = conn.cursor()

login_app = Blueprint("login",__name__)

@login_app.route("/Login/", methods=["POST"])
def Login():
    try:
        user_atual = GerenciaLoginAtual()
        if user_atual:
            return jsonify({
                "mensagem": "Usuário já está logado",
            }), 200
        else:
            data = request.get_json()
            Cpf = data.get("Cpf")
            Rm = data.get("Rm")

            if not all([Cpf, Rm]):
                        return jsonify({"erro": "Cpf, Rm são obrigatórios."}), 400

            cursor.execute("""
                Select Cpf, Nome, Email, Rm, Ocupacao, Dt_Nascimento, Curso, 
                Periodo, Dt_Formacao_Esperado, Dt_Cpu, Id_Usuario from Users
                where Cpf = ? 
                and Rm = ?
                Limit 1
                """, (Cpf, Rm))
            
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
                    "Dt_Cpu": resultado[9],
                    "Id_Usuario": resultado[10]
                } 

                with open("./.cache/userLogin.json","w") as arquivo:
                    json.dump(usuario, arquivo , indent = 4)

                return jsonify({"mensagem": f"Bem-Vindo {resultado[4]}:{resultado[1]}"}), 200
            else:
                return jsonify({"erro": "Usuário não cadastrado"}), 404
        
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao buscar usúario em base: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500

@login_app.route("/Sign_Out/", methods=["POST"])
def SignOut():
    caminho = ".cache/userLogin.json"
    try:
        if os.path.exists(caminho):
            os.remove(caminho)
            return {"mensagem": "User desconectado"}
        else:
            return {"erro": "Não foi encontrado usúario logado"}
    except Exception as e:
        return {"erro": str(e)}

def GerenciaLoginAtual():
    caminho = ".cache/userLogin.json"
    
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            return dados
        except json.JSONDecodeError:
            print("Erro: JSON inválido")
            return None
    else:
        print("Arquivo não encontrado")
        return None