from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rebobina.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configuração da pasta de uploads
    app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'uploads')

    # Inicializa o banco de dados
    db.init_app(app)

    # Importa e registra rotas
    from .routes import register_routes
    register_routes(app)

    # Criação do banco de dados dentro do contexto
    with app.app_context():
        db.create_all()

    return app
