"""
Start me with

    FLASK_APP=start_app flask run

"""
import os
from app import create_app
from version import version

app = create_app(os.environ.get("FLASK_ENV", "default"))

# I need to add tests!
