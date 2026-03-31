from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

conn = sqlite3.connect("fiaplab.db")
cursor = conn.cursor()

app = Flask(__name__)

@app.route("/Horarios/", methods=["POST"])
def RegisterHorario():
    try:

        return jsonify()
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao buscar usúario em base: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500
    
@app.route("/Cadastro/", methods=["GET"])
def GetUsers():
    try:
        return jsonify()
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500

@app.route("/Cadastro/", methods=["PUT"])
def GetUsers():
    try:
        return jsonify()
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500
    

@app.route("/Cadastro/", methods=["DELET"])
def GetUsers():
    try:
            return jsonify()
    except sqlite3.IntegrityError as e:
        return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 409

    except Exception as e:
        return jsonify({"erro": f": {str(e)}"}), 500
      