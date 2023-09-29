from django.db import models
from medico.models import Medico
from cita.models import Cita

class Horario(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return {'cita':self.cita,'medico':self.medico,'date':self.date,'time':self.time}