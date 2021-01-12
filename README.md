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

I use Conda to manage python environments, so...

```bash
conda create --name=accela
conda install --name=accela --file=requirements.txt
conda activate accela
```

I use Visual Studio Code as my IDE, so this project includes a .vscode/launch.json file
and a workspace file. I refer to code provided by Accela from time to time (accela/accela-rest-nodejs at github) and some I wrote myself which will be incorporated here
today.

## Deploy

No deployments yet so no docs.

