from celery import Celery

def make_celery(app):
    """ Set up celery """
    celery = Celery(app.import_name,
                    broker=app.config['CELERY_BROKER'],
                    backend=app.config['CELERY_BACKEND'])
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
