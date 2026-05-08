from flask import Flask
import os
from models import db
from controllers import api

app = Flask(__name__)

# --- CONFIGURACIÓN PARA DESPLIEGUE EN VERCEL ---
# Vercel no permite escribir en la raíz, por eso usamos /tmp para la base de datos
db_path = os.path.join('/tmp', 'juegos.db')

app.config['SECRET_KEY'] = 'clave_secreta_athziri_123'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos con la app
db.init_app(app)

# Registramos tus rutas (Blueprint) que están en controllers.py
# El prefix '/api' significa que tus rutas funcionarán como: tu-url.com/api/...
app.register_blueprint(api, url_prefix='/api')

# Ruta de cortesía para que no salga "Not Found" al entrar al link directo
@app.route('/')
def home():
    return """
    <h1>¡Sistema de Videojuegos Online!</h1>
    <p>El servidor Flask está funcionando correctamente en Vercel.</p>
    <p><b>Nota:</b> Recuerda usar las rutas de tu API (ejemplo: /api/videojuegos) para interactuar con el sistema.</p>
    """

# Crear las tablas en la base de datos al arrancar
with app.app_context():
    try:
        db.create_all()
        print("Base de datos creada exitosamente en /tmp")
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

# Para Vercel NO usamos app.run(), Vercel detecta el objeto 'app' automáticamente
