from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cita
from .forms import CitaForm
from .logic.cita_logic import crear_cita, get_citas, get_cita

def cita_list(request):
    citas = get_citas()
    context = {'citas':citas}
    return render(request, 'citas.html', context)

def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            crear_cita(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created cita')
            return HttpResponseRedirect(reverse('citaCreate'))
        else:
            print(form.errors)
    else:
        form = CitaForm()

    context = {
        'form': form,
    }
    return render(request, 'citaCreate.html', context)

#¿?
def get_cita(request):
    cita = get_cita()
    context = {'cita':cita}
    return render(request, 'citas.html', context)



