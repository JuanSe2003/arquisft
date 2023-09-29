from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Horario
from .logic.horario_logic import create_horario, get_horarios, get_horario

def horario_list(request):
    horarios = get_horarios()
    context = {'horarios':horarios}
    return render(request, 'horario/horario_list.html', context)

def get_horario(request):
    horario = get_horario()
    context = {'horario':horario}
    return render(request, 'horario/horario_list.html', context)

def horario_create(request):
    if request.method == 'POST':
        var = {'cita':request.POST['cita'],'medico':request.POST['medico'],'date':request.POST['date'],'time':request.POST['time']}
        horario = create_horario(var)
        messages.success(request, 'horario creado exitosamente.')
        return HttpResponseRedirect(reverse('horario:horario_list'))
    else:
        return render(request, 'horario/horario_create.html')

