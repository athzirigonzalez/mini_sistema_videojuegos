from flask import Flask
import os

# Importaciones directas (sin puntos ni nombres de carpeta)
try:
    from models import db
    from controllers import api
except ImportError:
    # Esto es por si Vercel intenta buscar en rutas relativas
    from .models import db
    from .controllers import api

app = Flask(__name__)

# Configuración de seguridad y base de datos
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave_temporal_123')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'juegos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB
db.init_app(app)

# Registrar Blueprint
app.register_blueprint(api, url_prefix='/api')

# Crear tablas si no existen
with app.app_context():
    db.create_all()

# Vercel necesita el objeto 'app'
