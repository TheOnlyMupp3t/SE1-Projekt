import datetime as dt
from .schema.it import ItSchema, it
from .schema.test import TestSchema

class DatabaseManager():

    @staticmethod
    def write(documentType, data):
        if (documentType == 'it'):
            document = ItSchema(**data)
            document.save()


# debug DatabaseManager-class
if __name__ == '__main__':
    print('*'*10 + ' Debug: DatabaseManager ' + '*'*10 )

    print(len(TestSchema.query.all()))
    doc = TestSchema(news='Test')
    doc.save()
    print(TestSchema.query.all())
    doc.remove()
    print(TestSchema.query.all())