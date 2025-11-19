from django.urls import path
from . import views

urlpatterns = [
    path('compromissos/', views.listar_compromissos, name='listar_compromissos'),
]
