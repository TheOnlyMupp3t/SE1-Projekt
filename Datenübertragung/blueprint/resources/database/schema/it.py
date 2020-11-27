from ..setup import db

it = 'it'

class ItSchema(db.Document):
    time = db.DateTimeField()
    server_cpu_usage = db.IntField()
    server_ram_usage = db.IntField()
    server_login_failed = db.IntField()
    server_login_success = db.IntField()
    traffic_upload = db.IntField()
    traffic_download = db.IntField()
    news = db.StringField()
