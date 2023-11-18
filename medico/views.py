from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Medico
from .tests import MedicoForm
from .logic.medico_logic import crear_medico, get_medico, get_medicos
from  app.auth0backend import getRole


@login_required
def medico_list(request):
        medicos = get_medicos()
        context = {'medicos':medicos}
        return render(request, 'medicos.html', context)


def medico_create(request):
    role=getRole(request)
    if role =="supervisor":
        if request.method == 'POST':
                form = MedicoForm(request.POST)
                if form.is_valid():
                    crear_medico(form)
                    messages.add_message(request, messages.SUCCESS, 'Successfully created medico')
                    return HttpResponseRedirect(reverse('medicoCreate'))
                else:
                    print(form.errors)
        else:
                form = MedicoForm()

        context = {
                'form': form,
        }
        return render(request, 'medicoCreate.html', context)
    else:
        return HttpResponse("Usuario no autorizado")

def get_medico(request):
    medico = get_medico()
    context = {'medico':medico}
    return render(request, 'medico_list.html', context)

#def medico_list(request):
   #medicos = get_medicos()
   #context = {'medicos':medicos}
   #return render(request, 'medicos.html', context)
