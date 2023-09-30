from horario.models import Horario
from medico.models import Medico 

def get_horarios():
    horario=Horario.objects.all()
    return horario

def get_horario(var_pk):
    horario=Horario.objects.get(pk=var_pk)
    return horario


def create_horario(form):
    horario = form.save(commit=False)
    horario.profesional=form.Medico
    horario.save()
    return ()
