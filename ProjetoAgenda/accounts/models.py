from django.db import models
from contatos.models import Contato
from django import forms


class FormContato(forms.ModelForm):
    """
    Formulário automático para Contato.
    Obs: Exclui campos 'mostrar', e 'do_usuario'
    """
    class Meta:
        model = Contato
        exclude = ('mostrar','do_usuario')