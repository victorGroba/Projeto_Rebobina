from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Critica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data_postagem = db.Column(db.DateTime, default=datetime.utcnow)
    imagem = db.Column(db.String(100))  # Caminho da imagem
    video = db.Column(db.String(100))   # Caminho do vídeo

    def __repr__(self):
        return f'<Crítica {self.titulo}>'
