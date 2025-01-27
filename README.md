# README.md
# Quadra
markdown
Copy
# Quadra 🍔

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Plataforma colaborativa para descubrir y calificar puestos de comida callejera

## 📌 Características Clave

### **Funcionalidades Principales**
- 🧑💻 Autenticación de usuarios (registro/login)
- 📋 CRUD completo de puestos de comida
- ⭐ Sistema de calificaciones (1-5 estrellas)
- 💬 Comentarios en tiempo real
- 📸 Subida de imágenes con validación
- 📱 Diseño responsive con Bootstrap 5

### **Tech Stack**
| **Categoría**       | **Tecnologías**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| **Frontend**         | Jinja2, Bootstrap 5, HTML5, CSS3                                               |
| **Backend**          | Python, Flask, SQLAlchemy                                                      |
| **Base de Datos**    | PostgreSQL                                                                     |
| **Seguridad**        | Flask-Login, Werkzeug, CSRF Protection                                        |
| **Otros**            | WTForms, Pipenv, Flask-WTF                                                    |

## 🚀 Instalación Rápida

### Requisitos Previos
- Python 3.8+
- PostgreSQL
- pip

### Pasos de Configuración
1. Clonar repositorio:
   ```bash
   git clone https://github.com/tu-usuario/quadra.git
   cd quadra
Configurar entorno virtual:
bash
Copy
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instalar dependencias:
bash
Copy
pip install -r requirements.txt
Configurar base de datos:
bash
Copy
flask shell
>>> from app import create_app
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
Variables de entorno (.env):
env
Copy
SECRET_KEY=tu_clave_secreta
DATABASE_URL=postgresql://user:password@localhost/db_name
Iniciar aplicación:
bash
Copy
flask run --debug
🖥️ Uso Básico

bash
Copy
# Acceso a rutas principales
http://localhost:5000/          # Página principal
http://localhost:5000/login     # Inicio de sesión
http://localhost:5000/register  # Registro de usuario
http://localhost:5000/add_puesto # Añadir nuevo puesto
Flujo típico:

Registrarse como nuevo usuario
Iniciar sesión
Añadir puesto de comida
Calificar y comentar en puestos existentes
Explorar puestos por ubicación
🛠️ Estructura del Proyecto

tree
Copy
quadra/
├── app.py
├── config.py
├── models.py
├── routes.py
├── forms.py
├── extensions.py
├── requirements.txt
├── static/
│   └── uploads/
└── templates/
    ├── auth/
    │   ├── login.html
    │   └── register.html
    ├── puestos/
    │   ├── add_puesto.html
    │   └── detalle_puesto.html
    ├── index.html
    └── base.html
🌟 Roadmap

Estado	Función	Descripción
✅	Autenticación básica	Registro/login funcional
✅	CRUD Puestos	Gestión completa de puestos
🔄	Sistema de ratings	Calificaciones 1-5 estrellas
⏳	Búsqueda avanzada	Filtrado por ubicación/rating
⏳	Panel de administración	Gestión de usuarios/contenido
🤝 Cómo Contribuir

Haz fork del repositorio
Crea una rama feature:
bash
Copy
git checkout -b feature/nueva-funcionalidad
Haz commit de tus cambios:
bash
Copy
git commit -m 'feat: añade nueva funcionalidad'
Haz push a la rama:
bash
Copy
git push origin feature/nueva-funcionalidad
Abre un Pull Request
📄 Licencia

Este proyecto está bajo licencia MIT - ver LICENSE para más detalles.

Desarrollado con ❤️ por [Tu Nombre]
Twitter
LinkedIn

Copy

Este formato incluye:
- Badges profesionales
- Tablas organizadas
- Sintaxis de código resaltada
- Secciones claramente diferenciadas
- Iconos visuales
- Estructura jerárquica lógica
- Enlaces de contacto
- Estado del proyecto visual

¡Ahora tu README tendrá una apariencia profesional y será fácil de navegar! 😊