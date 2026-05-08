from flask import Flask
from models import db
# Cambiamos 'api.routes' por 'controllers' porque así se llama tu archivo
from controllers import api 
import os

app = Flask(__name__)

# Configuración de ruta para la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'juegos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'una-clave-muy-secreta')

db.init_app(app)

# Registrar la API (Blueprint)
app.register_blueprint(api, url_prefix='/api')

# Crear la base de datos si no existe
with app.app_context():
    db.create_all()

# Para Vercel, no necesitamos el app.run()
