from django.db import models
from medico.models import Medico

class Horario(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return {'cita':self.cita,'medico':self.medico}