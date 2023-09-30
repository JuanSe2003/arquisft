from django.test import TestCase
from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'id',
            'medico',
            'horario',
            'date',
            'nombre',
            'apellido'
        ]
        labels = {
            'id':'Id',
            'medico': 'Medico',
            'horario':'Horario',
            'date': 'Date',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
        }