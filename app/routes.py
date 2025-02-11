import os
from flask import render_template, request, redirect, url_for, current_app
from app import db
from app.models import Post  # Supondo que Post seja um modelo definido em 'app/models.py'

# Funções para buscar dados no banco de dados
def get_destaques():
    return db.session.query(Post).filter(Post.destaque == True).all()

def get_ultimas_materias():
    return db.session.query(Post).order_by(Post.data_criacao.desc()).limit(3).all()

# Registrar rotas no Flask
def register_routes(app):
    @app.route('/')
    def index():
        destaques = get_destaques()  # Busca os posts em destaque
        ultimas_materias = get_ultimas_materias()  # Busca as últimas matérias
        return render_template('index.html', destaques=destaques, ultimas_materias=ultimas_materias)

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if request.method == 'POST':
            file = request.files['file']
            if file:
                upload_folder = current_app.config['UPLOAD_FOLDER']  # Diretório de upload configurado no Flask
                file.save(os.path.join(upload_folder, file.filename))  # Salva o arquivo
                return redirect(url_for('index'))  # Redireciona para a página inicial

        return render_template('upload.html')  # Exibe o formulário de upload
