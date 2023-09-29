from django.db import models
from medico.models import Medico
from horario.models import Horario

class Cita(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario =models.ForeignKey(Horario, on_delete=models.CASCADE)
    date = models.DateField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    def __str__(self):
        return {'medico':self.medico,'horario':self.horario,'date':self.date,'nombre':self.nombre,'apellido':self.apellido}