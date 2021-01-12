"""
Celery server

Run me with:

celery -A tasks worker -l info

"""
from celery import Celery

REDIS_URL = "redis://cc-testmaps:6379/0"
app = Celery("tasks", broker=REDIS_URL, backend=REDIS_URL)

@app.task(name='query.parcels')
def query_parcels(query):
    """ Query Accela and return results. """
    some_data = ['Hello world']
    return some_data

@app.task(name='add')
def add(x,y):
    return x+y


