import medico.models as Medico
def crear_medico(var):
    Medico=Medico(nombre=var['nombre'],apellido=var['apellido'],especialidad=var['especialidad'],telefono=var['telefono'],email=var['email'])
    Medico.save()
    return Medico

def get_medicos(var_pk):
    medico=medico.objects.all()
    return medico

def get_medico(var_pk):
    medico=medico.objects.get(pk=var_pk)
    return medico
