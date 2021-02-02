from logging import DEBUG
import os
import inspect

basedir = os.path.abspath(os.path.dirname(__file__))

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
    TABLE_URL = os.environ.get('TABLE_URL', "https://delta.co.clatsop.or.us/server/rest/services/Taxlots/FeatureServer/1")

# Celery stuff
    CELERY_BROKER = os.environ.get('CELERY_BROKER')
    CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

    enable_utc = True
    timezone = 'America/Los_Angeles'

    @staticmethod
    def asdict(config):
        d = {}
        for k,v in inspect.getmembers(config):
            # I am using callable() here to exclude asdict and init_app.
            if not callable(v) and not k.startswith('__'): 
                d[k] = v
        return d

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}



if __name__ == "__main__":
    config = config['testing']
    dconfig = TestConfig.asdict(config)
    print(dconfig)

    assert config.SECRET_KEY != type("")
    assert config.PORTAL_URL != type("")
    assert config.PORTAL_USER != type("")
    assert config.PORTAL_PASSWORD != type("")
    assert config.TABLE_URL != type("")

    assert type(Config.enable_utc) == type(True)
    assert config.timezone != type("")
    pass

# That's all!
