from django.db import models
from django.contrib.auth.models import User

class Agendamento(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Agendamento de {self.cliente.username} para {self.servico}'

