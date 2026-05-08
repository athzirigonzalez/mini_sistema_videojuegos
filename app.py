from flask import Flask
import os
from models import db
from controllers import api

app = Flask(__name__)

# CONFIGURACIÓN MAESTRA PARA VERCEL
# Usamos la carpeta /tmp porque es la única con permisos de escritura
db_path = os.path.join('/tmp', 'juegos.db')

app.config['SECRET_KEY'] = 'clave_athziri_2024'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(api, url_prefix='/api')

# Intentar crear la base de datos en la carpeta temporal
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Error creando la DB: {e}")

# Vercel usará este objeto 'app'
