from django.shortcuts import render
from django.views.generic import ListView
# from ger_func.models import Funcionario



# class ListaFuncionarios(ListView):
#     template_name = 'templates/funcionarios.html'
#     model = Funcionario
#     context_object_name = 'funcionarios'


# def lista_funcionarios(request):
#     # Primeiro, buscamos os funcionarios
#     funcionarios = Funcionario.Objetos.all()
#
#     # Incluimos no contexto
#     contexto = {
#         'funcionarios': funcionarios
#     }
#
#     # Retornamos o tempate para listar os funcionarios
#     return render(
#         request,
#         'templates/funcionarios.html',
#         contexto
#     )