from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Medico
from .logic.medico_logic import crear_medico, get_medico, get_medicos

def medico_create(request):
    if request.method == 'POST':
        var = {'nombre':request.POST['nombre'],'apellido':request.POST['apellido'],'especialidad':request.POST['especialidad'],'telefono':request.POST['telefono'],'email':request.POST['email']}
        medico = crear_medico(var)
        messages.success(request, 'medico creado exitosamente.')
        return HttpResponseRedirect(reverse('medico:medico_create'))
    else:
        return render(request, 'medico/medico_create.html')

def medico_list(request):
    medicos = get_medicos()
    context = {'medicos':medicos}
    return render(request, 'medico/medico_list.html', context)

def get_horario(request):
    medico = get_medico()
    context = {'medico':medico}
    return render(request, 'medico/medico_list.html', context)
