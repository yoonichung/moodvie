from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # database
migrate = Migrate(app, db) # migration engine

from app import routes, models # bottom import as a workaround to circular imports
