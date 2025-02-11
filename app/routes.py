from flask import render_template, request, redirect, url_for, current_app
from app import db  # Apenas importa o db da instância de 'app'

# Funções para buscar dados no banco ou em qualquer outra fonte
def get_destaques():
    # Exemplo de busca no banco de dados. Ajuste conforme sua estrutura de dados.
    return db.session.query(Post).filter(Post.destaque == True).all()

def get_ultimas_materias():
    # Exemplo de busca para as últimas matérias. Ajuste conforme sua estrutura de dados.
    return db.session.query(Post).order_by(Post.data_criacao.desc()).limit(3).all()

# Ao invés de 'app.route', use o 'current_app.route' para registrar rotas.
def register_routes(app):
    @app.route('/')
    def index():
        # Buscando os dados para as variáveis 'destaques' e 'ultimas_materias'
        destaques = get_destaques()  # Função para buscar os posts em destaque
        ultimas_materias = get_ultimas_materias()  # Função para buscar as últimas matérias
        return render_template('index.html', destaques=destaques, ultimas_materias=ultimas_materias)

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if request.method == 'POST':
            file = request.files['file']
            if file:
                upload_folder = current_app.config['UPLOAD_FOLDER']  # Usa current_app para acessar configurações
                file.save(os.path.join(upload_folder, file.filename))
                return redirect(url_for('index'))

        return render_template('upload.html')
