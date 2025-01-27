# routes.py (actualizado)
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
import os
from models import Usuario, Puesto, Calificacion, Comentario
from forms import LoginForm, RegisterForm, PuestoForm, CalificacionForm, ComentarioForm
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    puestos = Puesto.query.all()
    return render_template('index.html', puestos=puestos)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.check_password(form.password.data):
            login_user(usuario)
            return redirect(url_for('main.index'))
        flash('Credenciales incorrectas')
    return render_template('login.html', form=form)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        usuario = Usuario(nombre=form.nombre.data, email=form.email.data)
        usuario.set_password(form.password.data)
        db.session.add(usuario)
        db.session.commit()
        flash('¡Registro exitoso!')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main_bp.route('/add_puesto', methods=['GET', 'POST'])
@login_required
def add_puesto():
    form = PuestoForm()
    if form.validate_on_submit():
        foto = form.foto.data
        filename = None
        if foto:
            filename = secure_filename(foto.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            foto.save(file_path)
        
# En la ruta add_puesto, cambiar:
        puesto = Puesto(
            nombre=form.nombre.data,
            ubicacion=form.ubicacion.data,
            reseña=form.reseña.data,
            foto_url=filename,
            usuario_id=current_user.id  # Usar usuario_id en lugar de creador
        )
        db.session.add(puesto)
        db.session.commit()
        flash('Puesto añadido exitosamente')
        return redirect(url_for('main.index'))
    return render_template('add_puesto.html', form=form)

@main_bp.route('/puesto/<int:puesto_id>')
def detalle_puesto(puesto_id):
    puesto = Puesto.query.get_or_404(puesto_id)
    calificacion_form = CalificacionForm()
    comentario_form = ComentarioForm()
    return render_template('detalle_puesto.html',
                         puesto=puesto,
                         calificacion_form=calificacion_form,
                         comentario_form=comentario_form)

@main_bp.route('/calificar/<int:puesto_id>', methods=['POST'])
@login_required
def calificar_puesto(puesto_id):
    form = CalificacionForm()
    if form.validate_on_submit():
        calificacion = Calificacion(
            puntuacion=form.puntuacion.data,
            usuario_id=current_user.id,
            puesto_id=puesto_id
        )
        db.session.add(calificacion)
        db.session.commit()
        flash('Calificación enviada')
    return redirect(url_for('main.detalle_puesto', puesto_id=puesto_id))

@main_bp.route('/comentario/<int:puesto_id>', methods=['POST'])
@login_required
def agregar_comentario(puesto_id):
    form = ComentarioForm()
    if form.validate_on_submit():
        comentario = Comentario(
            texto=form.texto.data,
            usuario_id=current_user.id,
            puesto_id=puesto_id
        )
        db.session.add(comentario)
        db.session.commit()
        flash('Comentario agregado')
    return redirect(url_for('main.detalle_puesto', puesto_id=puesto_id))