from pymongo import MongoClient

class MongoConnection:
    def __init__(self, collection_name, uri="mongodb://localhost:27017/", db_name="agenda"):
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = None
        self.db = None
        self.collection = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
            print(f"✔ Conectado ao MongoDB (banco: {self.db_name}, coleção: {self.collection_name})")
            return self.collection
        except Exception as e:
            print("❌ Erro ao conectar ao MongoDB:", e)
            return None

    def close(self):
        if self.client:
            self.client.close()
            print("🔌 Conexão encerrada.")
