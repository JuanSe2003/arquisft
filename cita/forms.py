from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'medico',
            'date',
            'nombre',
            'apellido'
        ]
        labels = {
            'medico': 'Medico',
            'date': 'Date',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
        }