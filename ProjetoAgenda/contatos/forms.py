from django import forms
from .models import Contato

# Criando um formulario
class ContatoForm(forms.ModelForm):

    # criando a meta-classe
    class Meta:
        # especificando o modelo que será usado
        model = Contato
        # especificando os campos que serão usados
        fields = [
            "nome",
            "sobrenome",
            "telefone",
            "email",
            "data_de_criacao",
            "descricao",
            "categoria",
            "foto"
        ]