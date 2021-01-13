"""
Celery server

To execute workers, run me with: 

    celery -A tasks worker -l info

To start a worker, import me into your flask app:

    import tasks
    from celery.result import AsyncResult
    ..etc

"""
from celery import Celery

REDIS_URL = "redis://cc-testmaps:6379/0"
celery = Celery("tasks", broker=REDIS_URL, backend=REDIS_URL)

@celery.task(name='query.parcels')
def query_parcels(query):
    """ Query Accela and return results. """
    some_data = ['Hello world']
    return some_data

@celery.task(name='add')
def add(x,y):
    print("adding %d + %d" % (x,y))
    return x+y


