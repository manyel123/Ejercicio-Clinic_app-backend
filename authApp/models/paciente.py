from django.db import models

class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    document = models.CharField('Documento', max_length = 10)
    name = models.CharField('Nombre', max_length = 30)
    email = models.EmailField('Email', max_length = 100)
    fechaNacim = models.CharField('Fecha de Nacimiento', max_length = 10)
    telefono = models.CharField('Telefono', max_length = 10)
    direccion = models.CharField('Direccion', max_length = 30)
    ciudad = models.CharField('Ciudad', max_length = 20)