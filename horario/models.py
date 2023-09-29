from django.db import models
from medico.models import Medico

class Horario(models.Model):
    medico = models.DecimalField(Medico.id)
    date = models.DateField()

    def __str__(self):
        return {'cita':self.cita,'medico':self.medico}