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


🎯 Objetivo do Projeto

✔ Demonstrar como utilizar MongoDB como banco de dados principal para entidades de negócio

✔ Exibir como o MongoEngine substitui o ORM padrão do Django

✔ Explorar CRUD real utilizando documentos MongoDB

✔ Integrar Django + MongoDB de maneira limpa e escalável

✔ Ensinar a estrutura correta para trabalhar com coleções MongoDB em apps Django


Acesse:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/login/)

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

🔹 Tela de Login

<img width="981" height="672" alt="image" src="https://github.com/user-attachments/assets/c1fe2a1b-ec59-45a9-ab28-6fc7b84bd42c" />


🔹 Lista de Contatos

<img width="1133" height="554" alt="image" src="https://github.com/user-attachments/assets/c3fe37b4-024b-4ddb-91c3-6eae81ae6db1" />


🔹 Formulário de Edição

<img width="790" height="771" alt="image" src="https://github.com/user-attachments/assets/0a47143c-5e2e-45d9-bb32-7920fff49799" />


📝 Licença

Este projeto é livre para uso pessoal, acadêmico e profissional.

🤝 Contribuições

Contribuições são bem-vindas!
Abra um PR ou Issue caso deseje sugerir melhorias.
