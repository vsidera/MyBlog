from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import routes