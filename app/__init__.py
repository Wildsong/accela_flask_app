import os
import logging
from flask import Flask, render_template
from config import config
from .celery_factory import make_celery
from .extensions import *

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)
log = logging.getLogger(__name__)

bootstrap = Bootstrap()
debug_toolbar = DebugToolbarExtension()


def page_not_found(error):
    return render_template('404.html'), 404


def create_app(config_name='default'):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        configuration: the python path of the config object,
                     e.g. project.config.ProdConfig
    """
    app = Flask(__name__)

    config_obj = config[config_name]
    app.config.from_object(config_obj)
    config_obj.init_app(app)

    bootstrap.init_app(app)
    debug_toolbar.init_app(app)

    # I have not figured out a better way to make this visible from tasks.
    global celery 
    celery = make_celery(app)
    # This makes it visible in celery_worker
    app.celery = celery

    # Add routes and custom error pages

    # Load blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.register_error_handler(404, page_not_found)
    return app


# That's all!
