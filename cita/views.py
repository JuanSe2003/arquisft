from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cita
from .logic.cita_logic import crear_cita, get_citas, get_cita

def cita_list(request):
    citas = get_citas()
    context = {'citas':citas}
    return render(request, 'cita/cita_list.html', context)

def cita_create(request):
    if request.method == 'POST':
        var = {'medico':request.POST['medico'],'date':request.POST['date'],'time':request.POST['time'],'nombre':request.POST['nombre'],'apellido':request.POST['apellido']}
        cita = crear_cita(var)
        messages.success(request, 'cita creada exitosamente.')
        return HttpResponseRedirect(reverse('cita:cita_create'))
    else:
        return render(request, 'cita/cita_create.html')
    
def get_cita(request):
    cita = get_cita()
    context = {'cita':cita}
    return render(request, 'cita/cita_list.html', context)



