from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from publicacoes.models import Publicacoes # para PostIndex()
from django.db.models import Q, Count, Case, When # para ejetar numero de comentarios em
                                                  # PostIndex >> get_queryset()

# Create your views here.
class PostIndex(ListView):
    model = Publicacoes
    template_name = 'publicacoes/index.html'
    paginate_by = 6
    context_object_name = 'publicacoes' # obejto iteravel que setá usado em index.html

    def get_queryset(self): # sobrescrever método para mudar a ordem de exibição das
                            # publicoes na página
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)
        # ejetar na consulta o numero de comentarios publicados
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(
                        comentario__publicado_comentario=True,
                        then=1
                    )
                )
            )
        )
        return qs

class PostBusca(PostIndex):
    pass

class PostCategoria(PostIndex):
    pass

class PostDetalhes(UpdateView):
    pass