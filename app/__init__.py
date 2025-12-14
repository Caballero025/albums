import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.models import Albums

#Importar y registrar blueprints
from app.routes.album import alb_bp


# Crear las tablas si no existen
with app.app_context():
    db.create_all()

app.register_blueprint(alb_bp, url_prefix='/')


#Ruta principal home
@app.route('/')
def index():
     return render_template('index.html')