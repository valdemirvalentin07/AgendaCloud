class Agenda:
    def __init__(self, nome_completo, telefone, email, observacao=None):
        self.nome_completo = nome_completo
        self.telefone = telefone
        self.email = email
        self.observacao = observacao

    def to_dict(self):
        return {
            "nome_completo": self.nome_completo,
            "telefone": self.telefone,
            "email": self.email,
            "observacao": self.observacao
        }
