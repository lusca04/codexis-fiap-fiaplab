from database.Tabelas import init_db
from Endpoints.Gerencia_Usuario import user_app
from Endpoints.Login import login_app
from flask import Flask, jsonify

app = Flask(__name__)

app.register_blueprint(user_app)
app.register_blueprint(login_app)
app.register_blueprint(horario_app)

@app.route("/")
def home():
    return jsonify({"mensagem": "API rodando!"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)