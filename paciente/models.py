from django.db import models

class Paciente(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    cc = models.IntegerField(default=0)
    plan_Salud = models.CharField(max_length=200)

    def _str_(self):
        return f'{self.nombre} {self.correo}'