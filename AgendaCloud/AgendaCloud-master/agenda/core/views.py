from django.shortcuts import render, redirect
from core.forms import LoginForm, AgendaForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Agenda  # modelo do MongoEngine


# ------------------- LOGIN -------------------
def login_view(request):
    if request.user.id is not None:
        return redirect("core:home")   # corrigido

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("core:home")   # corrigido
        context = {'form': form, 'acesso_negado': True}
        return render(request, 'login.html', context)

    return render(request, 'login.html', {'form': LoginForm()})


# ------------------- LOGOUT -------------------
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("core:home")   # corrigido


# ------------------- HOME -------------------
@login_required
def home(request):
    return render(request, 'index.html', {})


# ------------------- CRUD MONGODB -------------------
from mongoengine.queryset.visitor import Q

@login_required
def lista_contatos(request):
    q = request.GET.get("q", "").strip()

    if q:
        contatos = Agenda.objects(
            Q(nome_completo__icontains=q) |
            Q(email__icontains=q) |
            Q(telefone__icontains=q) |
            Q(observacao__icontains=q)
        )
    else:
        contatos = Agenda.objects.all()

    return render(request, 'listar_contatos.html', {
        'contatos': contatos,
        'q': q
    })


@login_required
def novo_contato(request):
    form = AgendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core:listar_contatos')   # corrigido
    return render(request, 'novo_contato.html', {'form': form})


@login_required
def editar_contato(request, id):
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
            return redirect('core:lista_edita')   # corrigido
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
    try:
        contato = Agenda.objects.get(id=id)
    except Agenda.DoesNotExist:
        raise Http404("Contato não encontrado")

    if request.method == 'POST':
        contato.delete()
        return redirect('core:lista_exclui')   # corrigido

    return render(request, 'excluir_contato.html', {'contato': contato})


from mongoengine.queryset.visitor import Q

@login_required
def lista_edita(request):
    q = request.GET.get("q", "").strip()

    if q:
        contatos = Agenda.objects(
            Q(nome_completo__icontains=q) |
            Q(email__icontains=q) |
            Q(telefone__icontains=q) |
            Q(observacao__icontains=q)
        )
    else:
        contatos = Agenda.objects.all()

    return render(request, 'lista_edita.html', {
        'contatos': contatos,
        'q': q
    })


from mongoengine.queryset.visitor import Q

@login_required
def lista_exclui(request):
    q = request.GET.get("q", "").strip()

    if q:
        contatos = Agenda.objects(
            Q(nome_completo__icontains=q) |
            Q(email__icontains=q) |
            Q(telefone__icontains=q) |
            Q(observacao__icontains=q)
        )
    else:
        contatos = Agenda.objects.all()

    return render(request, 'lista_exclui.html', {
        'contatos': contatos,
        'q': q
    })


from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

@login_required
def relatorio_pdf(request):
    q = request.GET.get("q", "").strip()

    if q:
        contatos = Agenda.objects(
            Q(nome_completo__icontains=q) |
            Q(email__icontains=q) |
            Q(telefone__icontains=q) |
            Q(observacao__icontains=q)
        )
    else:
        contatos = Agenda.objects.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_contatos.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    largura, altura = A4

    y = altura - 50
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Relatório de Contatos")
    
    y -= 40
    p.setFont("Helvetica", 12)
    p.drawString(50, y, f"Filtro aplicado: {q if q else 'Nenhum'}")

    y -= 40
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Nome")
    p.drawString(200, y, "Email")
    p.drawString(380, y, "Telefone")

    y -= 20
    p.line(50, y, 550, y)
    y -= 20

    p.setFont("Helvetica", 11)

    for contato in contatos:
        if y < 80:
            p.showPage()
            y = altura - 50

        p.drawString(50, y, contato.nome_completo[:25])
        p.drawString(200, y, contato.email[:25])
        p.drawString(380, y, contato.telefone)
        y -= 20

    p.showPage()
    p.save()
    return response
