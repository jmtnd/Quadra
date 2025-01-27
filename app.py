# app.py
from flask import Flask
from extensions import db, login_manager
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Crear directorio de uploads
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    
    # Registrar blueprints PRIMERO
    from routes import main_bp
    app.register_blueprint(main_bp)
    
    # Crear tablas DESPUÉS de registrar blueprints
    with app.app_context():
        db.create_all()
    
    # Configurar user loader
    @login_manager.user_loader
    def load_user(user_id):
        from models import Usuario
        return Usuario.query.get(int(user_id))
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)