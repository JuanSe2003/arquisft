from ..models import Cita

def crear_cita(var):
    Cita=Cita(medico=var['medico'],date=var['date'],time=var['time'],nombre=var['nombre'],apellido=var['apellido'])
    Cita.save()
    return Cita

def get_citas():
    Cita=Cita.objects.all()
    return Cita

