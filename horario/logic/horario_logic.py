from horario.models import Horario
from medico.models import Medico 
from medico.logic.medico_logic import get_medico

def get_horarios():
    horario=Horario.objects.all()
    return horario

def get_horario(var_pk):
    horario=Horario.objects.get(pk=var_pk)
    return horario


### crea una funcion que 
def create_horario(form):
    horario = form.save()
    doctores = get_medico(3)
    horario.profesional = doctores
    horario.save()
    return ()
