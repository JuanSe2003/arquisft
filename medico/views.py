from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Medico
from .forms import MedicoForm
from .logic.medico_logic import crear_medico, get_medico, get_medicos

def medico_create(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            medico_create(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created medico')
            return HttpResponseRedirect(reverse('medicoCreate'))
        else:
            print(form.errors)
    else:
        form = MedicoForm()

    context = {
        'form': form,
    }
    return render(request, 'Medico/medicoCreate.html', context)

def medico_list(request):
    medicos = get_medicos()
    context = {'medicos':medicos}
    return render(request, 'Medico/medicos.html', context)

#¿?
def get_medico(request):
    medico = get_medico()
    context = {'medico':medico}
    return render(request, 'medico/medico_list.html', context)
