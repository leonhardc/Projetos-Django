from django.shortcuts import render
from django.http import Http404
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)
        return render(request, 'contatos/ver_contato.html', {
            'contato': contato
        })
    except Contato.DoesNotExist as e:
        print(e)
        # O erro abaixo se refere a uma página web não encontrada.
        return Http404()

# outra forma de fazer a view 'ver_contato'
#
#
#
# from django.shortcuts import get_object_or_404
# def ver_contato(request, contato_id):
#     contato = Contato.objects.get(id=contato_id)
#     contato = get_object_or_404(Contato, id=contato_id)
#     return render(request, 'contatos/ver_contato.html', {
#         'contato': contato
#     })

