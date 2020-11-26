import datetime as dt
from flask_mongoalchemy import MongoAlchemy
from ..server import app
from ..utils import config

app.config['MONGOALCHEMY_SERVER'] = config['DATABASE']['host']
app.config['MONGOALCHEMY_PORT'] = config['DATABASE']['port']
app.config['MONGOALCHEMY_DATABASE'] = config['DATABASE']['database_name']
if (config['DATABASE']['authentification'] == True):
    app.config['MONGOALCHEMY_USER'] = config['DATABASE']['user']
    app.config['MONGOALCHEMY_PASSWORD'] = config['DATABASE']['password']

db = MongoAlchemy(app)
