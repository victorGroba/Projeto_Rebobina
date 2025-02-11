from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

# Instância do banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="app/templates")

    # Configurações do Flask
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')

    # Inicializa o banco de dados
    db.init_app(app)

    # Importa as rotas
    from app import routes
    return app
