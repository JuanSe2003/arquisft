from django.test import TestCase

from .models import Horario
from django import forms

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'medico',
            'dia',
            'hora_inicio',
            'hora_fin',
            'disponible',
        ]
        labels = {
            'medico': 'Medico',
            'dia': 'Dia',
            'hora_inicio': 'Hora_inicio',
            'hora_fin': 'Hora_fin',
            'disponible': 'Disponible',
        }