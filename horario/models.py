from django.db import models
from medico.models import Medico

class Horario(models.Model):
    id=models.IntegerField(primary_key=True)
    profesional = models.ForeignKey(Medico, on_delete=models.CASCADE,default=None)
    date = models.DateField(default='00/00/2000')
    hora = models.IntegerField(default=0)

    def __str__(self):
        return f'ID: {self.id}, hora:{self.hora}'