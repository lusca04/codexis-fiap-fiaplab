from flask import Flask, jsonify
from api.database.Tabelas import init_db
from api.Controllers.usuario_controller import user_app
from api.Controllers.login_controller import login_app
from api.Controllers.horario_controller import horario_app

def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_app)
    app.register_blueprint(login_app)
    app.register_blueprint(horario_app)

    @app.route("/")
    def home():
        return jsonify({"mensagem": "API rodando!"})

    return app

if __name__ == "__main__":
    init_db()
    app = create_app()
    app.run(debug=True)