from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'evento'

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y')

    def get_hora_evento(self):
        return self.data_evento.strftime('%H:%M')




