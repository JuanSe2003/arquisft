from django.test import TestCase
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'id',
            'nombre',
            'correo'
        ]
        labels = {
            'id': 'Id',
            'nombre': 'Nombre',
            'correo': 'Correo'
        }