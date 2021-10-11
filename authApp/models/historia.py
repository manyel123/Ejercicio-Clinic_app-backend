from django.db import models
from .paciente import Paciente

class Historia(models.Model):
    id = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, related_name='paciente', on_delete=models.CASCADE)
    ultMedTrat = models.CharField('Ultimo medico tratante', max_length = 30)
    antQuirurgicos = models.CharField('Antecedentes quirurgicos', max_length = 100)
    antMedicos = models.CharField('Antecedentes medicos', max_length = 100)
    antFarmacologicos = models.CharField('Antecedentes farmacologicos', max_length = 100)
    tratamientoFarmacol = models.CharField('Tratamiento farmacologico actual', max_length = 100)
    diagPrevio = models.CharField('Diagnostico previo', max_length = 100)
    diagActual = models.CharField('Diagnostico actual', max_length = 100)
    observacion = models.TextField('Observaciones', max_length = 10000)