from django.db import models
from medico.models import Medico

class Horario(models.Model):
    id=models.IntegerField(primary_key=True)
    profesional = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return {'id':self.id,'medico':self.profesional,'date':self.date}