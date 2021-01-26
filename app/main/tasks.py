from .. import celery
from flask import current_app as app
from ..data import bigData


@celery.task(name='Add')
def Add(x,y):
    """ Just add two integers together to test the whole Celery thing. """
    print("Add(%d, %d)" % (x,y))
    return x+y


@celery.task(name='QueryParcels')
def QueryParcels(query):
    """ Query Accela and return results. """
    print("QueryParcels(%s)")

    layername = app.config["TABLE_URL"]
  
    print("Loading data from %s", layername)
    dObj = bigData(app.config)
    df = dObj.read_df(layername)

    return df.to_html()

