from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    # exibir na interface admin os campos abaixo
    list_display = ['id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_de_criacao', 'categoria', 'mostrar', 'do_usuario']

    # tornar os campos abaixo clicáveis
    list_display_links = ['id', 'nome', 'sobrenome']

    # acrescentar filtros por nome e sobrenome
    list_filter = ['nome', 'sobrenome']

    # exibir somente 10 elementos por página
    list_per_page = 10

    # adiciona fields de busca
    search_fields = ['nome', 'sobrenome']

    # campos editáveis na janela admin
    list_editable = ('telefone', 'mostrar')


# registrar as classes abaixo na interface de admin
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
