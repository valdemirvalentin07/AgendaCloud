from mongoengine import Document, StringField, DateTimeField

class Compromisso(Document):
    titulo = StringField(required=True, max_length=100)
    data = DateTimeField(required=True)

    meta = {'collection': 'compromissos'}
