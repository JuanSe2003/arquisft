from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Medico
from .logic.medico_logic import crear_medico

def create_medico(request):
    if request.method == 'POST':
        var = {'nombre':request.POST['nombre'],'apellido':request.POST['apellido'],'especialidad':request.POST['especialidad'],'telefono':request.POST['telefono'],'email':request.POST['email']}
        medico = crear_medico(var)
        messages.success(request, 'Medico creado exitosamente.')
        return HttpResponseRedirect(reverse('medico:medico_create'))
    else:
        return render(request, 'Medico/medico_create.html')

