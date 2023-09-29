from .models import Horario
from django import forms

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'medico',
            'date'
        ]
        labels = {
            'medico': 'Medico',
            'date': 'Date'
        }