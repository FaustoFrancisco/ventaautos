from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

#Crear app de Flask
app = Flask(__name__)

#Configurando la aplicacion
app.config.from_object(Config)

#Conectar la aplicacion con la BD
db=SQLAlchemy(app)

from app import models, rutas
