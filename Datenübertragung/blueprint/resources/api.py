import json
from .config import config
from http.client import HTTPConnection, HTTPSConnection
from base64 import b64encode
from enum import Enum

class ApiAbfrage():
    def __init__(self):
        self.host = config['DEFAULT']['host']
        self.port = config['DEFAULT']['port']
        self.protocol = config['DEFAULT']['protocol']
        self.username = config['DEFAULT']['username']
        self.password = config['DEFAULT']['password']

    def get(self, endpoint):

        if (self.protocol == "http"):
            c = HTTPConnection(self.host, int(self.port))
        else:
            c = HTTPSConnection(self.host, int(self.port))
        
        userAndPass = b64encode(bytes(self.username + ':' + self.password, 'utf-8')).decode("ascii")
        headers = { 'Authorization' : 'Basic %s' %  userAndPass }
        c.request('GET', endpoint.value, headers=headers)        
        res = c.getresponse()

        if (res.getcode() == 200):
            return json.loads(res.read().decode())
        return None

class Endpoints(Enum):
    IT = '/it'
    TERMINAL = '/terminal'
    RADAR = '/radar'
    FLIGHTPLANS = '/flightplans'


api = ApiAbfrage()
print(api.get(Endpoints.IT))
print(api.get(Endpoints.FLIGHTPLANS))
print(api.get(Endpoints.IT))
