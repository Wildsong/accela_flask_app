import os

# In PRODUCTION conda sets up the environment,
# so look in ~/.conda/envs/covid/etc/conda/activate.d/env_vars.sh
# to see how it is set up.

class Config(object):
    """ Read environment here to create configuration data. """

    SECRET_KEY = os.environ.get('SECRET_KEY') or "12345678"
 
    PORTAL_URL      = os.environ.get('PORTAL_URL')
    PORTAL_USER     = os.environ.get('PORTAL_USER')
    PORTAL_PASSWORD = os.environ.get('PORTAL_PASSWORD')

# Where data live
    TABLE_URL = os.environ.get('TABLE_URL')

    pass

if __name__ == "__main__":

    assert Config.PORTAL_URL
    assert Config.PORTAL_USER
    assert Config.PORTAL_PASSWORD
    assert Config.TABLE_URL
    pass

# That's all!
