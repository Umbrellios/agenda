from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# def index(request):
#     return redirect('/agenda/')

def consulta_evento (request, titulo_evento):
    consulta = Evento.objects.get(titulo=titulo_evento)
    titulo = consulta.titulo
    data_evento = consulta.data_evento
    return HttpResponse('Evento: {} <br>Data: {}'.format(titulo, data_evento))

def lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados_evento = {'eventos' : evento}
    return render(request, 'agenda.html', dados_evento)
