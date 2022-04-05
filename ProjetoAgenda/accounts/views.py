from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email # validar email
from django.contrib.auth.models import User # checar a existência de um usuário na base de dados


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    # checando o formulário está vazio.
    if request.method != 'POST':
        messages.info(request, 'NADA POSTADO.')
        return render(request, 'accounts/register.html')
    # declarando variáveis
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha_dois = request.POST.get('senha2')
    # fazendo checagem das variáveis
    if not nome or not sobrenome or not email or not usuario or not senha or not senha_dois:
        messages.error(request, 'Nenhum dos campos pode ser vazio.')

    try:
        # validação de email
        validate_email(email)

    except:
        messages.error(request, 'O campo "Email" não é válido.')
        return render(request, 'accounts/register.html')

    if len(senha) < 6:
        # validação do tamanho da senha
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/register.html')

    if len(usuario) < 6:
        # validação do tamanho do usuário
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/register.html')

    if senha != senha_dois:
        # validação se a primeira senha coincide com a segunda senha.
        messages.error(request, 'Senhas não são iguais.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        # checa se o usuário digitado no formulário existe na base de dados
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        # checa se o usuário digitado no formulário existe na base de dados
        messages.error(request, 'Email já existe.')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Registrado com Sucesso.')
    # registrar o usuário na base de dados
    user = User.objects.create_user(username=usuario,
                                    email=email,
                                    password=senha,
                                    first_name=nome,
                                    last_name=sobrenome)
    user.save()
    # redireciona para tela de login
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

