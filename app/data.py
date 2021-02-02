import sys
import os
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
from datetime import datetime
#from pytz import timezone
#from tzlocal import get_localzone
#from utils import local2utc
import unittest

time_format = "%m/%d/%Y %H:%M"
error = "ERROR 99999"

def parsetime(s) :
    """ Parse a time string and return a datetime object. """
    return datetime.strptime(s, time_format)

def urlfmt(row):
    display = row['ACCOUNT_ID']
    return display


class bigData(object):

    def __init__(self, config):
        """
        Arguments:
            config is a dictionary containing configuration settings
        """
        self.config = config

    def connect(self, layername):
        layer = None
        try:
            portal = GIS(self.config['PORTAL_URL'], 
                self.config['PORTAL_USER'], self.config['PORTAL_PASSWORD'])
            #print("Logged in as " + str(portal.properties.user.username))
            layer = FeatureLayer(layername, portal)
        except Exception as e:
            print("Make sure the environment variables are set correctly.")
            sys.exit("Could not connect to portal. \"%s\"" % e)
        return layer

    def read_df(self, layername):
        """
        Read the feature layer into a dataframe.

        @Returns
        Dataframe
        """
        fields = ["TAXMAPKEY", "ACCOUNT_ID"]
        layer = self.connect(layername)
        sdf = layer.query(where="TAXMAPKEY LIKE '80918AA%'", out_fields=fields).sdf

        df = sdf.drop(labels='SHAPE', axis=1).set_index('OBJECTID')
        df['property_details'] = df.apply(urlfmt, axis=1)
        return df

# ========================================================================================

class DataTestCase(unittest.TestCase):

    def setUp(self):
        self.configObj = config['testing']

    def test_loaddata(self):
        dconfig = TestConfig.asdict(self.configObj)
        coolBeans = bigData(dconfig)
        df = coolBeans.read_df(dconfig['TABLE_URL'])
#        print(df.columns, len(df))
#        print(df)
        self.assertTrue(len(df) > 0)

if __name__ == "__main__":
    from config import config, TestConfig
    tests = DataTestCase()
    tests.setUp()
    tests.test_loaddata()

    unittest.main()
    
# That's all!
