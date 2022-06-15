from django.urls import path
from . import views


urlpatterns = [
    path('', views.url_vazia),
    path('index/', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>/', views.ver_contato, name='ver_contato'),
    path('<int:contato_id>/update/', views.atualiza_contato, name="atualiza_contato"),
    path('<int:contato_id>/delete', views.excluir_contato, name='excluir_contato'),
]