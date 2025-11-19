📘 AgendaCloud – Sistema de Agenda de Contatos

O AgendaCloud é um sistema moderno de gerenciamento de contatos criado com Django e MongoDB (via MongoEngine).
Ele permite cadastrar, listar, editar e excluir contatos em uma interface intuitiva, responsiva e estilizada com Bootstrap 5, utilizando autenticação de usuários nativa do Django.

Este projeto une o poder do Django com a flexibilidade do MongoDB, oferecendo um CRUD rápido e eficiente em um ambiente seguro e escalável.

🚀 Tecnologias Utilizadas
🖥 Backend

Python 3.x

Django 5.x

MongoDB + MongoEngine

SQLite (para login e sessões)

🎨 Frontend

HTML5 / CSS3

Bootstrap 5

FontAwesome Icons

📌 Principais Funcionalidades
✔ Autenticação

Login e Logout

Proteção de rotas com login_required

✔ Gestão de Contatos (MongoDB)

Criar contato

Editar contato

Excluir contato

Listar todos os contatos

Listas separadas para edição e exclusão

Formulários responsivos com layout moderno

✔ Interface Moderna

Cards centralizados

Fundo em gradiente (tema escuro/azul)

Botões estilizados

Tabelas responsivas

Ícones FontAwesome

📂 Estrutura do Projeto
AgendaCloud/
│
├── agenda/                # Configurações principais do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                  # Aplicação principal
│   ├── models.py          # Modelo Agenda (MongoEngine)
│   ├── forms.py           # Formulários
│   ├── views.py           # Lógica do CRUD + Login
│   ├── urls.py            # Rotas da aplicação
│   ├── db_mongo.py        # Conexão com MongoDB
│   └── templates/         # Arquivos HTML
│       ├── index.html
│       ├── login.html
│       ├── listar_contatos.html
│       ├── novo_contato.html
│       ├── editar_contato.html
│       ├── excluir_contato.html
│       ├── lista_edita.html
│       └── lista_exclui.html
│
├── db.sqlite3             # Banco padrão do Django (users, sessions)
├── manage.py              # Executar e gerenciar o projeto
└── requirements.txt       # Dependências

⚙️ Instalação e Configuração
1️⃣ Clone o repositório
git clone https://github.com/SEU_USUARIO/AgendaCloud.git
cd AgendaCloud

2️⃣ Crie o ambiente virtual
python -m venv venv


Ative:

Windows

venv\Scripts\activate


Linux/macOS

source venv/bin/activate

3️⃣ Instale as dependências
pip install -r requirements.txt

🗄️ Configuração do MongoDB

Edite o arquivo:

core/db_mongo.py


Exemplo de conexão:

from mongoengine import connect

def get_db():
    return connect(
        db='agenda_cloud',
        host='mongodb://localhost:27017/agenda_cloud'
    )


Certifique-se de que o MongoDB está rodando:

mongod

🔧 Migre o banco SQLite (autenticação)
python manage.py migrate

(opcional) Crie um usuário admin
python manage.py createsuperuser

▶️ Executar o projeto
python manage.py runserver


Acesse:

http://127.0.0.1:8000/

📖 Como funciona o CRUD do MongoEngine
Modelo (MongoEngine)
class Agenda(Document):
    nome_completo = StringField(required=True)
    email = StringField(required=True)
    telefone = StringField()
    observacao = StringField()

Operações
Ação	Método
Criar	Agenda(...).save()
Listar	Agenda.objects.all()
Editar	Agenda.objects.get(id=id)
Excluir	contato.delete()
🖼️ Screenshots (adicione aqui)
🔹 Tela de Login

<img width="1179" height="823" alt="login" src="https://github.com/user-attachments/assets/192a2264-2afa-4d93-b7d2-b6ac0793469f" />


🔹 Lista de Contatos

<img width="1133" height="554" alt="image" src="https://github.com/user-attachments/assets/c3fe37b4-024b-4ddb-91c3-6eae81ae6db1" />


🔹 Formulário de Edição

<img width="790" height="771" alt="image" src="https://github.com/user-attachments/assets/0a47143c-5e2e-45d9-bb32-7920fff49799" />


📝 Licença

Este projeto é livre para uso pessoal, acadêmico e profissional.

🤝 Contribuições

Contribuições são bem-vindas!
Abra um PR ou Issue caso deseje sugerir melhorias.
