from horario.models import Horario

def get_horarios(var_pk):
    horario=Horario.objects.all()
    return horario

def get_horario(var_pk):
    horario=Horario.objects.get(pk=var_pk)
    return horario


def create_horario(var):
    horario=Horario(cita=var['cita'],medico=var['medico'],date=var['date'],time=var['time'])
    horario.save()
    return horario
