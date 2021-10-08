from django.db import models
from .user import User
from .paciente import Paciente

class Cita(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, related_name='paciente_id', on_delete=models.CASCADE)
    fechaCita = models.CharField('Fecha de Cita', max_length = 10)