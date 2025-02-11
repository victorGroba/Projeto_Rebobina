from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed

class CriticaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(max=150)])
    conteudo = TextAreaField('Conteúdo', validators=[DataRequired()])
    imagem = FileField('Imagem', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    video = FileField('Vídeo', validators=[FileAllowed(['mp4', 'mov', 'avi'])])
    submit = SubmitField('Postar')
