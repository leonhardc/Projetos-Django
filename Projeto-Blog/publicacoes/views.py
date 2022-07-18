from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from publicacoes.models import Publicacoes # para PostIndex()

# Create your views here.
class PostIndex(ListView):
    model = Publicacoes
    template_name = 'publicacoes/index.html'
    paginate_by = 3
    context_object_name = 'publicacoes' # obejto iteravel que setá usado em index.html

class PostBusca(PostIndex):
    pass

class PostCategoria(PostIndex):
    pass

class PostDetalhes(UpdateView):
    pass