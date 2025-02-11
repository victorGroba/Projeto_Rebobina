from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Inicializando o banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Exemplo de banco de dados SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configuração para uploads
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')

    # Inicializar o banco de dados
    db.init_app(app)

    # Registrar as rotas
    from .routes import register_routes
    register_routes(app)

    return app
