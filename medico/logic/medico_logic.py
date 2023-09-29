import medico.models as Medico
def crear_medico(var):
    Medico=Medico(nombre=var['nombre'],apellido=var['apellido'],especialidad=var['especialidad'],telefono=var['telefono'],email=var['email'])
    Medico.save()
    return Medico