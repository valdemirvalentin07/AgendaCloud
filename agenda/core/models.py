from mongoengine import Document, StringField, EmailField

class Contato(Document):
    nome = StringField(required=True, max_length=100)
    email = EmailField(required=True)
    telefone = StringField(max_length=20)

    meta = {'collection': 'contatos'}

    def __str__(self):
        return self.nome


class Agenda(Document):
    nome_completo = StringField(required=True, max_length=150)
    telefone = StringField(max_length=20)
    email = EmailField(required=True)
    observacao = StringField()

    meta = {'collection': 'agendas'}

    def __str__(self):
        return f"{self.nome_completo} - {self.email}"
