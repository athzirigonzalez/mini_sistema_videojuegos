from flask import Flask
from models import db
# Eliminamos el "api." porque en tu GitHub el archivo está en la raíz
from routes import api 
import os

app = Flask(__name__)

# Configuración de ruta absoluta para la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'juegos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave-por-defecto')

db.init_app(app)

# Registrar API
app.register_blueprint(api, url_prefix='/api')

# Crear DB
with app.app_context():
    db.create_all()

# IMPORTANTE: Vercel necesita que 'app' esté disponible globalmente
# No hace falta el app.run para el despliegue
