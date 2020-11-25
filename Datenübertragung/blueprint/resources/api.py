from config import config
import urllib.request
from enum import Enum


class ApiAbfrage():
    def __init__(self):
        self.host = config['DEFAULT']['host']
        self.port = config['DEFAULT']['port']
        self.username = config['DEFAULT']['username']
        self.password = config['DEFAULT']['password']

        print(self.host)
        print(self.port)
        print(self.username)
        print(self.password)

        self.passwdmanager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        self.passwdmanager.add_password(
            None, 'http://asm.fl.dlr.de:10001', 'tinf19cs', '$sse1%8Dh2bw')

        handler = urllib.request.HTTPBasicAuthHandler(self.passwdmanager)
        opener = urllib.request.build_opener(handler)

        urllib.request.install_opener(opener)

        with opener.open('http://asm.fl.dlr.de:10001/it') as url:
            data = json.loads(url.read().decode())
            print(data)

    def get(self, endpoint):
        # with urllib.request.urlopen(self.host + ':' + self.port + '/' + str(endpoint)) as url:
        with urllib.request.urlopen('http://asm.fl.dlr.de:10001/it') as url:
            data = json.loads(url.read().decode())
            print(data)


class Endpoints(Enum):
    IT = 'it'
    TERMINAL = 'terminal'
    RADAR = 'radar'
    FLIGHTPLANS = 'flightplans'


api = ApiAbfrage()
api.get(Endpoints.IT)
