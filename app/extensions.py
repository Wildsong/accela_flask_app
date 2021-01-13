from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from celery import Celery

bootstrap = Bootstrap()
debug_toolbar = DebugToolbarExtension()

REDIS_URL = "redis://cc-testmaps:6379/0"
app = Celery("tasks", broker=REDIS_URL, backend=REDIS_URL)
