from ..setup import db

test = 'test'

class TestSchema(db.Document):
    news = db.StringField()
