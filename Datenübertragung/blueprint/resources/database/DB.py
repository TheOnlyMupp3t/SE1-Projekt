from flask import Flask
from flask_mongoalchemy import MongoAlchemy
import datetime as dt
server = "localhost"
port = "27017"
# user =
# password =
database = "jo"
app = Flask(__name__)
# enter Database Configuration herev
app.config['MONGOALCHEMY_SERVER'] = server
app.config['MONGOALCHEMY_PORT'] = port
# app.config['MONGOALCHEMY_USER'] =
# app.config['MONGOALCHEMY_PASSWORD'] =
app.config['MONGOALCHEMY_DATABASE'] = database
db = MongoAlchemy(app)
print(dt.datetime.now())


class dbManager():
    def write_it(self, json):

        itdict = {"time": dt.datetime.now()}
        for elem in json:
            key = elem['name'].replace('-', '_')
            itdict[key] = elem['value']
        x = it( **itdict)
        x.save()

class it(db.Document):
    time = db.DateTimeField()
    server_cpu_usage = db.IntField()
    server_ram_usage = db.IntField()
    server_login_failed = db.IntField()
    server_login_success = db.IntField()
    traffic_upload = db.IntField()
    traffic_download = db.IntField()
    news = db.StringField()


json = [
    {
        "name": "server-cpu-usage",
        "unit": "%",
        "value": 51
    },
    {
        "name": "server-ram-usage",
        "unit": "%",
        "value": 19
    },
    {
        "name": "server-login-failed",
        "unit": "count",
        "value": 107
    },
    {
        "name": "server-login-success",
        "unit": "count",
        "value": 1038
    },
    {
        "name": "traffic-upload",
        "unit": "Mb/s",
        "value": 42
    },
    {
        "name": "traffic-download",
        "unit": "Mb/s",
        "value": 72
    },
    {
        "name": "news",
        "unit": "-",
        "value": "pre check of ubuntu 20.05 LTS initiated<br>"
    }
]
peter = dbManager()
peter.write_it(json)
