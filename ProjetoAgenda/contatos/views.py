from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato
from django.db.models import Q, Value # Q -> modulo django para fazer consultas mais complexas
from django.db.models.functions import Concat
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def index(request):
    # adicionando paginação no projeto

    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True, do_usuario=auth.get_user(request).id
    )
    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


@login_required(redirect_field_name='login')
def ver_contato(request, contato_id):
    try:
        usuario_id = auth.get_user(request).id
        contato = Contato.objects.get(id=contato_id, do_usuario=usuario_id)

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
        raise Http404()


@login_required(redirect_field_name='login')
def excluir_contato(request, contato_id):

    # excluir contato
    record = Contato.objects.get(id=contato_id)
    record.delete()

    return redirect('index')

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

    if termo is None or not termo:
        messages.add_message(request,
                             messages.ERROR,
                             'O campo não pode ficar vazio.')
        return redirect('index')



    campos = Concat('nome', Value(' '),'sobrenome')
    usuario_id = auth.get_user(request).id
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) & Q(do_usuario__icontains=usuario_id)
        | Q(telefone__icontains=termo)  & Q(do_usuario__icontains=usuario_id)
    )

    if contatos:
        messages.add_message(request,
                             messages.INFO,
                             'Busca realizada com sucesso.')

    else:
        messages.add_message(request,
                             messages.INFO,
                             'Nenhum resultado encontrado.')


    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })

def url_vazia(request):
    return render(request, 'empty.html')