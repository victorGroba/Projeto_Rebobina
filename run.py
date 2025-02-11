import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Define o diretório da pasta static
app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), 'app/templates'),
            static_folder=os.path.join(os.path.dirname(__file__), 'app/static'))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rebobina.db'
db = SQLAlchemy(app)

# Modelo para as reviews
class MovieReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(500), nullable=False)
    review = db.Column(db.Text, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    featured_review = MovieReview.query.order_by(MovieReview.created_at.desc()).first()
    reviews = MovieReview.query.order_by(MovieReview.created_at.desc()).limit(6).all()
    return render_template('index.html', featured_review=featured_review, reviews=reviews)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
