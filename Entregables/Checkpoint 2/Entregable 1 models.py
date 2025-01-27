# models.py
from extensions import db
from flask_login import UserMixin  # Importación correcta al inicio
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    puestos = db.relationship('Puesto', backref='creador', lazy='dynamic')
    calificaciones = db.relationship('Calificacion', backref='usuario', lazy='dynamic')
    comentarios = db.relationship('Comentario', backref='autor', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Puesto(db.Model):
    __tablename__ = 'puestos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(100))
    reseña = db.Column(db.Text)
    foto_url = db.Column(db.String(200))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    calificaciones = db.relationship('Calificacion', backref='puesto', lazy='dynamic')
    comentarios = db.relationship('Comentario', backref='puesto', lazy='dynamic')

class Calificacion(db.Model):
    __tablename__ = 'calificaciones'
    id = db.Column(db.Integer, primary_key=True)
    puntuacion = db.Column(db.Integer, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    puesto_id = db.Column(db.Integer, db.ForeignKey('puestos.id'))  # Error corregido

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    puesto_id = db.Column(db.Integer, db.ForeignKey('puestos.id'))  # Línea corregida