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

Gerar Relatório

✔ Interface Moderna

Cards centralizados

Fundo em gradiente (tema escuro/azul)

Botões estilizados

Tabelas responsivas

Ícones FontAwesome

Filtros digitaveis


🎯 Objetivo do Projeto

✔ Demonstrar como utilizar MongoDB como banco de dados principal para entidades de negócio

✔ Exibir como o MongoEngine substitui o ORM padrão do Django

✔ Explorar CRUD real utilizando documentos MongoDB

✔ Integrar Django + MongoDB de maneira limpa e escalável

✔ Ensinar a estrutura correta para trabalhar com coleções MongoDB em apps Django


Acesse:
[
(http://127.0.0.1:8000/login/)](http://127.0.0.1:8000/accounts/login/?next=/)

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



📝 Licença

Este projeto é livre para uso pessoal, acadêmico e profissional.

🤝 Contribuições

Contribuições são bem-vindas!
Abra um PR ou Issue caso deseje sugerir melhorias.
