from django.http import JsonResponse
from .models import Compromisso

def listar_compromissos(request):
    compromissos = Compromisso.objects.all()
    data = [{"titulo": c.titulo, "data": str(c.data)} for c in compromissos]
    return JsonResponse(data, safe=False)



