from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from publicacoes.models import Publicacoes # para PostIndex()

# Create your views here.
class PostIndex(ListView):
    model = Publicacoes
    template_name = 'publicacoes/index.html'
    paginate_by = 6
    context_object_name = 'publicacoes' # obejto iteravel que setá usado em index.html

    def get_queryset(self): # sobrescrever método para mudar a ordem de exibição das
                            # publicoes na página
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        return qs

class PostBusca(PostIndex):
    pass

class PostCategoria(PostIndex):
    pass

class PostDetalhes(UpdateView):
    pass