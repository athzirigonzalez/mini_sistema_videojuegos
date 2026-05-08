from flask import Flask
import os
from models import db
# IMPORTANTE: Cambiamos api.routes por controllers porque así se llama tu archivo
from controllers import api 

app = Flask(__name__)

# Configuración para que Vercel encuentre la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'clave_segura_athziri'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'juegos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registramos el blueprint que está en controllers.py
app.register_blueprint(api, url_prefix='/api')

with app.app_context():
    db.create_all()

# No pongas app.run() al final, Vercel no lo necesita
