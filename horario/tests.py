from django.test import TestCase

from .models import Horario
from django import forms

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'id',
            'profesional',
            'hora'
        ]
        labels = {
            'id': 'ID',
            'profesional': 'Medico',
            'hora':'Hora'
        
        }