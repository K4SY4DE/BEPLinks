from django import forms
from .models import Tema, Recurso


# Formulário para criar Tema
class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'resumo']


# Formulário para criar e editar Recurso
class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = [
            'tema',
            'nome',
            'descricao',
            'tipo',
            'url',
            'gratuito'
        ]