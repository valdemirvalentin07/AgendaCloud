from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from mongoengine import DoesNotExist
from .models import Agenda  # usamos o modelo do mongoengine


# --- LOGIN FORM ---
class LoginForm(forms.Form):
    email = forms.EmailField(
        label="E-Mail:",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail institucional'
        })
    )
    password = forms.CharField(
        label="Senha:",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@fatec.sp.gov.br'):
            raise ValidationError('Informe seu e-mail institucional.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise ValidationError("Usuário com esse e-mail não encontrado.")

            user = authenticate(username=user.username, password=password)
            if user is None:
                raise ValidationError("Senha incorreta para o e-mail informado.")

            self.user = user
        return cleaned_data


# --- CONTATO/AGENDA FORM (usando MongoDB) ---
class AgendaForm(forms.Form):
    nome_completo = forms.CharField(
        label="Nome Completo",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telefone = forms.CharField(
        label="Telefone",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    observacao = forms.CharField(
        label="Observação",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    def save(self):
        """Salva os dados no MongoDB"""
        data = self.cleaned_data
        agenda = Agenda(
            nome_completo=data['nome_completo'],
            telefone=data.get('telefone', ''),
            email=data['email'],
            observacao=data.get('observacao', '')
        )
        agenda.save()
        return agenda
