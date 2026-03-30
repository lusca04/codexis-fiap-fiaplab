from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

conn = sqlite3.connect("fiaplab.db")
cursor = conn.cursor()

app = Flask(__name__)

Ocupacoes = ["ALUNO", "ADMINISTRADOR"]

@app.route("/Cadastro/", methods=["POST"])
def Cadastro():
    try:
        Cpf = request.form.get("Cpf")
        Nome = request.form.get("Nome")
        Email = request.form.get("Email")
        Rm = request.form.get("Rm")
        Ocupacao = request.form.get("Ocupacao")
        Dt_Nascimento = request.form.get("Dt_Nascimento")
        Curso = request.form.get("Curso/Area")
        Periodo = request.form.get("Periodo")
        Dt_Formacao = request.form.get("Dt_formacao")
        Dt_Cpu = datetime.now()

        if not all([Cpf, Nome, Email]):
                    return jsonify({"erro": "Cpf, Nome, Email, Rm, Ocupacao e Data de Nascimento"
                    "são obrigatórios."}), 400
        
        if Ocupacao not in Ocupacoes:
            return jsonify({"erro": f"Ocupação inválida. Valores permitidos: {Ocupacoes}"}), 400
        
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