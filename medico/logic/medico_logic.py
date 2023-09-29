import medico.models as Medico
def crear_medico(var):
    medico=Medico(nombre=var['nombre'],apellido=var['apellido'],especialidad=var['especialidad'],telefono=var['telefono'],email=var['email'])
    medico.save()
    return medico

def get_medicos(var_pk):
    medico=Medico.objects.all()
    return medico

def get_medico(var_pk):
    medico=Medico.objects.get(pk=var_pk)
    return medico
