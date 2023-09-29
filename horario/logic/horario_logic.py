from horario.models import Horario

def get_horarios(var_pk):
    Horario=Horario.objects.all()
    return Horario

def get_horario(var_pk):
    Horario=Horario.objects.get(pk=var_pk)
    return Horario


def create_horario(var):
    Horario=Horario(cita=var['cita'],medico=var['medico'],date=var['date'],time=var['time'])
    Horario.save()
    return Horario
