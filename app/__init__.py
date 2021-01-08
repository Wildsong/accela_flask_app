from flask import Flask
from flask_bootstrap import Bootstrap
import logging
# I don't know where logging will go right now!

app = Flask(__name__)
#app.config.from_object(Config)

bootstrap = Bootstrap(app)

from app import routes
