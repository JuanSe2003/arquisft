from ..models import Paciente

def create_Paciente(form):
    paciente = form.save()
    paciente.save()
    return ()

def get_Paciente(var_pk):
    paciente=Paciente.objects.get(pk=var_pk)
    return paciente

def get_Pacientes():
    paciente=Paciente.objects.all()
    return paciente