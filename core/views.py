from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# def index(request):
#     return redirect('/agenda/')

def consulta_evento (request, titulo_evento):
    consulta = Evento.objects.get(titulo=titulo_evento)
    titulo = consulta.titulo
    data_evento = consulta.data_evento
    return HttpResponse('Evento: {} <br>Data: {}'.format(titulo, data_evento))

def login_user(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados_evento = {'eventos' : evento}
    return render(request, 'agenda.html', dados_evento)

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou Senha inválidos')
            return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def evento (request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados ['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

    return render(request, 'evento.html')

def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                       data_evento=data_evento,
                                                       descricao=descricao,
                                                       local=local)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  local=local,
                                  usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')






