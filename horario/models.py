from django.db import models
from medico.models import Medico

class Horario(models.Model):
    id=models.IntegerField(primary_key=True)
    profesional = models.ForeignKey(Medico, on_delete=models.CASCADE,default=None)
    time = models.TimeField()

    def __str__(self):
        return f'ID: {self.id}, Date: {self.date}'