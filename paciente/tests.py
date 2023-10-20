from django.test import TestCase

from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'id',
            'nombre',
            'correo',
            'cc',
            'plan_Salud'
        ]
        labels = {
            'id': 'Id',
            'nombre': 'Nombre',
            'correo': 'Correo',
            'cc': 'Cc',
            'plan_Salud': 'Plan_Salud',
        }