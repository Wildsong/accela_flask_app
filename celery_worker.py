"""
    This is called from the celery CLI to start the worker, for example,

    celery -A celery_worker worker --loglevel=info
"""
import os
from app import create_app

config_name = os.environ.get('FLASK_ENV', 'default')
flask_app = create_app(config_name)

# The celery CLI needs to see that "celery" is defined.
celery = flask_app.celery
