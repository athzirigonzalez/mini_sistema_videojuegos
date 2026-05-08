from flask import Blueprint, jsonify, request
from models import db, Juego # Importación directa desde el mismo nivel

api = Blueprint('api', __name__)

# Aquí sigue el resto de tus rutas (get, post, etc.)
