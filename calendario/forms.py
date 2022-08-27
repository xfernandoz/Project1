from django import forms
from django.forms import ModelForm
from .models import Event



# crear un form de evento

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date')
        labels = {
            'name': '', #aca se puede modificar lo que dice el formulario
            'name_event': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'name_event': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre del Evento'}),
        }

        