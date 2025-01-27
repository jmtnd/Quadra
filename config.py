# config.py (actualizado)
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu-clave-secreta'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:J0shua123@localhost/quadra_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}