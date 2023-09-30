from django.db import models
from medico.models import Medico

class Horario(models.Model):
    id=models.AutoField(primary_key=True)
    profesional = models.ForeignKey(Medico, on_delete=models.CASCADE,default=None)
    date = models.DateField()

    def __str__(self):
        return f'ID: {self.id}, Date: {self.date}'