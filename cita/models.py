from django.db import models
from medico.models import Medico

class Cita(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    def __str__(self):
        return {'medico':self.medico,'date':self.date,'time':self.time}