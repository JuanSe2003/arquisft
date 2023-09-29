from ..models import Cita

def crear_cita(var):
    cita=Cita(medico=var['medico'],date=var['date'],time=var['time'],nombre=var['nombre'],apellido=var['apellido'])
    cita.save()
    return cita

def get_citas():
    cita=Cita.objects.all()
    return cita

def get_cita(var_pk):
    cita=Cita.objects.get(pk=var_pk)
    return cita

