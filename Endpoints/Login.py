from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3, json

conn = sqlite3.connect("fiaplab.db")
cursor = conn.cursor()

app = Flask(__name__)

@app.route("/Login/", methods=["POST"])
def Login():
    try:
        Cpf = request.form.get("Cpf")
        Rm = request.form.get("Rm")

        if not all([Cpf, Rm]):
                    return jsonify({"erro": "Cpf, Rm são obrigatórios."}), 400

        cursor.execute("""
            Select Cpf, Nome, Email, Rm, Ocupacao, Dt_Nascimento, Curso, 
            Periodo, Dt_Formacao_Esperado, Dt_Cpu from Users
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
                "Dt_Cpu": resultado[9]
            } 
            
            with open("C:\Users\lucas\Downloads\CP1-Engenharia_de_Software\codexis-fiap-fiaplab\.cache\userLogin.json","w") as arquivo:
                 json.dump(usuario, arquivo , indent = 4)

            return jsonify({"mensagem": f"Bem-Vindo {resultado[4]}:{resultado[1]}"}), 200
        else:
            return jsonify({"erro": "Usuário não cadastrado"}), 404
    
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao buscar usúario em base: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500