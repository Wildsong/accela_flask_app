import sys
import os
from arcgis.gis import GIS
from arcgis.features import FeatureLayer

from datetime import datetime
#from pytz import timezone
#from tzlocal import get_localzone
#from utils import local2utc

from config import Config

portal_url = Config.PORTAL_URL
portal_user = Config.PORTAL_USER
portal_password  = Config.PORTAL_PASSWORD
table_url = Config.TABLE_URL

assert portal_url
assert portal_user
assert portal_password
assert table_url

time_format = "%m/%d/%Y %H:%M"
error = "ERROR 99999"

def parsetime(s) :
    """ Parse a time string and return a datetime object. """
    return datetime.strptime(s, time_format)

def connect(layername):
    layer = None
    try:
        portal = GIS(portal_url, portal_user, portal_password)
        #print("Logged in as " + str(portal.properties.user.username))
        layer = FeatureLayer(layername, portal)
    except Exception as e:
        print("Make sure the environment variables are set correctly.")
        sys.exit("Could not connect to portal. \"%s\"" % e)
    return layer

def read_sdf(layername):
    """
    Read the feature layer into a dataframe.

    @Returns
    Dataframe
    """
    fields = ["TAXMAPKEY", "ACCOUNT_ID"]
    layer = connect(layername)
    sdf = layer.query(where="TAXMAPKEY LIKE '80918AA%'", out_fields=fields).sdf
    del layer
    return sdf

if __name__ == "__main__":

    df = read_sdf(Config.TABLE_URL)
    print(df.columns, len(df))
    print(df)

# That's all!
