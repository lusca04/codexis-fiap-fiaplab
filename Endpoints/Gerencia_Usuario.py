from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

conn = sqlite3.connect("fiaplab.db")
cursor = conn.cursor()

app = Flask(__name__)

Ocupacoes = ["ALUNO", "ADMINISTRADOR"]

@app.route("/Cadastro/", methods=["POST"])
def RegisterUsers():
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
            Select Cpf, Nome, Email, Rm, Ocupacao, Dt_Nascimento, Curso, 
            Periodo, Dt_Formacao_Esperado, Dt_Cpu from Users
            where Cpf = ? 
            and Rm = ?
            and Nome = ?
            and Email = ?
            and Ocupacao = ?
            and Dt_Nascimento = ?
            and Curso = ?
            and Periodo = ?
            AND Dt_Formacao_Esperado = ? 
            Limit 1
            """, (Cpf, Rm, Nome, Email, Ocupacao, Dt_Nascimento, Curso, 
            Periodo, Dt_Formacao))

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
            return jsonify("Usúario ja cadastrado"), 200
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

#colocar filtro para que so possa usar caso o usuario esteja logado e seja adm 
#para metodos abaixo
@app.route("/Cadastro/", methods=["DELET"])
def DeleteUsers():
    try:
            Cpf = request.form.get("Cpf")
            Email = request.form.get("Email")
            Rm = request.form.get("Rm")
            Dt_Nascimento = request.form.get("Dt_Nascimento")

            cursor.execute("""
            DELETE * FROM Users
            WHERE Cpf = ?
            AND Email = ?
            AND Rm = ?
            Dt_Nascimento = ? 
            """,(Cpf, Email, Rm, Dt_Nascimento))
    
            return  jsonify({"mensagem": "Usuário deleteado com sucesso!"}), 201
    
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500
    
@app.route("/Cadastro/", methods=["GET"])
def GetUsers():
    try:
            
            cursor.execute("""
            SELECT * FROM Users
            """)

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

            return  jsonify(resultado)
            # return  jsonify(usuario)

    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500
      
@app.route("/Cadastro/", methods=["PUT"])
def UpdateUsers():
    try:
        
        Cpf = request.form.get("Cpf")
        Email = request.form.get("Email")
        Rm = request.form.get("Rm")
        Dt_Nascimento = request.form.get("Dt_Nascimento")
        
        cursor.execute("""
        UPDATE * FROM Users
        WHERE
        """)

        # PREGUICA, CONTINUA DPS
        
        resultado = cursor.fetchone()
            
        if resultado:
            usuario = {

            }

        return  jsonify(resultado)
        # return  jsonify(usuario)

    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500