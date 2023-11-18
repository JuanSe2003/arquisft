from  app.auth0backend import getRole
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Paciente
from .tests import PacienteForm
from .logic.paciente_logic import create_Paciente,get_Paciente,get_Pacientes

def paciente_create(request):
    role=getRole(request)
    if role =="Empleado CallCenter":
        if request.method == 'POST':
            form = PacienteForm(request.POST)
            if form.is_valid():
                create_Paciente(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created paciente')
                return HttpResponseRedirect(reverse('pacienteCreate'))
            else:
                print(form.errors)
        else:
            form = PacienteForm()
    
        context = {
            'form': form,
        }
        return render(request, 'pacienteCreate.html', context)
    else:
        return HttpResponse("Usuario no autorizado")

def paciente_list(request):
    pacientes = get_Pacientes()
    context = {'pacientes':pacientes}
    return render(request, 'pacientes.html', context)

#¿?
def get_paciente(request):
    paciente = get_Paciente()
    context = {'paciente':paciente}
    return render(request, 'paciente_list.html', context)
