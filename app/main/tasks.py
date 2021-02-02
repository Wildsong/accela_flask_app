from .. import celery
from flask import current_app as app
from ..data import bigData


@celery.task(name='add')
def add(x,y):
    """ Just add two integers together to test the whole Celery thing. """
    print("Add(%d, %d)" % (x,y))
    return x+y


@celery.task(name='queryparcels')
def queryparcels(query):
    """ Query Accela and return results. """
    print("QueryParcels(%s)")

    layername = app.config["TABLE_URL"]
  
    dObj = bigData(app.config)
    try:
        df = dObj.read_df(layername)
        #data = "Data from %s" % layername
        data = df.to_html()
    except Exception as e:
        data = "Data fetch from %s failed, %s" % (layername, e)
    
    return data

