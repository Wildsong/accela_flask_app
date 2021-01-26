# accela_flask_app
Flask microservice to access data stored in Accela via the Construct API

Currently it lets you enter a parcel number and then queries Accela for
information.

## Set up

Copy sample.env to .env and then localize it. You have to have
an Accela developer account, and access to an Accela server.
Use the developer account to create an app so that you can fill in the
API key and the secret key in the .env file.

### Development

During development, I run Redis in a docker but start and run the web app
and the celery worker directly. This means I can start a shell and launch
the celery worker and then run VSCode to debug the flask app.

I use Conda to manage python environments, so set the environment up first.
```bash
conda create --name=accela --file=requirements.txt
conda activate accela
```

Start a Redis instance with this:
```bash
docker run -d -p 6379:6379 redis:latest
```

Start celery with this:
```bash
. celery.env && ./scripts/start_celery_worker.sh
```

Now you are ready to debug the web app. 
I use Visual Studio Code as my IDE, so this project includes a .vscode/launch.json file
and a workspace file. 

## Celery

Celery is the task handler.
Official documentation: 
https://docs.celeryproject.org/en/latest/

## Redis

Redis is an in-memory database used to manage the task queue for Celery.

You can monitor what is going on in the Redis server, 
see https://redis.io/commands/monitor and try this:

```bash
docker exec -it your_image_name_bere redis-cli monitor
```

## Deployment

All three components (web app, celery worker, redis) are dockerized. So once
everything is functioning, you can deploy with Docker Swarm.

```bash
docker stack deploy -c docker-compose.yml accela
```

## TODO

* Examine security, I think we're good because the containers will use isolated network
once I dockerize the flask app.
* Add healthchecks.
* Move the Flask app to waitress.
* Currently running always in debug mode from the start_app.py script. Fix that.
