from django.shortcuts import render, redirect
from core.forms import LoginForm, AgendaForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Agenda  # modelo do MongoEngine


# ------------------- LOGIN -------------------
def login(request):
    if request.user.id is not None:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        context = {'form': form, 'acesso_negado': True}
        return render(request, 'login.html', context)

    return render(request, 'login.html', {'form': LoginForm()})


# ------------------- LOGOUT -------------------
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("home")


# ------------------- HOME -------------------
@login_required
def home(request):
    return render(request, 'index.html', {})


# ------------------- CRUD MONGODB -------------------
@login_required
def lista_contatos(request):
    """Lista todos os contatos salvos no MongoDB"""
    contatos = Agenda.objects.all()
    return render(request, 'listar_contatos.html', {'contatos': contatos})


@login_required
def novo_contato(request):
    """Cria um novo contato no MongoDB"""
    form = AgendaForm(request.POST or None)
    if form.is_valid():
        form.save()  # salva direto no Mongo
        return redirect('listar_contatos')
    return render(request, 'novo_contato.html', {'form': form})


@login_required
def editar_contato(request, id):
    """Edita um contato existente no MongoDB"""
    try:
        contato = Agenda.objects.get(id=id)
    except Agenda.DoesNotExist:
        raise Http404("Contato não encontrado")

    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contato.nome_completo = data['nome_completo']
            contato.telefone = data.get('telefone', '')
            contato.email = data['email']
            contato.observacao = data.get('observacao', '')
            contato.save()
            return redirect('lista_edita')
    else:
        form = AgendaForm(initial={
            'nome_completo': contato.nome_completo,
            'telefone': contato.telefone,
            'email': contato.email,
            'observacao': contato.observacao
        })

    return render(request, 'editar_contato.html', {'form': form, 'contato': contato})


@login_required
def excluir_contato(request, id):
    """Exclui um contato no MongoDB"""
    try:
        contato = Agenda.objects.get(id=id)
    except Agenda.DoesNotExist:
        raise Http404("Contato não encontrado")

    if request.method == 'POST':
        contato.delete()
        return redirect('lista_exclui')

    return render(request, 'excluir_contato.html', {'contato': contato})


@login_required
def lista_edita(request):
    """Lista contatos para edição"""
    contatos = Agenda.objects.all()
    return render(request, 'lista_edita.html', {'contatos': contatos})


@login_required
def lista_exclui(request):
    """Lista contatos para exclusão"""
    contatos = Agenda.objects.all()
    return render(request, 'lista_exclui.html', {'contatos': contatos})

from core.db_mongo import get_db

db = get_db()
colecao = db.contatos

