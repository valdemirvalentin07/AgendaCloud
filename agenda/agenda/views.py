from django.shortcuts import render, redirect
from .repository import AgendaRepository

repo = AgendaRepository()

def novo_contato(request):
    if request.method == 'POST':
        dados = {
            "nome_completo": request.POST.get("nome_completo"),
            "telefone": request.POST.get("telefone"),
            "email": request.POST.get("email"),
            "observacao": request.POST.get("observacao"),
        }

        repo.adicionar(dados)
        return redirect('listar_contatos')

    return render(request, 'novo_contato.html')
    


def listar_contatos(request):
    contatos = repo.listar()
    return render(request, 'listar_contatos.html', {'contatos': contatos})
