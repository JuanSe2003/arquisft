from django.test import TestCase

from django import forms
from .models import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            'id',
            'name',
            'last_name'
        ]
        labels = {
            'id': 'Id',
            'name': 'Name',
            'last_name': 'Last_name'
        }