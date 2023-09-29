from django.db import models

class Medico(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return {'id':self.id,'name':self.name,'last_name':self.last_name}

    
