from django.db import models

class Medico(models.Model):
    numero=models.IntegerField()
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return {'id':self.numero,'name':self.name,'last_name':self.last_name}

    
