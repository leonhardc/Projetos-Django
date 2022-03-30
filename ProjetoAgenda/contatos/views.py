from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato
from django.db.models import Q, Value # Q -> modulo django para fazer consultas mais complexas
from django.db.models.functions import Concat


def index(request):
    # adicionando paginação no projeto
    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)

        if not contato.mostrar:
            # se o campo 'mostrar' não estiver marcado, levantar
            # um erro "Page not found" (404)
            raise Http404()

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

def busca(request):
    termo = request.GET.get('termo')

    if termo is None:
        raise Http404()

    campos = Concat('nome', Value(' '),'sobrenome') # esse trecho faz parte da SOLUÇÃO 3

    # SOLUÇÃO 1
    # O trecho de codigo abaixo verifica se o termo digitado na caixa de busca
    # está contido no campo 'nome' de algum contato na nossa base de dados
    #
    # contatos = Contato.objects.order_by('nome').filter(
    #     nome__icontains=termo,
    #     mostrar=True
    # )

    # SOLUÇÃO 2
    # O trecho de codigo abaixo verifica se o termo digitado na caixa de busca
    # está contido no campo 'nome' da nossa base de dados ou se o termo digitado
    # na nossa caixa de busca está contido no termo 'sobrenome' da nossa base de dados
    #
    # contatos = Contato.objects.order_by('nome').filter(
    #     Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
    #     mostrar=True
    # )

    # SOLUÇÃO 3
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
