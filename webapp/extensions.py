from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from celery import Celery

bootstrap = Bootstrap()
celery = Celery(broker="redis://localhost:6379/0")
debug_toolbar = DebugToolbarExtension()

