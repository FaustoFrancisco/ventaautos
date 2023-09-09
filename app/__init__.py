from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#Crear app de Flask
app = Flask(__name__)
CORS(app)
#Configurando la aplicacion
app.config.from_object(Config)

#Conectar la aplicacion con la BD
db=SQLAlchemy(app)

from app import models, rutas
