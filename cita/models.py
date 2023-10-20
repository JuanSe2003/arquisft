from django.db import models
from medico.models import Medico
from horario.models import Horario
from paciente.models import Paciente

class Cita(models.Model):
    id=models.IntegerField(primary_key=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE,default=None)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,default=None)
    horario =models.ForeignKey(Horario, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return {'id':self.id}