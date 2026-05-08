from flask import Flask
import os
from models import db
from controllers import api

app = Flask(__name__)

# Esto ayuda a Vercel a encontrar tu base de datos
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'una-clave-cualquiera'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'juegos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(api, url_prefix='/api')

with app.app_context():
    db.create_all()
