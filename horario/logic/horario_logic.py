from horario.models import Horario

def get_horarios():
    horario=Horario.objects.all()
    return horario

def get_horario(var_pk):
    horario=Horario.objects.get(pk=var_pk)
    return horario


def create_horario(form):
    horario = form.save()
    horario.save()
    return ()
