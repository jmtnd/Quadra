# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, NumberRange
from flask_wtf.file import FileField, FileAllowed
from models import Usuario

class CalificacionForm(FlaskForm):
    puntuacion = IntegerField('Puntuación (1-5)', validators=[
        DataRequired(), 
        NumberRange(min=1, max=5, message="La puntuación debe ser entre 1 y 5")
    ])
    submit = SubmitField('Enviar Calificación')

class ComentarioForm(FlaskForm):
    texto = TextAreaField('Comentario', validators=[DataRequired()])
    submit = SubmitField('Publicar Comentario')

class PuestoForm(FlaskForm):
    nombre = StringField('Nombre del puesto', validators=[DataRequired()])
    ubicacion = StringField('Ubicación', validators=[DataRequired()])
    reseña = TextAreaField('Reseña', validators=[DataRequired()])
    foto = FileField('Foto del puesto', validators=[
        FileAllowed(['jpg', 'png'], 'Solo imágenes JPG o PNG!')
    ])
    submit = SubmitField('Guardar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class RegisterForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repetir Contraseña', validators=[
        DataRequired(), 
        EqualTo('password', message='Las contraseñas deben coincidir')
    ])
    submit = SubmitField('Registrarse')

    def validate_email(self, field):
        if Usuario.query.filter_by(email=field.data).first():
            raise ValidationError('Este correo electrónico ya está registrado.')